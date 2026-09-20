# bench run: perplexity on simpleqa

- run: 20260920-062329 (git 90c657a), sample `simpleqa_n200_seed20260919` frozen 2026-09-19
- calls: 200 (200 questions x 1 repeat(s)), errors: 0
- retrieval hit-rate: **92.5%** (95% CI [88.0%, 95.4%], Wilson)
- answer accuracy (answer-producing provider): **93.5%** (187/200 CORRECT), abstains: 1 (never counted as correct)
- SimpleQA official-prompt judge cross-check ran on 200 answers: 185 CORRECT / 12 WRONG / 1 NOT_ATTEMPTED / 2 errors
- latency (client-side): mean 1.799s, p50 1.5s, p95 2.995s, max 13.956s

## Per-question

| id | calls | hit_all | hit_any | verdicts | mean latency |
|---|---|---|---|---|---|
| simpleqa-0031 | 1 | True | True | CORRECT | 1.261s |
| simpleqa-0034 | 1 | True | True | CORRECT | 1.234s |
| simpleqa-0039 | 1 | True | True | CORRECT | 1.132s |
| simpleqa-0072 | 1 | True | True | CORRECT | 1.56s |
| simpleqa-0095 | 1 | True | True | CORRECT | 1.571s |
| simpleqa-0110 | 1 | True | True | CORRECT | 2.749s |
| simpleqa-0117 | 1 | True | True | CORRECT | 1.378s |
| simpleqa-0131 | 1 | False | False | CORRECT | 1.94s |
| simpleqa-0142 | 1 | True | True | CORRECT | 2.546s |
| simpleqa-0184 | 1 | True | True | CORRECT | 1.836s |
| simpleqa-0189 | 1 | True | True | CORRECT | 1.503s |
| simpleqa-0192 | 1 | True | True | CORRECT | 1.613s |
| simpleqa-0204 | 1 | True | True | CORRECT | 1.475s |
| simpleqa-0230 | 1 | True | True | CORRECT | 1.388s |
| simpleqa-0260 | 1 | True | True | CORRECT | 1.287s |
| simpleqa-0272 | 1 | True | True | CORRECT | 3.143s |
| simpleqa-0297 | 1 | True | True | CORRECT | 1.55s |
| simpleqa-0298 | 1 | True | True | CORRECT | 1.279s |
| simpleqa-0340 | 1 | True | True | CORRECT | 1.338s |
| simpleqa-0368 | 1 | True | True | CORRECT | 1.547s |
| simpleqa-0376 | 1 | True | True | CORRECT | 1.091s |
| simpleqa-0379 | 1 | True | True | CORRECT | 1.654s |
| simpleqa-0404 | 1 | False | False | CORRECT | 1.5s |
| simpleqa-0409 | 1 | True | True | CORRECT | 1.184s |
| simpleqa-0454 | 1 | False | False | CORRECT | 2.435s |
| simpleqa-0512 | 1 | True | True | CORRECT | 1.534s |
| simpleqa-0516 | 1 | False | False | ABSTAIN | 1.884s |
| simpleqa-0522 | 1 | True | True | CORRECT | 1.584s |
| simpleqa-0553 | 1 | False | False | WRONG | 1.956s |
| simpleqa-0556 | 1 | True | True | CORRECT | 1.877s |
| simpleqa-0572 | 1 | False | False | WRONG | 2.077s |
| simpleqa-0626 | 1 | True | True | CORRECT | 1.356s |
| simpleqa-0651 | 1 | True | True | CORRECT | 1.577s |
| simpleqa-0653 | 1 | True | True | CORRECT | 1.452s |
| simpleqa-0655 | 1 | True | True | WRONG | 1.307s |
| simpleqa-0662 | 1 | True | True | CORRECT | 1.606s |
| simpleqa-0663 | 1 | True | True | CORRECT | 1.221s |
| simpleqa-0667 | 1 | True | True | CORRECT | 1.735s |
| simpleqa-0669 | 1 | True | True | CORRECT | 1.427s |
| simpleqa-0671 | 1 | True | True | CORRECT | 1.225s |
| simpleqa-0677 | 1 | True | True | CORRECT | 1.258s |
| simpleqa-0682 | 1 | True | True | CORRECT | 1.353s |
| simpleqa-0722 | 1 | True | True | CORRECT | 1.856s |
| simpleqa-0738 | 1 | True | True | CORRECT | 1.415s |
| simpleqa-0750 | 1 | True | True | CORRECT | 1.23s |
| simpleqa-0761 | 1 | True | True | CORRECT | 1.364s |
| simpleqa-0781 | 1 | True | True | CORRECT | 1.664s |
| simpleqa-0783 | 1 | True | True | CORRECT | 1.118s |
| simpleqa-0805 | 1 | True | True | CORRECT | 1.22s |
| simpleqa-0812 | 1 | True | True | CORRECT | 2.174s |
| simpleqa-0824 | 1 | True | True | CORRECT | 1.752s |
| simpleqa-0825 | 1 | True | True | CORRECT | 1.545s |
| simpleqa-0831 | 1 | True | True | CORRECT | 1.482s |
| simpleqa-0833 | 1 | True | True | CORRECT | 2.059s |
| simpleqa-0873 | 1 | True | True | CORRECT | 3.024s |
| simpleqa-0894 | 1 | True | True | CORRECT | 2.129s |
| simpleqa-0896 | 1 | True | True | CORRECT | 1.33s |
| simpleqa-0972 | 1 | False | False | WRONG | 1.074s |
| simpleqa-0979 | 1 | True | True | CORRECT | 1.544s |
| simpleqa-1017 | 1 | True | True | CORRECT | 2.46s |
| simpleqa-1020 | 1 | True | True | WRONG | 1.665s |
| simpleqa-1025 | 1 | False | False | CORRECT | 1.214s |
| simpleqa-1028 | 1 | True | True | WRONG | 1.195s |
| simpleqa-1135 | 1 | True | True | CORRECT | 1.621s |
| simpleqa-1142 | 1 | True | True | CORRECT | 2.192s |
| simpleqa-1263 | 1 | True | True | CORRECT | 1.294s |
| simpleqa-1270 | 1 | True | True | CORRECT | 1.727s |
| simpleqa-1271 | 1 | True | True | CORRECT | 2.76s |
| simpleqa-1302 | 1 | True | True | CORRECT | 1.244s |
| simpleqa-1317 | 1 | True | True | CORRECT | 2.576s |
| simpleqa-1359 | 1 | True | True | CORRECT | 2.694s |
| simpleqa-1415 | 1 | True | True | CORRECT | 2.344s |
| simpleqa-1437 | 1 | True | True | CORRECT | 1.411s |
| simpleqa-1438 | 1 | True | True | CORRECT | 1.489s |
| simpleqa-1480 | 1 | True | True | CORRECT | 1.979s |
| simpleqa-1490 | 1 | True | True | CORRECT | 1.138s |
| simpleqa-1501 | 1 | True | True | CORRECT | 2.302s |
| simpleqa-1504 | 1 | True | True | CORRECT | 3.448s |
| simpleqa-1510 | 1 | True | True | CORRECT | 1.417s |
| simpleqa-1514 | 1 | True | True | CORRECT | 1.541s |
| simpleqa-1518 | 1 | True | True | CORRECT | 2.222s |
| simpleqa-1525 | 1 | True | True | CORRECT | 1.437s |
| simpleqa-1540 | 1 | True | True | CORRECT | 1.775s |
| simpleqa-1548 | 1 | True | True | CORRECT | 3.335s |
| simpleqa-1579 | 1 | True | True | CORRECT | 2.242s |
| simpleqa-1583 | 1 | True | True | CORRECT | 11.461s |
| simpleqa-1615 | 1 | True | True | CORRECT | 1.21s |
| simpleqa-1627 | 1 | True | True | CORRECT | 2.325s |
| simpleqa-1636 | 1 | True | True | CORRECT | 1.342s |
| simpleqa-1642 | 1 | False | False | CORRECT | 1.181s |
| simpleqa-1644 | 1 | True | True | CORRECT | 2.167s |
| simpleqa-1708 | 1 | True | True | CORRECT | 1.716s |
| simpleqa-1787 | 1 | True | True | CORRECT | 1.094s |
| simpleqa-1795 | 1 | True | True | CORRECT | 3.035s |
| simpleqa-1808 | 1 | False | False | WRONG | 1.739s |
| simpleqa-1839 | 1 | True | True | CORRECT | 1.468s |
| simpleqa-1851 | 1 | True | True | WRONG | 1.759s |
| simpleqa-1867 | 1 | True | True | CORRECT | 1.26s |
| simpleqa-1884 | 1 | True | True | CORRECT | 1.159s |
| simpleqa-1892 | 1 | True | True | CORRECT | 1.569s |
| simpleqa-1927 | 1 | True | True | CORRECT | 1.551s |
| simpleqa-1928 | 1 | True | True | CORRECT | 1.942s |
| simpleqa-1930 | 1 | True | True | CORRECT | 1.347s |
| simpleqa-1944 | 1 | False | False | CORRECT | 1.318s |
| simpleqa-1951 | 1 | True | True | CORRECT | 2.987s |
| simpleqa-2042 | 1 | True | True | CORRECT | 1.568s |
| simpleqa-2081 | 1 | True | True | CORRECT | 1.636s |
| simpleqa-2118 | 1 | True | True | CORRECT | 1.708s |
| simpleqa-2130 | 1 | True | True | CORRECT | 1.366s |
| simpleqa-2134 | 1 | True | True | CORRECT | 2.346s |
| simpleqa-2148 | 1 | True | True | CORRECT | 1.263s |
| simpleqa-2163 | 1 | True | True | CORRECT | 1.482s |
| simpleqa-2191 | 1 | True | True | CORRECT | 1.086s |
| simpleqa-2204 | 1 | True | True | CORRECT | 1.108s |
| simpleqa-2295 | 1 | True | True | CORRECT | 1.956s |
| simpleqa-2351 | 1 | True | True | CORRECT | 2.866s |
| simpleqa-2411 | 1 | True | True | CORRECT | 1.368s |
| simpleqa-2441 | 1 | True | True | CORRECT | 1.247s |
| simpleqa-2451 | 1 | True | True | CORRECT | 1.776s |
| simpleqa-2453 | 1 | True | True | CORRECT | 1.327s |
| simpleqa-2462 | 1 | True | True | WRONG | 1.546s |
| simpleqa-2517 | 1 | True | True | CORRECT | 1.973s |
| simpleqa-2521 | 1 | True | True | CORRECT | 1.43s |
| simpleqa-2539 | 1 | True | True | CORRECT | 1.46s |
| simpleqa-2553 | 1 | True | True | CORRECT | 1.819s |
| simpleqa-2564 | 1 | True | True | CORRECT | 2.678s |
| simpleqa-2588 | 1 | True | True | CORRECT | 1.187s |
| simpleqa-2605 | 1 | True | True | CORRECT | 1.455s |
| simpleqa-2651 | 1 | True | True | CORRECT | 1.364s |
| simpleqa-2662 | 1 | True | True | CORRECT | 0.992s |
| simpleqa-2663 | 1 | True | True | CORRECT | 1.252s |
| simpleqa-2681 | 1 | True | True | CORRECT | 1.159s |
| simpleqa-2728 | 1 | True | True | CORRECT | 1.397s |
| simpleqa-2773 | 1 | True | True | CORRECT | 4.091s |
| simpleqa-2781 | 1 | True | True | CORRECT | 1.427s |
| simpleqa-2786 | 1 | True | True | CORRECT | 1.49s |
| simpleqa-2804 | 1 | True | True | CORRECT | 1.517s |
| simpleqa-2844 | 1 | True | True | CORRECT | 1.416s |
| simpleqa-2849 | 1 | True | True | CORRECT | 2.995s |
| simpleqa-2859 | 1 | True | True | CORRECT | 1.252s |
| simpleqa-2875 | 1 | True | True | CORRECT | 1.286s |
| simpleqa-2889 | 1 | True | True | CORRECT | 1.408s |
| simpleqa-2914 | 1 | True | True | WRONG | 1.651s |
| simpleqa-2923 | 1 | True | True | CORRECT | 1.166s |
| simpleqa-2943 | 1 | True | True | CORRECT | 1.473s |
| simpleqa-2954 | 1 | True | True | CORRECT | 2.997s |
| simpleqa-2994 | 1 | True | True | WRONG | 1.275s |
| simpleqa-2995 | 1 | True | True | CORRECT | 1.313s |
| simpleqa-3010 | 1 | True | True | CORRECT | 1.289s |
| simpleqa-3022 | 1 | True | True | CORRECT | 2.678s |
| simpleqa-3092 | 1 | True | True | CORRECT | 1.398s |
| simpleqa-3103 | 1 | True | True | CORRECT | 1.58s |
| simpleqa-3107 | 1 | True | True | CORRECT | 2.411s |
| simpleqa-3127 | 1 | True | True | CORRECT | 1.302s |
| simpleqa-3140 | 1 | True | True | CORRECT | 1.938s |
| simpleqa-3159 | 1 | False | False | CORRECT | 1.23s |
| simpleqa-3186 | 1 | True | True | CORRECT | 1.364s |
| simpleqa-3200 | 1 | True | True | CORRECT | 1.424s |
| simpleqa-3220 | 1 | True | True | CORRECT | 1.148s |
| simpleqa-3237 | 1 | True | True | CORRECT | 1.304s |
| simpleqa-3271 | 1 | True | True | CORRECT | 3.081s |
| simpleqa-3282 | 1 | True | True | CORRECT | 2.071s |
| simpleqa-3295 | 1 | True | True | CORRECT | 1.391s |
| simpleqa-3343 | 1 | True | True | CORRECT | 1.277s |
| simpleqa-3379 | 1 | True | True | CORRECT | 13.956s |
| simpleqa-3389 | 1 | True | True | CORRECT | 1.549s |
| simpleqa-3411 | 1 | False | False | CORRECT | 1.601s |
| simpleqa-3463 | 1 | True | True | CORRECT | 1.955s |
| simpleqa-3474 | 1 | False | False | CORRECT | 1.218s |
| simpleqa-3479 | 1 | True | True | CORRECT | 2.476s |
| simpleqa-3506 | 1 | True | True | CORRECT | 2.945s |
| simpleqa-3593 | 1 | True | True | CORRECT | 1.529s |
| simpleqa-3620 | 1 | True | True | CORRECT | 2.031s |
| simpleqa-3630 | 1 | True | True | CORRECT | 1.231s |
| simpleqa-3642 | 1 | True | True | CORRECT | 2.498s |
| simpleqa-3644 | 1 | True | True | CORRECT | 1.129s |
| simpleqa-3697 | 1 | True | True | CORRECT | 1.753s |
| simpleqa-3728 | 1 | True | True | WRONG | 1.302s |
| simpleqa-3772 | 1 | True | True | CORRECT | 2.779s |
| simpleqa-3793 | 1 | True | True | CORRECT | 2.345s |
| simpleqa-3862 | 1 | True | True | CORRECT | 1.128s |
| simpleqa-3896 | 1 | True | True | CORRECT | 1.249s |
| simpleqa-3922 | 1 | True | True | CORRECT | 1.255s |
| simpleqa-3934 | 1 | True | True | CORRECT | 1.614s |
| simpleqa-3977 | 1 | True | True | CORRECT | 1.317s |
| simpleqa-3988 | 1 | True | True | CORRECT | 1.181s |
| simpleqa-4009 | 1 | True | True | CORRECT | 1.13s |
| simpleqa-4029 | 1 | False | False | CORRECT | 1.756s |
| simpleqa-4045 | 1 | True | True | CORRECT | 1.244s |
| simpleqa-4051 | 1 | True | True | CORRECT | 1.465s |
| simpleqa-4086 | 1 | True | True | CORRECT | 2.175s |
| simpleqa-4095 | 1 | True | True | CORRECT | 2.095s |
| simpleqa-4170 | 1 | True | True | CORRECT | 1.276s |
| simpleqa-4174 | 1 | True | True | CORRECT | 1.354s |
| simpleqa-4224 | 1 | True | True | CORRECT | 1.25s |
| simpleqa-4227 | 1 | True | True | CORRECT | 2.25s |
| simpleqa-4266 | 1 | True | True | CORRECT | 1.945s |
| simpleqa-4273 | 1 | True | True | CORRECT | 1.038s |
| simpleqa-4288 | 1 | True | True | CORRECT | 1.485s |
| simpleqa-4290 | 1 | True | True | CORRECT | 1.909s |

## Misses (audit trail)

- simpleqa-0131 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-0404 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-0454 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-0516 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-0553 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-0572 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-0972 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-1025 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-1642 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-1808 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-1944 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-3159 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-3411 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-3474 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-4029 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)

Grading is deterministic (benchlib/graders.py): no LLM judge ran for this summary.
