# bench run: perplexity on frames

- run: 20260920-045040 (git f756e7a), sample `frames_n100_seed20260919` frozen 2026-09-19
- calls: 100 (100 questions x 1 repeat(s)), errors: 0
- retrieval hit-rate: **50.0%** (95% CI [40.4%, 59.6%], Wilson)
- answer accuracy (answer-producing provider): **40.0%** (40/100 CORRECT), abstains: 1 (never counted as correct)
- latency (client-side): mean 2.148s, p50 1.901s, p95 3.911s, max 6.29s

## Per-question

| id | calls | hit_all | hit_any | verdicts | mean latency |
|---|---|---|---|---|---|
| frames-0003 | 1 | True | True | CORRECT | 3.294s |
| frames-0004 | 1 | True | True | CORRECT | 1.375s |
| frames-0011 | 1 | True | True | CORRECT | 1.901s |
| frames-0013 | 1 | True | True | CORRECT | 1.397s |
| frames-0023 | 1 | True | True | CORRECT | 1.654s |
| frames-0024 | 1 | True | True | CORRECT | 2.323s |
| frames-0034 | 1 | True | True | CORRECT | 2.076s |
| frames-0037 | 1 | False | False | WRONG | 1.98s |
| frames-0046 | 1 | False | False | WRONG | 1.54s |
| frames-0050 | 1 | False | False | WRONG | 1.783s |
| frames-0056 | 1 | False | False | ABSTAIN | 6.29s |
| frames-0064 | 1 | False | False | WRONG | 2.439s |
| frames-0069 | 1 | True | True | CORRECT | 1.646s |
| frames-0082 | 1 | True | True | WRONG | 2.46s |
| frames-0083 | 1 | False | False | WRONG | 2.019s |
| frames-0084 | 1 | False | False | WRONG | 2.617s |
| frames-0085 | 1 | True | True | CORRECT | 1.82s |
| frames-0095 | 1 | True | True | CORRECT | 2.617s |
| frames-0100 | 1 | True | True | CORRECT | 2.058s |
| frames-0101 | 1 | False | False | WRONG | 1.632s |
| frames-0103 | 1 | False | False | WRONG | 2.29s |
| frames-0104 | 1 | True | True | CORRECT | 1.474s |
| frames-0122 | 1 | False | False | WRONG | 1.873s |
| frames-0128 | 1 | False | False | WRONG | 3.744s |
| frames-0142 | 1 | True | True | CORRECT | 1.639s |
| frames-0158 | 1 | True | True | CORRECT | 1.729s |
| frames-0169 | 1 | True | True | CORRECT | 3.877s |
| frames-0185 | 1 | False | False | WRONG | 2.16s |
| frames-0186 | 1 | False | False | WRONG | 4.075s |
| frames-0188 | 1 | True | True | WRONG | 1.379s |
| frames-0189 | 1 | False | False | WRONG | 1.479s |
| frames-0201 | 1 | False | False | WRONG | 2.563s |
| frames-0213 | 1 | True | True | CORRECT | 4.01s |
| frames-0224 | 1 | False | False | WRONG | 1.999s |
| frames-0226 | 1 | False | False | WRONG | 2.029s |
| frames-0229 | 1 | False | False | WRONG | 4.478s |
| frames-0236 | 1 | True | True | WRONG | 1.596s |
| frames-0260 | 1 | True | True | WRONG | 1.465s |
| frames-0264 | 1 | False | False | WRONG | 1.68s |
| frames-0273 | 1 | False | False | WRONG | 1.47s |
| frames-0286 | 1 | False | False | WRONG | 2.992s |
| frames-0319 | 1 | True | True | CORRECT | 1.735s |
| frames-0325 | 1 | True | True | CORRECT | 3.045s |
| frames-0332 | 1 | True | True | CORRECT | 1.756s |
| frames-0346 | 1 | True | True | CORRECT | 1.473s |
| frames-0359 | 1 | True | True | CORRECT | 1.266s |
| frames-0374 | 1 | True | True | CORRECT | 1.541s |
| frames-0392 | 1 | False | False | WRONG | 1.59s |
| frames-0411 | 1 | True | True | CORRECT | 1.472s |
| frames-0426 | 1 | True | True | CORRECT | 1.366s |
| frames-0432 | 1 | True | True | CORRECT | 1.541s |
| frames-0434 | 1 | False | False | WRONG | 2.608s |
| frames-0438 | 1 | False | False | WRONG | 1.843s |
| frames-0449 | 1 | True | True | CORRECT | 2.36s |
| frames-0452 | 1 | True | True | CORRECT | 1.611s |
| frames-0482 | 1 | False | False | WRONG | 1.515s |
| frames-0487 | 1 | False | False | WRONG | 1.558s |
| frames-0505 | 1 | False | False | WRONG | 2.45s |
| frames-0511 | 1 | True | True | CORRECT | 3.911s |
| frames-0521 | 1 | True | True | WRONG | 1.705s |
| frames-0544 | 1 | True | True | CORRECT | 1.96s |
| frames-0547 | 1 | False | False | WRONG | 1.755s |
| frames-0549 | 1 | True | True | WRONG | 1.663s |
| frames-0550 | 1 | True | True | WRONG | 1.429s |
| frames-0551 | 1 | False | False | WRONG | 2.274s |
| frames-0563 | 1 | True | True | CORRECT | 2.113s |
| frames-0570 | 1 | False | False | WRONG | 1.271s |
| frames-0573 | 1 | True | True | WRONG | 3.06s |
| frames-0581 | 1 | False | False | WRONG | 2.361s |
| frames-0583 | 1 | False | False | WRONG | 1.689s |
| frames-0585 | 1 | False | False | WRONG | 1.946s |
| frames-0589 | 1 | True | True | WRONG | 1.945s |
| frames-0603 | 1 | False | False | WRONG | 1.852s |
| frames-0612 | 1 | False | False | WRONG | 1.935s |
| frames-0619 | 1 | True | True | CORRECT | 1.319s |
| frames-0630 | 1 | True | True | CORRECT | 1.648s |
| frames-0632 | 1 | False | False | WRONG | 1.91s |
| frames-0641 | 1 | False | False | WRONG | 2.448s |
| frames-0648 | 1 | True | True | CORRECT | 3.029s |
| frames-0670 | 1 | True | True | CORRECT | 2.558s |
| frames-0674 | 1 | True | True | CORRECT | 1.591s |
| frames-0690 | 1 | False | False | WRONG | 2.87s |
| frames-0698 | 1 | False | False | WRONG | 3.079s |
| frames-0700 | 1 | True | True | WRONG | 1.823s |
| frames-0702 | 1 | True | True | CORRECT | 1.695s |
| frames-0715 | 1 | False | False | WRONG | 1.395s |
| frames-0719 | 1 | False | False | WRONG | 1.449s |
| frames-0737 | 1 | False | False | WRONG | 2.389s |
| frames-0741 | 1 | False | False | WRONG | 2.326s |
| frames-0746 | 1 | False | False | WRONG | 2.128s |
| frames-0749 | 1 | False | False | WRONG | 1.172s |
| frames-0765 | 1 | False | False | WRONG | 5.305s |
| frames-0766 | 1 | False | False | WRONG | 1.523s |
| frames-0771 | 1 | False | False | WRONG | 2.537s |
| frames-0784 | 1 | False | False | WRONG | 1.752s |
| frames-0789 | 1 | False | False | WRONG | 2.306s |
| frames-0796 | 1 | True | True | CORRECT | 2.486s |
| frames-0801 | 1 | True | True | CORRECT | 1.432s |
| frames-0806 | 1 | True | True | CORRECT | 2.108s |
| frames-0807 | 1 | True | True | CORRECT | 2.003s |

## Misses (audit trail)

- frames-0037 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0046 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0050 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0056 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0064 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0083 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0084 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0101 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0103 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0122 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0128 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0185 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0186 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0189 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0201 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0224 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0226 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0229 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0264 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0273 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0286 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0392 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0434 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0438 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0482 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0487 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0505 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0547 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0551 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0570 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0581 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0583 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0585 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0603 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0612 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0632 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0641 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
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
- frames-0784 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0789 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)

Grading is deterministic (benchlib/graders.py): no LLM judge ran for this summary.
