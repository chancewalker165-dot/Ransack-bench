# bench run: exa on frames

- run: 20260920-033944 (git a203acf), sample `frames_n100_seed20260919` frozen 2026-09-19
- calls: 100 (100 questions x 1 repeat(s)), errors: 0
- retrieval hit-rate: **17.0%** (95% CI [10.9%, 25.5%], Wilson)
- latency (client-side): mean 1.759s, p50 1.396s, p95 4.017s, max 6.201s

## Per-question

| id | calls | hit_all | hit_any | verdicts | mean latency |
|---|---|---|---|---|---|
| frames-0003 | 1 | True | True | MISS | 2.2s |
| frames-0004 | 1 | False | False | MISS | 2.39s |
| frames-0011 | 1 | False | False | MISS | 1.132s |
| frames-0013 | 1 | True | True | MISS | 1.053s |
| frames-0023 | 1 | False | False | MISS | 1.049s |
| frames-0024 | 1 | False | False | MISS | 2.502s |
| frames-0034 | 1 | False | False | MISS | 1.911s |
| frames-0037 | 1 | False | False | MISS | 1.296s |
| frames-0046 | 1 | False | False | MISS | 3.773s |
| frames-0050 | 1 | False | False | MISS | 2.903s |
| frames-0056 | 1 | False | False | MISS | 3.517s |
| frames-0064 | 1 | False | False | MISS | 1.2s |
| frames-0069 | 1 | False | False | MISS | 3.86s |
| frames-0082 | 1 | False | False | MISS | 1.202s |
| frames-0083 | 1 | False | False | MISS | 4.478s |
| frames-0084 | 1 | False | False | MISS | 1.435s |
| frames-0085 | 1 | True | True | MISS | 1.143s |
| frames-0095 | 1 | False | False | MISS | 3.483s |
| frames-0100 | 1 | True | True | MISS | 1.718s |
| frames-0101 | 1 | False | False | MISS | 1.314s |
| frames-0103 | 1 | False | False | MISS | 0.768s |
| frames-0104 | 1 | False | False | MISS | 0.996s |
| frames-0122 | 1 | False | False | MISS | 4.36s |
| frames-0128 | 1 | False | False | MISS | 2.997s |
| frames-0142 | 1 | False | False | MISS | 1.033s |
| frames-0158 | 1 | False | False | MISS | 3.79s |
| frames-0169 | 1 | False | False | MISS | 3.61s |
| frames-0185 | 1 | False | False | MISS | 1.375s |
| frames-0186 | 1 | False | False | MISS | 1.371s |
| frames-0188 | 1 | False | False | MISS | 1.343s |
| frames-0189 | 1 | False | False | MISS | 1.643s |
| frames-0201 | 1 | False | False | MISS | 1.14s |
| frames-0213 | 1 | True | True | MISS | 1.398s |
| frames-0224 | 1 | False | False | MISS | 1.924s |
| frames-0226 | 1 | False | False | MISS | 1.34s |
| frames-0229 | 1 | False | False | MISS | 1.199s |
| frames-0236 | 1 | True | True | MISS | 1.045s |
| frames-0260 | 1 | False | False | MISS | 2.988s |
| frames-0264 | 1 | False | False | MISS | 1.049s |
| frames-0273 | 1 | False | False | MISS | 1.049s |
| frames-0286 | 1 | False | False | MISS | 1.199s |
| frames-0319 | 1 | False | False | MISS | 1.126s |
| frames-0325 | 1 | True | True | MISS | 1.396s |
| frames-0332 | 1 | True | True | MISS | 1.058s |
| frames-0346 | 1 | False | False | MISS | 2.499s |
| frames-0359 | 1 | False | False | MISS | 1.256s |
| frames-0374 | 1 | False | False | MISS | 1.891s |
| frames-0392 | 1 | False | False | MISS | 1.223s |
| frames-0411 | 1 | False | False | MISS | 1.231s |
| frames-0426 | 1 | True | True | MISS | 1.323s |
| frames-0432 | 1 | False | False | MISS | 1.73s |
| frames-0434 | 1 | False | False | MISS | 1.359s |
| frames-0438 | 1 | False | False | MISS | 0.938s |
| frames-0449 | 1 | True | True | MISS | 1.117s |
| frames-0452 | 1 | True | True | MISS | 1.203s |
| frames-0482 | 1 | False | False | MISS | 1.025s |
| frames-0487 | 1 | False | False | MISS | 1.541s |
| frames-0505 | 1 | False | False | MISS | 1.9s |
| frames-0511 | 1 | True | True | MISS | 1.335s |
| frames-0521 | 1 | False | False | MISS | 1.528s |
| frames-0544 | 1 | True | True | MISS | 1.11s |
| frames-0547 | 1 | False | False | MISS | 1.526s |
| frames-0549 | 1 | True | True | MISS | 6.201s |
| frames-0550 | 1 | False | False | MISS | 0.117s |
| frames-0551 | 1 | False | False | MISS | 0.161s |
| frames-0563 | 1 | False | False | MISS | 2.08s |
| frames-0570 | 1 | False | False | MISS | 0.489s |
| frames-0573 | 1 | False | False | MISS | 2.104s |
| frames-0581 | 1 | False | False | MISS | 0.117s |
| frames-0583 | 1 | False | False | MISS | 2.352s |
| frames-0585 | 1 | False | False | MISS | 2.105s |
| frames-0589 | 1 | True | True | MISS | 0.131s |
| frames-0603 | 1 | False | False | MISS | 2.228s |
| frames-0612 | 1 | False | False | MISS | 3.275s |
| frames-0619 | 1 | False | False | MISS | 4.017s |
| frames-0630 | 1 | False | False | MISS | 2.953s |
| frames-0632 | 1 | False | False | MISS | 0.113s |
| frames-0641 | 1 | False | False | MISS | 0.117s |
| frames-0648 | 1 | False | False | MISS | 2.299s |
| frames-0670 | 1 | False | False | MISS | 1.145s |
| frames-0674 | 1 | False | False | MISS | 2.163s |
| frames-0690 | 1 | False | False | MISS | 0.11s |
| frames-0698 | 1 | False | False | MISS | 4.071s |
| frames-0700 | 1 | False | False | MISS | 0.116s |
| frames-0702 | 1 | True | True | MISS | 0.106s |
| frames-0715 | 1 | False | False | MISS | 1.564s |
| frames-0719 | 1 | False | False | MISS | 2.416s |
| frames-0737 | 1 | False | False | MISS | 4.125s |
| frames-0741 | 1 | False | False | MISS | 1.947s |
| frames-0746 | 1 | False | False | MISS | 3.025s |
| frames-0749 | 1 | False | False | MISS | 0.113s |
| frames-0765 | 1 | False | False | MISS | 2.419s |
| frames-0766 | 1 | False | False | MISS | 1.772s |
| frames-0771 | 1 | False | False | MISS | 0.123s |
| frames-0784 | 1 | False | False | MISS | 1.83s |
| frames-0789 | 1 | False | False | MISS | 2.518s |
| frames-0796 | 1 | True | True | MISS | 0.108s |
| frames-0801 | 1 | False | False | MISS | 2.495s |
| frames-0806 | 1 | False | False | MISS | 0.116s |
| frames-0807 | 1 | False | False | MISS | 2.271s |

## Misses (audit trail)

- frames-0004 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0011 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0023 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
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
- frames-0229 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0260 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0264 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0273 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0286 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0319 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
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
- frames-0521 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
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
- frames-0700 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0715 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0719 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0737 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0741 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0746 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0749 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0765 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0766 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0771 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0784 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0789 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0801 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0806 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0807 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)

Grading is deterministic (bench/graders.py): no LLM judge ran for this summary.
