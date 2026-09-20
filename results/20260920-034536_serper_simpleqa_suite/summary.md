# bench run: serper on simpleqa

- run: 20260920-034536 (git a203acf), sample `simpleqa_n200_seed20260919` frozen 2026-09-19
- calls: 100 (100 questions x 1 repeat(s)), errors: 0
- retrieval hit-rate: **66.0%** (95% CI [56.3%, 74.5%], Wilson)
- judge was configured but did not run (no OPENAI_API_KEY): answer grades fall back to containment; judge cross-check skipped, and this is recorded
- latency (client-side): mean 1.343s, p50 1.027s, p95 3.05s, max 7.188s

## Per-question

| id | calls | hit_all | hit_any | verdicts | mean latency |
|---|---|---|---|---|---|
| simpleqa-0031 | 1 | True | True | MISS | 1.127s |
| simpleqa-0034 | 1 | True | True | MISS | 0.896s |
| simpleqa-0039 | 1 | True | True | MISS | 1.293s |
| simpleqa-0072 | 1 | False | False | MISS | 6.068s |
| simpleqa-0095 | 1 | False | False | MISS | 1.052s |
| simpleqa-0110 | 1 | False | False | MISS | 0.73s |
| simpleqa-0117 | 1 | True | True | MISS | 0.749s |
| simpleqa-0131 | 1 | False | False | MISS | 1.258s |
| simpleqa-0142 | 1 | True | True | MISS | 0.759s |
| simpleqa-0184 | 1 | False | False | MISS | 2.518s |
| simpleqa-0189 | 1 | True | True | MISS | 1.327s |
| simpleqa-0192 | 1 | True | True | MISS | 2.025s |
| simpleqa-0204 | 1 | False | False | MISS | 0.831s |
| simpleqa-0230 | 1 | False | False | MISS | 7.188s |
| simpleqa-0260 | 1 | False | False | MISS | 0.716s |
| simpleqa-0272 | 1 | True | True | MISS | 0.848s |
| simpleqa-0297 | 1 | True | True | MISS | 1.899s |
| simpleqa-0298 | 1 | True | True | MISS | 1.243s |
| simpleqa-0340 | 1 | True | True | MISS | 0.838s |
| simpleqa-0368 | 1 | False | False | MISS | 1.015s |
| simpleqa-0376 | 1 | True | True | MISS | 0.987s |
| simpleqa-0379 | 1 | True | True | MISS | 0.924s |
| simpleqa-0404 | 1 | False | False | MISS | 4.141s |
| simpleqa-0409 | 1 | True | True | MISS | 0.779s |
| simpleqa-0454 | 1 | False | False | MISS | 0.913s |
| simpleqa-0512 | 1 | True | True | MISS | 1.048s |
| simpleqa-0516 | 1 | False | False | MISS | 0.718s |
| simpleqa-0522 | 1 | True | True | MISS | 1.04s |
| simpleqa-0553 | 1 | False | False | MISS | 1.308s |
| simpleqa-0556 | 1 | True | True | MISS | 0.912s |
| simpleqa-0572 | 1 | False | False | MISS | 0.74s |
| simpleqa-0626 | 1 | False | False | MISS | 1.039s |
| simpleqa-0651 | 1 | False | False | MISS | 1.028s |
| simpleqa-0653 | 1 | True | True | MISS | 0.942s |
| simpleqa-0655 | 1 | True | True | MISS | 1.269s |
| simpleqa-0662 | 1 | True | True | MISS | 2.174s |
| simpleqa-0663 | 1 | True | True | MISS | 0.881s |
| simpleqa-0667 | 1 | True | True | MISS | 0.804s |
| simpleqa-0669 | 1 | False | False | MISS | 0.793s |
| simpleqa-0671 | 1 | True | True | MISS | 0.627s |
| simpleqa-0677 | 1 | True | True | MISS | 0.829s |
| simpleqa-0682 | 1 | True | True | MISS | 0.928s |
| simpleqa-0722 | 1 | True | True | MISS | 0.952s |
| simpleqa-0738 | 1 | False | False | MISS | 1.055s |
| simpleqa-0750 | 1 | True | True | MISS | 1.412s |
| simpleqa-0761 | 1 | True | True | MISS | 1.471s |
| simpleqa-0781 | 1 | True | True | MISS | 1.147s |
| simpleqa-0783 | 1 | True | True | MISS | 0.845s |
| simpleqa-0805 | 1 | True | True | MISS | 0.892s |
| simpleqa-0812 | 1 | True | True | MISS | 0.829s |
| simpleqa-0824 | 1 | True | True | MISS | 0.886s |
| simpleqa-0825 | 1 | True | True | MISS | 3.05s |
| simpleqa-0831 | 1 | True | True | MISS | 0.718s |
| simpleqa-0833 | 1 | True | True | MISS | 0.914s |
| simpleqa-0873 | 1 | True | True | MISS | 1.045s |
| simpleqa-0894 | 1 | False | False | MISS | 0.901s |
| simpleqa-0896 | 1 | True | True | MISS | 0.726s |
| simpleqa-0972 | 1 | False | False | MISS | 1.12s |
| simpleqa-0979 | 1 | True | True | MISS | 0.99s |
| simpleqa-1017 | 1 | False | False | MISS | 1.111s |
| simpleqa-1020 | 1 | True | True | MISS | 0.807s |
| simpleqa-1025 | 1 | True | True | MISS | 1.358s |
| simpleqa-1028 | 1 | True | True | MISS | 0.985s |
| simpleqa-1135 | 1 | True | True | MISS | 0.885s |
| simpleqa-1142 | 1 | True | True | MISS | 1.082s |
| simpleqa-1263 | 1 | False | False | MISS | 1.704s |
| simpleqa-1270 | 1 | False | False | MISS | 5.732s |
| simpleqa-1271 | 1 | True | True | MISS | 0.771s |
| simpleqa-1302 | 1 | True | True | MISS | 1.35s |
| simpleqa-1317 | 1 | True | True | MISS | 1.68s |
| simpleqa-1359 | 1 | True | True | MISS | 1.312s |
| simpleqa-1415 | 1 | True | True | MISS | 0.857s |
| simpleqa-1437 | 1 | False | False | MISS | 1.005s |
| simpleqa-1438 | 1 | True | True | MISS | 1.036s |
| simpleqa-1480 | 1 | False | False | MISS | 0.996s |
| simpleqa-1490 | 1 | True | True | MISS | 0.768s |
| simpleqa-1501 | 1 | True | True | MISS | 1.501s |
| simpleqa-1504 | 1 | False | False | MISS | 3.381s |
| simpleqa-1510 | 1 | False | False | MISS | 1.065s |
| simpleqa-1514 | 1 | True | True | MISS | 1.541s |
| simpleqa-1518 | 1 | True | True | MISS | 1.056s |
| simpleqa-1525 | 1 | True | True | MISS | 1.187s |
| simpleqa-1540 | 1 | False | False | MISS | 0.707s |
| simpleqa-1548 | 1 | False | False | MISS | 0.863s |
| simpleqa-1579 | 1 | True | True | MISS | 1.309s |
| simpleqa-1583 | 1 | False | False | MISS | 1.775s |
| simpleqa-1615 | 1 | True | True | MISS | 0.987s |
| simpleqa-1627 | 1 | True | True | MISS | 1.474s |
| simpleqa-1636 | 1 | False | False | MISS | 0.904s |
| simpleqa-1642 | 1 | False | False | MISS | 1.546s |
| simpleqa-1644 | 1 | True | True | MISS | 1.034s |
| simpleqa-1708 | 1 | True | True | MISS | 1.18s |
| simpleqa-1787 | 1 | True | True | MISS | 2.145s |
| simpleqa-1795 | 1 | True | True | MISS | 0.912s |
| simpleqa-1808 | 1 | False | False | MISS | 2.799s |
| simpleqa-1839 | 1 | True | True | MISS | 0.695s |
| simpleqa-1851 | 1 | False | False | MISS | 0.938s |
| simpleqa-1867 | 1 | True | True | MISS | 1.733s |
| simpleqa-1884 | 1 | True | True | MISS | 0.958s |
| simpleqa-1892 | 1 | True | True | MISS | 1.027s |

## Misses (audit trail)

- simpleqa-0072 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-0095 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-0110 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-0131 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-0184 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
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
- simpleqa-0651 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-0669 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-0738 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-0894 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-0972 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-1017 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-1263 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-1270 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-1437 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-1480 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-1504 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-1510 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-1540 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-1548 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-1583 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-1636 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-1642 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-1808 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-1851 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)

Grading is deterministic (bench/graders.py): no LLM judge ran for this summary.
