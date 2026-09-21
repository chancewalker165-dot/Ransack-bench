#!/usr/bin/env python3
"""Ingest the owner's browser pass into the Eval A manifest.

The pre-registration (docs/eval-a-fetch-ladder-prereg.md) requires an owner browser
pass for entries that plain HTTP cannot reach independently: for those pages the only
source of ground truth that is not the product being measured is a human looking at
the page in a normal browser.

Input file: owner-pass.txt, one line per page, format

    F-013 | https://www.crunchbase.com/organization/openai | <fact copied from the page>

Blank facts are skipped, so a page the owner could not open simply stays unanchored.
Each accepted fact is validated with the same rules the automated capture uses
(printable, prose, survives grading normalization) and recorded with
fact_source="owner_browser" so the provenance of every anchor stays auditable.

Usage:
  python3 scripts/apply_owner_anchors.py owner-pass.txt            # apply
  python3 scripts/apply_owner_anchors.py owner-pass.txt --dry-run  # preview only
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import datetime, timezone

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fill_fact_anchors import valid_anchor  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MANIFEST = os.path.join(ROOT, "datasets", "fetch_eval_sample_v1.json")


def parse(path: str) -> list[tuple[str, str, str]]:
    out = []
    for raw in open(path, encoding="utf-8"):
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        parts = [p.strip() for p in line.split("|")]
        if len(parts) < 3:
            continue
        pid, url, fact = parts[0], parts[1], " | ".join(parts[2:]).strip()
        if fact:
            out.append((pid, url, fact))
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("file", nargs="?", default="owner-pass.txt")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    facts = parse(args.file)
    if not facts:
        print(f"no facts found in {args.file}: nothing to apply "
              f"(fill in the text after the second '|' on each line)")
        return 1

    doc = json.load(open(MANIFEST))
    by_id = {e["id"]: e for e in doc["questions"]}
    utc = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    applied, rejected = 0, []
    for pid, url, fact in facts:
        e = by_id.get(pid)
        if e is None:
            rejected.append((pid, "unknown id"))
            continue
        if e["url"].rstrip("/") != url.rstrip("/"):
            rejected.append((pid, f"url mismatch: manifest has {e['url']}"))
            continue
        if not valid_anchor(fact, "body_text"):
            rejected.append((pid, "fact fails validation (too short, markup, code, "
                                   "wall notice, or not enough real words)"))
            continue
        e.update({"fact_anchor": fact, "fact_source": "owner_browser",
                  "anchor_confidence": "body_text", "anchor_captured_utc": utc,
                  "needs_owner_verification": False,
                  "anchor_note": "owner browser pass (prereg option-4 gate)"})
        applied += 1
        print(f"{pid} OK   {fact[:70]!r}")

    for pid, why in rejected:
        print(f"{pid} SKIP {why}")

    print(f"\napplied {applied}, skipped {len(rejected)}")
    if args.dry_run:
        print("dry run: manifest NOT written")
        return 0
    json.dump(doc, open(MANIFEST, "w"), indent=1, ensure_ascii=False)
    print(f"manifest written: {MANIFEST}")
    print("next: python3 scripts/run_fetch_eval.py --lane background --poll-cap 200")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())