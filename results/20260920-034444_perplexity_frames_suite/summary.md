# bench run: perplexity on frames

- run: 20260920-034444 (git a203acf), sample `frames_n100_seed20260919` frozen 2026-09-19
- calls: 100 (100 questions x 1 repeat(s)), errors: 50
- retrieval hit-rate: **38.0%** (95% CI [25.9%, 51.8%], Wilson)
- answer accuracy (answer-producing provider): **26.0%** (13/50 CORRECT), abstains: 0 (never counted as correct)
- latency (client-side): mean 2.151s, p50 1.838s, p95 4.316s, max 5.906s

## Per-question

| id | calls | hit_all | hit_any | verdicts | mean latency |
|---|---|---|---|---|---|
| frames-0003 | 1 | True | True | WRONG | 1.76s |
| frames-0004 | 1 | False | False | ERROR | 0.16s |
| frames-0011 | 1 | False | False | ERROR | 0.15s |
| frames-0013 | 1 | False | False | ERROR | 0.148s |
| frames-0023 | 1 | True | True | CORRECT | 1.58s |
| frames-0024 | 1 | False | False | ERROR | 0.161s |
| frames-0034 | 1 | False | False | ERROR | 0.153s |
| frames-0037 | 1 | False | False | ERROR | 0.144s |
| frames-0046 | 1 | False | False | WRONG | 1.587s |
| frames-0050 | 1 | False | False | WRONG | 1.632s |
| frames-0056 | 1 | False | False | ERROR | 0.156s |
| frames-0064 | 1 | False | False | ERROR | 0.154s |
| frames-0069 | 1 | False | False | ERROR | 0.174s |
| frames-0082 | 1 | True | True | WRONG | 1.688s |
| frames-0083 | 1 | False | False | ERROR | 0.161s |
| frames-0084 | 1 | False | False | ERROR | 0.163s |
| frames-0085 | 1 | False | False | ERROR | 0.15s |
| frames-0095 | 1 | False | False | ERROR | 0.167s |
| frames-0100 | 1 | False | False | ERROR | 0.16s |
| frames-0101 | 1 | False | False | WRONG | 1.515s |
| frames-0103 | 1 | False | False | WRONG | 1.946s |
| frames-0104 | 1 | False | False | ERROR | 0.166s |
| frames-0122 | 1 | False | False | WRONG | 1.975s |
| frames-0128 | 1 | False | False | ERROR | 0.189s |
| frames-0142 | 1 | False | False | ERROR | 0.164s |
| frames-0158 | 1 | False | False | ERROR | 0.17s |
| frames-0169 | 1 | True | True | CORRECT | 4.316s |
| frames-0185 | 1 | False | False | ERROR | 0.152s |
| frames-0186 | 1 | False | False | WRONG | 4.891s |
| frames-0188 | 1 | False | False | ERROR | 0.187s |
| frames-0189 | 1 | False | False | ERROR | 0.148s |
| frames-0201 | 1 | False | False | WRONG | 1.999s |
| frames-0213 | 1 | False | False | ERROR | 0.201s |
| frames-0224 | 1 | True | True | CORRECT | 2.721s |
| frames-0226 | 1 | False | False | WRONG | 2.313s |
| frames-0229 | 1 | False | False | WRONG | 3.183s |
| frames-0236 | 1 | True | True | WRONG | 1.676s |
| frames-0260 | 1 | False | False | ERROR | 0.164s |
| frames-0264 | 1 | False | False | ERROR | 0.149s |
| frames-0273 | 1 | False | False | ERROR | 0.166s |
| frames-0286 | 1 | False | False | WRONG | 2.385s |
| frames-0319 | 1 | True | True | CORRECT | 1.719s |
| frames-0325 | 1 | False | False | ERROR | 0.176s |
| frames-0332 | 1 | False | False | ERROR | 0.157s |
| frames-0346 | 1 | False | False | ERROR | 0.153s |
| frames-0359 | 1 | True | True | CORRECT | 1.548s |
| frames-0374 | 1 | True | True | CORRECT | 1.561s |
| frames-0392 | 1 | False | False | ERROR | 0.153s |
| frames-0411 | 1 | False | False | ERROR | 0.165s |
| frames-0426 | 1 | False | False | ERROR | 0.159s |
| frames-0432 | 1 | False | False | ERROR | 0.163s |
| frames-0434 | 1 | False | False | WRONG | 1.747s |
| frames-0438 | 1 | False | False | ERROR | 0.16s |
| frames-0449 | 1 | False | False | ERROR | 0.154s |
| frames-0452 | 1 | False | False | ERROR | 0.165s |
| frames-0482 | 1 | False | False | WRONG | 1.486s |
| frames-0487 | 1 | False | False | ERROR | 0.162s |
| frames-0505 | 1 | False | False | ERROR | 0.311s |
| frames-0511 | 1 | False | False | ERROR | 0.152s |
| frames-0521 | 1 | True | True | WRONG | 1.878s |
| frames-0544 | 1 | False | False | ERROR | 0.159s |
| frames-0547 | 1 | False | False | ERROR | 0.148s |
| frames-0549 | 1 | True | True | CORRECT | 1.784s |
| frames-0550 | 1 | False | False | ERROR | 0.153s |
| frames-0551 | 1 | False | False | ERROR | 0.17s |
| frames-0563 | 1 | False | False | ERROR | 0.152s |
| frames-0570 | 1 | False | False | WRONG | 2.12s |
| frames-0573 | 1 | True | True | WRONG | 3.063s |
| frames-0581 | 1 | False | False | WRONG | 3.184s |
| frames-0583 | 1 | False | False | WRONG | 1.664s |
| frames-0585 | 1 | False | False | ERROR | 0.146s |
| frames-0589 | 1 | False | False | ERROR | 0.184s |
| frames-0603 | 1 | False | False | ERROR | 0.186s |
| frames-0612 | 1 | False | False | WRONG | 1.822s |
| frames-0619 | 1 | False | False | ERROR | 0.184s |
| frames-0630 | 1 | False | False | ERROR | 0.152s |
| frames-0632 | 1 | False | False | WRONG | 2.577s |
| frames-0641 | 1 | False | False | WRONG | 1.808s |
| frames-0648 | 1 | False | False | ERROR | 0.158s |
| frames-0670 | 1 | False | False | ERROR | 0.179s |
| frames-0674 | 1 | True | True | CORRECT | 1.529s |
| frames-0690 | 1 | False | False | WRONG | 1.787s |
| frames-0698 | 1 | False | False | WRONG | 1.838s |
| frames-0700 | 1 | True | True | WRONG | 1.88s |
| frames-0702 | 1 | True | True | CORRECT | 2.12s |
| frames-0715 | 1 | False | False | WRONG | 1.502s |
| frames-0719 | 1 | False | False | WRONG | 2.008s |
| frames-0737 | 1 | False | False | WRONG | 2.326s |
| frames-0741 | 1 | False | False | WRONG | 2.395s |
| frames-0746 | 1 | False | False | WRONG | 2.523s |
| frames-0749 | 1 | False | False | WRONG | 1.981s |
| frames-0765 | 1 | False | False | WRONG | 1.497s |
| frames-0766 | 1 | False | False | WRONG | 1.638s |
| frames-0771 | 1 | False | False | WRONG | 1.824s |
| frames-0784 | 1 | False | False | WRONG | 1.978s |
| frames-0789 | 1 | False | False | WRONG | 2.103s |
| frames-0796 | 1 | True | True | CORRECT | 1.692s |
| frames-0801 | 1 | True | True | CORRECT | 5.906s |
| frames-0806 | 1 | True | True | CORRECT | 2.35s |
| frames-0807 | 1 | True | True | CORRECT | 1.536s |

## Misses (audit trail)

- frames-0046 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0050 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0101 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0103 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0122 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0186 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0201 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0226 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0229 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0286 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0434 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0482 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0570 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0581 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0583 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
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

Grading is deterministic (bench/graders.py): no LLM judge ran for this summary.
