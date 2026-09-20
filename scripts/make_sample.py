#!/usr/bin/env python3
"""make_sample: build a frozen, reproducible sample manifest from a fetched full dataset.

Determinism: ids are sorted, then selected with Python's random.Random(seed)
via random.sample on the sorted id list. Same seed + same source sha = same
sample, forever. The manifest records both, so any future run can prove it.

Usage:
  python3 scripts/make_sample.py --full data/simpleqa_full.json \
      --dataset simpleqa --n 200 --seed 20260919 \
      --license "MIT (openai/simple-evals)" --grader simpleqa_judge \
      --out datasets/simpleqa_sample_200.json
"""

from __future__ import annotations

import argparse
import json
import os
import random
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from benchlib.datasets import sha256_file  # noqa: E402


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--full", required=True, help="path to data/<name>_full.json")
    ap.add_argument("--dataset", required=True)
    ap.add_argument("--n", type=int, required=True)
    ap.add_argument("--seed", type=int, required=True)
    ap.add_argument("--license", required=True)
    ap.add_argument("--source-url", required=True)
    ap.add_argument("--grader", default="alias_exact", choices=["alias_exact", "simpleqa_judge"])
    ap.add_argument("--ids-only", action="store_true",
                    help="commit sample ids only (license forbids re-distribution); "
                         "content is materialized from --full at load time")
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    full = json.load(open(args.full, encoding="utf-8"))
    qs = full["questions"]
    ids = sorted(q["id"] for q in qs)
    if args.n > len(ids):
        raise SystemExit(f"asked for {args.n}, dataset has {len(ids)}")
    rng = random.Random(args.seed)
    chosen = sorted(rng.sample(ids, args.n))
    by_id = {q["id"]: q for q in qs}

    manifest = {
        "dataset": args.dataset,
        "sample_id": f"{args.dataset}_n{args.n}_seed{args.seed}",
        "seed": args.seed,
        "frozen_on": __import__("datetime").date.today().isoformat(),
        "source": {"url": args.source_url, "license": args.license,
                   "fetched": __import__("datetime").date.today().isoformat()},
        "full_dataset_sha256": sha256_file(args.full),
        "grader": args.grader,
        "selection": "sorted ids + random.Random(seed).sample, committed so the freeze is reproducible",
    }
    if args.ids_only:
        manifest["mode"] = "ids_only"
        manifest["materialize_from"] = os.path.basename(args.full)
        manifest["sample_ids"] = chosen
    else:
        manifest["questions"] = [by_id[i] for i in chosen]

    json.dump(manifest, open(args.out, "w"), indent=2, ensure_ascii=False)
    mode = "ids_only" if args.ids_only else "full"
    print(f"wrote {args.out}: {len(chosen)}/{len(ids)} questions, mode={mode}, "
          f"source sha {manifest['full_dataset_sha256'][:12]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
