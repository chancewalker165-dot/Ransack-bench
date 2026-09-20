# bench run: ransack on control_trivia

- run: 20260920-015659 (git 3a0c0bf), sample `control_trivia_v1` frozen 2026-09-19
- calls: 10 (10 questions x 1 repeat(s)), errors: 0
- retrieval hit-rate: **100.0%** (95% CI [72.2%, 100.0%], Wilson)
- NOTE: this dataset is labeled non-discriminative (sanity floor). Scores are not meant to rank providers.
- latency (client-side): mean 0.549s, p50 0.513s, p95 0.847s, max 0.847s

## Per-question

| id | calls | hit_all | hit_any | verdicts | mean latency |
|---|---|---|---|---|---|
| A1 | 1 | True | True | MISS | 0.847s |
| A2 | 1 | True | True | MISS | 0.521s |
| A3 | 1 | True | True | MISS | 0.54s |
| A4 | 1 | True | True | MISS | 0.499s |
| A5 | 1 | True | True | MISS | 0.599s |
| A6 | 1 | True | True | MISS | 0.513s |
| A7 | 1 | True | True | MISS | 0.521s |
| A8 | 1 | True | True | MISS | 0.494s |
| A9 | 1 | True | True | MISS | 0.47s |
| A10 | 1 | True | True | MISS | 0.49s |

Grading is deterministic (bench/graders.py): no LLM judge ran for this summary.
