# bench run: serper on frames

- run: 20260920-021836 (git 1c148c3), sample `frames_n100_seed20260919` frozen 2026-09-19
- calls: 1 (1 questions x 1 repeat(s)), errors: 1
- retrieval hit-rate: **0.0%** (95% CI [0.0%, 0.0%], Wilson)
- latency (client-side): mean Nones, p50 Nones, p95 Nones, max Nones

## Per-question

| id | calls | hit_all | hit_any | verdicts | mean latency |
|---|---|---|---|---|---|
| frames-0003 | 1 | False | False | ERROR | 0.212s |

Grading is deterministic (bench/graders.py): no LLM judge ran for this summary.
