# bench run: ransack on simpleqa

- run: 20260920-033547 (git a203acf), sample `simpleqa_n200_seed20260919` frozen 2026-09-19
- calls: 100 (100 questions x 1 repeat(s)), errors: 0
- retrieval hit-rate: **66.0%** (95% CI [56.3%, 74.5%], Wilson)
- judge was configured but did not run (no OPENAI_API_KEY): answer grades fall back to containment; judge cross-check skipped, and this is recorded
- latency (client-side): mean 2.798s, p50 2.263s, p95 5.249s, max 20.76s

## Per-question

| id | calls | hit_all | hit_any | verdicts | mean latency |
|---|---|---|---|---|---|
| simpleqa-0031 | 1 | True | True | MISS | 3.135s |
| simpleqa-0034 | 1 | True | True | MISS | 3.499s |
| simpleqa-0039 | 1 | True | True | MISS | 1.928s |
| simpleqa-0072 | 1 | True | True | MISS | 2.291s |
| simpleqa-0095 | 1 | False | False | MISS | 2.153s |
| simpleqa-0110 | 1 | False | False | MISS | 1.928s |
| simpleqa-0117 | 1 | True | True | MISS | 2.372s |
| simpleqa-0131 | 1 | False | False | MISS | 3.081s |
| simpleqa-0142 | 1 | True | True | MISS | 2.286s |
| simpleqa-0184 | 1 | True | True | MISS | 1.821s |
| simpleqa-0189 | 1 | True | True | MISS | 1.814s |
| simpleqa-0192 | 1 | True | True | MISS | 5.807s |
| simpleqa-0204 | 1 | False | False | MISS | 2.817s |
| simpleqa-0230 | 1 | False | False | MISS | 1.562s |
| simpleqa-0260 | 1 | False | False | MISS | 1.482s |
| simpleqa-0272 | 1 | True | True | MISS | 3.864s |
| simpleqa-0297 | 1 | True | True | MISS | 2.276s |
| simpleqa-0298 | 1 | True | True | MISS | 1.956s |
| simpleqa-0340 | 1 | True | True | MISS | 2.123s |
| simpleqa-0368 | 1 | False | False | MISS | 4.091s |
| simpleqa-0376 | 1 | True | True | MISS | 2.617s |
| simpleqa-0379 | 1 | False | False | MISS | 20.76s |
| simpleqa-0404 | 1 | False | False | MISS | 2.088s |
| simpleqa-0409 | 1 | True | True | MISS | 2.496s |
| simpleqa-0454 | 1 | False | False | MISS | 1.549s |
| simpleqa-0512 | 1 | True | True | MISS | 2.237s |
| simpleqa-0516 | 1 | False | False | MISS | 2.699s |
| simpleqa-0522 | 1 | True | True | MISS | 1.785s |
| simpleqa-0553 | 1 | False | False | MISS | 2.992s |
| simpleqa-0556 | 1 | True | True | MISS | 2.779s |
| simpleqa-0572 | 1 | False | False | MISS | 4.47s |
| simpleqa-0626 | 1 | False | False | MISS | 2.035s |
| simpleqa-0651 | 1 | False | False | MISS | 1.943s |
| simpleqa-0653 | 1 | True | True | MISS | 2.237s |
| simpleqa-0655 | 1 | True | True | MISS | 1.552s |
| simpleqa-0662 | 1 | True | True | MISS | 1.853s |
| simpleqa-0663 | 1 | True | True | MISS | 4.553s |
| simpleqa-0667 | 1 | True | True | MISS | 2.077s |
| simpleqa-0669 | 1 | False | False | MISS | 2.085s |
| simpleqa-0671 | 1 | True | True | MISS | 1.98s |
| simpleqa-0677 | 1 | True | True | MISS | 1.216s |
| simpleqa-0682 | 1 | True | True | MISS | 2.23s |
| simpleqa-0722 | 1 | True | True | MISS | 1.903s |
| simpleqa-0738 | 1 | False | False | MISS | 1.476s |
| simpleqa-0750 | 1 | True | True | MISS | 2.88s |
| simpleqa-0761 | 1 | False | False | MISS | 2.065s |
| simpleqa-0781 | 1 | True | True | MISS | 2.21s |
| simpleqa-0783 | 1 | True | True | MISS | 2.224s |
| simpleqa-0805 | 1 | True | True | MISS | 3.702s |
| simpleqa-0812 | 1 | True | True | MISS | 2.395s |
| simpleqa-0824 | 1 | False | False | MISS | 1.989s |
| simpleqa-0825 | 1 | True | True | MISS | 1.892s |
| simpleqa-0831 | 1 | True | True | MISS | 2.461s |
| simpleqa-0833 | 1 | True | True | MISS | 2.307s |
| simpleqa-0873 | 1 | True | True | MISS | 2.735s |
| simpleqa-0894 | 1 | False | False | MISS | 2.198s |
| simpleqa-0896 | 1 | True | True | MISS | 6.841s |
| simpleqa-0972 | 1 | False | False | MISS | 1.906s |
| simpleqa-0979 | 1 | True | True | MISS | 3.06s |
| simpleqa-1017 | 1 | False | False | MISS | 2.562s |
| simpleqa-1020 | 1 | True | True | MISS | 2.164s |
| simpleqa-1025 | 1 | True | True | MISS | 2.681s |
| simpleqa-1028 | 1 | True | True | MISS | 2.035s |
| simpleqa-1135 | 1 | True | True | MISS | 3.104s |
| simpleqa-1142 | 1 | True | True | MISS | 1.962s |
| simpleqa-1263 | 1 | False | False | MISS | 2.108s |
| simpleqa-1270 | 1 | True | True | MISS | 1.452s |
| simpleqa-1271 | 1 | True | True | MISS | 2.754s |
| simpleqa-1302 | 1 | True | True | MISS | 1.895s |
| simpleqa-1317 | 1 | False | False | MISS | 2.971s |
| simpleqa-1359 | 1 | True | True | MISS | 3.83s |
| simpleqa-1415 | 1 | False | False | MISS | 8.435s |
| simpleqa-1437 | 1 | True | True | MISS | 5.997s |
| simpleqa-1438 | 1 | False | False | MISS | 3.934s |
| simpleqa-1480 | 1 | False | False | MISS | 1.773s |
| simpleqa-1490 | 1 | True | True | MISS | 2.738s |
| simpleqa-1501 | 1 | True | True | MISS | 3.838s |
| simpleqa-1504 | 1 | False | False | MISS | 3.056s |
| simpleqa-1510 | 1 | False | False | MISS | 2.291s |
| simpleqa-1514 | 1 | True | True | MISS | 2.414s |
| simpleqa-1518 | 1 | True | True | MISS | 2.183s |
| simpleqa-1525 | 1 | True | True | MISS | 1.698s |
| simpleqa-1540 | 1 | True | True | MISS | 1.527s |
| simpleqa-1548 | 1 | False | False | MISS | 1.775s |
| simpleqa-1579 | 1 | True | True | MISS | 1.784s |
| simpleqa-1583 | 1 | False | False | MISS | 1.548s |
| simpleqa-1615 | 1 | True | True | MISS | 2.473s |
| simpleqa-1627 | 1 | True | True | MISS | 1.849s |
| simpleqa-1636 | 1 | False | False | MISS | 2.352s |
| simpleqa-1642 | 1 | False | False | MISS | 4.194s |
| simpleqa-1644 | 1 | True | True | MISS | 2.263s |
| simpleqa-1708 | 1 | True | True | MISS | 2.296s |
| simpleqa-1787 | 1 | True | True | MISS | 2.077s |
| simpleqa-1795 | 1 | True | True | MISS | 1.771s |
| simpleqa-1808 | 1 | True | True | MISS | 4.003s |
| simpleqa-1839 | 1 | True | True | MISS | 2.534s |
| simpleqa-1851 | 1 | False | False | MISS | 2.164s |
| simpleqa-1867 | 1 | True | True | MISS | 2.528s |
| simpleqa-1884 | 1 | True | True | MISS | 5.249s |
| simpleqa-1892 | 1 | True | True | MISS | 2.803s |

## Misses (audit trail)

- simpleqa-0095 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-0110 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-0131 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-0204 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-0230 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-0260 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-0368 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-0379 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-0404 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-0454 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-0516 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-0553 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-0572 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-0626 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-0651 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-0669 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-0738 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-0761 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-0824 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-0894 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-0972 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-1017 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-1263 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-1317 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-1415 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-1438 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-1480 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-1504 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-1510 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-1548 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-1583 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-1636 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-1642 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-1851 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)

Grading is deterministic (bench/graders.py): no LLM judge ran for this summary.
