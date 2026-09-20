# bench run: serper on simpleqa

- run: 20260920-030635 (git 98bc1f0), sample `simpleqa_n200_seed20260919` frozen 2026-09-19
- calls: 100 (100 questions x 1 repeat(s)), errors: 0
- retrieval hit-rate: **63.0%** (95% CI [53.2%, 71.8%], Wilson)
- judge was configured but did not run (no OPENAI_API_KEY): answer grades fall back to containment; judge cross-check skipped, and this is recorded
- latency (client-side): mean 1.499s, p50 1.082s, p95 4.081s, max 8.67s

## Per-question

| id | calls | hit_all | hit_any | verdicts | mean latency |
|---|---|---|---|---|---|
| simpleqa-0031 | 1 | True | True | MISS | 0.801s |
| simpleqa-0034 | 1 | True | True | MISS | 0.843s |
| simpleqa-0039 | 1 | True | True | MISS | 1.198s |
| simpleqa-0072 | 1 | False | False | MISS | 1.481s |
| simpleqa-0095 | 1 | False | False | MISS | 0.959s |
| simpleqa-0110 | 1 | False | False | MISS | 0.824s |
| simpleqa-0117 | 1 | True | True | MISS | 1.084s |
| simpleqa-0131 | 1 | False | False | MISS | 4.081s |
| simpleqa-0142 | 1 | True | True | MISS | 3.581s |
| simpleqa-0184 | 1 | True | True | MISS | 0.64s |
| simpleqa-0189 | 1 | True | True | MISS | 1.354s |
| simpleqa-0192 | 1 | True | True | MISS | 0.843s |
| simpleqa-0204 | 1 | False | False | MISS | 0.911s |
| simpleqa-0230 | 1 | False | False | MISS | 0.984s |
| simpleqa-0260 | 1 | False | False | MISS | 0.862s |
| simpleqa-0272 | 1 | True | True | MISS | 1.774s |
| simpleqa-0297 | 1 | True | True | MISS | 1.677s |
| simpleqa-0298 | 1 | True | True | MISS | 1.277s |
| simpleqa-0340 | 1 | True | True | MISS | 1.249s |
| simpleqa-0368 | 1 | False | False | MISS | 1.667s |
| simpleqa-0376 | 1 | True | True | MISS | 0.824s |
| simpleqa-0379 | 1 | True | True | MISS | 1.562s |
| simpleqa-0404 | 1 | False | False | MISS | 0.91s |
| simpleqa-0409 | 1 | True | True | MISS | 2.166s |
| simpleqa-0454 | 1 | False | False | MISS | 0.74s |
| simpleqa-0512 | 1 | True | True | MISS | 1.153s |
| simpleqa-0516 | 1 | False | False | MISS | 0.749s |
| simpleqa-0522 | 1 | True | True | MISS | 0.984s |
| simpleqa-0553 | 1 | False | False | MISS | 1.426s |
| simpleqa-0556 | 1 | True | True | MISS | 4.678s |
| simpleqa-0572 | 1 | False | False | MISS | 1.397s |
| simpleqa-0626 | 1 | False | False | MISS | 1.001s |
| simpleqa-0651 | 1 | True | True | MISS | 1.451s |
| simpleqa-0653 | 1 | True | True | MISS | 0.916s |
| simpleqa-0655 | 1 | True | True | MISS | 0.746s |
| simpleqa-0662 | 1 | True | True | MISS | 2.012s |
| simpleqa-0663 | 1 | True | True | MISS | 1.45s |
| simpleqa-0667 | 1 | True | True | MISS | 2.689s |
| simpleqa-0669 | 1 | False | False | MISS | 1.147s |
| simpleqa-0671 | 1 | True | True | MISS | 0.795s |
| simpleqa-0677 | 1 | True | True | MISS | 1.297s |
| simpleqa-0682 | 1 | True | True | MISS | 0.769s |
| simpleqa-0722 | 1 | True | True | MISS | 0.946s |
| simpleqa-0738 | 1 | False | False | MISS | 1.106s |
| simpleqa-0750 | 1 | True | True | MISS | 1.001s |
| simpleqa-0761 | 1 | False | False | MISS | 0.864s |
| simpleqa-0781 | 1 | True | True | MISS | 1.58s |
| simpleqa-0783 | 1 | True | True | MISS | 0.939s |
| simpleqa-0805 | 1 | False | False | MISS | 3.195s |
| simpleqa-0812 | 1 | True | True | MISS | 1.075s |
| simpleqa-0824 | 1 | False | False | MISS | 0.985s |
| simpleqa-0825 | 1 | True | True | MISS | 0.978s |
| simpleqa-0831 | 1 | True | True | MISS | 0.92s |
| simpleqa-0833 | 1 | True | True | MISS | 2.708s |
| simpleqa-0873 | 1 | True | True | MISS | 0.966s |
| simpleqa-0894 | 1 | False | False | MISS | 1.005s |
| simpleqa-0896 | 1 | True | True | MISS | 0.953s |
| simpleqa-0972 | 1 | False | False | MISS | 8.67s |
| simpleqa-0979 | 1 | True | True | MISS | 1.24s |
| simpleqa-1017 | 1 | False | False | MISS | 1.203s |
| simpleqa-1020 | 1 | True | True | MISS | 0.815s |
| simpleqa-1025 | 1 | False | False | MISS | 0.734s |
| simpleqa-1028 | 1 | True | True | MISS | 0.664s |
| simpleqa-1135 | 1 | True | True | MISS | 1.202s |
| simpleqa-1142 | 1 | True | True | MISS | 0.879s |
| simpleqa-1263 | 1 | False | False | MISS | 1.051s |
| simpleqa-1270 | 1 | True | True | MISS | 0.997s |
| simpleqa-1271 | 1 | True | True | MISS | 1.502s |
| simpleqa-1302 | 1 | True | True | MISS | 1.018s |
| simpleqa-1317 | 1 | False | False | MISS | 3.209s |
| simpleqa-1359 | 1 | False | False | MISS | 1.362s |
| simpleqa-1415 | 1 | False | False | MISS | 4.105s |
| simpleqa-1437 | 1 | False | False | MISS | 1.523s |
| simpleqa-1438 | 1 | True | True | MISS | 3.008s |
| simpleqa-1480 | 1 | False | False | MISS | 0.743s |
| simpleqa-1490 | 1 | True | True | MISS | 0.835s |
| simpleqa-1501 | 1 | True | True | MISS | 1.246s |
| simpleqa-1504 | 1 | False | False | MISS | 0.993s |
| simpleqa-1510 | 1 | False | False | MISS | 1.022s |
| simpleqa-1514 | 1 | True | True | MISS | 1.082s |
| simpleqa-1518 | 1 | True | True | MISS | 3.311s |
| simpleqa-1525 | 1 | True | True | MISS | 1.148s |
| simpleqa-1540 | 1 | True | True | MISS | 1.035s |
| simpleqa-1548 | 1 | False | False | MISS | 0.751s |
| simpleqa-1579 | 1 | True | True | MISS | 0.917s |
| simpleqa-1583 | 1 | False | False | MISS | 1.796s |
| simpleqa-1615 | 1 | True | True | MISS | 1.01s |
| simpleqa-1627 | 1 | True | True | MISS | 1.465s |
| simpleqa-1636 | 1 | False | False | MISS | 1.114s |
| simpleqa-1642 | 1 | False | False | MISS | 5.145s |
| simpleqa-1644 | 1 | True | True | MISS | 1.244s |
| simpleqa-1708 | 1 | True | True | MISS | 4.344s |
| simpleqa-1787 | 1 | True | True | MISS | 1.177s |
| simpleqa-1795 | 1 | True | True | MISS | 1.063s |
| simpleqa-1808 | 1 | False | False | MISS | 0.94s |
| simpleqa-1839 | 1 | True | True | MISS | 1.466s |
| simpleqa-1851 | 1 | False | False | MISS | 0.978s |
| simpleqa-1867 | 1 | True | True | MISS | 1.307s |
| simpleqa-1884 | 1 | True | True | MISS | 1.405s |
| simpleqa-1892 | 1 | True | True | MISS | 0.999s |

## Misses (audit trail)

- simpleqa-0072 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-0095 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-0110 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-0131 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-0204 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-0230 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-0260 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-0368 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-0404 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-0454 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-0516 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-0553 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-0572 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-0626 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-0669 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-0738 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-0761 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-0805 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-0824 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-0894 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-0972 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-1017 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-1025 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-1263 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-1317 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-1359 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-1415 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-1437 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-1480 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-1504 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-1510 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-1548 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-1583 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-1636 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-1642 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-1808 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-1851 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)

Grading is deterministic (bench/graders.py): no LLM judge ran for this summary.
