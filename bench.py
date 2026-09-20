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

from benchlib.datasets import list_datasets, load_dataset  # noqa: E402
from benchlib.report import render_compare  # noqa: E402
from benchlib.schema import validate_manifest  # noqa: E402

PROVIDERS = ["mock", "ransack", "ransack-research", "nosearch",
             "tavily", "brave", "serper", "exa", "exa-answer", "perplexity"]

# env each provider needs to be considered "available" in the suite
PROVIDER_ENV = {
    "mock": [],
    "ransack": ["RANSACK_MCP_TOKEN"],
    "ransack-research": ["RANSACK_MCP_TOKEN"],
    "nosearch": ["OPENAI_API_KEY"],
    "tavily": ["TAVILY_API_KEY"],
    "brave": ["BRAVE_API_KEY"],
    "serper": ["SERPER_API_KEY"],
    "exa": ["EXA_API_KEY"],
    "exa-answer": ["EXA_API_KEY"],
    "perplexity": ["PERPLEXITY_API_KEY"],
}

# the full suite plan: (dataset, provider) in priority order
PLAN = [
    ("frames_sample_100", "nosearch"),
    ("frames_sample_100", "ransack"),
    ("frames_sample_100", "ransack-research"),
    ("frames_sample_100", "tavily"),
    ("frames_sample_100", "brave"),
    ("frames_sample_100", "serper"),
    ("frames_sample_100", "exa"),
    ("frames_sample_100", "exa-answer"),
    ("frames_sample_100", "perplexity"),
    ("simpleqa_sample_200", "nosearch"),
    ("simpleqa_sample_200", "ransack"),
    ("simpleqa_sample_200", "tavily"),
    ("simpleqa_sample_200", "brave"),
    ("simpleqa_sample_200", "serper"),
]


def _load_dotenv(root: str) -> int:
    """Load .env into os.environ. Never overrides already-set vars. Skips
    empty values and leftover [PLACEHOLDER] tokens."""
    path = os.path.join(root, ".env")
    if not os.path.exists(path):
        return 0
    count = 0
    for line in open(path, encoding="utf-8"):
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, val = line.partition("=")
        key, val = key.strip(), val.strip().strip('"').strip("'")
        if not key or not val or val.startswith("[") or key in os.environ:
            continue
        os.environ[key] = val
        count += 1
    return count


def cmd_suite(args) -> int:
    root = os.path.dirname(os.path.abspath(__file__))
    loaded = _load_dotenv(root)
    print(f".env: {loaded} var(s) loaded" if loaded else ".env: not found, using current env")

    allowed = set(args.providers) if args.providers else None
    plan = [(d, p) for d, p in PLAN if not allowed or p in allowed or d in allowed]
    if not plan:
        print("nothing to run: no plan entries match", file=sys.stderr)
        return 2

    available, skipped = [], []
    for dataset, prov in plan:
        missing = [v for v in PROVIDER_ENV[prov] if not os.environ.get(v)]
        (skipped if missing else available).append((dataset, prov, missing))
    for dataset, prov, missing in skipped:
        print(f"skip {prov} on {dataset}: missing {','.join(missing)}")

    from benchlib.datasets import load_dataset
    calls = 0
    for dataset, prov, _ in available:
        try:
            calls += len(load_dataset(dataset)["questions"])
        except Exception as e:  # noqa: BLE001
            print(f"warn: cannot load {dataset}: {e}", file=sys.stderr)
    if not args.yes:
        answer = input(f"about to run {len(available)} runs (~{calls} calls total). continue? [y/N] ")
        if answer.strip().lower() != "y":
            print("aborted")
            return 1

    from benchlib.runner import run
    outdirs: dict[str, list[str]] = {}
    for i, (dataset, prov, _) in enumerate(available, 1):
        print(f"\n=== [{i}/{len(available)}] {prov} on {dataset} ===")
        try:
            out = run(dataset, prov, repeat=args.repeat, limit=args.limit, tag="suite")
            outdirs.setdefault(dataset, []).append(out["outdir"])
        except Exception as e:  # noqa: BLE001 - one dead provider must not kill the suite
            print(f"SUITE: {prov} on {dataset} failed: {e}", file=sys.stderr)

    from benchlib.report import render_compare
    md_path = os.path.join(root, "results", "COMPARISON.md")
    with open(md_path, "a") as md:
        for dataset, dirs in outdirs.items():
            if len(dirs) < 2:
                continue
            summaries = [json.load(open(os.path.join(d, "summary.json"))) for d in dirs]
            md.write(f"\n\n## {dataset}\n\n" + render_compare(summaries))
    if any(len(d) >= 2 for d in outdirs.values()):
        print(f"\ncomparison written: {md_path}")
    return 0


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
    from benchlib.runner import run
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

    p_suite = sub.add_parser("suite", help="run the whole priority plan, skipping providers without keys")
    p_suite.add_argument("--providers", nargs="*", default=None,
                         help="restrict to these providers (default: full plan)")
    p_suite.add_argument("--repeat", type=int, default=1)
    p_suite.add_argument("--limit", type=int, default=None)
    p_suite.add_argument("--yes", action="store_true", help="skip the confirmation prompt")
    p_suite.set_defaults(func=cmd_suite)

    args = ap.parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
