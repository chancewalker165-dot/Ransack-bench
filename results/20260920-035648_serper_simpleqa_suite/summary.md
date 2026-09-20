# bench run: serper on simpleqa

- run: 20260920-035648 (git aea6ecd), sample `simpleqa_n200_seed20260919` frozen 2026-09-19
- calls: 200 (200 questions x 1 repeat(s)), errors: 0
- retrieval hit-rate: **70.5%** (95% CI [63.8%, 76.4%], Wilson)
- judge was configured but did not run (no OPENAI_API_KEY): answer grades fall back to containment; judge cross-check skipped, and this is recorded
- latency (client-side): mean 1.511s, p50 1.041s, p95 4.377s, max 8.108s

## Per-question

| id | calls | hit_all | hit_any | verdicts | mean latency |
|---|---|---|---|---|---|
| simpleqa-0031 | 1 | True | True | MISS | 1.054s |
| simpleqa-0034 | 1 | True | True | MISS | 8.108s |
| simpleqa-0039 | 1 | True | True | MISS | 1.399s |
| simpleqa-0072 | 1 | False | False | MISS | 0.95s |
| simpleqa-0095 | 1 | False | False | MISS | 1.637s |
| simpleqa-0110 | 1 | False | False | MISS | 0.779s |
| simpleqa-0117 | 1 | True | True | MISS | 1.526s |
| simpleqa-0131 | 1 | False | False | MISS | 0.915s |
| simpleqa-0142 | 1 | True | True | MISS | 2.098s |
| simpleqa-0184 | 1 | False | False | MISS | 0.689s |
| simpleqa-0189 | 1 | True | True | MISS | 1.016s |
| simpleqa-0192 | 1 | True | True | MISS | 0.878s |
| simpleqa-0204 | 1 | False | False | MISS | 1.05s |
| simpleqa-0230 | 1 | False | False | MISS | 1.116s |
| simpleqa-0260 | 1 | False | False | MISS | 0.727s |
| simpleqa-0272 | 1 | True | True | MISS | 6.529s |
| simpleqa-0297 | 1 | True | True | MISS | 0.884s |
| simpleqa-0298 | 1 | True | True | MISS | 0.764s |
| simpleqa-0340 | 1 | True | True | MISS | 1.511s |
| simpleqa-0368 | 1 | False | False | MISS | 1.147s |
| simpleqa-0376 | 1 | True | True | MISS | 0.995s |
| simpleqa-0379 | 1 | False | False | MISS | 1.241s |
| simpleqa-0404 | 1 | False | False | MISS | 1.072s |
| simpleqa-0409 | 1 | True | True | MISS | 1.409s |
| simpleqa-0454 | 1 | False | False | MISS | 0.82s |
| simpleqa-0512 | 1 | True | True | MISS | 1.325s |
| simpleqa-0516 | 1 | False | False | MISS | 1.842s |
| simpleqa-0522 | 1 | True | True | MISS | 0.81s |
| simpleqa-0553 | 1 | False | False | MISS | 1.228s |
| simpleqa-0556 | 1 | True | True | MISS | 0.832s |
| simpleqa-0572 | 1 | False | False | MISS | 1.458s |
| simpleqa-0626 | 1 | False | False | MISS | 1.077s |
| simpleqa-0651 | 1 | False | False | MISS | 2.042s |
| simpleqa-0653 | 1 | True | True | MISS | 1.674s |
| simpleqa-0655 | 1 | True | True | MISS | 1.581s |
| simpleqa-0662 | 1 | True | True | MISS | 3.744s |
| simpleqa-0663 | 1 | True | True | MISS | 5.073s |
| simpleqa-0667 | 1 | True | True | MISS | 1.038s |
| simpleqa-0669 | 1 | False | False | MISS | 0.883s |
| simpleqa-0671 | 1 | True | True | MISS | 1.045s |
| simpleqa-0677 | 1 | True | True | MISS | 0.845s |
| simpleqa-0682 | 1 | True | True | MISS | 1.314s |
| simpleqa-0722 | 1 | True | True | MISS | 1.513s |
| simpleqa-0738 | 1 | False | False | MISS | 1.12s |
| simpleqa-0750 | 1 | True | True | MISS | 1.001s |
| simpleqa-0761 | 1 | True | True | MISS | 0.88s |
| simpleqa-0781 | 1 | True | True | MISS | 1.197s |
| simpleqa-0783 | 1 | True | True | MISS | 0.912s |
| simpleqa-0805 | 1 | True | True | MISS | 1.039s |
| simpleqa-0812 | 1 | True | True | MISS | 0.821s |
| simpleqa-0824 | 1 | False | False | MISS | 0.987s |
| simpleqa-0825 | 1 | True | True | MISS | 1.887s |
| simpleqa-0831 | 1 | True | True | MISS | 0.777s |
| simpleqa-0833 | 1 | True | True | MISS | 0.579s |
| simpleqa-0873 | 1 | True | True | MISS | 0.938s |
| simpleqa-0894 | 1 | False | False | MISS | 1.346s |
| simpleqa-0896 | 1 | True | True | MISS | 0.642s |
| simpleqa-0972 | 1 | False | False | MISS | 0.945s |
| simpleqa-0979 | 1 | True | True | MISS | 0.895s |
| simpleqa-1017 | 1 | False | False | MISS | 0.817s |
| simpleqa-1020 | 1 | True | True | MISS | 0.928s |
| simpleqa-1025 | 1 | True | True | MISS | 1.517s |
| simpleqa-1028 | 1 | True | True | MISS | 0.946s |
| simpleqa-1135 | 1 | True | True | MISS | 0.862s |
| simpleqa-1142 | 1 | True | True | MISS | 1.153s |
| simpleqa-1263 | 1 | False | False | MISS | 0.906s |
| simpleqa-1270 | 1 | True | True | MISS | 1.459s |
| simpleqa-1271 | 1 | True | True | MISS | 0.811s |
| simpleqa-1302 | 1 | True | True | MISS | 0.838s |
| simpleqa-1317 | 1 | True | True | MISS | 0.984s |
| simpleqa-1359 | 1 | False | False | MISS | 1.231s |
| simpleqa-1415 | 1 | True | True | MISS | 1.882s |
| simpleqa-1437 | 1 | True | True | MISS | 3.657s |
| simpleqa-1438 | 1 | False | False | MISS | 1.028s |
| simpleqa-1480 | 1 | False | False | MISS | 7.827s |
| simpleqa-1490 | 1 | True | True | MISS | 1.978s |
| simpleqa-1501 | 1 | True | True | MISS | 0.913s |
| simpleqa-1504 | 1 | False | False | MISS | 0.946s |
| simpleqa-1510 | 1 | False | False | MISS | 0.865s |
| simpleqa-1514 | 1 | True | True | MISS | 1.606s |
| simpleqa-1518 | 1 | True | True | MISS | 1.642s |
| simpleqa-1525 | 1 | True | True | MISS | 0.968s |
| simpleqa-1540 | 1 | True | True | MISS | 1.099s |
| simpleqa-1548 | 1 | False | False | MISS | 0.979s |
| simpleqa-1579 | 1 | True | True | MISS | 1.015s |
| simpleqa-1583 | 1 | False | False | MISS | 1.089s |
| simpleqa-1615 | 1 | True | True | MISS | 1.02s |
| simpleqa-1627 | 1 | True | True | MISS | 1.01s |
| simpleqa-1636 | 1 | False | False | MISS | 1.132s |
| simpleqa-1642 | 1 | False | False | MISS | 1.192s |
| simpleqa-1644 | 1 | True | True | MISS | 0.716s |
| simpleqa-1708 | 1 | True | True | MISS | 1.544s |
| simpleqa-1787 | 1 | True | True | MISS | 0.807s |
| simpleqa-1795 | 1 | True | True | MISS | 0.849s |
| simpleqa-1808 | 1 | True | True | MISS | 3.865s |
| simpleqa-1839 | 1 | True | True | MISS | 1.025s |
| simpleqa-1851 | 1 | False | False | MISS | 0.803s |
| simpleqa-1867 | 1 | True | True | MISS | 1.695s |
| simpleqa-1884 | 1 | True | True | MISS | 0.85s |
| simpleqa-1892 | 1 | True | True | MISS | 0.992s |
| simpleqa-1927 | 1 | True | True | MISS | 0.834s |
| simpleqa-1928 | 1 | True | True | MISS | 1.227s |
| simpleqa-1930 | 1 | True | True | MISS | 1.095s |
| simpleqa-1944 | 1 | False | False | MISS | 0.822s |
| simpleqa-1951 | 1 | False | False | MISS | 2.194s |
| simpleqa-2042 | 1 | True | True | MISS | 1.508s |
| simpleqa-2081 | 1 | True | True | MISS | 0.966s |
| simpleqa-2118 | 1 | True | True | MISS | 5.794s |
| simpleqa-2130 | 1 | True | True | MISS | 0.868s |
| simpleqa-2134 | 1 | True | True | MISS | 1.046s |
| simpleqa-2148 | 1 | True | True | MISS | 7.483s |
| simpleqa-2163 | 1 | True | True | MISS | 0.978s |
| simpleqa-2191 | 1 | True | True | MISS | 1.68s |
| simpleqa-2204 | 1 | True | True | MISS | 0.814s |
| simpleqa-2295 | 1 | True | True | MISS | 7.567s |
| simpleqa-2351 | 1 | True | True | MISS | 0.922s |
| simpleqa-2411 | 1 | False | False | MISS | 0.704s |
| simpleqa-2441 | 1 | True | True | MISS | 1.061s |
| simpleqa-2451 | 1 | False | False | MISS | 1.359s |
| simpleqa-2453 | 1 | True | True | MISS | 0.911s |
| simpleqa-2462 | 1 | True | True | MISS | 1.529s |
| simpleqa-2517 | 1 | False | False | MISS | 1.137s |
| simpleqa-2521 | 1 | True | True | MISS | 0.987s |
| simpleqa-2539 | 1 | True | True | MISS | 0.762s |
| simpleqa-2553 | 1 | True | True | MISS | 0.866s |
| simpleqa-2564 | 1 | False | False | MISS | 0.979s |
| simpleqa-2588 | 1 | True | True | MISS | 1.018s |
| simpleqa-2605 | 1 | True | True | MISS | 2.56s |
| simpleqa-2651 | 1 | True | True | MISS | 1.041s |
| simpleqa-2662 | 1 | True | True | MISS | 1.035s |
| simpleqa-2663 | 1 | True | True | MISS | 1.421s |
| simpleqa-2681 | 1 | False | False | MISS | 0.968s |
| simpleqa-2728 | 1 | True | True | MISS | 2.119s |
| simpleqa-2773 | 1 | False | False | MISS | 4.135s |
| simpleqa-2781 | 1 | True | True | MISS | 1.122s |
| simpleqa-2786 | 1 | True | True | MISS | 1.154s |
| simpleqa-2804 | 1 | True | True | MISS | 0.936s |
| simpleqa-2844 | 1 | True | True | MISS | 1.015s |
| simpleqa-2849 | 1 | True | True | MISS | 1.716s |
| simpleqa-2859 | 1 | False | False | MISS | 0.835s |
| simpleqa-2875 | 1 | False | False | MISS | 3.15s |
| simpleqa-2889 | 1 | True | True | MISS | 1.02s |
| simpleqa-2914 | 1 | False | False | MISS | 0.843s |
| simpleqa-2923 | 1 | True | True | MISS | 1.106s |
| simpleqa-2943 | 1 | False | False | MISS | 1.317s |
| simpleqa-2954 | 1 | True | True | MISS | 1.835s |
| simpleqa-2994 | 1 | False | False | MISS | 0.773s |
| simpleqa-2995 | 1 | False | False | MISS | 1.019s |
| simpleqa-3010 | 1 | True | True | MISS | 1.042s |
| simpleqa-3022 | 1 | True | True | MISS | 0.845s |
| simpleqa-3092 | 1 | True | True | MISS | 3.065s |
| simpleqa-3103 | 1 | True | True | MISS | 1.291s |
| simpleqa-3107 | 1 | True | True | MISS | 1.459s |
| simpleqa-3127 | 1 | True | True | MISS | 0.916s |
| simpleqa-3140 | 1 | True | True | MISS | 6.447s |
| simpleqa-3159 | 1 | False | False | MISS | 0.915s |
| simpleqa-3186 | 1 | True | True | MISS | 1.276s |
| simpleqa-3200 | 1 | True | True | MISS | 0.897s |
| simpleqa-3220 | 1 | True | True | MISS | 1.494s |
| simpleqa-3237 | 1 | False | False | MISS | 2.209s |
| simpleqa-3271 | 1 | True | True | MISS | 6.563s |
| simpleqa-3282 | 1 | True | True | MISS | 0.773s |
| simpleqa-3295 | 1 | True | True | MISS | 0.908s |
| simpleqa-3343 | 1 | True | True | MISS | 1.274s |
| simpleqa-3379 | 1 | True | True | MISS | 1.534s |
| simpleqa-3389 | 1 | True | True | MISS | 1.094s |
| simpleqa-3411 | 1 | False | False | MISS | 0.97s |
| simpleqa-3463 | 1 | True | True | MISS | 0.86s |
| simpleqa-3474 | 1 | False | False | MISS | 1.265s |
| simpleqa-3479 | 1 | True | True | MISS | 1.896s |
| simpleqa-3506 | 1 | False | False | MISS | 0.897s |
| simpleqa-3593 | 1 | True | True | MISS | 4.377s |
| simpleqa-3620 | 1 | True | True | MISS | 1.014s |
| simpleqa-3630 | 1 | True | True | MISS | 1.902s |
| simpleqa-3642 | 1 | True | True | MISS | 0.85s |
| simpleqa-3644 | 1 | True | True | MISS | 0.957s |
| simpleqa-3697 | 1 | True | True | MISS | 0.787s |
| simpleqa-3728 | 1 | True | True | MISS | 0.786s |
| simpleqa-3772 | 1 | True | True | MISS | 1.191s |
| simpleqa-3793 | 1 | True | True | MISS | 0.962s |
| simpleqa-3862 | 1 | True | True | MISS | 5.694s |
| simpleqa-3896 | 1 | True | True | MISS | 1.274s |
| simpleqa-3922 | 1 | True | True | MISS | 1.0s |
| simpleqa-3934 | 1 | True | True | MISS | 1.606s |
| simpleqa-3977 | 1 | True | True | MISS | 1.124s |
| simpleqa-3988 | 1 | True | True | MISS | 1.185s |
| simpleqa-4009 | 1 | False | False | MISS | 0.904s |
| simpleqa-4029 | 1 | False | False | MISS | 1.05s |
| simpleqa-4045 | 1 | True | True | MISS | 0.856s |
| simpleqa-4051 | 1 | False | False | MISS | 0.799s |
| simpleqa-4086 | 1 | True | True | MISS | 2.7s |
| simpleqa-4095 | 1 | True | True | MISS | 0.911s |
| simpleqa-4170 | 1 | True | True | MISS | 0.746s |
| simpleqa-4174 | 1 | True | True | MISS | 0.828s |
| simpleqa-4224 | 1 | False | False | MISS | 0.867s |
| simpleqa-4227 | 1 | True | True | MISS | 1.387s |
| simpleqa-4266 | 1 | True | True | MISS | 0.795s |
| simpleqa-4273 | 1 | True | True | MISS | 1.062s |
| simpleqa-4288 | 1 | False | False | MISS | 1.581s |
| simpleqa-4290 | 1 | False | False | MISS | 1.755s |

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
- simpleqa-0824 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-0894 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-0972 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-1017 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-1263 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-1359 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-1438 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-1480 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-1504 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-1510 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-1548 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-1583 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-1636 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-1642 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-1851 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-1944 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-1951 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-2411 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-2451 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-2517 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-2564 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-2681 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-2773 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-2859 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-2875 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-2914 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-2943 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-2994 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-2995 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-3159 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-3237 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-3411 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-3474 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-3506 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-4009 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-4029 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-4051 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-4224 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-4288 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-4290 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)

Grading is deterministic (bench/graders.py): no LLM judge ran for this summary.
