# bench run: tavily on frames

- run: 20260920-033547 (git a203acf), sample `frames_n100_seed20260919` frozen 2026-09-19
- calls: 100 (100 questions x 1 repeat(s)), errors: 0
- retrieval hit-rate: **38.0%** (95% CI [29.1%, 47.8%], Wilson)
- answer accuracy (answer-producing provider): **24.0%** (24/100 CORRECT), abstains: 0 (never counted as correct)
- latency (client-side): mean 2.991s, p50 2.698s, p95 5.015s, max 5.497s

## Per-question

| id | calls | hit_all | hit_any | verdicts | mean latency |
|---|---|---|---|---|---|
| frames-0003 | 1 | True | True | WRONG | 2.254s |
| frames-0004 | 1 | False | False | WRONG | 2.698s |
| frames-0011 | 1 | False | False | WRONG | 2.87s |
| frames-0013 | 1 | True | True | CORRECT | 4.071s |
| frames-0023 | 1 | True | True | WRONG | 2.517s |
| frames-0024 | 1 | False | False | WRONG | 3.165s |
| frames-0034 | 1 | False | False | WRONG | 2.551s |
| frames-0037 | 1 | True | True | WRONG | 2.892s |
| frames-0046 | 1 | False | False | WRONG | 2.603s |
| frames-0050 | 1 | False | False | WRONG | 2.597s |
| frames-0056 | 1 | False | False | WRONG | 2.365s |
| frames-0064 | 1 | False | False | WRONG | 2.697s |
| frames-0069 | 1 | True | True | CORRECT | 2.869s |
| frames-0082 | 1 | False | False | WRONG | 2.347s |
| frames-0083 | 1 | False | False | WRONG | 2.806s |
| frames-0084 | 1 | False | False | WRONG | 2.335s |
| frames-0085 | 1 | True | True | CORRECT | 3.528s |
| frames-0095 | 1 | True | True | CORRECT | 2.634s |
| frames-0100 | 1 | True | True | CORRECT | 2.283s |
| frames-0101 | 1 | False | False | WRONG | 3.254s |
| frames-0103 | 1 | False | False | WRONG | 2.074s |
| frames-0104 | 1 | True | True | CORRECT | 3.014s |
| frames-0122 | 1 | False | False | WRONG | 3.431s |
| frames-0128 | 1 | False | False | WRONG | 3.066s |
| frames-0142 | 1 | False | False | WRONG | 5.497s |
| frames-0158 | 1 | True | True | WRONG | 2.413s |
| frames-0169 | 1 | False | False | WRONG | 2.947s |
| frames-0185 | 1 | True | True | WRONG | 4.777s |
| frames-0186 | 1 | False | False | WRONG | 2.369s |
| frames-0188 | 1 | False | False | WRONG | 1.945s |
| frames-0189 | 1 | False | False | WRONG | 2.304s |
| frames-0201 | 1 | False | False | WRONG | 3.394s |
| frames-0213 | 1 | False | False | WRONG | 5.102s |
| frames-0224 | 1 | False | False | WRONG | 2.16s |
| frames-0226 | 1 | False | False | WRONG | 1.847s |
| frames-0229 | 1 | True | True | WRONG | 5.244s |
| frames-0236 | 1 | True | True | WRONG | 1.913s |
| frames-0260 | 1 | False | False | WRONG | 2.608s |
| frames-0264 | 1 | False | False | WRONG | 2.446s |
| frames-0273 | 1 | True | True | WRONG | 2.51s |
| frames-0286 | 1 | False | False | WRONG | 2.38s |
| frames-0319 | 1 | True | True | CORRECT | 3.867s |
| frames-0325 | 1 | False | False | WRONG | 1.88s |
| frames-0332 | 1 | True | True | WRONG | 2.422s |
| frames-0346 | 1 | False | False | WRONG | 4.065s |
| frames-0359 | 1 | True | True | CORRECT | 3.154s |
| frames-0374 | 1 | True | True | WRONG | 2.186s |
| frames-0392 | 1 | True | True | CORRECT | 4.315s |
| frames-0411 | 1 | False | False | WRONG | 4.936s |
| frames-0426 | 1 | True | True | CORRECT | 1.841s |
| frames-0432 | 1 | False | False | WRONG | 2.517s |
| frames-0434 | 1 | False | False | WRONG | 2.36s |
| frames-0438 | 1 | False | False | WRONG | 1.662s |
| frames-0449 | 1 | True | True | CORRECT | 1.535s |
| frames-0452 | 1 | True | True | CORRECT | 4.751s |
| frames-0482 | 1 | False | False | WRONG | 3.193s |
| frames-0487 | 1 | False | False | WRONG | 3.831s |
| frames-0505 | 1 | False | False | WRONG | 2.77s |
| frames-0511 | 1 | True | True | CORRECT | 3.18s |
| frames-0521 | 1 | True | True | WRONG | 2.363s |
| frames-0544 | 1 | True | True | CORRECT | 1.713s |
| frames-0547 | 1 | True | True | WRONG | 4.836s |
| frames-0549 | 1 | True | True | CORRECT | 2.569s |
| frames-0550 | 1 | False | False | WRONG | 5.047s |
| frames-0551 | 1 | False | False | WRONG | 2.455s |
| frames-0563 | 1 | False | False | WRONG | 1.892s |
| frames-0570 | 1 | False | False | WRONG | 4.144s |
| frames-0573 | 1 | False | False | WRONG | 2.915s |
| frames-0581 | 1 | False | False | WRONG | 2.547s |
| frames-0583 | 1 | True | True | CORRECT | 1.902s |
| frames-0585 | 1 | False | False | WRONG | 2.549s |
| frames-0589 | 1 | True | True | CORRECT | 2.99s |
| frames-0603 | 1 | False | False | WRONG | 2.77s |
| frames-0612 | 1 | False | False | WRONG | 2.28s |
| frames-0619 | 1 | False | False | WRONG | 2.273s |
| frames-0630 | 1 | True | True | CORRECT | 2.431s |
| frames-0632 | 1 | False | False | WRONG | 3.118s |
| frames-0641 | 1 | False | False | WRONG | 3.384s |
| frames-0648 | 1 | False | False | WRONG | 1.858s |
| frames-0670 | 1 | True | True | CORRECT | 3.559s |
| frames-0674 | 1 | True | True | CORRECT | 2.054s |
| frames-0690 | 1 | False | False | WRONG | 5.015s |
| frames-0698 | 1 | False | False | WRONG | 4.61s |
| frames-0700 | 1 | True | True | WRONG | 2.947s |
| frames-0702 | 1 | True | True | CORRECT | 4.225s |
| frames-0715 | 1 | False | False | WRONG | 2.124s |
| frames-0719 | 1 | False | False | WRONG | 2.526s |
| frames-0737 | 1 | False | False | WRONG | 5.466s |
| frames-0741 | 1 | False | False | WRONG | 4.659s |
| frames-0746 | 1 | False | False | WRONG | 2.977s |
| frames-0749 | 1 | False | False | WRONG | 3.34s |
| frames-0765 | 1 | False | False | WRONG | 2.092s |
| frames-0766 | 1 | False | False | WRONG | 2.767s |
| frames-0771 | 1 | False | False | WRONG | 4.22s |
| frames-0784 | 1 | True | True | WRONG | 2.518s |
| frames-0789 | 1 | False | False | WRONG | 2.816s |
| frames-0796 | 1 | True | True | CORRECT | 4.053s |
| frames-0801 | 1 | False | False | WRONG | 2.305s |
| frames-0806 | 1 | True | True | CORRECT | 2.823s |
| frames-0807 | 1 | True | True | CORRECT | 2.771s |

## Misses (audit trail)

- frames-0004 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0011 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0024 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0034 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0046 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0050 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0056 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0064 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0082 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0083 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0084 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0101 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0103 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0122 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0128 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0142 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0169 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0186 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0188 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0189 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0201 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0213 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0224 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0226 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0260 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0264 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0286 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0325 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0346 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0411 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0432 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0434 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0438 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0482 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0487 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0505 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0550 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0551 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0563 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0570 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0573 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0581 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0585 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0603 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0612 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0619 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0632 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0641 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0648 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0690 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0698 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
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
- frames-0801 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)

Grading is deterministic (bench/graders.py): no LLM judge ran for this summary.
