# bench run: exa-answer on frames

- run: 20260920-034240 (git a203acf), sample `frames_n100_seed20260919` frozen 2026-09-19
- calls: 100 (100 questions x 1 repeat(s)), errors: 0
- retrieval hit-rate: **52.0%** (95% CI [42.3%, 61.5%], Wilson)
- answer accuracy (answer-producing provider): **45.0%** (45/100 CORRECT), abstains: 0 (never counted as correct)
- latency (client-side): mean 1.229s, p50 1.159s, p95 1.543s, max 3.731s

## Per-question

| id | calls | hit_all | hit_any | verdicts | mean latency |
|---|---|---|---|---|---|
| frames-0003 | 1 | True | True | CORRECT | 1.163s |
| frames-0004 | 1 | False | False | WRONG | 1.143s |
| frames-0011 | 1 | True | True | CORRECT | 1.065s |
| frames-0013 | 1 | True | True | CORRECT | 0.98s |
| frames-0023 | 1 | True | True | CORRECT | 1.158s |
| frames-0024 | 1 | False | False | WRONG | 1.211s |
| frames-0034 | 1 | True | True | CORRECT | 1.238s |
| frames-0037 | 1 | True | True | CORRECT | 1.047s |
| frames-0046 | 1 | False | False | WRONG | 1.054s |
| frames-0050 | 1 | False | False | WRONG | 1.248s |
| frames-0056 | 1 | False | False | WRONG | 1.674s |
| frames-0064 | 1 | False | False | WRONG | 1.295s |
| frames-0069 | 1 | True | True | CORRECT | 1.176s |
| frames-0082 | 1 | True | True | CORRECT | 1.277s |
| frames-0083 | 1 | False | False | WRONG | 1.259s |
| frames-0084 | 1 | False | False | WRONG | 1.314s |
| frames-0085 | 1 | True | True | CORRECT | 1.176s |
| frames-0095 | 1 | True | True | CORRECT | 1.128s |
| frames-0100 | 1 | True | True | CORRECT | 1.083s |
| frames-0101 | 1 | False | False | WRONG | 1.008s |
| frames-0103 | 1 | True | True | WRONG | 1.411s |
| frames-0104 | 1 | True | True | CORRECT | 1.207s |
| frames-0122 | 1 | False | False | WRONG | 3.731s |
| frames-0128 | 1 | False | False | WRONG | 1.225s |
| frames-0142 | 1 | False | False | WRONG | 1.098s |
| frames-0158 | 1 | True | True | CORRECT | 1.045s |
| frames-0169 | 1 | True | True | WRONG | 1.854s |
| frames-0185 | 1 | False | False | WRONG | 1.007s |
| frames-0186 | 1 | False | False | WRONG | 1.943s |
| frames-0188 | 1 | False | False | WRONG | 1.092s |
| frames-0189 | 1 | False | False | WRONG | 1.056s |
| frames-0201 | 1 | False | False | WRONG | 1.204s |
| frames-0213 | 1 | True | True | CORRECT | 1.253s |
| frames-0224 | 1 | True | True | WRONG | 1.089s |
| frames-0226 | 1 | False | False | WRONG | 1.302s |
| frames-0229 | 1 | True | True | CORRECT | 1.417s |
| frames-0236 | 1 | True | True | CORRECT | 1.088s |
| frames-0260 | 1 | False | False | WRONG | 1.05s |
| frames-0264 | 1 | False | False | WRONG | 0.903s |
| frames-0273 | 1 | False | False | WRONG | 1.496s |
| frames-0286 | 1 | False | False | WRONG | 0.999s |
| frames-0319 | 1 | True | True | CORRECT | 1.144s |
| frames-0325 | 1 | True | True | CORRECT | 1.382s |
| frames-0332 | 1 | True | True | CORRECT | 1.135s |
| frames-0346 | 1 | True | True | CORRECT | 0.936s |
| frames-0359 | 1 | True | True | WRONG | 1.14s |
| frames-0374 | 1 | True | True | CORRECT | 1.116s |
| frames-0392 | 1 | True | True | CORRECT | 1.257s |
| frames-0411 | 1 | True | True | CORRECT | 1.066s |
| frames-0426 | 1 | True | True | CORRECT | 0.981s |
| frames-0432 | 1 | True | True | CORRECT | 1.094s |
| frames-0434 | 1 | False | False | WRONG | 1.164s |
| frames-0438 | 1 | False | False | WRONG | 1.042s |
| frames-0449 | 1 | True | True | CORRECT | 1.043s |
| frames-0452 | 1 | True | True | CORRECT | 1.023s |
| frames-0482 | 1 | False | False | WRONG | 1.159s |
| frames-0487 | 1 | False | False | WRONG | 1.139s |
| frames-0505 | 1 | False | False | WRONG | 1.453s |
| frames-0511 | 1 | True | True | CORRECT | 1.486s |
| frames-0521 | 1 | True | True | CORRECT | 1.064s |
| frames-0544 | 1 | True | True | CORRECT | 1.146s |
| frames-0547 | 1 | False | False | WRONG | 1.153s |
| frames-0549 | 1 | True | True | CORRECT | 1.523s |
| frames-0550 | 1 | True | True | WRONG | 1.048s |
| frames-0551 | 1 | False | False | WRONG | 1.208s |
| frames-0563 | 1 | True | True | CORRECT | 0.963s |
| frames-0570 | 1 | False | False | WRONG | 1.129s |
| frames-0573 | 1 | False | False | WRONG | 1.045s |
| frames-0581 | 1 | False | False | WRONG | 1.446s |
| frames-0583 | 1 | True | True | CORRECT | 1.448s |
| frames-0585 | 1 | False | False | WRONG | 1.065s |
| frames-0589 | 1 | True | True | CORRECT | 1.312s |
| frames-0603 | 1 | False | False | WRONG | 1.089s |
| frames-0612 | 1 | False | False | WRONG | 1.413s |
| frames-0619 | 1 | True | True | CORRECT | 1.227s |
| frames-0630 | 1 | True | True | CORRECT | 1.195s |
| frames-0632 | 1 | False | False | WRONG | 1.5s |
| frames-0641 | 1 | False | False | WRONG | 1.076s |
| frames-0648 | 1 | False | False | WRONG | 0.958s |
| frames-0670 | 1 | True | True | CORRECT | 1.078s |
| frames-0674 | 1 | True | True | CORRECT | 1.168s |
| frames-0690 | 1 | True | True | WRONG | 1.23s |
| frames-0698 | 1 | False | False | WRONG | 1.152s |
| frames-0700 | 1 | True | True | CORRECT | 1.402s |
| frames-0702 | 1 | True | True | CORRECT | 1.259s |
| frames-0715 | 1 | False | False | WRONG | 0.858s |
| frames-0719 | 1 | False | False | WRONG | 0.935s |
| frames-0737 | 1 | False | False | WRONG | 1.166s |
| frames-0741 | 1 | False | False | WRONG | 1.475s |
| frames-0746 | 1 | False | False | WRONG | 1.15s |
| frames-0749 | 1 | True | True | CORRECT | 1.161s |
| frames-0765 | 1 | False | False | WRONG | 1.056s |
| frames-0766 | 1 | False | False | WRONG | 1.293s |
| frames-0771 | 1 | False | False | WRONG | 1.372s |
| frames-0784 | 1 | True | True | WRONG | 1.457s |
| frames-0789 | 1 | False | False | WRONG | 0.949s |
| frames-0796 | 1 | True | True | CORRECT | 1.543s |
| frames-0801 | 1 | True | True | CORRECT | 1.298s |
| frames-0806 | 1 | True | True | CORRECT | 1.788s |
| frames-0807 | 1 | True | True | CORRECT | 1.215s |

## Misses (audit trail)

- frames-0004 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0024 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0046 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0050 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0056 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0064 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0083 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0084 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0101 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0122 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0128 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0142 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0185 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0186 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0188 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0189 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0201 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0226 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0260 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0264 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0273 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0286 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
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
- frames-0585 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0603 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0612 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0632 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0641 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0648 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0698 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0715 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0719 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0737 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0741 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0746 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0765 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0766 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0771 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- frames-0789 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)

Grading is deterministic (bench/graders.py): no LLM judge ran for this summary.
