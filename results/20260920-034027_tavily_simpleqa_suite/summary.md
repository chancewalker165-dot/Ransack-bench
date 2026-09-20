# bench run: tavily on simpleqa

- run: 20260920-034027 (git a203acf), sample `simpleqa_n200_seed20260919` frozen 2026-09-19
- calls: 100 (100 questions x 1 repeat(s)), errors: 0
- retrieval hit-rate: **77.0%** (95% CI [67.8%, 84.2%], Wilson)
- answer accuracy (answer-producing provider): **57.0%** (57/100 CORRECT), abstains: 0 (never counted as correct)
- judge was configured but did not run (no OPENAI_API_KEY): answer grades fall back to containment; judge cross-check skipped, and this is recorded
- latency (client-side): mean 2.497s, p50 2.322s, p95 4.043s, max 5.186s

## Per-question

| id | calls | hit_all | hit_any | verdicts | mean latency |
|---|---|---|---|---|---|
| simpleqa-0031 | 1 | True | True | CORRECT | 3.509s |
| simpleqa-0034 | 1 | True | True | CORRECT | 1.826s |
| simpleqa-0039 | 1 | True | True | CORRECT | 2.795s |
| simpleqa-0072 | 1 | True | True | WRONG | 2.216s |
| simpleqa-0095 | 1 | True | True | WRONG | 2.449s |
| simpleqa-0110 | 1 | False | False | WRONG | 2.13s |
| simpleqa-0117 | 1 | True | True | CORRECT | 3.0s |
| simpleqa-0131 | 1 | False | False | WRONG | 2.479s |
| simpleqa-0142 | 1 | True | True | CORRECT | 2.671s |
| simpleqa-0184 | 1 | True | True | WRONG | 2.088s |
| simpleqa-0189 | 1 | True | True | CORRECT | 2.579s |
| simpleqa-0192 | 1 | True | True | CORRECT | 2.584s |
| simpleqa-0204 | 1 | False | False | WRONG | 1.772s |
| simpleqa-0230 | 1 | True | True | WRONG | 3.575s |
| simpleqa-0260 | 1 | True | True | CORRECT | 5.009s |
| simpleqa-0272 | 1 | True | True | CORRECT | 4.228s |
| simpleqa-0297 | 1 | True | True | CORRECT | 1.472s |
| simpleqa-0298 | 1 | True | True | CORRECT | 1.979s |
| simpleqa-0340 | 1 | False | False | WRONG | 1.517s |
| simpleqa-0368 | 1 | True | True | WRONG | 1.759s |
| simpleqa-0376 | 1 | True | True | WRONG | 2.437s |
| simpleqa-0379 | 1 | True | True | WRONG | 2.418s |
| simpleqa-0404 | 1 | False | False | WRONG | 3.221s |
| simpleqa-0409 | 1 | True | True | CORRECT | 1.641s |
| simpleqa-0454 | 1 | False | False | WRONG | 1.42s |
| simpleqa-0512 | 1 | True | True | CORRECT | 2.456s |
| simpleqa-0516 | 1 | False | False | WRONG | 5.186s |
| simpleqa-0522 | 1 | True | True | CORRECT | 1.828s |
| simpleqa-0553 | 1 | False | False | WRONG | 2.227s |
| simpleqa-0556 | 1 | True | True | WRONG | 2.025s |
| simpleqa-0572 | 1 | True | True | CORRECT | 1.919s |
| simpleqa-0626 | 1 | True | True | CORRECT | 1.38s |
| simpleqa-0651 | 1 | True | True | CORRECT | 2.085s |
| simpleqa-0653 | 1 | True | True | CORRECT | 2.681s |
| simpleqa-0655 | 1 | False | False | WRONG | 1.682s |
| simpleqa-0662 | 1 | True | True | CORRECT | 1.724s |
| simpleqa-0663 | 1 | True | True | CORRECT | 1.911s |
| simpleqa-0667 | 1 | True | True | WRONG | 3.798s |
| simpleqa-0669 | 1 | False | False | WRONG | 2.186s |
| simpleqa-0671 | 1 | True | True | CORRECT | 2.117s |
| simpleqa-0677 | 1 | True | True | CORRECT | 2.359s |
| simpleqa-0682 | 1 | True | True | CORRECT | 1.989s |
| simpleqa-0722 | 1 | True | True | WRONG | 2.151s |
| simpleqa-0738 | 1 | True | True | WRONG | 1.87s |
| simpleqa-0750 | 1 | True | True | CORRECT | 1.666s |
| simpleqa-0761 | 1 | True | True | WRONG | 2.12s |
| simpleqa-0781 | 1 | True | True | CORRECT | 1.668s |
| simpleqa-0783 | 1 | False | False | WRONG | 2.116s |
| simpleqa-0805 | 1 | False | False | WRONG | 2.322s |
| simpleqa-0812 | 1 | True | True | CORRECT | 2.003s |
| simpleqa-0824 | 1 | True | True | CORRECT | 2.88s |
| simpleqa-0825 | 1 | True | True | CORRECT | 3.466s |
| simpleqa-0831 | 1 | False | False | WRONG | 1.889s |
| simpleqa-0833 | 1 | True | True | CORRECT | 2.293s |
| simpleqa-0873 | 1 | True | True | WRONG | 2.383s |
| simpleqa-0894 | 1 | True | True | CORRECT | 2.885s |
| simpleqa-0896 | 1 | True | True | WRONG | 1.658s |
| simpleqa-0972 | 1 | False | False | WRONG | 1.646s |
| simpleqa-0979 | 1 | True | True | CORRECT | 2.032s |
| simpleqa-1017 | 1 | True | True | CORRECT | 1.703s |
| simpleqa-1020 | 1 | True | True | CORRECT | 3.204s |
| simpleqa-1025 | 1 | True | True | WRONG | 1.775s |
| simpleqa-1028 | 1 | True | True | CORRECT | 1.615s |
| simpleqa-1135 | 1 | True | True | CORRECT | 2.02s |
| simpleqa-1142 | 1 | True | True | WRONG | 3.042s |
| simpleqa-1263 | 1 | False | False | WRONG | 2.927s |
| simpleqa-1270 | 1 | True | True | WRONG | 3.593s |
| simpleqa-1271 | 1 | True | True | CORRECT | 1.675s |
| simpleqa-1302 | 1 | False | False | WRONG | 3.6s |
| simpleqa-1317 | 1 | True | True | WRONG | 2.505s |
| simpleqa-1359 | 1 | True | True | CORRECT | 2.638s |
| simpleqa-1415 | 1 | True | True | CORRECT | 3.113s |
| simpleqa-1437 | 1 | True | True | CORRECT | 2.361s |
| simpleqa-1438 | 1 | True | True | CORRECT | 2.194s |
| simpleqa-1480 | 1 | True | True | CORRECT | 1.601s |
| simpleqa-1490 | 1 | True | True | CORRECT | 2.693s |
| simpleqa-1501 | 1 | True | True | CORRECT | 4.012s |
| simpleqa-1504 | 1 | True | True | CORRECT | 2.375s |
| simpleqa-1510 | 1 | False | False | WRONG | 2.973s |
| simpleqa-1514 | 1 | False | False | WRONG | 3.29s |
| simpleqa-1518 | 1 | True | True | CORRECT | 2.435s |
| simpleqa-1525 | 1 | True | True | CORRECT | 2.022s |
| simpleqa-1540 | 1 | False | False | WRONG | 2.514s |
| simpleqa-1548 | 1 | False | False | WRONG | 4.709s |
| simpleqa-1579 | 1 | True | True | CORRECT | 1.734s |
| simpleqa-1583 | 1 | True | True | WRONG | 3.279s |
| simpleqa-1615 | 1 | True | True | CORRECT | 2.524s |
| simpleqa-1627 | 1 | True | True | CORRECT | 2.469s |
| simpleqa-1636 | 1 | False | False | WRONG | 2.953s |
| simpleqa-1642 | 1 | False | False | WRONG | 2.284s |
| simpleqa-1644 | 1 | True | True | CORRECT | 3.9s |
| simpleqa-1708 | 1 | True | True | CORRECT | 2.452s |
| simpleqa-1787 | 1 | True | True | CORRECT | 2.064s |
| simpleqa-1795 | 1 | True | True | WRONG | 1.598s |
| simpleqa-1808 | 1 | True | True | CORRECT | 2.823s |
| simpleqa-1839 | 1 | True | True | CORRECT | 1.77s |
| simpleqa-1851 | 1 | False | False | WRONG | 5.064s |
| simpleqa-1867 | 1 | True | True | CORRECT | 2.237s |
| simpleqa-1884 | 1 | True | True | CORRECT | 4.043s |
| simpleqa-1892 | 1 | True | True | CORRECT | 2.549s |

## Misses (audit trail)

- simpleqa-0110 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-0131 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-0204 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-0340 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-0404 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-0454 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-0516 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-0553 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-0655 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-0669 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-0783 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-0805 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-0831 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-0972 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-1263 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-1302 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-1510 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-1514 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-1540 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-1548 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-1636 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-1642 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-1851 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)

Grading is deterministic (bench/graders.py): no LLM judge ran for this summary.
