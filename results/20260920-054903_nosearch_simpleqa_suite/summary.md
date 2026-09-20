# bench run: nosearch on simpleqa

- run: 20260920-054903 (git 5aeb219), sample `simpleqa_n200_seed20260919` frozen 2026-09-19
- calls: 200 (200 questions x 1 repeat(s)), errors: 0
- retrieval hit-rate: **39.0%** (95% CI [32.5%, 45.9%], Wilson)
- answer accuracy (answer-producing provider): **39.6%** (78/197 CORRECT), abstains: 0 (never counted as correct)
- SimpleQA official-prompt judge cross-check ran on 197 answers: 0 CORRECT / 0 WRONG / 0 NOT_ATTEMPTED / 197 errors
- latency (client-side): mean 9.785s, p50 5.404s, p95 34.072s, max 67.645s

## Per-question

| id | calls | hit_all | hit_any | verdicts | mean latency |
|---|---|---|---|---|---|
| simpleqa-0031 | 1 | False | False | WRONG | 4.987s |
| simpleqa-0034 | 1 | False | False | WRONG | 1.983s |
| simpleqa-0039 | 1 | True | True | CORRECT | 9.896s |
| simpleqa-0072 | 1 | True | True | CORRECT | 62.598s |
| simpleqa-0095 | 1 | False | False | WRONG | 11.953s |
| simpleqa-0110 | 1 | True | True | CORRECT | 1.686s |
| simpleqa-0117 | 1 | True | True | CORRECT | 3.267s |
| simpleqa-0131 | 1 | False | False | WRONG | 6.834s |
| simpleqa-0142 | 1 | True | True | CORRECT | 1.278s |
| simpleqa-0184 | 1 | False | False | WRONG | 7.535s |
| simpleqa-0189 | 1 | True | True | CORRECT | 9.43s |
| simpleqa-0192 | 1 | True | True | CORRECT | 1.616s |
| simpleqa-0204 | 1 | True | True | CORRECT | 9.586s |
| simpleqa-0230 | 1 | False | False | WRONG | 14.903s |
| simpleqa-0260 | 1 | False | False | WRONG | 12.3s |
| simpleqa-0272 | 1 | True | True | CORRECT | 3.979s |
| simpleqa-0297 | 1 | False | False | WRONG | 3.827s |
| simpleqa-0298 | 1 | False | False | WRONG | 3.261s |
| simpleqa-0340 | 1 | False | False | WRONG | 2.923s |
| simpleqa-0368 | 1 | True | True | CORRECT | 0.749s |
| simpleqa-0376 | 1 | False | False | WRONG | 1.589s |
| simpleqa-0379 | 1 | True | True | CORRECT | 4.86s |
| simpleqa-0404 | 1 | False | False | WRONG | 3.86s |
| simpleqa-0409 | 1 | True | True | CORRECT | 1.395s |
| simpleqa-0454 | 1 | False | False | WRONG | 3.599s |
| simpleqa-0512 | 1 | False | False | WRONG | 4.813s |
| simpleqa-0516 | 1 | False | False | WRONG | 20.752s |
| simpleqa-0522 | 1 | True | True | CORRECT | 2.133s |
| simpleqa-0553 | 1 | False | False | WRONG | 17.04s |
| simpleqa-0556 | 1 | True | True | CORRECT | 6.516s |
| simpleqa-0572 | 1 | False | False | WRONG | 2.933s |
| simpleqa-0626 | 1 | True | True | CORRECT | 3.137s |
| simpleqa-0651 | 1 | False | False | WRONG | 7.755s |
| simpleqa-0653 | 1 | False | False | WRONG | 5.52s |
| simpleqa-0655 | 1 | False | False | WRONG | 5.964s |
| simpleqa-0662 | 1 | False | False | WRONG | 23.143s |
| simpleqa-0663 | 1 | False | False | WRONG | 3.582s |
| simpleqa-0667 | 1 | False | False | WRONG | 15.488s |
| simpleqa-0669 | 1 | False | False | WRONG | 3.273s |
| simpleqa-0671 | 1 | True | True | CORRECT | 1.225s |
| simpleqa-0677 | 1 | False | False | WRONG | 12.246s |
| simpleqa-0682 | 1 | False | False | WRONG | 6.52s |
| simpleqa-0722 | 1 | True | True | CORRECT | 5.849s |
| simpleqa-0738 | 1 | False | False | WRONG | 4.06s |
| simpleqa-0750 | 1 | False | False | WRONG | 4.997s |
| simpleqa-0761 | 1 | False | False | WRONG | 5.258s |
| simpleqa-0781 | 1 | True | True | CORRECT | 2.549s |
| simpleqa-0783 | 1 | False | False | WRONG | 2.721s |
| simpleqa-0805 | 1 | False | False | WRONG | 25.366s |
| simpleqa-0812 | 1 | True | True | CORRECT | 2.956s |
| simpleqa-0824 | 1 | True | True | CORRECT | 4.121s |
| simpleqa-0825 | 1 | False | False | WRONG | 3.599s |
| simpleqa-0831 | 1 | True | True | CORRECT | 2.79s |
| simpleqa-0833 | 1 | False | False | WRONG | 2.602s |
| simpleqa-0873 | 1 | True | True | CORRECT | 2.523s |
| simpleqa-0894 | 1 | False | False | WRONG | 16.337s |
| simpleqa-0896 | 1 | False | False | WRONG | 7.678s |
| simpleqa-0972 | 1 | False | False | WRONG | 1.952s |
| simpleqa-0979 | 1 | True | True | CORRECT | 5.713s |
| simpleqa-1017 | 1 | False | False | MISS | 54.924s |
| simpleqa-1020 | 1 | False | False | WRONG | 10.274s |
| simpleqa-1025 | 1 | False | False | WRONG | 2.279s |
| simpleqa-1028 | 1 | False | False | WRONG | 4.732s |
| simpleqa-1135 | 1 | True | True | CORRECT | 1.618s |
| simpleqa-1142 | 1 | False | False | WRONG | 4.762s |
| simpleqa-1263 | 1 | True | True | CORRECT | 14.301s |
| simpleqa-1270 | 1 | False | False | WRONG | 34.072s |
| simpleqa-1271 | 1 | False | False | WRONG | 3.735s |
| simpleqa-1302 | 1 | True | True | CORRECT | 1.773s |
| simpleqa-1317 | 1 | False | False | WRONG | 3.121s |
| simpleqa-1359 | 1 | False | False | WRONG | 10.723s |
| simpleqa-1415 | 1 | False | False | WRONG | 16.537s |
| simpleqa-1437 | 1 | False | False | WRONG | 4.26s |
| simpleqa-1438 | 1 | True | True | CORRECT | 25.104s |
| simpleqa-1480 | 1 | False | False | WRONG | 51.826s |
| simpleqa-1490 | 1 | True | True | CORRECT | 2.251s |
| simpleqa-1501 | 1 | True | True | CORRECT | 2.587s |
| simpleqa-1504 | 1 | False | False | WRONG | 9.847s |
| simpleqa-1510 | 1 | False | False | WRONG | 5.926s |
| simpleqa-1514 | 1 | False | False | WRONG | 10.001s |
| simpleqa-1518 | 1 | False | False | MISS | 3.968s |
| simpleqa-1525 | 1 | True | True | CORRECT | 7.643s |
| simpleqa-1540 | 1 | False | False | WRONG | 48.363s |
| simpleqa-1548 | 1 | True | True | CORRECT | 17.847s |
| simpleqa-1579 | 1 | False | False | WRONG | 14.534s |
| simpleqa-1583 | 1 | False | False | WRONG | 7.053s |
| simpleqa-1615 | 1 | False | False | WRONG | 14.077s |
| simpleqa-1627 | 1 | False | False | WRONG | 14.822s |
| simpleqa-1636 | 1 | False | False | WRONG | 23.877s |
| simpleqa-1642 | 1 | False | False | WRONG | 67.645s |
| simpleqa-1644 | 1 | True | True | CORRECT | 4.91s |
| simpleqa-1708 | 1 | True | True | CORRECT | 3.728s |
| simpleqa-1787 | 1 | False | False | WRONG | 4.159s |
| simpleqa-1795 | 1 | False | False | WRONG | 19.099s |
| simpleqa-1808 | 1 | True | True | CORRECT | 1.955s |
| simpleqa-1839 | 1 | False | False | WRONG | 8.063s |
| simpleqa-1851 | 1 | False | False | WRONG | 63.518s |
| simpleqa-1867 | 1 | False | False | WRONG | 10.516s |
| simpleqa-1884 | 1 | False | False | WRONG | 3.921s |
| simpleqa-1892 | 1 | True | True | CORRECT | 3.015s |
| simpleqa-1927 | 1 | True | True | CORRECT | 4.364s |
| simpleqa-1928 | 1 | True | True | CORRECT | 1.557s |
| simpleqa-1930 | 1 | False | False | WRONG | 5.404s |
| simpleqa-1944 | 1 | False | False | WRONG | 12.692s |
| simpleqa-1951 | 1 | False | False | WRONG | 7.87s |
| simpleqa-2042 | 1 | True | True | CORRECT | 2.322s |
| simpleqa-2081 | 1 | False | False | WRONG | 28.673s |
| simpleqa-2118 | 1 | False | False | WRONG | 2.841s |
| simpleqa-2130 | 1 | True | True | CORRECT | 1.91s |
| simpleqa-2134 | 1 | False | False | WRONG | 4.84s |
| simpleqa-2148 | 1 | False | False | WRONG | 4.836s |
| simpleqa-2163 | 1 | True | True | CORRECT | 6.449s |
| simpleqa-2191 | 1 | False | False | WRONG | 2.719s |
| simpleqa-2204 | 1 | False | False | WRONG | 9.734s |
| simpleqa-2295 | 1 | True | True | CORRECT | 4.986s |
| simpleqa-2351 | 1 | True | True | CORRECT | 1.439s |
| simpleqa-2411 | 1 | False | False | WRONG | 13.814s |
| simpleqa-2441 | 1 | False | False | MISS | 3.85s |
| simpleqa-2451 | 1 | False | False | WRONG | 4.1s |
| simpleqa-2453 | 1 | True | True | CORRECT | 7.689s |
| simpleqa-2462 | 1 | True | True | CORRECT | 23.955s |
| simpleqa-2517 | 1 | True | True | CORRECT | 3.201s |
| simpleqa-2521 | 1 | False | False | WRONG | 13.882s |
| simpleqa-2539 | 1 | True | True | CORRECT | 1.975s |
| simpleqa-2553 | 1 | True | True | CORRECT | 2.967s |
| simpleqa-2564 | 1 | False | False | WRONG | 19.994s |
| simpleqa-2588 | 1 | True | True | CORRECT | 6.238s |
| simpleqa-2605 | 1 | False | False | WRONG | 6.214s |
| simpleqa-2651 | 1 | True | True | CORRECT | 3.125s |
| simpleqa-2662 | 1 | False | False | WRONG | 4.557s |
| simpleqa-2663 | 1 | True | True | CORRECT | 2.628s |
| simpleqa-2681 | 1 | True | True | CORRECT | 14.336s |
| simpleqa-2728 | 1 | False | False | WRONG | 5.5s |
| simpleqa-2773 | 1 | True | True | CORRECT | 2.109s |
| simpleqa-2781 | 1 | True | True | CORRECT | 6.86s |
| simpleqa-2786 | 1 | True | True | CORRECT | 7.021s |
| simpleqa-2804 | 1 | False | False | WRONG | 14.807s |
| simpleqa-2844 | 1 | False | False | WRONG | 16.333s |
| simpleqa-2849 | 1 | True | True | CORRECT | 9.72s |
| simpleqa-2859 | 1 | True | True | CORRECT | 6.182s |
| simpleqa-2875 | 1 | True | True | CORRECT | 6.871s |
| simpleqa-2889 | 1 | True | True | CORRECT | 14.679s |
| simpleqa-2914 | 1 | False | False | WRONG | 10.856s |
| simpleqa-2923 | 1 | False | False | WRONG | 4.835s |
| simpleqa-2943 | 1 | False | False | WRONG | 4.351s |
| simpleqa-2954 | 1 | True | True | CORRECT | 1.834s |
| simpleqa-2994 | 1 | False | False | WRONG | 4.154s |
| simpleqa-2995 | 1 | False | False | WRONG | 17.286s |
| simpleqa-3010 | 1 | False | False | WRONG | 3.659s |
| simpleqa-3022 | 1 | False | False | WRONG | 5.978s |
| simpleqa-3092 | 1 | False | False | WRONG | 18.256s |
| simpleqa-3103 | 1 | False | False | WRONG | 7.17s |
| simpleqa-3107 | 1 | False | False | WRONG | 53.724s |
| simpleqa-3127 | 1 | False | False | WRONG | 2.723s |
| simpleqa-3140 | 1 | False | False | WRONG | 2.933s |
| simpleqa-3159 | 1 | False | False | WRONG | 3.744s |
| simpleqa-3186 | 1 | True | True | CORRECT | 2.538s |
| simpleqa-3200 | 1 | True | True | CORRECT | 1.554s |
| simpleqa-3220 | 1 | False | False | WRONG | 37.03s |
| simpleqa-3237 | 1 | False | False | WRONG | 32.857s |
| simpleqa-3271 | 1 | False | False | WRONG | 8.543s |
| simpleqa-3282 | 1 | True | True | CORRECT | 2.197s |
| simpleqa-3295 | 1 | False | False | WRONG | 3.891s |
| simpleqa-3343 | 1 | False | False | WRONG | 44.454s |
| simpleqa-3379 | 1 | False | False | WRONG | 5.974s |
| simpleqa-3389 | 1 | True | True | CORRECT | 4.253s |
| simpleqa-3411 | 1 | False | False | WRONG | 3.962s |
| simpleqa-3463 | 1 | True | True | CORRECT | 3.254s |
| simpleqa-3474 | 1 | False | False | WRONG | 13.89s |
| simpleqa-3479 | 1 | False | False | WRONG | 24.76s |
| simpleqa-3506 | 1 | True | True | CORRECT | 3.307s |
| simpleqa-3593 | 1 | False | False | WRONG | 2.951s |
| simpleqa-3620 | 1 | True | True | CORRECT | 4.831s |
| simpleqa-3630 | 1 | False | False | WRONG | 11.838s |
| simpleqa-3642 | 1 | True | True | CORRECT | 9.232s |
| simpleqa-3644 | 1 | True | True | CORRECT | 1.593s |
| simpleqa-3697 | 1 | True | True | CORRECT | 2.563s |
| simpleqa-3728 | 1 | True | True | CORRECT | 1.749s |
| simpleqa-3772 | 1 | False | False | WRONG | 8.607s |
| simpleqa-3793 | 1 | True | True | CORRECT | 2.929s |
| simpleqa-3862 | 1 | True | True | CORRECT | 12.211s |
| simpleqa-3896 | 1 | False | False | WRONG | 5.435s |
| simpleqa-3922 | 1 | False | False | WRONG | 7.711s |
| simpleqa-3934 | 1 | False | False | WRONG | 10.008s |
| simpleqa-3977 | 1 | False | False | WRONG | 14.228s |
| simpleqa-3988 | 1 | False | False | WRONG | 17.371s |
| simpleqa-4009 | 1 | True | True | CORRECT | 3.559s |
| simpleqa-4029 | 1 | False | False | WRONG | 3.951s |
| simpleqa-4045 | 1 | False | False | WRONG | 10.545s |
| simpleqa-4051 | 1 | True | True | CORRECT | 2.168s |
| simpleqa-4086 | 1 | False | False | WRONG | 3.737s |
| simpleqa-4095 | 1 | False | False | WRONG | 15.045s |
| simpleqa-4170 | 1 | False | False | WRONG | 5.485s |
| simpleqa-4174 | 1 | True | True | CORRECT | 12.751s |
| simpleqa-4224 | 1 | False | False | WRONG | 12.031s |
| simpleqa-4227 | 1 | False | False | WRONG | 3.219s |
| simpleqa-4266 | 1 | True | True | CORRECT | 35.441s |
| simpleqa-4273 | 1 | False | False | WRONG | 15.119s |
| simpleqa-4288 | 1 | True | True | CORRECT | 8.515s |
| simpleqa-4290 | 1 | True | True | CORRECT | 2.68s |

## Misses (audit trail)

- simpleqa-0031 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-0034 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-0095 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-0131 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-0184 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-0230 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-0260 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-0297 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-0298 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-0340 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-0376 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-0404 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-0454 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-0512 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-0516 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-0553 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-0572 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-0651 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-0653 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-0655 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-0662 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-0663 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-0667 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-0669 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-0677 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-0682 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-0738 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-0750 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-0761 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-0783 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-0805 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-0825 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-0833 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-0894 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-0896 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-0972 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-1017 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-1020 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-1025 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-1028 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-1142 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-1270 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-1271 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-1317 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-1359 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-1415 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-1437 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-1480 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-1504 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-1510 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-1514 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-1518 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-1540 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-1579 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-1583 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-1615 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-1627 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-1636 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-1642 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-1787 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-1795 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-1839 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-1851 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-1867 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-1884 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-1930 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-1944 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-1951 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-2081 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-2118 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-2134 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-2148 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-2191 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-2204 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-2411 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-2441 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-2451 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-2521 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-2564 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-2605 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-2662 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-2728 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-2804 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-2844 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-2914 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-2923 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-2943 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-2994 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-2995 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-3010 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-3022 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-3092 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-3103 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-3107 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-3127 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-3140 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-3159 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-3220 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-3237 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-3271 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-3295 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-3343 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-3379 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-3411 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-3474 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-3479 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-3593 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-3630 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-3772 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-3896 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-3922 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-3934 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-3977 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-3988 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-4029 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-4045 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-4086 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-4095 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-4170 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-4224 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-4227 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-4273 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)

Grading is deterministic (benchlib/graders.py): no LLM judge ran for this summary.
