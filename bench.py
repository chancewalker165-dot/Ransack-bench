#!/usr/bin/env python3
"""Ransack-bench v2 CLI.

  python3 bench.py list                                      # datasets + providers
  python3 bench.py validate                                  # schema-check all manifests
  python3 bench.py run --dataset control_trivia --provider mock --limit 3
  python3 bench.py run --dataset simpleqa --provider ransack --repeat 3
  python3 bench.py compare results/20260919-..._ransack_control_trivia results/...
"""

from __future__ import annotations

import argparse
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from bench.datasets import list_datasets, load_dataset  # noqa: E402
from bench.report import render_compare  # noqa: E402
from bench.schema import validate_manifest  # noqa: E402

PROVIDERS = ["mock", "ransack", "ransack-research", "nosearch",
             "tavily", "brave", "serper", "exa", "exa-answer", "perplexity"]


def cmd_validate(_args) -> int:
    import glob
    root = os.path.dirname(os.path.abspath(__file__))
    manifests = sorted(glob.glob(os.path.join(root, "datasets", "*.json")))
    bad = 0
    for path in manifests:
        m = json.load(open(path, encoding="utf-8"))
        errs = validate_manifest(m)
        name = os.path.basename(path)
        if errs:
            bad += 1
            print(f"INVALID {name}: " + "; ".join(errs))
        else:
            n = len(m.get("questions", m.get("sample_ids", [])))
            print(f"ok       {name}: {n} questions, grader={m['grader']}, "
                  f"mode={m.get('mode', 'full')}")
    print(f"\n{len(manifests) - bad}/{len(manifests)} manifests valid")
    return 1 if bad else 0


def cmd_run(args) -> int:
    from bench.runner import run
    out = run(args.dataset, args.provider, repeat=args.repeat, limit=args.limit,
              k=args.k, tag=args.tag)
    return 0 if out["summary"]["errors"] == 0 else 0  # errors are reported, not fatal


def cmd_compare(args) -> int:
    summaries = []
    for d in args.run_dirs:
        path = os.path.join(d, "summary.json")
        if not os.path.exists(path):
            print(f"skipping {d}: no summary.json", file=sys.stderr)
            continue
        summaries.append(json.load(open(path)))
    if len(summaries) < 2:
        print("need at least two run dirs to compare", file=sys.stderr)
        return 2
    print(render_compare(summaries))
    return 0


def cmd_list(_args) -> int:
    print("datasets:")
    for name in list_datasets():
        try:
            m = load_dataset(name)
            print(f"  {name}: {len(m['questions'])} questions, "
                  f"grader={m['grader']}, non_discriminative={m.get('non_discriminative', False)}")
        except Exception as e:  # noqa: BLE001
            print(f"  {name}: UNAVAILABLE ({e})")
    print("providers: " + ", ".join(PROVIDERS))
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)

    sub.add_parser("list").set_defaults(func=cmd_list)
    sub.add_parser("validate").set_defaults(func=cmd_validate)

    p_run = sub.add_parser("run", help="run a dataset against a provider")
    p_run.add_argument("--dataset", required=True)
    p_run.add_argument("--provider", required=True, choices=PROVIDERS)
    p_run.add_argument("--repeat", type=int, default=1)
    p_run.add_argument("--limit", type=int, default=None)
    p_run.add_argument("--k", type=int, default=5, help="results per query")
    p_run.add_argument("--tag", default=None)
    p_run.set_defaults(func=cmd_run)

    p_cmp = sub.add_parser("compare", help="comparison table across run dirs")
    p_cmp.add_argument("run_dirs", nargs="+")
    p_cmp.set_defaults(func=cmd_compare)

    args = ap.parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
