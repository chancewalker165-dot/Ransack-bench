# bench run: brave on frames

- run: 20260920-033602 (git a203acf), sample `frames_n100_seed20260919` frozen 2026-09-19
- calls: 100 (100 questions x 1 repeat(s)), errors: 0
- retrieval hit-rate: **20.0%** (95% CI [13.3%, 28.9%], Wilson)
- latency (client-side): mean 0.56s, p50 0.623s, p95 0.755s, max 1.106s

## Per-question

| id | calls | hit_all | hit_any | verdicts | mean latency |
|---|---|---|---|---|---|
| frames-0003 | 1 | False | False | MISS | 0.835s |
| frames-0004 | 1 | False | False | MISS | 0.671s |
| frames-0011 | 1 | False | False | MISS | 0.62s |
| frames-0013 | 1 | False | False | MISS | 0.66s |
| frames-0023 | 1 | True | True | MISS | 0.728s |
| frames-0024 | 1 | False | False | MISS | 0.74s |
| frames-0034 | 1 | False | False | MISS | 0.64s |
| frames-0037 | 1 | False | False | MISS | 0.668s |
| frames-0046 | 1 | False | False | MISS | 1.106s |
| frames-0050 | 1 | False | False | MISS | 0.588s |
| frames-0056 | 1 | False | False | MISS | 0.686s |
| frames-0064 | 1 | False | False | MISS | 0.664s |
| frames-0069 | 1 | False | False | MISS | 0.755s |
| frames-0082 | 1 | False | False | MISS | 0.62s |
| frames-0083 | 1 | False | False | MISS | 0.597s |
| frames-0084 | 1 | False | False | MISS | 0.634s |
| frames-0085 | 1 | True | True | MISS | 0.75s |
| frames-0095 | 1 | False | False | MISS | 0.713s |
| frames-0100 | 1 | True | True | MISS | 0.556s |
| frames-0101 | 1 | False | False | MISS | 0.61s |
| frames-0103 | 1 | False | False | MISS | 0.579s |
| frames-0104 | 1 | False | False | MISS | 0.554s |
| frames-0122 | 1 | False | False | MISS | 0.646s |
| frames-0128 | 1 | False | False | MISS | 0.696s |
| frames-0142 | 1 | False | False | MISS | 0.571s |
| frames-0158 | 1 | False | False | MISS | 0.659s |
| frames-0169 | 1 | False | False | MISS | 0.842s |
| frames-0185 | 1 | False | False | MISS | 0.623s |
| frames-0186 | 1 | False | False | MISS | 0.703s |
| frames-0188 | 1 | False | False | MISS | 0.646s |
| frames-0189 | 1 | False | False | MISS | 0.6s |
| frames-0201 | 1 | False | False | MISS | 0.705s |
| frames-0213 | 1 | True | True | MISS | 0.648s |
| frames-0224 | 1 | False | False | MISS | 0.755s |
| frames-0226 | 1 | False | False | MISS | 0.566s |
| frames-0229 | 1 | True | True | MISS | 0.7s |
| frames-0236 | 1 | False | False | MISS | 0.534s |
| frames-0260 | 1 | False | False | MISS | 0.671s |
| frames-0264 | 1 | False | False | MISS | 0.629s |
| frames-0273 | 1 | False | False | MISS | 0.622s |
| frames-0286 | 1 | False | False | MISS | 0.643s |
| frames-0319 | 1 | True | True | MISS | 0.657s |
| frames-0325 | 1 | False | False | MISS | 0.629s |
| frames-0332 | 1 | True | True | MISS | 0.643s |
| frames-0346 | 1 | False | False | MISS | 0.519s |
| frames-0359 | 1 | False | False | MISS | 0.724s |
| frames-0374 | 1 | False | False | MISS | 0.557s |
| frames-0392 | 1 | False | False | MISS | 0.67s |
| frames-0411 | 1 | False | False | MISS | 0.658s |
| frames-0426 | 1 | True | True | MISS | 0.647s |
| frames-0432 | 1 | False | False | MISS | 0.668s |
| frames-0434 | 1 | False | False | MISS | 0.637s |
| frames-0438 | 1 | False | False | MISS | 0.551s |
| frames-0449 | 1 | True | True | MISS | 0.602s |
| frames-0452 | 1 | True | True | MISS | 0.643s |
| frames-0482 | 1 | False | False | MISS | 0.591s |
| frames-0487 | 1 | False | False | MISS | 0.748s |
| frames-0505 | 1 | False | False | MISS | 0.747s |
| frames-0511 | 1 | True | True | MISS | 0.633s |
| frames-0521 | 1 | True | True | MISS | 0.765s |
| frames-0544 | 1 | True | True | MISS | 0.536s |
| frames-0547 | 1 | False | False | MISS | 0.575s |
| frames-0549 | 1 | True | True | MISS | 0.601s |
| frames-0550 | 1 | False | False | MISS | 0.547s |
| frames-0551 | 1 | False | False | MISS | 0.62s |
| frames-0563 | 1 | False | False | MISS | 0.578s |
| frames-0570 | 1 | False | False | MISS | 0.558s |
| frames-0573 | 1 | False | False | MISS | 0.763s |
| frames-0581 | 1 | False | False | MISS | 0.57s |
| frames-0583 | 1 | False | False | MISS | 0.629s |
| frames-0585 | 1 | False | False | MISS | 0.704s |
| frames-0589 | 1 | True | True | MISS | 0.72s |
| frames-0603 | 1 | False | False | MISS | 0.632s |
| frames-0612 | 1 | False | False | MISS | 0.636s |
| frames-0619 | 1 | False | False | MISS | 0.698s |
| frames-0630 | 1 | False | False | MISS | 0.743s |
| frames-0632 | 1 | False | False | MISS | 0.252s |
| frames-0641 | 1 | False | False | MISS | 0.212s |
| frames-0648 | 1 | False | False | MISS | 0.261s |
| frames-0670 | 1 | False | False | MISS | 0.24s |
| frames-0674 | 1 | False | False | MISS | 0.249s |
| frames-0690 | 1 | False | False | MISS | 0.662s |
| frames-0698 | 1 | False | False | MISS | 0.225s |
| frames-0700 | 1 | True | True | MISS | 0.197s |
| frames-0702 | 1 | False | False | MISS | 0.211s |
| frames-0715 | 1 | False | False | MISS | 0.169s |
| frames-0719 | 1 | False | False | MISS | 0.293s |
| frames-0737 | 1 | False | False | MISS | 0.224s |
| frames-0741 | 1 | False | False | MISS | 0.249s |
| frames-0746 | 1 | False | False | MISS | 0.206s |
| frames-0749 | 1 | False | False | MISS | 0.212s |
| frames-0765 | 1 | False | False | MISS | 0.272s |
| frames-0766 | 1 | False | False | MISS | 0.263s |
| frames-0771 | 1 | False | False | MISS | 0.31s |
| frames-0784 | 1 | True | True | MISS | 0.267s |
| frames-0789 | 1 | False | False | MISS | 0.317s |
| frames-0796 | 1 | True | True | MISS | 0.211s |
| frames-0801 | 1 | True | True | MISS | 0.263s |
| frames-0806 | 1 | True | True | MISS | 0.245s |
| frames-0807 | 1 | False | False | MISS | 0.204s |

## Misses (audit trail)

- frames-0003 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0004 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0011 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0013 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0024 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0034 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0037 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0046 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0050 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0056 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0064 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0069 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0082 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0083 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0084 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0095 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0101 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0103 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0104 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0122 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0128 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0142 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0158 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0169 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0185 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0186 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0188 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0189 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0201 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0224 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0226 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0236 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0260 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0264 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0273 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0286 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0325 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0346 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0359 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0374 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0392 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0411 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0432 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0434 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0438 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0482 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0487 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0505 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0547 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0550 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0551 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0563 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0570 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0573 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0581 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0583 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0585 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0603 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0612 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0619 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0630 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0632 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0641 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0648 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0670 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0674 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0690 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0698 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0702 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0715 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0719 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0737 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0741 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0746 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0749 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0765 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0766 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0771 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0789 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0807 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)

Grading is deterministic (bench/graders.py): no LLM judge ran for this summary.
