# bench run: ransack on frames

- run: 20260920-025450 (git 98bc1f0), sample `frames_n100_seed20260919` frozen 2026-09-19
- calls: 100 (100 questions x 1 repeat(s)), errors: 0
- retrieval hit-rate: **20.0%** (95% CI [13.3%, 28.9%], Wilson)
- latency (client-side): mean 3.028s, p50 2.783s, p95 5.654s, max 10.581s

## Per-question

| id | calls | hit_all | hit_any | verdicts | mean latency |
|---|---|---|---|---|---|
| frames-0003 | 1 | True | True | MISS | 0.657s |
| frames-0004 | 1 | False | False | MISS | 0.573s |
| frames-0011 | 1 | False | False | MISS | 1.027s |
| frames-0013 | 1 | False | False | MISS | 0.538s |
| frames-0023 | 1 | False | False | MISS | 0.484s |
| frames-0024 | 1 | False | False | MISS | 0.512s |
| frames-0034 | 1 | False | False | MISS | 0.491s |
| frames-0037 | 1 | False | False | MISS | 0.524s |
| frames-0046 | 1 | False | False | MISS | 0.472s |
| frames-0050 | 1 | False | False | MISS | 0.474s |
| frames-0056 | 1 | False | False | MISS | 10.581s |
| frames-0064 | 1 | False | False | MISS | 4.344s |
| frames-0069 | 1 | True | True | MISS | 2.307s |
| frames-0082 | 1 | False | False | MISS | 3.076s |
| frames-0083 | 1 | False | False | MISS | 5.207s |
| frames-0084 | 1 | False | False | MISS | 3.22s |
| frames-0085 | 1 | True | True | MISS | 2.32s |
| frames-0095 | 1 | False | False | MISS | 2.209s |
| frames-0100 | 1 | True | True | MISS | 2.455s |
| frames-0101 | 1 | False | False | MISS | 1.913s |
| frames-0103 | 1 | False | False | MISS | 2.783s |
| frames-0104 | 1 | False | False | MISS | 1.883s |
| frames-0122 | 1 | False | False | MISS | 5.081s |
| frames-0128 | 1 | False | False | MISS | 4.108s |
| frames-0142 | 1 | False | False | MISS | 3.076s |
| frames-0158 | 1 | True | True | MISS | 3.822s |
| frames-0169 | 1 | False | False | MISS | 9.525s |
| frames-0185 | 1 | False | False | MISS | 2.159s |
| frames-0186 | 1 | False | False | MISS | 3.002s |
| frames-0188 | 1 | False | False | MISS | 4.25s |
| frames-0189 | 1 | False | False | MISS | 1.753s |
| frames-0201 | 1 | False | False | MISS | 1.951s |
| frames-0213 | 1 | True | True | MISS | 7.103s |
| frames-0224 | 1 | False | False | MISS | 2.718s |
| frames-0226 | 1 | False | False | MISS | 7.967s |
| frames-0229 | 1 | False | False | MISS | 4.757s |
| frames-0236 | 1 | True | True | MISS | 1.724s |
| frames-0260 | 1 | False | False | MISS | 3.774s |
| frames-0264 | 1 | False | False | MISS | 3.972s |
| frames-0273 | 1 | False | False | MISS | 3.101s |
| frames-0286 | 1 | False | False | MISS | 4.669s |
| frames-0319 | 1 | True | True | MISS | 3.402s |
| frames-0325 | 1 | False | False | MISS | 1.898s |
| frames-0332 | 1 | True | True | MISS | 4.065s |
| frames-0346 | 1 | False | False | MISS | 4.351s |
| frames-0359 | 1 | False | False | MISS | 2.898s |
| frames-0374 | 1 | True | True | MISS | 2.119s |
| frames-0392 | 1 | False | False | MISS | 2.557s |
| frames-0411 | 1 | False | False | MISS | 2.384s |
| frames-0426 | 1 | False | False | MISS | 3.223s |
| frames-0432 | 1 | False | False | MISS | 3.24s |
| frames-0434 | 1 | False | False | MISS | 2.513s |
| frames-0438 | 1 | False | False | MISS | 3.512s |
| frames-0449 | 1 | True | True | MISS | 2.52s |
| frames-0452 | 1 | True | True | MISS | 3.38s |
| frames-0482 | 1 | False | False | MISS | 2.434s |
| frames-0487 | 1 | False | False | MISS | 4.954s |
| frames-0505 | 1 | False | False | MISS | 2.221s |
| frames-0511 | 1 | True | True | MISS | 3.125s |
| frames-0521 | 1 | True | True | MISS | 1.718s |
| frames-0544 | 1 | True | True | MISS | 3.178s |
| frames-0547 | 1 | False | False | MISS | 4.113s |
| frames-0549 | 1 | True | True | MISS | 2.852s |
| frames-0550 | 1 | True | True | MISS | 2.194s |
| frames-0551 | 1 | False | False | MISS | 3.176s |
| frames-0563 | 1 | False | False | MISS | 1.783s |
| frames-0570 | 1 | False | False | MISS | 2.347s |
| frames-0573 | 1 | False | False | MISS | 2.868s |
| frames-0581 | 1 | False | False | MISS | 2.941s |
| frames-0583 | 1 | False | False | MISS | 2.04s |
| frames-0585 | 1 | False | False | MISS | 3.141s |
| frames-0589 | 1 | True | True | MISS | 2.599s |
| frames-0603 | 1 | False | False | MISS | 7.421s |
| frames-0612 | 1 | False | False | MISS | 3.723s |
| frames-0619 | 1 | False | False | MISS | 1.711s |
| frames-0630 | 1 | False | False | MISS | 2.047s |
| frames-0632 | 1 | False | False | MISS | 3.69s |
| frames-0641 | 1 | False | False | MISS | 2.587s |
| frames-0648 | 1 | False | False | MISS | 2.196s |
| frames-0670 | 1 | False | False | MISS | 1.868s |
| frames-0674 | 1 | False | False | MISS | 1.819s |
| frames-0690 | 1 | False | False | MISS | 2.31s |
| frames-0698 | 1 | False | False | MISS | 2.967s |
| frames-0700 | 1 | True | True | MISS | 4.476s |
| frames-0702 | 1 | True | True | MISS | 1.767s |
| frames-0715 | 1 | False | False | MISS | 4.554s |
| frames-0719 | 1 | False | False | MISS | 4.339s |
| frames-0737 | 1 | False | False | MISS | 5.654s |
| frames-0741 | 1 | False | False | MISS | 3.808s |
| frames-0746 | 1 | False | False | MISS | 2.069s |
| frames-0749 | 1 | False | False | MISS | 5.494s |
| frames-0765 | 1 | False | False | MISS | 2.851s |
| frames-0766 | 1 | False | False | MISS | 2.705s |
| frames-0771 | 1 | False | False | MISS | 3.465s |
| frames-0784 | 1 | False | False | MISS | 2.982s |
| frames-0789 | 1 | False | False | MISS | 1.866s |
| frames-0796 | 1 | False | False | MISS | 1.672s |
| frames-0801 | 1 | False | False | MISS | 1.79s |
| frames-0806 | 1 | False | False | MISS | 2.884s |
| frames-0807 | 1 | False | False | MISS | 1.784s |

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
- frames-0056 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0064 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
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
- frames-0325 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0346 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0359 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0392 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0411 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0426 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0432 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0434 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0438 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0482 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0487 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0505 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0547 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
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
- frames-0796 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0801 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0806 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0807 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)

Grading is deterministic (bench/graders.py): no LLM judge ran for this summary.
