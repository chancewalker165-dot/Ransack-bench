# bench run: ransack on frames

- run: 20260920-015705 (git 3a0c0bf), sample `frames_n100_seed20260919` frozen 2026-09-19
- calls: 10 (10 questions x 1 repeat(s)), errors: 0
- retrieval hit-rate: **10.0%** (95% CI [1.8%, 40.4%], Wilson)
- latency (client-side): mean 0.486s, p50 0.486s, p95 0.514s, max 0.514s

## Per-question

| id | calls | hit_all | hit_any | verdicts | mean latency |
|---|---|---|---|---|---|
| frames-0003 | 1 | True | True | MISS | 0.5s |
| frames-0004 | 1 | False | False | MISS | 0.486s |
| frames-0011 | 1 | False | False | MISS | 0.464s |
| frames-0013 | 1 | False | False | MISS | 0.451s |
| frames-0023 | 1 | False | False | MISS | 0.514s |
| frames-0024 | 1 | False | False | MISS | 0.499s |
| frames-0034 | 1 | False | False | MISS | 0.502s |
| frames-0037 | 1 | False | False | MISS | 0.47s |
| frames-0046 | 1 | False | False | MISS | 0.49s |
| frames-0050 | 1 | False | False | MISS | 0.481s |

## Misses (audit trail)

- frames-0004 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0011 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0013 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0023 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0024 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0034 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0037 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0046 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0050 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)

Grading is deterministic (bench/graders.py): no LLM judge ran for this summary.
