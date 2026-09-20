# bench run: ransack-research on frames

- run: 20260920-015857 (git 3a0c0bf), sample `frames_n100_seed20260919` frozen 2026-09-19
- calls: 10 (10 questions x 1 repeat(s)), errors: 0
- retrieval hit-rate: **70.0%** (95% CI [39.7%, 89.2%], Wilson)
- answer accuracy (answer-producing provider): **40.0%** (4/10 CORRECT), abstains: 0 (never counted as correct)
- latency (client-side): mean 7.95s, p50 4.765s, p95 17.028s, max 17.028s

## Per-question

| id | calls | hit_all | hit_any | verdicts | mean latency |
|---|---|---|---|---|---|
| frames-0003 | 1 | True | True | CORRECT | 8.818s |
| frames-0004 | 1 | True | True | CORRECT | 4.622s |
| frames-0011 | 1 | True | True | CORRECT | 4.618s |
| frames-0013 | 1 | True | True | WRONG | 4.637s |
| frames-0023 | 1 | True | True | WRONG | 4.637s |
| frames-0024 | 1 | True | True | CORRECT | 8.693s |
| frames-0034 | 1 | False | False | WRONG | 17.028s |
| frames-0037 | 1 | True | True | WRONG | 12.881s |
| frames-0046 | 1 | False | False | WRONG | 4.765s |
| frames-0050 | 1 | False | False | WRONG | 8.8s |

## Misses (audit trail)

- frames-0034 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0046 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0050 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)

Grading is deterministic (bench/graders.py): no LLM judge ran for this summary.
