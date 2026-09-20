#!/usr/bin/env python3
"""rejudge: offline judge pass over a finished simpleqa run dir.

When a run finished before the judge was fixed (or with the judge skipped),
this re-grades the recorded answers from transcript.jsonl WITHOUT re-calling
the provider: only judge calls are spent. Updates results.jsonl verdicts,
recomputes summary.json, and writes rejudge.jsonl with per-question judge
output for auditability.

Usage: python3 scripts/rejudge.py results/<run-dir>
"""

from __future__ import annotations

import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from benchlib.datasets import load_dataset  # noqa: E402
from benchlib.graders_judge import judge_available, judge_grade  # noqa: E402
from benchlib.runner import aggregate  # noqa: E402

MANIFEST_FOR = {"frames": "frames_sample_100", "simpleqa": "simpleqa_sample_200"}


def extract_answer(provider: str, raw) -> str | None:
    if raw is None:
        return None
    if provider == "tavily":
        return raw.get("answer")
    if provider in ("nosearch", "perplexity"):
        try:
            return raw["choices"][0]["message"]["content"]
        except (KeyError, IndexError, TypeError):
            return None
    if provider in ("ransack-research", "exa-answer"):
        a = raw.get("answer")
        return a if isinstance(a, str) else json.dumps(a) if a else None
    return None


def main() -> int:
    if len(sys.argv) != 2:
        print(__doc__, file=sys.stderr)
        return 2
    run_dir = sys.argv[1]
    if not judge_available():
        print("judge unavailable: set OPENAI_API_KEY (and JUDGE_MODEL)", file=sys.stderr)
        return 2

    summary = json.load(open(os.path.join(run_dir, "summary.json")))
    provider = summary["provider"]
    manifest = load_dataset(MANIFEST_FOR.get(summary["dataset"], summary["dataset"]))
    items = {q["id"]: q for q in manifest["questions"]}

    records = [json.loads(l) for l in open(os.path.join(run_dir, "results.jsonl"))]
    transcripts = {}
    tpath = os.path.join(run_dir, "transcript.jsonl")
    if os.path.exists(tpath):
        for line in open(tpath):
            t = json.loads(line)
            transcripts[(t["id"], t.get("repeat", 0))] = t.get("raw")

    rj = open(os.path.join(run_dir, "rejudge.jsonl"), "w")
    changed = 0
    for rec in records:
        raw = transcripts.get((rec["id"], rec.get("repeat", 0)))
        answer = extract_answer(provider, raw)
        if not answer:
            continue
        item = items[rec["id"]]
        jv = judge_grade(item["question"], item["expected"], answer)
        rj.write(json.dumps({"id": rec["id"], "judge_verdict": jv}) + "\n")
        if jv in ("CORRECT", "WRONG", "ABSTAIN"):
            if rec.get("judge_verdict") != jv:
                changed += 1
            rec["judge_verdict"] = jv
            rec["answer_verdict"] = jv
    rj.close()

    with open(os.path.join(run_dir, "results.jsonl"), "w") as fh:
        for rec in records:
            fh.write(json.dumps(rec, default=str) + "\n")

    new_summary = aggregate(manifest, provider, records, summary.get("repeat", 1))
    new_summary["judge_note"] = (f"offline rejudge from transcript (judge model: "
                                 f"{os.environ.get('JUDGE_MODEL', 'default')})")
    json.dump(new_summary, open(os.path.join(run_dir, "summary.json"), "w"), indent=2, default=str)
    print(f"rejudged {len(records)} records in {run_dir}: "
          f"{new_summary['judge']} | verdict changes: {changed}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
