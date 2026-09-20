#!/usr/bin/env python3
"""fetch_datasets: pull the full source datasets into data/ (gitignored).

Deterministic on purpose:
- FRAMES: datasets-server /rows pages in row_idx order, config=default split=test
- SimpleQA: the exact CSV openai/simple-evals' own code downloads
- ids are assigned in stable row order; no dates inside the full files (dates
  live in data/provenance.json), so an unchanged upstream produces an
  unchanged sha256 and frozen sample manifests keep verifying.

Usage: python3 scripts/fetch_datasets.py [--only frames|simpleqa]
"""

from __future__ import annotations

import argparse
import csv
import io
import json
import os
import sys
import urllib.request
from datetime import date

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from bench.datasets import DATA_DIR, sha256_file  # noqa: E402

FRAMES_URL = "https://huggingface.co/datasets/google/frames-benchmark"
SIMPLEQA_URL = "https://openaipublic.blob.core.windows.net/simple-evals/simple_qa_test_set.csv"
UA = "RansackBench/2.0 (+https://github.com/chancewalker165-dot/Ransack-bench)"


def get(url: str) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read()


def fetch_frames() -> dict:
    rows = []
    for off in range(0, 900, 100):
        url = ("https://datasets-server.huggingface.co/rows?dataset=google%2Fframes-benchmark"
               f"&config=default&split=test&offset={off}&length=100")
        data = json.loads(get(url))
        got = data.get("rows", [])
        if not got:
            break
        rows.extend(got)
    questions = []
    for i, r in enumerate(rows):
        row = r["row"]
        q = {
            "id": f"frames-{i:04d}",
            "question": (row.get("Prompt") or "").strip(),
            "expected": (row.get("Answer") or "").strip(),
            "aliases": [],
        }
        links = [u for u in (row.get("wiki_links") or []) if isinstance(u, str)]
        if links:
            q["source_urls"] = links
        rt = row.get("reasoning_types")
        if rt:
            q["meta"] = {"reasoning_types": rt}
        if q["question"] and q["expected"]:
            questions.append(q)
    full = {"dataset": "frames", "questions": questions,
            "source_url": FRAMES_URL, "rows_raw": len(rows)}
    with open(os.path.join(DATA_DIR, "frames_full.json"), "w", encoding="utf-8") as fh:
        json.dump(full, fh, indent=1, ensure_ascii=False)
    return {"rows": len(rows), "questions": len(questions)}


def fetch_simpleqa() -> dict:
    raw = get(SIMPLEQA_URL)
    reader = csv.DictReader(io.StringIO(raw.decode("utf-8", "replace")))
    questions = []
    for i, row in enumerate(reader):
        q = {
            "id": f"simpleqa-{i:04d}",
            "question": (row.get("problem") or "").strip(),
            "expected": (row.get("answer") or "").strip(),
            "aliases": [],
        }
        meta = {k: v for k, v in row.items() if k not in ("problem", "answer") and v}
        if meta:
            q["meta"] = meta
        if q["question"] and q["expected"]:
            questions.append(q)
    full = {"dataset": "simpleqa", "questions": questions,
            "source_url": SIMPLEQA_URL, "rows_raw": len(questions)}
    with open(os.path.join(DATA_DIR, "simpleqa_full.json"), "w", encoding="utf-8") as fh:
        json.dump(full, fh, indent=1, ensure_ascii=False)
    return {"rows": len(questions), "questions": len(questions)}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", choices=["frames", "simpleqa"], default=None)
    ap.add_argument("--force", action="store_true",
                    help="refetch even if data/<name>_full.json exists "
                         "(a refetch that changes the sha will break frozen manifests, loudly)")
    args = ap.parse_args()
    os.makedirs(DATA_DIR, exist_ok=True)

    provenance_path = os.path.join(DATA_DIR, "provenance.json")
    prov = json.load(open(provenance_path)) if os.path.exists(provenance_path) else {}
    today = date.today().isoformat()

    sources = {"frames": (FRAMES_URL, "Apache-2.0"), "simpleqa": (SIMPLEQA_URL, "MIT (openai/simple-evals)")}
    jobs = {"frames": fetch_frames, "simpleqa": fetch_simpleqa}
    for name, fn in jobs.items():
        if args.only and name != args.only:
            continue
        path = os.path.join(DATA_DIR, f"{name}_full.json")
        url, license_name = sources[name]
        if os.path.exists(path) and not args.force:
            prov.setdefault(name, {"url": url, "fetched": today, "license": license_name,
                                   "sha256": sha256_file(path), "note": "pre-existing file, not refetched"})
            print(f"{name}: keeping existing {path} (sha {prov[name]['sha256'][:12]}); use --force to refetch")
            continue
        stats = fn()
        prov[name] = {"url": url, "fetched": today, "license": license_name,
                      "sha256": sha256_file(path), **stats}
        print(f"{name}: {stats} -> {path} sha {prov[name]['sha256'][:12]}")

    with open(provenance_path, "w") as fh:
        json.dump(prov, fh, indent=2)
    print(f"provenance -> {provenance_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
