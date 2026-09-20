# bench run: nosearch on frames

- run: 20260920-052551 (git 0a28b9f), sample `frames_n100_seed20260919` frozen 2026-09-19
- calls: 100 (100 questions x 1 repeat(s)), errors: 0
- retrieval hit-rate: **47.0%** (95% CI [37.5%, 56.7%], Wilson)
- answer accuracy (answer-producing provider): **48.0%** (47/98 CORRECT), abstains: 1 (never counted as correct)
- latency (client-side): mean 13.44s, p50 4.432s, p95 48.455s, max 144.221s

## Per-question

| id | calls | hit_all | hit_any | verdicts | mean latency |
|---|---|---|---|---|---|
| frames-0003 | 1 | True | True | CORRECT | 6.572s |
| frames-0004 | 1 | False | False | WRONG | 29.22s |
| frames-0011 | 1 | False | False | WRONG | 65.042s |
| frames-0013 | 1 | True | True | CORRECT | 1.973s |
| frames-0023 | 1 | True | True | CORRECT | 44.005s |
| frames-0024 | 1 | False | False | WRONG | 19.4s |
| frames-0034 | 1 | True | True | CORRECT | 2.967s |
| frames-0037 | 1 | True | True | CORRECT | 3.872s |
| frames-0046 | 1 | False | False | WRONG | 10.091s |
| frames-0050 | 1 | False | False | WRONG | 60.945s |
| frames-0056 | 1 | False | False | WRONG | 20.053s |
| frames-0064 | 1 | False | False | WRONG | 7.757s |
| frames-0069 | 1 | True | True | CORRECT | 7.037s |
| frames-0082 | 1 | False | False | WRONG | 3.776s |
| frames-0083 | 1 | True | True | CORRECT | 5.326s |
| frames-0084 | 1 | False | False | WRONG | 67.824s |
| frames-0085 | 1 | False | False | MISS | 48.316s |
| frames-0095 | 1 | True | True | CORRECT | 2.356s |
| frames-0100 | 1 | False | False | WRONG | 39.067s |
| frames-0101 | 1 | False | False | WRONG | 1.854s |
| frames-0103 | 1 | False | False | WRONG | 37.83s |
| frames-0104 | 1 | True | True | CORRECT | 1.293s |
| frames-0122 | 1 | False | False | WRONG | 29.833s |
| frames-0128 | 1 | False | False | WRONG | 19.954s |
| frames-0142 | 1 | False | False | WRONG | 17.738s |
| frames-0158 | 1 | True | True | CORRECT | 2.976s |
| frames-0169 | 1 | True | True | CORRECT | 5.663s |
| frames-0185 | 1 | False | False | WRONG | 5.719s |
| frames-0186 | 1 | False | False | MISS | 89.163s |
| frames-0188 | 1 | False | False | WRONG | 2.608s |
| frames-0189 | 1 | False | False | WRONG | 20.626s |
| frames-0201 | 1 | True | True | CORRECT | 7.431s |
| frames-0213 | 1 | True | True | CORRECT | 2.654s |
| frames-0224 | 1 | True | True | CORRECT | 3.947s |
| frames-0226 | 1 | True | True | CORRECT | 2.408s |
| frames-0229 | 1 | True | True | CORRECT | 6.793s |
| frames-0236 | 1 | True | True | CORRECT | 1.463s |
| frames-0260 | 1 | False | False | WRONG | 6.219s |
| frames-0264 | 1 | False | False | WRONG | 6.176s |
| frames-0273 | 1 | True | True | CORRECT | 8.603s |
| frames-0286 | 1 | False | False | ABSTAIN | 144.221s |
| frames-0319 | 1 | True | True | CORRECT | 3.021s |
| frames-0325 | 1 | True | True | CORRECT | 1.861s |
| frames-0332 | 1 | True | True | CORRECT | 2.88s |
| frames-0346 | 1 | True | True | CORRECT | 1.547s |
| frames-0359 | 1 | False | False | WRONG | 13.817s |
| frames-0374 | 1 | False | False | WRONG | 8.82s |
| frames-0392 | 1 | True | True | CORRECT | 2.954s |
| frames-0411 | 1 | True | True | CORRECT | 2.685s |
| frames-0426 | 1 | True | True | CORRECT | 5.835s |
| frames-0432 | 1 | True | True | CORRECT | 2.328s |
| frames-0434 | 1 | False | False | WRONG | 2.011s |
| frames-0438 | 1 | False | False | WRONG | 1.954s |
| frames-0449 | 1 | True | True | CORRECT | 1.943s |
| frames-0452 | 1 | True | True | CORRECT | 3.492s |
| frames-0482 | 1 | False | False | WRONG | 3.067s |
| frames-0487 | 1 | False | False | WRONG | 2.079s |
| frames-0505 | 1 | False | False | WRONG | 4.619s |
| frames-0511 | 1 | True | True | CORRECT | 4.119s |
| frames-0521 | 1 | True | True | CORRECT | 15.29s |
| frames-0544 | 1 | True | True | CORRECT | 1.182s |
| frames-0547 | 1 | False | False | WRONG | 1.822s |
| frames-0549 | 1 | True | True | CORRECT | 1.42s |
| frames-0550 | 1 | True | True | CORRECT | 4.432s |
| frames-0551 | 1 | False | False | WRONG | 2.995s |
| frames-0563 | 1 | True | True | CORRECT | 12.559s |
| frames-0570 | 1 | False | False | WRONG | 1.496s |
| frames-0573 | 1 | False | False | WRONG | 27.526s |
| frames-0581 | 1 | False | False | WRONG | 1.654s |
| frames-0583 | 1 | True | True | CORRECT | 3.904s |
| frames-0585 | 1 | True | True | CORRECT | 48.455s |
| frames-0589 | 1 | True | True | CORRECT | 4.013s |
| frames-0603 | 1 | False | False | WRONG | 16.136s |
| frames-0612 | 1 | False | False | WRONG | 14.261s |
| frames-0619 | 1 | True | True | CORRECT | 10.029s |
| frames-0630 | 1 | False | False | WRONG | 12.703s |
| frames-0632 | 1 | False | False | WRONG | 12.002s |
| frames-0641 | 1 | False | False | WRONG | 21.181s |
| frames-0648 | 1 | False | False | WRONG | 16.92s |
| frames-0670 | 1 | True | True | CORRECT | 0.884s |
| frames-0674 | 1 | True | True | CORRECT | 1.671s |
| frames-0690 | 1 | False | False | WRONG | 37.541s |
| frames-0698 | 1 | False | False | WRONG | 3.202s |
| frames-0700 | 1 | True | True | CORRECT | 3.029s |
| frames-0702 | 1 | True | True | CORRECT | 7.849s |
| frames-0715 | 1 | False | False | WRONG | 1.949s |
| frames-0719 | 1 | True | True | CORRECT | 3.872s |
| frames-0737 | 1 | False | False | WRONG | 41.06s |
| frames-0741 | 1 | False | False | WRONG | 3.165s |
| frames-0746 | 1 | False | False | WRONG | 11.627s |
| frames-0749 | 1 | True | True | CORRECT | 8.256s |
| frames-0765 | 1 | False | False | WRONG | 1.579s |
| frames-0766 | 1 | False | False | WRONG | 5.349s |
| frames-0771 | 1 | False | False | WRONG | 1.65s |
| frames-0784 | 1 | False | False | WRONG | 3.647s |
| frames-0789 | 1 | False | False | WRONG | 1.598s |
| frames-0796 | 1 | True | True | CORRECT | 1.371s |
| frames-0801 | 1 | True | True | CORRECT | 30.357s |
| frames-0806 | 1 | True | True | CORRECT | 2.312s |
| frames-0807 | 1 | False | False | WRONG | 2.263s |

## Misses (audit trail)

- frames-0004 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0011 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0024 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0046 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0050 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0056 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0064 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0082 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0084 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0085 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0100 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0101 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0103 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0122 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0128 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0142 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0185 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0186 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0188 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0189 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0260 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0264 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0286 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0359 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0374 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0434 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0438 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0482 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0487 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0505 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0547 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0551 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0570 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0573 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0581 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0603 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0612 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0630 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0632 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0641 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0648 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0690 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0698 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0715 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0737 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0741 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0746 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0765 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0766 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0771 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0784 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0789 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0807 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)

Grading is deterministic (benchlib/graders.py): no LLM judge ran for this summary.
