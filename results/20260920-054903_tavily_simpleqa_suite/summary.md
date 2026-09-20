# bench run: tavily on simpleqa

- run: 20260920-054903 (git 5aeb219), sample `simpleqa_n200_seed20260919` frozen 2026-09-19
- calls: 200 (200 questions x 1 repeat(s)), errors: 0
- retrieval hit-rate: **83.0%** (95% CI [77.2%, 87.6%], Wilson)
- answer accuracy (answer-producing provider): **68.0%** (136/200 CORRECT), abstains: 0 (never counted as correct)
- SimpleQA official-prompt judge cross-check ran on 200 answers: 0 CORRECT / 0 WRONG / 0 NOT_ATTEMPTED / 200 errors
- latency (client-side): mean 2.328s, p50 2.159s, p95 4.057s, max 5.07s

## Per-question

| id | calls | hit_all | hit_any | verdicts | mean latency |
|---|---|---|---|---|---|
| simpleqa-0031 | 1 | True | True | CORRECT | 3.643s |
| simpleqa-0034 | 1 | True | True | CORRECT | 1.681s |
| simpleqa-0039 | 1 | True | True | CORRECT | 1.786s |
| simpleqa-0072 | 1 | True | True | WRONG | 1.717s |
| simpleqa-0095 | 1 | True | True | CORRECT | 4.425s |
| simpleqa-0110 | 1 | True | True | CORRECT | 2.074s |
| simpleqa-0117 | 1 | True | True | CORRECT | 2.249s |
| simpleqa-0131 | 1 | False | False | WRONG | 2.883s |
| simpleqa-0142 | 1 | True | True | CORRECT | 2.999s |
| simpleqa-0184 | 1 | True | True | CORRECT | 2.186s |
| simpleqa-0189 | 1 | True | True | CORRECT | 2.404s |
| simpleqa-0192 | 1 | True | True | CORRECT | 1.56s |
| simpleqa-0204 | 1 | False | False | WRONG | 1.829s |
| simpleqa-0230 | 1 | True | True | WRONG | 2.312s |
| simpleqa-0260 | 1 | True | True | CORRECT | 3.024s |
| simpleqa-0272 | 1 | True | True | CORRECT | 2.894s |
| simpleqa-0297 | 1 | True | True | CORRECT | 1.462s |
| simpleqa-0298 | 1 | True | True | CORRECT | 1.672s |
| simpleqa-0340 | 1 | False | False | WRONG | 1.751s |
| simpleqa-0368 | 1 | True | True | WRONG | 1.652s |
| simpleqa-0376 | 1 | True | True | WRONG | 2.499s |
| simpleqa-0379 | 1 | True | True | WRONG | 4.827s |
| simpleqa-0404 | 1 | False | False | WRONG | 3.653s |
| simpleqa-0409 | 1 | True | True | CORRECT | 2.177s |
| simpleqa-0454 | 1 | False | False | WRONG | 1.504s |
| simpleqa-0512 | 1 | True | True | CORRECT | 1.776s |
| simpleqa-0516 | 1 | False | False | WRONG | 3.41s |
| simpleqa-0522 | 1 | True | True | CORRECT | 2.18s |
| simpleqa-0553 | 1 | False | False | WRONG | 3.128s |
| simpleqa-0556 | 1 | True | True | WRONG | 2.159s |
| simpleqa-0572 | 1 | True | True | CORRECT | 1.688s |
| simpleqa-0626 | 1 | True | True | CORRECT | 2.193s |
| simpleqa-0651 | 1 | True | True | CORRECT | 2.562s |
| simpleqa-0653 | 1 | True | True | CORRECT | 2.128s |
| simpleqa-0655 | 1 | False | False | WRONG | 1.488s |
| simpleqa-0662 | 1 | True | True | CORRECT | 1.706s |
| simpleqa-0663 | 1 | True | True | CORRECT | 1.521s |
| simpleqa-0667 | 1 | True | True | WRONG | 1.868s |
| simpleqa-0669 | 1 | True | True | WRONG | 2.005s |
| simpleqa-0671 | 1 | True | True | CORRECT | 1.405s |
| simpleqa-0677 | 1 | True | True | CORRECT | 2.75s |
| simpleqa-0682 | 1 | True | True | CORRECT | 1.458s |
| simpleqa-0722 | 1 | True | True | WRONG | 2.46s |
| simpleqa-0738 | 1 | True | True | WRONG | 1.817s |
| simpleqa-0750 | 1 | True | True | CORRECT | 2.179s |
| simpleqa-0761 | 1 | True | True | WRONG | 2.358s |
| simpleqa-0781 | 1 | True | True | CORRECT | 2.03s |
| simpleqa-0783 | 1 | True | True | CORRECT | 2.795s |
| simpleqa-0805 | 1 | True | True | WRONG | 2.234s |
| simpleqa-0812 | 1 | True | True | WRONG | 2.759s |
| simpleqa-0824 | 1 | True | True | CORRECT | 2.614s |
| simpleqa-0825 | 1 | True | True | CORRECT | 3.475s |
| simpleqa-0831 | 1 | False | False | WRONG | 1.754s |
| simpleqa-0833 | 1 | False | False | WRONG | 1.614s |
| simpleqa-0873 | 1 | True | True | CORRECT | 2.511s |
| simpleqa-0894 | 1 | True | True | CORRECT | 3.023s |
| simpleqa-0896 | 1 | True | True | WRONG | 1.362s |
| simpleqa-0972 | 1 | False | False | WRONG | 1.952s |
| simpleqa-0979 | 1 | True | True | CORRECT | 1.852s |
| simpleqa-1017 | 1 | True | True | CORRECT | 1.907s |
| simpleqa-1020 | 1 | True | True | WRONG | 2.51s |
| simpleqa-1025 | 1 | True | True | WRONG | 1.915s |
| simpleqa-1028 | 1 | True | True | CORRECT | 1.574s |
| simpleqa-1135 | 1 | True | True | CORRECT | 2.617s |
| simpleqa-1142 | 1 | False | False | WRONG | 4.789s |
| simpleqa-1263 | 1 | True | True | CORRECT | 2.469s |
| simpleqa-1270 | 1 | True | True | WRONG | 1.703s |
| simpleqa-1271 | 1 | True | True | CORRECT | 2.097s |
| simpleqa-1302 | 1 | True | True | WRONG | 4.227s |
| simpleqa-1317 | 1 | True | True | WRONG | 2.199s |
| simpleqa-1359 | 1 | True | True | CORRECT | 3.641s |
| simpleqa-1415 | 1 | True | True | CORRECT | 1.674s |
| simpleqa-1437 | 1 | True | True | CORRECT | 1.801s |
| simpleqa-1438 | 1 | True | True | CORRECT | 2.332s |
| simpleqa-1480 | 1 | True | True | CORRECT | 2.143s |
| simpleqa-1490 | 1 | True | True | CORRECT | 1.772s |
| simpleqa-1501 | 1 | True | True | CORRECT | 2.468s |
| simpleqa-1504 | 1 | True | True | CORRECT | 2.772s |
| simpleqa-1510 | 1 | False | False | WRONG | 2.278s |
| simpleqa-1514 | 1 | True | True | CORRECT | 2.813s |
| simpleqa-1518 | 1 | True | True | CORRECT | 2.655s |
| simpleqa-1525 | 1 | True | True | CORRECT | 1.451s |
| simpleqa-1540 | 1 | False | False | WRONG | 2.504s |
| simpleqa-1548 | 1 | True | True | WRONG | 2.454s |
| simpleqa-1579 | 1 | True | True | CORRECT | 1.73s |
| simpleqa-1583 | 1 | True | True | WRONG | 2.969s |
| simpleqa-1615 | 1 | True | True | CORRECT | 2.406s |
| simpleqa-1627 | 1 | True | True | CORRECT | 2.04s |
| simpleqa-1636 | 1 | False | False | WRONG | 2.495s |
| simpleqa-1642 | 1 | False | False | WRONG | 4.701s |
| simpleqa-1644 | 1 | True | True | CORRECT | 1.72s |
| simpleqa-1708 | 1 | True | True | CORRECT | 2.341s |
| simpleqa-1787 | 1 | True | True | CORRECT | 2.029s |
| simpleqa-1795 | 1 | True | True | WRONG | 1.565s |
| simpleqa-1808 | 1 | True | True | CORRECT | 1.562s |
| simpleqa-1839 | 1 | True | True | CORRECT | 1.528s |
| simpleqa-1851 | 1 | False | False | WRONG | 5.07s |
| simpleqa-1867 | 1 | True | True | CORRECT | 3.061s |
| simpleqa-1884 | 1 | True | True | CORRECT | 2.351s |
| simpleqa-1892 | 1 | True | True | CORRECT | 2.064s |
| simpleqa-1927 | 1 | True | True | CORRECT | 2.271s |
| simpleqa-1928 | 1 | True | True | CORRECT | 1.941s |
| simpleqa-1930 | 1 | False | False | WRONG | 2.101s |
| simpleqa-1944 | 1 | False | False | WRONG | 2.138s |
| simpleqa-1951 | 1 | False | False | WRONG | 1.838s |
| simpleqa-2042 | 1 | True | True | WRONG | 4.045s |
| simpleqa-2081 | 1 | True | True | CORRECT | 1.815s |
| simpleqa-2118 | 1 | False | False | WRONG | 1.779s |
| simpleqa-2130 | 1 | True | True | CORRECT | 2.74s |
| simpleqa-2134 | 1 | True | True | CORRECT | 2.275s |
| simpleqa-2148 | 1 | True | True | CORRECT | 2.27s |
| simpleqa-2163 | 1 | True | True | WRONG | 1.585s |
| simpleqa-2191 | 1 | True | True | CORRECT | 2.176s |
| simpleqa-2204 | 1 | True | True | WRONG | 2.103s |
| simpleqa-2295 | 1 | False | False | WRONG | 2.211s |
| simpleqa-2351 | 1 | True | True | CORRECT | 2.177s |
| simpleqa-2411 | 1 | True | True | CORRECT | 1.533s |
| simpleqa-2441 | 1 | True | True | CORRECT | 2.09s |
| simpleqa-2451 | 1 | False | False | WRONG | 2.598s |
| simpleqa-2453 | 1 | True | True | CORRECT | 2.517s |
| simpleqa-2462 | 1 | True | True | CORRECT | 1.776s |
| simpleqa-2517 | 1 | True | True | CORRECT | 3.51s |
| simpleqa-2521 | 1 | True | True | CORRECT | 1.606s |
| simpleqa-2539 | 1 | True | True | CORRECT | 1.912s |
| simpleqa-2553 | 1 | False | False | WRONG | 3.084s |
| simpleqa-2564 | 1 | False | False | WRONG | 2.777s |
| simpleqa-2588 | 1 | True | True | CORRECT | 3.189s |
| simpleqa-2605 | 1 | True | True | CORRECT | 2.747s |
| simpleqa-2651 | 1 | True | True | CORRECT | 1.915s |
| simpleqa-2662 | 1 | True | True | WRONG | 1.48s |
| simpleqa-2663 | 1 | True | True | CORRECT | 2.868s |
| simpleqa-2681 | 1 | True | True | CORRECT | 2.136s |
| simpleqa-2728 | 1 | True | True | CORRECT | 1.586s |
| simpleqa-2773 | 1 | False | False | WRONG | 1.986s |
| simpleqa-2781 | 1 | True | True | CORRECT | 1.467s |
| simpleqa-2786 | 1 | True | True | CORRECT | 1.509s |
| simpleqa-2804 | 1 | True | True | CORRECT | 2.345s |
| simpleqa-2844 | 1 | True | True | CORRECT | 2.54s |
| simpleqa-2849 | 1 | False | False | WRONG | 3.257s |
| simpleqa-2859 | 1 | True | True | CORRECT | 2.896s |
| simpleqa-2875 | 1 | True | True | CORRECT | 3.637s |
| simpleqa-2889 | 1 | True | True | WRONG | 1.727s |
| simpleqa-2914 | 1 | True | True | CORRECT | 2.191s |
| simpleqa-2923 | 1 | True | True | CORRECT | 1.429s |
| simpleqa-2943 | 1 | True | True | WRONG | 2.654s |
| simpleqa-2954 | 1 | True | True | CORRECT | 1.579s |
| simpleqa-2994 | 1 | True | True | CORRECT | 1.689s |
| simpleqa-2995 | 1 | True | True | CORRECT | 2.009s |
| simpleqa-3010 | 1 | True | True | CORRECT | 4.616s |
| simpleqa-3022 | 1 | True | True | CORRECT | 2.266s |
| simpleqa-3092 | 1 | True | True | CORRECT | 2.57s |
| simpleqa-3103 | 1 | True | True | CORRECT | 2.073s |
| simpleqa-3107 | 1 | True | True | CORRECT | 2.82s |
| simpleqa-3127 | 1 | True | True | CORRECT | 2.116s |
| simpleqa-3140 | 1 | True | True | CORRECT | 1.877s |
| simpleqa-3159 | 1 | False | False | WRONG | 1.836s |
| simpleqa-3186 | 1 | True | True | CORRECT | 3.675s |
| simpleqa-3200 | 1 | True | True | CORRECT | 1.646s |
| simpleqa-3220 | 1 | True | True | CORRECT | 2.419s |
| simpleqa-3237 | 1 | True | True | CORRECT | 1.997s |
| simpleqa-3271 | 1 | True | True | CORRECT | 1.307s |
| simpleqa-3282 | 1 | True | True | CORRECT | 2.381s |
| simpleqa-3295 | 1 | True | True | CORRECT | 4.106s |
| simpleqa-3343 | 1 | True | True | CORRECT | 1.386s |
| simpleqa-3379 | 1 | True | True | CORRECT | 4.057s |
| simpleqa-3389 | 1 | True | True | CORRECT | 3.111s |
| simpleqa-3411 | 1 | False | False | WRONG | 2.929s |
| simpleqa-3463 | 1 | True | True | CORRECT | 1.605s |
| simpleqa-3474 | 1 | True | True | WRONG | 2.453s |
| simpleqa-3479 | 1 | True | True | CORRECT | 1.399s |
| simpleqa-3506 | 1 | False | False | WRONG | 2.369s |
| simpleqa-3593 | 1 | True | True | CORRECT | 2.358s |
| simpleqa-3620 | 1 | True | True | CORRECT | 3.292s |
| simpleqa-3630 | 1 | True | True | CORRECT | 2.003s |
| simpleqa-3642 | 1 | True | True | CORRECT | 2.279s |
| simpleqa-3644 | 1 | True | True | CORRECT | 1.988s |
| simpleqa-3697 | 1 | True | True | CORRECT | 2.134s |
| simpleqa-3728 | 1 | True | True | CORRECT | 2.022s |
| simpleqa-3772 | 1 | True | True | CORRECT | 2.525s |
| simpleqa-3793 | 1 | True | True | CORRECT | 1.798s |
| simpleqa-3862 | 1 | True | True | CORRECT | 1.721s |
| simpleqa-3896 | 1 | True | True | CORRECT | 3.447s |
| simpleqa-3922 | 1 | True | True | CORRECT | 2.843s |
| simpleqa-3934 | 1 | True | True | CORRECT | 1.771s |
| simpleqa-3977 | 1 | True | True | CORRECT | 2.409s |
| simpleqa-3988 | 1 | True | True | CORRECT | 1.704s |
| simpleqa-4009 | 1 | False | False | WRONG | 1.75s |
| simpleqa-4029 | 1 | False | False | WRONG | 1.778s |
| simpleqa-4045 | 1 | True | True | CORRECT | 1.643s |
| simpleqa-4051 | 1 | True | True | CORRECT | 1.47s |
| simpleqa-4086 | 1 | True | True | CORRECT | 4.196s |
| simpleqa-4095 | 1 | True | True | CORRECT | 1.581s |
| simpleqa-4170 | 1 | True | True | CORRECT | 2.386s |
| simpleqa-4174 | 1 | True | True | CORRECT | 1.458s |
| simpleqa-4224 | 1 | True | True | CORRECT | 4.652s |
| simpleqa-4227 | 1 | True | True | CORRECT | 2.029s |
| simpleqa-4266 | 1 | True | True | CORRECT | 1.805s |
| simpleqa-4273 | 1 | True | True | WRONG | 2.931s |
| simpleqa-4288 | 1 | False | False | WRONG | 1.527s |
| simpleqa-4290 | 1 | False | False | WRONG | 1.904s |

## Misses (audit trail)

- simpleqa-0131 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-0204 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-0340 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-0404 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-0454 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-0516 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-0553 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-0655 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-0831 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-0833 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-0972 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-1142 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-1510 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-1540 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-1636 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-1642 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-1851 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-1930 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-1944 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-1951 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-2118 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-2295 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-2451 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-2553 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-2564 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-2773 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-2849 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-3159 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-3411 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-3506 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-4009 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-4029 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-4288 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-4290 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)

Grading is deterministic (benchlib/graders.py): no LLM judge ran for this summary.
