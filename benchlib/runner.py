"""Runner: loops questions, measures client-side, grades, writes a run dir.

Run dir layout (results/<UTC timestamp>_<provider>_<dataset>[_<tag>]/):
  run_config.json   manifest meta + provider + repeat/limit + git sha
  transcript.jsonl  one line per call: question, request, untouched raw response
  results.jsonl     one line per call: verdict, spans, latency, tokens, errors
  summary.json      machine-readable aggregates
  summary.md        human-readable report with Wilson CIs
"""

from __future__ import annotations

import json
import math
import os
import subprocess
import time
from datetime import datetime, timezone

from .datasets import load_dataset
from .graders import grade_item
from .providers.base import from_registry

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
RESULTS_DIR = os.path.join(ROOT, "results")


def wilson(k: int, n: int, z: float = 1.96) -> tuple[float, float]:
    if n == 0:
        return (0.0, 0.0)
    p = k / n
    denom = 1 + z * z / n
    center = (p + z * z / (2 * n)) / denom
    half = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / denom
    return (max(0.0, center - half), min(1.0, center + half))


def pctl(values: list[float], p: float) -> float | None:
    if not values:
        return None
    s = sorted(values)
    idx = max(0, min(len(s) - 1, int(math.ceil(p / 100 * len(s))) - 1))
    return round(s[idx], 3)


def git_sha() -> str:
    try:
        return subprocess.run(["git", "rev-parse", "--short", "HEAD"], cwd=ROOT,
                              capture_output=True, text=True, timeout=5).stdout.strip()
    except Exception:
        return "unknown"


def run(dataset: str, provider_name: str, repeat: int = 1, limit: int | None = None,
        k: int = 5, tag: str | None = None, results_root: str | None = None) -> dict:
    manifest = load_dataset(dataset)
    provider = from_registry(provider_name)

    stamp = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
    parts = [stamp, provider_name.replace("/", "-"), manifest["dataset"]]
    if tag:
        parts.append(tag)
    outdir = os.path.join(results_root or RESULTS_DIR, "_".join(parts))
    os.makedirs(outdir, exist_ok=True)

    questions = manifest["questions"]
    if limit:
        questions = questions[:limit]

    cfg = {
        "dataset": manifest["dataset"], "sample_id": manifest.get("sample_id"),
        "frozen_on": manifest.get("frozen_on"),
        "non_discriminative": manifest.get("non_discriminative", False),
        "grader": manifest.get("grader"),
        "provider": provider_name, "repeat": repeat, "k": k, "limit": limit,
        "tag": tag, "git_sha": git_sha(),
        "started_utc": stamp, "question_count": len(questions),
    }
    json.dump(cfg, open(os.path.join(outdir, "run_config.json"), "w"), indent=2)

    tfile = open(os.path.join(outdir, "transcript.jsonl"), "w")
    rfile = open(os.path.join(outdir, "results.jsonl"), "w")
    records: list[dict] = []

    for qi, q in enumerate(questions, 1):
        for rep in range(repeat):
            t0 = time.perf_counter()
            err = None
            result = None
            try:
                result = provider.ask(q["question"], k)
            except Exception as e:  # noqa: BLE001 - record everything, never abort the run
                err = f"{type(e).__name__}: {e}"
            latency = round(time.perf_counter() - t0, 3)

            rec = {"id": q["id"], "repeat": rep, "latency_s": latency}
            if err:
                rec.update({"error": err, "hit": False, "answer_verdict": ""})
            else:
                rec.update(grade_item(q, result))
                rec["tokens_est"] = result.get("tokens_est")
                rec["server_latency_s"] = result.get("server_latency_s")
                if manifest.get("grader") == "simpleqa_judge" and result.get("answer"):
                    from .graders_judge import judge_available, judge_grade
                    if judge_available():
                        try:
                            jv = judge_grade(q["question"], q["expected"], result["answer"])
                        except Exception as e:  # noqa: BLE001 - judge failure must not kill the run
                            jv = "JUDGE_ERROR"
                            rec["judge_error"] = f"{type(e).__name__}: {e}"[:160]
                        rec["judge_verdict"] = jv
                        if jv in ("CORRECT", "WRONG", "ABSTAIN"):
                            rec["answer_verdict"] = jv
                    else:
                        rec["judge_verdict"] = "SKIPPED_NO_KEY"
                tfile.write(json.dumps({
                    "id": q["id"], "repeat": rep, "question": q["question"], "k": k,
                    "raw": result.get("raw"),
                }, default=str) + "\n")
            rfile.write(json.dumps(rec, default=str) + "\n")
            records.append(rec)
            status = rec.get("error") and f"ERROR {err[:60]}" or (
                f"hit={rec['hit']}" + (f" answer={rec['answer_verdict']}" if rec.get("answer_verdict") else ""))
            print(f"[{qi}/{len(questions)}] {q['id']} rep{rep + 1}/{repeat} "
                  f"{latency:.2f}s {status}", flush=True)

    tfile.close()
    rfile.close()

    summary = aggregate(manifest, provider_name, records, repeat)
    json.dump(summary, open(os.path.join(outdir, "summary.json"), "w"), indent=2, default=str)
    from .report import render_summary
    md = render_summary(cfg, summary, records)
    open(os.path.join(outdir, "summary.md"), "w").write(md)
    print(f"\nrun dir: {outdir}\nhit-rate {summary['hit_rate_pct']}% "
          f"(n={summary['n_calls']}, errors={summary['errors']})")
    return {"outdir": outdir, "summary": summary}


def aggregate(manifest: dict, provider_name: str, records: list[dict], repeat: int) -> dict:
    n = len(records)
    errors = sum(1 for r in records if r.get("error"))
    hits = sum(1 for r in records if r.get("hit") and not r.get("error"))
    lo, hi = wilson(hits, n - errors)
    lat = [r["latency_s"] for r in records if not r.get("error")]
    answered = [r for r in records if r.get("answer_verdict")]
    correct = sum(1 for r in answered if r["answer_verdict"] == "CORRECT")
    abstain = sum(1 for r in answered if r["answer_verdict"] == "ABSTAIN")

    by_q: dict[str, list] = {}
    for r in records:
        by_q.setdefault(r["id"], []).append(r)
    per_question = []
    for qid, rs in by_q.items():
        per_question.append({
            "id": qid,
            "calls": len(rs),
            "hit_all": all(r["hit"] for r in rs if not r.get("error")) and any(not r.get("error") for r in rs),
            "hit_any": any(r["hit"] for r in rs),
            "verdicts": [r.get("answer_verdict") or ("ERROR" if r.get("error") else "MISS") for r in rs],
            "mean_latency_s": round(sum(r["latency_s"] for r in rs) / len(rs), 3),
        })

    judge_records = [r for r in records if r.get("judge_verdict") not in (None, "SKIPPED_NO_KEY")]
    judge_counts = {v: sum(1 for r in judge_records if r.get("judge_verdict") == v)
                    for v in ("CORRECT", "WRONG", "ABSTAIN", "JUDGE_ERROR")}

    return {
        "provider": provider_name,
        "dataset": manifest["dataset"],
        "sample_id": manifest.get("sample_id"),
        "frozen_on": manifest.get("frozen_on"),
        "non_discriminative": manifest.get("non_discriminative", False),
        "grader": manifest.get("grader"),
        "n_questions": len(by_q), "n_calls": n, "repeat": repeat,
        "hits": hits, "hit_rate_pct": round(100 * hits / max(1, n - errors), 1),
        "hit_ci95_pct": [round(100 * lo, 1), round(100 * hi, 1)],
        "errors": errors,
        "answer_calls": len(answered),
        "answer_correct": correct,
        "answer_accuracy_pct": round(100 * correct / len(answered), 1) if answered else None,
        "abstains": abstain,
        "judge": {"graded": len(judge_records), **judge_counts},
        "latency_mean_s": round(sum(lat) / len(lat), 3) if lat else None,
        "latency_p50_s": pctl(lat, 50),
        "latency_p95_s": pctl(lat, 95),
        "latency_max_s": round(max(lat), 3) if lat else None,
        "per_question": per_question,
    }
