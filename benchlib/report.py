"""Render human-readable summary.md for a run dir."""

from __future__ import annotations

from .runner import wilson


def render_summary(cfg: dict, summary: dict, records: list[dict]) -> str:
    lo, hi = summary["hit_ci95_pct"]
    lines = [
        f"# bench run: {summary['provider']} on {summary['dataset']}",
        "",
        f"- run: {cfg['started_utc']} (git {cfg['git_sha']}), sample `{summary.get('sample_id')}` frozen {summary.get('frozen_on')}",
        f"- calls: {summary['n_calls']} ({summary['n_questions']} questions x {summary['repeat']} repeat(s)), errors: {summary['errors']}",
        f"- retrieval hit-rate: **{summary['hit_rate_pct']}%** (95% CI [{lo}%, {hi}%], Wilson)",
    ]
    if summary.get("non_discriminative"):
        lines.append("- NOTE: this dataset is labeled non-discriminative (sanity floor). "
                     "Scores are not meant to rank providers.")
    if summary["answer_calls"]:
        lines.append(f"- answer accuracy (answer-producing provider): **{summary['answer_accuracy_pct']}%** "
                     f"({summary['answer_correct']}/{summary['answer_calls']} CORRECT), "
                     f"abstains: {summary['abstains']} (never counted as correct)")
    if summary.get("grader") == "simpleqa_judge":
        j = summary.get("judge", {})
        if j.get("graded"):
            lines.append(f"- SimpleQA official-prompt judge cross-check ran on {j['graded']} answers: "
                         f"{j.get('CORRECT', 0)} CORRECT / {j.get('WRONG', 0)} WRONG / "
                         f"{j.get('ABSTAIN', 0)} NOT_ATTEMPTED / {j.get('JUDGE_ERROR', 0)} errors")
        else:
            lines.append("- judge was configured but did not run (no OPENAI_API_KEY): "
                         "answer grades fall back to containment; judge cross-check skipped, and this is recorded")
    lines += [
        f"- latency (client-side): mean {summary['latency_mean_s']}s, "
        f"p50 {summary['latency_p50_s']}s, p95 {summary['latency_p95_s']}s, max {summary['latency_max_s']}s",
        "",
        "## Per-question",
        "",
        "| id | calls | hit_all | hit_any | verdicts | mean latency |",
        "|---|---|---|---|---|---|",
    ]
    for q in summary["per_question"]:
        verdicts = ",".join(q["verdicts"])
        lines.append(f"| {q['id']} | {q['calls']} | {q['hit_all']} | {q['hit_any']} | "
                     f"{verdicts} | {q['mean_latency_s']}s |")

    misses = [r for r in records if not r.get("hit") and not r.get("error")]
    if misses:
        lines += ["", "## Misses (audit trail)", ""]
        for r in misses:
            lines.append(f"- {r['id']} rep{r['repeat'] + 1}: no candidate matched "
                         "(see results.jsonl + transcript.jsonl for spans)")
    lines += ["", "Grading is deterministic (benchlib/graders.py): no LLM judge ran for this summary."]
    return "\n".join(lines) + "\n"


def render_compare(summaries: list[dict]) -> str:
    """Cross-provider comparison table. summaries: aggregate dicts from summary.json."""
    lines = [
        "# provider comparison",
        "",
        "| provider | dataset | n | hit-rate | 95% CI | p50 | p95 | errors | ans-acc | judged |",
        "|---|---|---|---|---|---|---|---|---|---|",
    ]
    for s in summaries:
        lo, hi = wilson(s["hits"], s["n_calls"] - s["errors"])
        acc = (f"{s['answer_correct']}/{s['answer_calls']}"
               if s.get("answer_calls") else "-")
        j = s.get("judge") or {}
        judge = (f"{j.get('CORRECT', 0)}/{j.get('graded', 0)}" if j.get("graded") else "-")
        lines.append(
            f"| {s['provider']} | {s['dataset']} | {s['n_calls']} | {s['hit_rate_pct']}% "
            f"| [{100 * lo:.1f}%, {100 * hi:.1f}%] | {s['latency_p50_s']}s "
            f"| {s['latency_p95_s']}s | {s['errors']} | {acc} | {judge} |")
    lines += ["", "Hit-rate = expected fact present in returned documents (retrieval). "
              "ans-acc = exact composed answer present in the provider's own answer field "
              "(containment; the official judge cross-check needs OPENAI_API_KEY and was not run). "
              "Answer accuracy only exists for answer-producing lanes."]
    return "\n".join(lines) + "\n"
