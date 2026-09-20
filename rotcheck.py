#!/usr/bin/env python3
"""rotcheck: flag seed rot before it silently corrupts a benchmark.

v1 lesson (H5): the expected answer was stale and was corrected AFTER the run,
in the same repo as the results. rotcheck makes that failure loud BEFORE a run.

Checks, over datasets/*.json (full mode):
  - questions flagged recency=true must carry verified_as_of
  - verified_as_of older than --max-age days (default 60) is flagged
  - questions flagged unverified=true are always flagged
  - ids_only manifests are skipped (content is pinned by sha, not by date)

Exit 0 if clean, 1 if flags found (use --strict in CI for recency datasets).
"""

from __future__ import annotations

import argparse
import glob
import json
import os
import sys
from datetime import date, datetime

HERE = os.path.dirname(os.path.abspath(__file__))
DATASETS_DIR = os.path.join(HERE, "datasets")


def parse_iso(s: str) -> date:
    return datetime.strptime(s, "%Y-%m-%d").date()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--max-age", type=int, default=60, help="max age (days) of verified_as_of")
    ap.add_argument("--strict", action="store_true", help="exit 1 on any flag (default: exit 0, report only)")
    args = ap.parse_args()

    today = date.today()
    flags = 0
    for path in sorted(glob.glob(os.path.join(DATASETS_DIR, "*.json"))):
        m = json.load(open(path, encoding="utf-8"))
        if m.get("mode", "full") == "ids_only":
            continue
        name = m.get("dataset", os.path.basename(path))
        for q in m.get("questions", []):
            if q.get("unverified"):
                print(f"FLAG {name}/{q['id']}: unverified=true - {q.get('notes', '')}")
                flags += 1
            if q.get("recency"):
                va = q.get("verified_as_of")
                if not va:
                    print(f"FLAG {name}/{q['id']}: recency question missing verified_as_of")
                    flags += 1
                else:
                    age = (today - parse_iso(va)).days
                    if age > args.max_age:
                        print(f"FLAG {name}/{q['id']}: verified_as_of {va} is {age}d old (> {args.max_age})")
                        flags += 1
    print(f"\nrotcheck: {flags} flag(s) across datasets/")
    return 1 if (flags and args.strict) else 0


if __name__ == "__main__":
    raise SystemExit(main())
