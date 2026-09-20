# bench run: ransack-research on frames

- run: 20260920-030321 (git 98bc1f0), sample `frames_n100_seed20260919` frozen 2026-09-19
- calls: 100 (100 questions x 1 repeat(s)), errors: 0
- retrieval hit-rate: **36.0%** (95% CI [27.3%, 45.8%], Wilson)
- answer accuracy (answer-producing provider): **26.0%** (26/100 CORRECT), abstains: 2 (never counted as correct)
- latency (client-side): mean 19.306s, p50 21.324s, p95 29.551s, max 33.844s

## Per-question

| id | calls | hit_all | hit_any | verdicts | mean latency |
|---|---|---|---|---|---|
| frames-0003 | 1 | False | False | ABSTAIN | 8.78s |
| frames-0004 | 1 | True | True | CORRECT | 4.715s |
| frames-0011 | 1 | True | True | CORRECT | 4.914s |
| frames-0013 | 1 | True | True | WRONG | 4.614s |
| frames-0023 | 1 | True | True | CORRECT | 29.444s |
| frames-0024 | 1 | True | True | WRONG | 29.537s |
| frames-0034 | 1 | False | False | WRONG | 4.68s |
| frames-0037 | 1 | True | True | WRONG | 13.414s |
| frames-0046 | 1 | False | False | WRONG | 4.67s |
| frames-0050 | 1 | False | False | WRONG | 8.873s |
| frames-0056 | 1 | False | False | WRONG | 29.857s |
| frames-0064 | 1 | False | False | WRONG | 25.545s |
| frames-0069 | 1 | False | False | WRONG | 17.037s |
| frames-0082 | 1 | False | False | WRONG | 12.977s |
| frames-0083 | 1 | False | False | WRONG | 29.546s |
| frames-0084 | 1 | False | False | WRONG | 29.397s |
| frames-0085 | 1 | True | True | CORRECT | 29.405s |
| frames-0095 | 1 | False | False | WRONG | 29.417s |
| frames-0100 | 1 | True | True | WRONG | 29.429s |
| frames-0101 | 1 | False | False | WRONG | 29.428s |
| frames-0103 | 1 | False | False | WRONG | 21.253s |
| frames-0104 | 1 | True | True | CORRECT | 12.944s |
| frames-0122 | 1 | False | False | WRONG | 17.654s |
| frames-0128 | 1 | False | False | WRONG | 29.454s |
| frames-0142 | 1 | True | True | CORRECT | 4.621s |
| frames-0158 | 1 | True | True | CORRECT | 29.456s |
| frames-0169 | 1 | False | False | WRONG | 12.897s |
| frames-0185 | 1 | False | False | WRONG | 29.38s |
| frames-0186 | 1 | False | False | WRONG | 29.485s |
| frames-0188 | 1 | False | False | WRONG | 4.682s |
| frames-0189 | 1 | False | False | WRONG | 8.991s |
| frames-0201 | 1 | False | False | WRONG | 4.599s |
| frames-0213 | 1 | True | True | CORRECT | 4.644s |
| frames-0224 | 1 | False | False | WRONG | 29.551s |
| frames-0226 | 1 | False | False | WRONG | 4.834s |
| frames-0229 | 1 | True | True | WRONG | 25.705s |
| frames-0236 | 1 | False | False | WRONG | 29.613s |
| frames-0260 | 1 | False | False | WRONG | 29.369s |
| frames-0264 | 1 | False | False | WRONG | 29.477s |
| frames-0273 | 1 | True | True | WRONG | 12.941s |
| frames-0286 | 1 | False | False | WRONG | 17.162s |
| frames-0319 | 1 | True | True | WRONG | 29.399s |
| frames-0325 | 1 | True | True | WRONG | 4.652s |
| frames-0332 | 1 | True | True | CORRECT | 12.881s |
| frames-0346 | 1 | False | False | WRONG | 13.007s |
| frames-0359 | 1 | False | False | WRONG | 29.472s |
| frames-0374 | 1 | True | True | CORRECT | 8.797s |
| frames-0392 | 1 | False | False | ABSTAIN | 12.874s |
| frames-0411 | 1 | True | True | CORRECT | 4.704s |
| frames-0426 | 1 | False | False | WRONG | 21.133s |
| frames-0432 | 1 | True | True | CORRECT | 17.001s |
| frames-0434 | 1 | False | False | WRONG | 12.89s |
| frames-0438 | 1 | False | False | WRONG | 29.426s |
| frames-0449 | 1 | True | True | CORRECT | 29.432s |
| frames-0452 | 1 | True | True | CORRECT | 4.677s |
| frames-0482 | 1 | False | False | WRONG | 4.637s |
| frames-0487 | 1 | False | False | WRONG | 4.652s |
| frames-0505 | 1 | False | False | WRONG | 29.534s |
| frames-0511 | 1 | True | True | CORRECT | 29.5s |
| frames-0521 | 1 | True | True | CORRECT | 25.714s |
| frames-0544 | 1 | True | True | CORRECT | 29.452s |
| frames-0547 | 1 | False | False | WRONG | 29.523s |
| frames-0549 | 1 | True | True | CORRECT | 29.572s |
| frames-0550 | 1 | False | False | WRONG | 25.31s |
| frames-0551 | 1 | True | True | CORRECT | 29.421s |
| frames-0563 | 1 | False | False | WRONG | 25.319s |
| frames-0570 | 1 | False | False | WRONG | 4.649s |
| frames-0573 | 1 | False | False | WRONG | 4.702s |
| frames-0581 | 1 | False | False | WRONG | 25.414s |
| frames-0583 | 1 | False | False | WRONG | 29.587s |
| frames-0585 | 1 | False | False | WRONG | 21.67s |
| frames-0589 | 1 | True | True | WRONG | 29.488s |
| frames-0603 | 1 | False | False | WRONG | 4.646s |
| frames-0612 | 1 | False | False | WRONG | 29.447s |
| frames-0619 | 1 | False | False | WRONG | 21.161s |
| frames-0630 | 1 | True | True | CORRECT | 4.683s |
| frames-0632 | 1 | False | False | WRONG | 25.269s |
| frames-0641 | 1 | False | False | WRONG | 29.501s |
| frames-0648 | 1 | True | True | CORRECT | 4.857s |
| frames-0670 | 1 | False | False | WRONG | 26.047s |
| frames-0674 | 1 | True | True | CORRECT | 21.235s |
| frames-0690 | 1 | False | False | WRONG | 29.419s |
| frames-0698 | 1 | False | False | WRONG | 25.289s |
| frames-0700 | 1 | False | False | WRONG | 29.454s |
| frames-0702 | 1 | False | False | WRONG | 29.54s |
| frames-0715 | 1 | False | False | WRONG | 4.636s |
| frames-0719 | 1 | False | False | WRONG | 29.48s |
| frames-0737 | 1 | False | False | WRONG | 4.603s |
| frames-0741 | 1 | False | False | WRONG | 25.331s |
| frames-0746 | 1 | False | False | WRONG | 4.679s |
| frames-0749 | 1 | False | False | WRONG | 29.449s |
| frames-0765 | 1 | False | False | WRONG | 33.844s |
| frames-0766 | 1 | False | False | WRONG | 21.3s |
| frames-0771 | 1 | False | False | WRONG | 25.612s |
| frames-0784 | 1 | True | True | WRONG | 21.324s |
| frames-0789 | 1 | False | False | WRONG | 21.216s |
| frames-0796 | 1 | True | True | CORRECT | 4.603s |
| frames-0801 | 1 | True | True | CORRECT | 21.219s |
| frames-0806 | 1 | True | True | CORRECT | 4.607s |
| frames-0807 | 1 | True | True | CORRECT | 25.222s |

## Misses (audit trail)

- frames-0003 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0034 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
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
- frames-0122 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0128 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
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
- frames-0286 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0346 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0359 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0392 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0426 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0434 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0438 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0482 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0487 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0505 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0547 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0550 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0563 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0570 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0573 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0581 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0583 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0585 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0603 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0612 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0619 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0632 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0641 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0670 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0690 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0698 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0700 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
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

Grading is deterministic (bench/graders.py): no LLM judge ran for this summary.
