# bench run: ransack on simpleqa

- run: 20260920-045040 (git f756e7a), sample `simpleqa_n200_seed20260919` frozen 2026-09-19
- calls: 200 (200 questions x 1 repeat(s)), errors: 0
- retrieval hit-rate: **74.5%** (95% CI [68.0%, 80.0%], Wilson)
- judge was configured but did not run (no OPENAI_API_KEY): answer grades fall back to containment; judge cross-check skipped, and this is recorded
- latency (client-side): mean 2.92s, p50 2.454s, p95 5.534s, max 21.109s

## Per-question

| id | calls | hit_all | hit_any | verdicts | mean latency |
|---|---|---|---|---|---|
| simpleqa-0031 | 1 | True | True | MISS | 3.232s |
| simpleqa-0034 | 1 | True | True | MISS | 2.024s |
| simpleqa-0039 | 1 | True | True | MISS | 1.65s |
| simpleqa-0072 | 1 | True | True | MISS | 2.189s |
| simpleqa-0095 | 1 | False | False | MISS | 2.158s |
| simpleqa-0110 | 1 | False | False | MISS | 2.975s |
| simpleqa-0117 | 1 | True | True | MISS | 2.968s |
| simpleqa-0131 | 1 | False | False | MISS | 2.025s |
| simpleqa-0142 | 1 | True | True | MISS | 4.85s |
| simpleqa-0184 | 1 | True | True | MISS | 2.218s |
| simpleqa-0189 | 1 | True | True | MISS | 2.112s |
| simpleqa-0192 | 1 | True | True | MISS | 1.84s |
| simpleqa-0204 | 1 | False | False | MISS | 1.536s |
| simpleqa-0230 | 1 | False | False | MISS | 4.949s |
| simpleqa-0260 | 1 | False | False | MISS | 1.472s |
| simpleqa-0272 | 1 | True | True | MISS | 2.564s |
| simpleqa-0297 | 1 | True | True | MISS | 1.663s |
| simpleqa-0298 | 1 | True | True | MISS | 3.053s |
| simpleqa-0340 | 1 | True | True | MISS | 9.713s |
| simpleqa-0368 | 1 | False | False | MISS | 5.401s |
| simpleqa-0376 | 1 | True | True | MISS | 2.034s |
| simpleqa-0379 | 1 | True | True | MISS | 21.109s |
| simpleqa-0404 | 1 | False | False | MISS | 1.969s |
| simpleqa-0409 | 1 | True | True | MISS | 1.829s |
| simpleqa-0454 | 1 | False | False | MISS | 1.816s |
| simpleqa-0512 | 1 | True | True | MISS | 1.83s |
| simpleqa-0516 | 1 | False | False | MISS | 1.925s |
| simpleqa-0522 | 1 | True | True | MISS | 2.566s |
| simpleqa-0553 | 1 | False | False | MISS | 2.529s |
| simpleqa-0556 | 1 | True | True | MISS | 3.114s |
| simpleqa-0572 | 1 | False | False | MISS | 3.875s |
| simpleqa-0626 | 1 | False | False | MISS | 1.921s |
| simpleqa-0651 | 1 | True | True | MISS | 2.454s |
| simpleqa-0653 | 1 | True | True | MISS | 3.089s |
| simpleqa-0655 | 1 | True | True | MISS | 2.125s |
| simpleqa-0662 | 1 | True | True | MISS | 2.986s |
| simpleqa-0663 | 1 | True | True | MISS | 5.519s |
| simpleqa-0667 | 1 | True | True | MISS | 1.611s |
| simpleqa-0669 | 1 | False | False | MISS | 2.621s |
| simpleqa-0671 | 1 | True | True | MISS | 1.661s |
| simpleqa-0677 | 1 | True | True | MISS | 1.896s |
| simpleqa-0682 | 1 | True | True | MISS | 2.232s |
| simpleqa-0722 | 1 | True | True | MISS | 3.193s |
| simpleqa-0738 | 1 | False | False | MISS | 2.182s |
| simpleqa-0750 | 1 | True | True | MISS | 3.286s |
| simpleqa-0761 | 1 | False | False | MISS | 6.102s |
| simpleqa-0781 | 1 | True | True | MISS | 2.113s |
| simpleqa-0783 | 1 | True | True | MISS | 1.972s |
| simpleqa-0805 | 1 | True | True | MISS | 4.543s |
| simpleqa-0812 | 1 | True | True | MISS | 4.063s |
| simpleqa-0824 | 1 | True | True | MISS | 2.339s |
| simpleqa-0825 | 1 | True | True | MISS | 1.934s |
| simpleqa-0831 | 1 | True | True | MISS | 2.559s |
| simpleqa-0833 | 1 | True | True | MISS | 2.801s |
| simpleqa-0873 | 1 | True | True | MISS | 3.627s |
| simpleqa-0894 | 1 | False | False | MISS | 2.388s |
| simpleqa-0896 | 1 | True | True | MISS | 2.109s |
| simpleqa-0972 | 1 | False | False | MISS | 1.654s |
| simpleqa-0979 | 1 | True | True | MISS | 2.459s |
| simpleqa-1017 | 1 | False | False | MISS | 3.673s |
| simpleqa-1020 | 1 | True | True | MISS | 8.842s |
| simpleqa-1025 | 1 | True | True | MISS | 2.383s |
| simpleqa-1028 | 1 | True | True | MISS | 1.971s |
| simpleqa-1135 | 1 | True | True | MISS | 2.774s |
| simpleqa-1142 | 1 | True | True | MISS | 3.622s |
| simpleqa-1263 | 1 | False | False | MISS | 1.967s |
| simpleqa-1270 | 1 | True | True | MISS | 2.519s |
| simpleqa-1271 | 1 | True | True | MISS | 4.333s |
| simpleqa-1302 | 1 | True | True | MISS | 2.716s |
| simpleqa-1317 | 1 | True | True | MISS | 3.494s |
| simpleqa-1359 | 1 | True | True | MISS | 6.196s |
| simpleqa-1415 | 1 | True | True | MISS | 1.958s |
| simpleqa-1437 | 1 | True | True | MISS | 7.537s |
| simpleqa-1438 | 1 | True | True | MISS | 1.768s |
| simpleqa-1480 | 1 | False | False | MISS | 1.426s |
| simpleqa-1490 | 1 | True | True | MISS | 2.343s |
| simpleqa-1501 | 1 | True | True | MISS | 2.439s |
| simpleqa-1504 | 1 | False | False | MISS | 2.106s |
| simpleqa-1510 | 1 | False | False | MISS | 2.074s |
| simpleqa-1514 | 1 | True | True | MISS | 3.689s |
| simpleqa-1518 | 1 | True | True | MISS | 2.106s |
| simpleqa-1525 | 1 | True | True | MISS | 1.572s |
| simpleqa-1540 | 1 | True | True | MISS | 1.439s |
| simpleqa-1548 | 1 | True | True | MISS | 4.506s |
| simpleqa-1579 | 1 | True | True | MISS | 2.01s |
| simpleqa-1583 | 1 | False | False | MISS | 3.269s |
| simpleqa-1615 | 1 | True | True | MISS | 1.963s |
| simpleqa-1627 | 1 | True | True | MISS | 3.458s |
| simpleqa-1636 | 1 | False | False | MISS | 2.704s |
| simpleqa-1642 | 1 | False | False | MISS | 2.529s |
| simpleqa-1644 | 1 | True | True | MISS | 2.285s |
| simpleqa-1708 | 1 | True | True | MISS | 3.183s |
| simpleqa-1787 | 1 | True | True | MISS | 2.132s |
| simpleqa-1795 | 1 | True | True | MISS | 1.595s |
| simpleqa-1808 | 1 | True | True | MISS | 3.515s |
| simpleqa-1839 | 1 | True | True | MISS | 2.485s |
| simpleqa-1851 | 1 | False | False | MISS | 2.682s |
| simpleqa-1867 | 1 | True | True | MISS | 1.786s |
| simpleqa-1884 | 1 | True | True | MISS | 3.845s |
| simpleqa-1892 | 1 | True | True | MISS | 8.96s |
| simpleqa-1927 | 1 | True | True | MISS | 1.901s |
| simpleqa-1928 | 1 | True | True | MISS | 3.668s |
| simpleqa-1930 | 1 | True | True | MISS | 2.576s |
| simpleqa-1944 | 1 | False | False | MISS | 2.25s |
| simpleqa-1951 | 1 | False | False | MISS | 3.324s |
| simpleqa-2042 | 1 | True | True | MISS | 1.707s |
| simpleqa-2081 | 1 | True | True | MISS | 1.776s |
| simpleqa-2118 | 1 | False | False | MISS | 2.67s |
| simpleqa-2130 | 1 | True | True | MISS | 1.79s |
| simpleqa-2134 | 1 | True | True | MISS | 3.177s |
| simpleqa-2148 | 1 | True | True | MISS | 1.92s |
| simpleqa-2163 | 1 | True | True | MISS | 2.643s |
| simpleqa-2191 | 1 | True | True | MISS | 1.479s |
| simpleqa-2204 | 1 | True | True | MISS | 1.995s |
| simpleqa-2295 | 1 | True | True | MISS | 1.267s |
| simpleqa-2351 | 1 | True | True | MISS | 1.637s |
| simpleqa-2411 | 1 | False | False | MISS | 2.466s |
| simpleqa-2441 | 1 | True | True | MISS | 2.892s |
| simpleqa-2451 | 1 | False | False | MISS | 2.919s |
| simpleqa-2453 | 1 | True | True | MISS | 1.307s |
| simpleqa-2462 | 1 | True | True | MISS | 2.333s |
| simpleqa-2517 | 1 | False | False | MISS | 5.534s |
| simpleqa-2521 | 1 | True | True | MISS | 1.926s |
| simpleqa-2539 | 1 | True | True | MISS | 3.717s |
| simpleqa-2553 | 1 | True | True | MISS | 3.763s |
| simpleqa-2564 | 1 | False | False | MISS | 2.478s |
| simpleqa-2588 | 1 | True | True | MISS | 2.899s |
| simpleqa-2605 | 1 | True | True | MISS | 1.781s |
| simpleqa-2651 | 1 | True | True | MISS | 4.94s |
| simpleqa-2662 | 1 | True | True | MISS | 1.986s |
| simpleqa-2663 | 1 | True | True | MISS | 1.924s |
| simpleqa-2681 | 1 | False | False | MISS | 2.189s |
| simpleqa-2728 | 1 | True | True | MISS | 2.058s |
| simpleqa-2773 | 1 | True | True | MISS | 4.08s |
| simpleqa-2781 | 1 | True | True | MISS | 1.576s |
| simpleqa-2786 | 1 | True | True | MISS | 2.195s |
| simpleqa-2804 | 1 | True | True | MISS | 2.307s |
| simpleqa-2844 | 1 | True | True | MISS | 1.736s |
| simpleqa-2849 | 1 | True | True | MISS | 1.591s |
| simpleqa-2859 | 1 | False | False | MISS | 4.826s |
| simpleqa-2875 | 1 | False | False | MISS | 1.91s |
| simpleqa-2889 | 1 | True | True | MISS | 1.928s |
| simpleqa-2914 | 1 | False | False | MISS | 2.543s |
| simpleqa-2923 | 1 | True | True | MISS | 1.904s |
| simpleqa-2943 | 1 | True | True | MISS | 2.987s |
| simpleqa-2954 | 1 | True | True | MISS | 2.171s |
| simpleqa-2994 | 1 | True | True | MISS | 1.588s |
| simpleqa-2995 | 1 | False | False | MISS | 3.029s |
| simpleqa-3010 | 1 | True | True | MISS | 2.635s |
| simpleqa-3022 | 1 | True | True | MISS | 3.19s |
| simpleqa-3092 | 1 | True | True | MISS | 3.477s |
| simpleqa-3103 | 1 | True | True | MISS | 2.167s |
| simpleqa-3107 | 1 | True | True | MISS | 2.462s |
| simpleqa-3127 | 1 | True | True | MISS | 3.332s |
| simpleqa-3140 | 1 | True | True | MISS | 3.934s |
| simpleqa-3159 | 1 | False | False | MISS | 3.375s |
| simpleqa-3186 | 1 | True | True | MISS | 3.159s |
| simpleqa-3200 | 1 | True | True | MISS | 2.048s |
| simpleqa-3220 | 1 | True | True | MISS | 2.333s |
| simpleqa-3237 | 1 | False | False | MISS | 3.47s |
| simpleqa-3271 | 1 | True | True | MISS | 1.644s |
| simpleqa-3282 | 1 | True | True | MISS | 6.202s |
| simpleqa-3295 | 1 | True | True | MISS | 3.588s |
| simpleqa-3343 | 1 | True | True | MISS | 2.338s |
| simpleqa-3379 | 1 | True | True | MISS | 3.008s |
| simpleqa-3389 | 1 | True | True | MISS | 5.762s |
| simpleqa-3411 | 1 | False | False | MISS | 3.956s |
| simpleqa-3463 | 1 | True | True | MISS | 2.396s |
| simpleqa-3474 | 1 | False | False | MISS | 2.294s |
| simpleqa-3479 | 1 | True | True | MISS | 2.215s |
| simpleqa-3506 | 1 | False | False | MISS | 2.122s |
| simpleqa-3593 | 1 | True | True | MISS | 3.873s |
| simpleqa-3620 | 1 | True | True | MISS | 4.36s |
| simpleqa-3630 | 1 | False | False | MISS | 2.005s |
| simpleqa-3642 | 1 | True | True | MISS | 2.266s |
| simpleqa-3644 | 1 | True | True | MISS | 3.717s |
| simpleqa-3697 | 1 | True | True | MISS | 2.974s |
| simpleqa-3728 | 1 | True | True | MISS | 2.525s |
| simpleqa-3772 | 1 | True | True | MISS | 2.292s |
| simpleqa-3793 | 1 | True | True | MISS | 2.921s |
| simpleqa-3862 | 1 | True | True | MISS | 3.461s |
| simpleqa-3896 | 1 | True | True | MISS | 4.258s |
| simpleqa-3922 | 1 | True | True | MISS | 2.365s |
| simpleqa-3934 | 1 | True | True | MISS | 2.575s |
| simpleqa-3977 | 1 | True | True | MISS | 1.827s |
| simpleqa-3988 | 1 | True | True | MISS | 2.559s |
| simpleqa-4009 | 1 | False | False | MISS | 2.246s |
| simpleqa-4029 | 1 | False | False | MISS | 3.359s |
| simpleqa-4045 | 1 | True | True | MISS | 1.73s |
| simpleqa-4051 | 1 | False | False | MISS | 3.685s |
| simpleqa-4086 | 1 | True | True | MISS | 3.52s |
| simpleqa-4095 | 1 | True | True | MISS | 2.348s |
| simpleqa-4170 | 1 | True | True | MISS | 3.311s |
| simpleqa-4174 | 1 | True | True | MISS | 1.939s |
| simpleqa-4224 | 1 | False | False | MISS | 1.844s |
| simpleqa-4227 | 1 | True | True | MISS | 1.77s |
| simpleqa-4266 | 1 | True | True | MISS | 1.977s |
| simpleqa-4273 | 1 | True | True | MISS | 2.5s |
| simpleqa-4288 | 1 | False | False | MISS | 2.965s |
| simpleqa-4290 | 1 | False | False | MISS | 5.972s |

## Misses (audit trail)

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
- simpleqa-0894 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-0972 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-1017 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-1263 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-1480 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-1504 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-1510 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-1583 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-1636 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-1642 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-1851 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-1944 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-1951 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-2118 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-2411 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-2451 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-2517 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-2564 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-2681 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-2859 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-2875 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-2914 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-2995 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-3159 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-3237 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-3411 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-3474 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-3506 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-3630 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-4009 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-4029 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-4051 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-4224 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-4288 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-4290 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)

Grading is deterministic (benchlib/graders.py): no LLM judge ran for this summary.
