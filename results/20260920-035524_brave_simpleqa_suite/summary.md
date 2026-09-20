# bench run: brave on simpleqa

- run: 20260920-035524 (git aea6ecd), sample `simpleqa_n200_seed20260919` frozen 2026-09-19
- calls: 200 (200 questions x 1 repeat(s)), errors: 0
- retrieval hit-rate: **70.0%** (95% CI [63.3%, 75.9%], Wilson)
- judge was configured but did not run (no OPENAI_API_KEY): answer grades fall back to containment; judge cross-check skipped, and this is recorded
- latency (client-side): mean 0.422s, p50 0.461s, p95 0.676s, max 0.811s

## Per-question

| id | calls | hit_all | hit_any | verdicts | mean latency |
|---|---|---|---|---|---|
| simpleqa-0031 | 1 | True | True | MISS | 0.29s |
| simpleqa-0034 | 1 | True | True | MISS | 0.19s |
| simpleqa-0039 | 1 | True | True | MISS | 0.222s |
| simpleqa-0072 | 1 | True | True | MISS | 0.248s |
| simpleqa-0095 | 1 | False | False | MISS | 0.198s |
| simpleqa-0110 | 1 | True | True | MISS | 0.286s |
| simpleqa-0117 | 1 | False | False | MISS | 0.243s |
| simpleqa-0131 | 1 | False | False | MISS | 0.279s |
| simpleqa-0142 | 1 | True | True | MISS | 0.213s |
| simpleqa-0184 | 1 | True | True | MISS | 0.248s |
| simpleqa-0189 | 1 | True | True | MISS | 0.224s |
| simpleqa-0192 | 1 | True | True | MISS | 0.229s |
| simpleqa-0204 | 1 | True | True | MISS | 0.224s |
| simpleqa-0230 | 1 | False | False | MISS | 0.194s |
| simpleqa-0260 | 1 | False | False | MISS | 0.136s |
| simpleqa-0272 | 1 | True | True | MISS | 0.198s |
| simpleqa-0297 | 1 | True | True | MISS | 0.238s |
| simpleqa-0298 | 1 | True | True | MISS | 0.204s |
| simpleqa-0340 | 1 | True | True | MISS | 0.22s |
| simpleqa-0368 | 1 | True | True | MISS | 0.261s |
| simpleqa-0376 | 1 | True | True | MISS | 0.256s |
| simpleqa-0379 | 1 | True | True | MISS | 0.244s |
| simpleqa-0404 | 1 | False | False | MISS | 0.198s |
| simpleqa-0409 | 1 | True | True | MISS | 0.247s |
| simpleqa-0454 | 1 | False | False | MISS | 0.212s |
| simpleqa-0512 | 1 | True | True | MISS | 0.646s |
| simpleqa-0516 | 1 | False | False | MISS | 0.193s |
| simpleqa-0522 | 1 | True | True | MISS | 0.205s |
| simpleqa-0553 | 1 | False | False | MISS | 0.262s |
| simpleqa-0556 | 1 | True | True | MISS | 0.267s |
| simpleqa-0572 | 1 | False | False | MISS | 0.209s |
| simpleqa-0626 | 1 | True | True | MISS | 0.287s |
| simpleqa-0651 | 1 | True | True | MISS | 0.232s |
| simpleqa-0653 | 1 | True | True | MISS | 0.336s |
| simpleqa-0655 | 1 | False | False | MISS | 0.285s |
| simpleqa-0662 | 1 | True | True | MISS | 0.255s |
| simpleqa-0663 | 1 | False | False | MISS | 0.327s |
| simpleqa-0667 | 1 | True | True | MISS | 0.17s |
| simpleqa-0669 | 1 | False | False | MISS | 0.177s |
| simpleqa-0671 | 1 | True | True | MISS | 0.33s |
| simpleqa-0677 | 1 | True | True | MISS | 0.262s |
| simpleqa-0682 | 1 | False | False | MISS | 0.221s |
| simpleqa-0722 | 1 | True | True | MISS | 0.256s |
| simpleqa-0738 | 1 | True | True | MISS | 0.206s |
| simpleqa-0750 | 1 | True | True | MISS | 0.269s |
| simpleqa-0761 | 1 | True | True | MISS | 0.265s |
| simpleqa-0781 | 1 | False | False | MISS | 0.191s |
| simpleqa-0783 | 1 | True | True | MISS | 0.204s |
| simpleqa-0805 | 1 | True | True | MISS | 0.18s |
| simpleqa-0812 | 1 | True | True | MISS | 0.196s |
| simpleqa-0824 | 1 | True | True | MISS | 0.233s |
| simpleqa-0825 | 1 | True | True | MISS | 0.223s |
| simpleqa-0831 | 1 | True | True | MISS | 0.255s |
| simpleqa-0833 | 1 | False | False | MISS | 0.234s |
| simpleqa-0873 | 1 | True | True | MISS | 0.268s |
| simpleqa-0894 | 1 | True | True | MISS | 0.282s |
| simpleqa-0896 | 1 | True | True | MISS | 0.216s |
| simpleqa-0972 | 1 | False | False | MISS | 0.258s |
| simpleqa-0979 | 1 | True | True | MISS | 0.197s |
| simpleqa-1017 | 1 | False | False | MISS | 0.225s |
| simpleqa-1020 | 1 | True | True | MISS | 0.291s |
| simpleqa-1025 | 1 | False | False | MISS | 0.296s |
| simpleqa-1028 | 1 | True | True | MISS | 0.248s |
| simpleqa-1135 | 1 | False | False | MISS | 0.201s |
| simpleqa-1142 | 1 | True | True | MISS | 0.264s |
| simpleqa-1263 | 1 | False | False | MISS | 0.276s |
| simpleqa-1270 | 1 | False | False | MISS | 0.284s |
| simpleqa-1271 | 1 | True | True | MISS | 0.198s |
| simpleqa-1302 | 1 | True | True | MISS | 0.202s |
| simpleqa-1317 | 1 | False | False | MISS | 0.248s |
| simpleqa-1359 | 1 | False | False | MISS | 0.317s |
| simpleqa-1415 | 1 | False | False | MISS | 0.282s |
| simpleqa-1437 | 1 | False | False | MISS | 0.133s |
| simpleqa-1438 | 1 | True | True | MISS | 0.22s |
| simpleqa-1480 | 1 | True | True | MISS | 0.236s |
| simpleqa-1490 | 1 | True | True | MISS | 0.237s |
| simpleqa-1501 | 1 | True | True | MISS | 0.237s |
| simpleqa-1504 | 1 | False | False | MISS | 0.255s |
| simpleqa-1510 | 1 | False | False | MISS | 0.246s |
| simpleqa-1514 | 1 | True | True | MISS | 0.269s |
| simpleqa-1518 | 1 | True | True | MISS | 0.399s |
| simpleqa-1525 | 1 | True | True | MISS | 0.26s |
| simpleqa-1540 | 1 | False | False | MISS | 0.205s |
| simpleqa-1548 | 1 | True | True | MISS | 0.209s |
| simpleqa-1579 | 1 | True | True | MISS | 0.251s |
| simpleqa-1583 | 1 | True | True | MISS | 0.195s |
| simpleqa-1615 | 1 | False | False | MISS | 0.209s |
| simpleqa-1627 | 1 | True | True | MISS | 0.492s |
| simpleqa-1636 | 1 | True | True | MISS | 0.185s |
| simpleqa-1642 | 1 | False | False | MISS | 0.222s |
| simpleqa-1644 | 1 | True | True | MISS | 0.266s |
| simpleqa-1708 | 1 | True | True | MISS | 0.209s |
| simpleqa-1787 | 1 | True | True | MISS | 0.207s |
| simpleqa-1795 | 1 | True | True | MISS | 0.199s |
| simpleqa-1808 | 1 | True | True | MISS | 0.25s |
| simpleqa-1839 | 1 | True | True | MISS | 0.299s |
| simpleqa-1851 | 1 | True | True | MISS | 0.182s |
| simpleqa-1867 | 1 | False | False | MISS | 0.223s |
| simpleqa-1884 | 1 | True | True | MISS | 0.255s |
| simpleqa-1892 | 1 | True | True | MISS | 0.298s |
| simpleqa-1927 | 1 | False | False | MISS | 0.633s |
| simpleqa-1928 | 1 | False | False | MISS | 0.681s |
| simpleqa-1930 | 1 | True | True | MISS | 0.493s |
| simpleqa-1944 | 1 | False | False | MISS | 0.542s |
| simpleqa-1951 | 1 | True | True | MISS | 0.573s |
| simpleqa-2042 | 1 | True | True | MISS | 0.811s |
| simpleqa-2081 | 1 | False | False | MISS | 0.523s |
| simpleqa-2118 | 1 | True | True | MISS | 0.586s |
| simpleqa-2130 | 1 | True | True | MISS | 0.551s |
| simpleqa-2134 | 1 | True | True | MISS | 0.599s |
| simpleqa-2148 | 1 | True | True | MISS | 0.777s |
| simpleqa-2163 | 1 | True | True | MISS | 0.62s |
| simpleqa-2191 | 1 | True | True | MISS | 0.565s |
| simpleqa-2204 | 1 | True | True | MISS | 0.594s |
| simpleqa-2295 | 1 | False | False | MISS | 0.639s |
| simpleqa-2351 | 1 | True | True | MISS | 0.717s |
| simpleqa-2411 | 1 | True | True | MISS | 0.564s |
| simpleqa-2441 | 1 | True | True | MISS | 0.599s |
| simpleqa-2451 | 1 | True | True | MISS | 0.605s |
| simpleqa-2453 | 1 | True | True | MISS | 0.586s |
| simpleqa-2462 | 1 | False | False | MISS | 0.527s |
| simpleqa-2517 | 1 | True | True | MISS | 0.584s |
| simpleqa-2521 | 1 | True | True | MISS | 0.589s |
| simpleqa-2539 | 1 | True | True | MISS | 0.573s |
| simpleqa-2553 | 1 | True | True | MISS | 0.52s |
| simpleqa-2564 | 1 | False | False | MISS | 0.625s |
| simpleqa-2588 | 1 | True | True | MISS | 0.552s |
| simpleqa-2605 | 1 | True | True | MISS | 0.566s |
| simpleqa-2651 | 1 | True | True | MISS | 0.658s |
| simpleqa-2662 | 1 | False | False | MISS | 0.552s |
| simpleqa-2663 | 1 | True | True | MISS | 0.589s |
| simpleqa-2681 | 1 | True | True | MISS | 0.658s |
| simpleqa-2728 | 1 | True | True | MISS | 0.59s |
| simpleqa-2773 | 1 | False | False | MISS | 0.571s |
| simpleqa-2781 | 1 | True | True | MISS | 0.624s |
| simpleqa-2786 | 1 | True | True | MISS | 0.57s |
| simpleqa-2804 | 1 | True | True | MISS | 0.602s |
| simpleqa-2844 | 1 | True | True | MISS | 0.612s |
| simpleqa-2849 | 1 | False | False | MISS | 0.526s |
| simpleqa-2859 | 1 | False | False | MISS | 0.589s |
| simpleqa-2875 | 1 | True | True | MISS | 0.6s |
| simpleqa-2889 | 1 | True | True | MISS | 0.577s |
| simpleqa-2914 | 1 | True | True | MISS | 0.683s |
| simpleqa-2923 | 1 | True | True | MISS | 0.632s |
| simpleqa-2943 | 1 | False | False | MISS | 0.548s |
| simpleqa-2954 | 1 | True | True | MISS | 0.544s |
| simpleqa-2994 | 1 | False | False | MISS | 0.676s |
| simpleqa-2995 | 1 | False | False | MISS | 0.455s |
| simpleqa-3010 | 1 | True | True | MISS | 0.548s |
| simpleqa-3022 | 1 | True | True | MISS | 0.715s |
| simpleqa-3092 | 1 | False | False | MISS | 0.673s |
| simpleqa-3103 | 1 | True | True | MISS | 0.523s |
| simpleqa-3107 | 1 | True | True | MISS | 0.56s |
| simpleqa-3127 | 1 | True | True | MISS | 0.621s |
| simpleqa-3140 | 1 | True | True | MISS | 0.549s |
| simpleqa-3159 | 1 | False | False | MISS | 0.529s |
| simpleqa-3186 | 1 | True | True | MISS | 0.584s |
| simpleqa-3200 | 1 | False | False | MISS | 0.466s |
| simpleqa-3220 | 1 | True | True | MISS | 0.78s |
| simpleqa-3237 | 1 | True | True | MISS | 0.561s |
| simpleqa-3271 | 1 | False | False | MISS | 0.722s |
| simpleqa-3282 | 1 | True | True | MISS | 0.574s |
| simpleqa-3295 | 1 | True | True | MISS | 0.636s |
| simpleqa-3343 | 1 | True | True | MISS | 0.594s |
| simpleqa-3379 | 1 | True | True | MISS | 0.529s |
| simpleqa-3389 | 1 | True | True | MISS | 0.637s |
| simpleqa-3411 | 1 | False | False | MISS | 0.543s |
| simpleqa-3463 | 1 | True | True | MISS | 0.567s |
| simpleqa-3474 | 1 | False | False | MISS | 0.613s |
| simpleqa-3479 | 1 | True | True | MISS | 0.605s |
| simpleqa-3506 | 1 | False | False | MISS | 0.646s |
| simpleqa-3593 | 1 | True | True | MISS | 0.547s |
| simpleqa-3620 | 1 | True | True | MISS | 0.541s |
| simpleqa-3630 | 1 | True | True | MISS | 0.531s |
| simpleqa-3642 | 1 | True | True | MISS | 0.576s |
| simpleqa-3644 | 1 | True | True | MISS | 0.602s |
| simpleqa-3697 | 1 | False | False | MISS | 0.585s |
| simpleqa-3728 | 1 | True | True | MISS | 0.663s |
| simpleqa-3772 | 1 | False | False | MISS | 0.659s |
| simpleqa-3793 | 1 | True | True | MISS | 0.461s |
| simpleqa-3862 | 1 | True | True | MISS | 0.546s |
| simpleqa-3896 | 1 | True | True | MISS | 0.606s |
| simpleqa-3922 | 1 | True | True | MISS | 0.59s |
| simpleqa-3934 | 1 | False | False | MISS | 0.621s |
| simpleqa-3977 | 1 | True | True | MISS | 0.596s |
| simpleqa-3988 | 1 | True | True | MISS | 0.628s |
| simpleqa-4009 | 1 | True | True | MISS | 0.594s |
| simpleqa-4029 | 1 | False | False | MISS | 0.647s |
| simpleqa-4045 | 1 | True | True | MISS | 0.61s |
| simpleqa-4051 | 1 | True | True | MISS | 0.639s |
| simpleqa-4086 | 1 | False | False | MISS | 0.719s |
| simpleqa-4095 | 1 | True | True | MISS | 0.569s |
| simpleqa-4170 | 1 | True | True | MISS | 0.658s |
| simpleqa-4174 | 1 | True | True | MISS | 0.673s |
| simpleqa-4224 | 1 | False | False | MISS | 0.548s |
| simpleqa-4227 | 1 | True | True | MISS | 0.615s |
| simpleqa-4266 | 1 | True | True | MISS | 0.693s |
| simpleqa-4273 | 1 | True | True | MISS | 0.549s |
| simpleqa-4288 | 1 | True | True | MISS | 0.658s |
| simpleqa-4290 | 1 | False | False | MISS | 0.559s |

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
- simpleqa-1927 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-1928 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-1944 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-2081 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-2295 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-2462 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-2564 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-2662 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-2773 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-2849 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-2859 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-2943 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-2994 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-2995 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-3092 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-3159 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-3200 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-3271 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-3411 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-3474 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-3506 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-3697 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-3772 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-3934 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-4029 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-4086 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-4224 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-4290 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)

Grading is deterministic (bench/graders.py): no LLM judge ran for this summary.
