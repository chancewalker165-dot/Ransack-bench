# bench run: brave on simpleqa

- run: 20260920-034436 (git a203acf), sample `simpleqa_n200_seed20260919` frozen 2026-09-19
- calls: 100 (100 questions x 1 repeat(s)), errors: 0
- retrieval hit-rate: **68.0%** (95% CI [58.3%, 76.3%], Wilson)
- judge was configured but did not run (no OPENAI_API_KEY): answer grades fall back to containment; judge cross-check skipped, and this is recorded
- latency (client-side): mean 0.594s, p50 0.587s, p95 0.686s, max 1.037s

## Per-question

| id | calls | hit_all | hit_any | verdicts | mean latency |
|---|---|---|---|---|---|
| simpleqa-0031 | 1 | True | True | MISS | 0.627s |
| simpleqa-0034 | 1 | True | True | MISS | 0.602s |
| simpleqa-0039 | 1 | True | True | MISS | 0.542s |
| simpleqa-0072 | 1 | True | True | MISS | 0.591s |
| simpleqa-0095 | 1 | False | False | MISS | 0.555s |
| simpleqa-0110 | 1 | True | True | MISS | 0.608s |
| simpleqa-0117 | 1 | False | False | MISS | 0.584s |
| simpleqa-0131 | 1 | False | False | MISS | 0.595s |
| simpleqa-0142 | 1 | True | True | MISS | 0.613s |
| simpleqa-0184 | 1 | True | True | MISS | 0.68s |
| simpleqa-0189 | 1 | True | True | MISS | 0.605s |
| simpleqa-0192 | 1 | True | True | MISS | 0.595s |
| simpleqa-0204 | 1 | True | True | MISS | 0.568s |
| simpleqa-0230 | 1 | False | False | MISS | 0.549s |
| simpleqa-0260 | 1 | False | False | MISS | 0.463s |
| simpleqa-0272 | 1 | True | True | MISS | 0.563s |
| simpleqa-0297 | 1 | True | True | MISS | 0.617s |
| simpleqa-0298 | 1 | True | True | MISS | 0.555s |
| simpleqa-0340 | 1 | True | True | MISS | 0.561s |
| simpleqa-0368 | 1 | True | True | MISS | 0.623s |
| simpleqa-0376 | 1 | True | True | MISS | 0.571s |
| simpleqa-0379 | 1 | True | True | MISS | 0.576s |
| simpleqa-0404 | 1 | False | False | MISS | 0.623s |
| simpleqa-0409 | 1 | True | True | MISS | 0.686s |
| simpleqa-0454 | 1 | False | False | MISS | 0.878s |
| simpleqa-0512 | 1 | True | True | MISS | 1.037s |
| simpleqa-0516 | 1 | False | False | MISS | 0.526s |
| simpleqa-0522 | 1 | True | True | MISS | 0.53s |
| simpleqa-0553 | 1 | False | False | MISS | 0.616s |
| simpleqa-0556 | 1 | True | True | MISS | 0.629s |
| simpleqa-0572 | 1 | False | False | MISS | 0.569s |
| simpleqa-0626 | 1 | True | True | MISS | 0.652s |
| simpleqa-0651 | 1 | True | True | MISS | 0.641s |
| simpleqa-0653 | 1 | True | True | MISS | 0.625s |
| simpleqa-0655 | 1 | False | False | MISS | 0.528s |
| simpleqa-0662 | 1 | True | True | MISS | 0.568s |
| simpleqa-0663 | 1 | False | False | MISS | 0.543s |
| simpleqa-0667 | 1 | True | True | MISS | 0.491s |
| simpleqa-0669 | 1 | False | False | MISS | 0.52s |
| simpleqa-0671 | 1 | True | True | MISS | 0.354s |
| simpleqa-0677 | 1 | True | True | MISS | 0.569s |
| simpleqa-0682 | 1 | False | False | MISS | 0.592s |
| simpleqa-0722 | 1 | True | True | MISS | 0.676s |
| simpleqa-0738 | 1 | True | True | MISS | 0.548s |
| simpleqa-0750 | 1 | True | True | MISS | 0.607s |
| simpleqa-0761 | 1 | True | True | MISS | 0.631s |
| simpleqa-0781 | 1 | False | False | MISS | 1.002s |
| simpleqa-0783 | 1 | True | True | MISS | 0.613s |
| simpleqa-0805 | 1 | True | True | MISS | 0.562s |
| simpleqa-0812 | 1 | True | True | MISS | 0.641s |
| simpleqa-0824 | 1 | True | True | MISS | 0.585s |
| simpleqa-0825 | 1 | True | True | MISS | 0.578s |
| simpleqa-0831 | 1 | True | True | MISS | 0.636s |
| simpleqa-0833 | 1 | False | False | MISS | 0.577s |
| simpleqa-0873 | 1 | True | True | MISS | 0.609s |
| simpleqa-0894 | 1 | True | True | MISS | 0.621s |
| simpleqa-0896 | 1 | True | True | MISS | 0.539s |
| simpleqa-0972 | 1 | False | False | MISS | 0.574s |
| simpleqa-0979 | 1 | True | True | MISS | 0.641s |
| simpleqa-1017 | 1 | False | False | MISS | 0.596s |
| simpleqa-1020 | 1 | True | True | MISS | 0.598s |
| simpleqa-1025 | 1 | False | False | MISS | 0.568s |
| simpleqa-1028 | 1 | True | True | MISS | 0.53s |
| simpleqa-1135 | 1 | False | False | MISS | 0.594s |
| simpleqa-1142 | 1 | True | True | MISS | 0.564s |
| simpleqa-1263 | 1 | False | False | MISS | 0.62s |
| simpleqa-1270 | 1 | False | False | MISS | 0.587s |
| simpleqa-1271 | 1 | True | True | MISS | 0.527s |
| simpleqa-1302 | 1 | True | True | MISS | 0.592s |
| simpleqa-1317 | 1 | False | False | MISS | 0.532s |
| simpleqa-1359 | 1 | False | False | MISS | 0.686s |
| simpleqa-1415 | 1 | False | False | MISS | 0.602s |
| simpleqa-1437 | 1 | False | False | MISS | 0.359s |
| simpleqa-1438 | 1 | True | True | MISS | 0.583s |
| simpleqa-1480 | 1 | True | True | MISS | 0.557s |
| simpleqa-1490 | 1 | True | True | MISS | 0.639s |
| simpleqa-1501 | 1 | True | True | MISS | 0.57s |
| simpleqa-1504 | 1 | False | False | MISS | 0.575s |
| simpleqa-1510 | 1 | False | False | MISS | 0.595s |
| simpleqa-1514 | 1 | True | True | MISS | 0.584s |
| simpleqa-1518 | 1 | True | True | MISS | 0.656s |
| simpleqa-1525 | 1 | True | True | MISS | 0.606s |
| simpleqa-1540 | 1 | False | False | MISS | 0.605s |
| simpleqa-1548 | 1 | True | True | MISS | 0.618s |
| simpleqa-1579 | 1 | True | True | MISS | 0.598s |
| simpleqa-1583 | 1 | True | True | MISS | 0.536s |
| simpleqa-1615 | 1 | False | False | MISS | 0.509s |
| simpleqa-1627 | 1 | True | True | MISS | 0.789s |
| simpleqa-1636 | 1 | True | True | MISS | 0.504s |
| simpleqa-1642 | 1 | False | False | MISS | 0.57s |
| simpleqa-1644 | 1 | True | True | MISS | 0.645s |
| simpleqa-1708 | 1 | True | True | MISS | 0.614s |
| simpleqa-1787 | 1 | True | True | MISS | 0.524s |
| simpleqa-1795 | 1 | True | True | MISS | 0.527s |
| simpleqa-1808 | 1 | True | True | MISS | 0.622s |
| simpleqa-1839 | 1 | True | True | MISS | 0.553s |
| simpleqa-1851 | 1 | True | True | MISS | 0.577s |
| simpleqa-1867 | 1 | False | False | MISS | 0.539s |
| simpleqa-1884 | 1 | True | True | MISS | 0.598s |
| simpleqa-1892 | 1 | True | True | MISS | 0.482s |

## Misses (audit trail)

- simpleqa-0095 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-0117 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-0131 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-0230 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-0260 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-0404 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-0454 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-0516 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-0553 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-0572 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-0655 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-0663 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-0669 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-0682 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-0781 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-0833 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-0972 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-1017 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-1025 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-1135 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-1263 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-1270 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-1317 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-1359 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-1415 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-1437 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-1504 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-1510 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-1540 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-1615 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-1642 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-1867 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)

Grading is deterministic (bench/graders.py): no LLM judge ran for this summary.
