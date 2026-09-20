# bench run: serper on frames

- run: 20260920-030328 (git 98bc1f0), sample `frames_n100_seed20260919` frozen 2026-09-19
- calls: 100 (100 questions x 1 repeat(s)), errors: 0
- retrieval hit-rate: **24.0%** (95% CI [16.7%, 33.2%], Wilson)
- latency (client-side): mean 1.866s, p50 1.348s, p95 4.075s, max 8.63s

## Per-question

| id | calls | hit_all | hit_any | verdicts | mean latency |
|---|---|---|---|---|---|
| frames-0003 | 1 | True | True | MISS | 1.96s |
| frames-0004 | 1 | True | True | MISS | 1.253s |
| frames-0011 | 1 | True | True | MISS | 4.763s |
| frames-0013 | 1 | False | False | MISS | 4.682s |
| frames-0023 | 1 | True | True | MISS | 1.324s |
| frames-0024 | 1 | False | False | MISS | 1.214s |
| frames-0034 | 1 | False | False | MISS | 1.717s |
| frames-0037 | 1 | False | False | MISS | 1.464s |
| frames-0046 | 1 | False | False | MISS | 1.034s |
| frames-0050 | 1 | False | False | MISS | 3.833s |
| frames-0056 | 1 | False | False | MISS | 3.231s |
| frames-0064 | 1 | False | False | MISS | 1.002s |
| frames-0069 | 1 | True | True | MISS | 0.968s |
| frames-0082 | 1 | False | False | MISS | 2.322s |
| frames-0083 | 1 | False | False | MISS | 1.219s |
| frames-0084 | 1 | False | False | MISS | 0.886s |
| frames-0085 | 1 | True | True | MISS | 1.417s |
| frames-0095 | 1 | False | False | MISS | 1.318s |
| frames-0100 | 1 | True | True | MISS | 4.034s |
| frames-0101 | 1 | False | False | MISS | 1.267s |
| frames-0103 | 1 | False | False | MISS | 2.194s |
| frames-0104 | 1 | False | False | MISS | 1.25s |
| frames-0122 | 1 | False | False | MISS | 0.884s |
| frames-0128 | 1 | False | False | MISS | 1.939s |
| frames-0142 | 1 | False | False | MISS | 1.869s |
| frames-0158 | 1 | True | True | MISS | 0.966s |
| frames-0169 | 1 | False | False | MISS | 3.474s |
| frames-0185 | 1 | False | False | MISS | 1.299s |
| frames-0186 | 1 | False | False | MISS | 4.113s |
| frames-0188 | 1 | False | False | MISS | 1.348s |
| frames-0189 | 1 | False | False | MISS | 4.009s |
| frames-0201 | 1 | False | False | MISS | 3.767s |
| frames-0213 | 1 | False | False | MISS | 2.141s |
| frames-0224 | 1 | False | False | MISS | 1.414s |
| frames-0226 | 1 | False | False | MISS | 1.788s |
| frames-0229 | 1 | False | False | MISS | 0.987s |
| frames-0236 | 1 | True | True | MISS | 1.223s |
| frames-0260 | 1 | False | False | MISS | 1.2s |
| frames-0264 | 1 | False | False | MISS | 1.187s |
| frames-0273 | 1 | True | True | MISS | 1.074s |
| frames-0286 | 1 | False | False | MISS | 3.267s |
| frames-0319 | 1 | True | True | MISS | 1.251s |
| frames-0325 | 1 | False | False | MISS | 1.621s |
| frames-0332 | 1 | True | True | MISS | 0.888s |
| frames-0346 | 1 | False | False | MISS | 1.797s |
| frames-0359 | 1 | True | True | MISS | 1.126s |
| frames-0374 | 1 | True | True | MISS | 1.396s |
| frames-0392 | 1 | False | False | MISS | 1.714s |
| frames-0411 | 1 | False | False | MISS | 1.353s |
| frames-0426 | 1 | False | False | MISS | 2.736s |
| frames-0432 | 1 | False | False | MISS | 1.372s |
| frames-0434 | 1 | False | False | MISS | 1.149s |
| frames-0438 | 1 | False | False | MISS | 1.314s |
| frames-0449 | 1 | True | True | MISS | 0.635s |
| frames-0452 | 1 | True | True | MISS | 1.271s |
| frames-0482 | 1 | False | False | MISS | 1.173s |
| frames-0487 | 1 | False | False | MISS | 2.298s |
| frames-0505 | 1 | False | False | MISS | 1.457s |
| frames-0511 | 1 | True | True | MISS | 1.863s |
| frames-0521 | 1 | True | True | MISS | 1.098s |
| frames-0544 | 1 | True | True | MISS | 0.965s |
| frames-0547 | 1 | False | False | MISS | 1.289s |
| frames-0549 | 1 | True | True | MISS | 1.184s |
| frames-0550 | 1 | True | True | MISS | 1.223s |
| frames-0551 | 1 | False | False | MISS | 2.33s |
| frames-0563 | 1 | False | False | MISS | 0.936s |
| frames-0570 | 1 | False | False | MISS | 3.403s |
| frames-0573 | 1 | False | False | MISS | 8.63s |
| frames-0581 | 1 | False | False | MISS | 1.283s |
| frames-0583 | 1 | False | False | MISS | 0.95s |
| frames-0585 | 1 | False | False | MISS | 2.058s |
| frames-0589 | 1 | False | False | MISS | 2.37s |
| frames-0603 | 1 | False | False | MISS | 1.66s |
| frames-0612 | 1 | False | False | MISS | 1.344s |
| frames-0619 | 1 | False | False | MISS | 2.26s |
| frames-0630 | 1 | False | False | MISS | 1.546s |
| frames-0632 | 1 | False | False | MISS | 1.613s |
| frames-0641 | 1 | False | False | MISS | 2.509s |
| frames-0648 | 1 | False | False | MISS | 0.983s |
| frames-0670 | 1 | True | True | MISS | 5.822s |
| frames-0674 | 1 | False | False | MISS | 3.815s |
| frames-0690 | 1 | False | False | MISS | 1.988s |
| frames-0698 | 1 | False | False | MISS | 1.802s |
| frames-0700 | 1 | True | True | MISS | 1.079s |
| frames-0702 | 1 | False | False | MISS | 1.004s |
| frames-0715 | 1 | False | False | MISS | 0.707s |
| frames-0719 | 1 | False | False | MISS | 2.151s |
| frames-0737 | 1 | False | False | MISS | 3.587s |
| frames-0741 | 1 | False | False | MISS | 1.546s |
| frames-0746 | 1 | False | False | MISS | 1.302s |
| frames-0749 | 1 | False | False | MISS | 0.793s |
| frames-0765 | 1 | False | False | MISS | 1.017s |
| frames-0766 | 1 | False | False | MISS | 0.897s |
| frames-0771 | 1 | False | False | MISS | 4.075s |
| frames-0784 | 1 | False | False | MISS | 0.946s |
| frames-0789 | 1 | False | False | MISS | 0.929s |
| frames-0796 | 1 | False | False | MISS | 1.098s |
| frames-0801 | 1 | False | False | MISS | 1.542s |
| frames-0806 | 1 | True | True | MISS | 1.053s |
| frames-0807 | 1 | False | False | MISS | 1.138s |

## Misses (audit trail)

- frames-0013 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
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
- frames-0213 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0224 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0226 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0229 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0260 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0264 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0286 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0325 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0346 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
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
- frames-0589 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0603 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0612 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0619 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0630 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0632 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0641 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0648 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
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
- frames-0784 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0789 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0796 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0801 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0807 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)

Grading is deterministic (bench/graders.py): no LLM judge ran for this summary.
