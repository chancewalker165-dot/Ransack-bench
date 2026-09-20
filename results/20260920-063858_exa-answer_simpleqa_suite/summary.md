# bench run: exa-answer on simpleqa

- run: 20260920-063858 (git 90c657a), sample `simpleqa_n200_seed20260919` frozen 2026-09-19
- calls: 200 (200 questions x 1 repeat(s)), errors: 0
- retrieval hit-rate: **91.0%** (95% CI [86.2%, 94.2%], Wilson)
- answer accuracy (answer-producing provider): **91.5%** (183/200 CORRECT), abstains: 4 (never counted as correct)
- SimpleQA official-prompt judge cross-check ran on 200 answers: 181 CORRECT / 13 WRONG / 4 NOT_ATTEMPTED / 2 errors
- latency (client-side): mean 1.15s, p50 1.064s, p95 1.566s, max 4.202s

## Per-question

| id | calls | hit_all | hit_any | verdicts | mean latency |
|---|---|---|---|---|---|
| simpleqa-0031 | 1 | True | True | CORRECT | 0.993s |
| simpleqa-0034 | 1 | True | True | CORRECT | 1.296s |
| simpleqa-0039 | 1 | True | True | CORRECT | 1.181s |
| simpleqa-0072 | 1 | True | True | CORRECT | 0.991s |
| simpleqa-0095 | 1 | True | True | CORRECT | 0.995s |
| simpleqa-0110 | 1 | True | True | CORRECT | 0.883s |
| simpleqa-0117 | 1 | True | True | CORRECT | 0.925s |
| simpleqa-0131 | 1 | False | False | CORRECT | 1.111s |
| simpleqa-0142 | 1 | True | True | CORRECT | 1.155s |
| simpleqa-0184 | 1 | True | True | CORRECT | 1.106s |
| simpleqa-0189 | 1 | True | True | CORRECT | 1.377s |
| simpleqa-0192 | 1 | True | True | CORRECT | 1.245s |
| simpleqa-0204 | 1 | True | True | CORRECT | 1.072s |
| simpleqa-0230 | 1 | True | True | CORRECT | 1.157s |
| simpleqa-0260 | 1 | True | True | CORRECT | 0.906s |
| simpleqa-0272 | 1 | True | True | CORRECT | 1.133s |
| simpleqa-0297 | 1 | True | True | CORRECT | 0.93s |
| simpleqa-0298 | 1 | True | True | WRONG | 1.254s |
| simpleqa-0340 | 1 | True | True | CORRECT | 0.929s |
| simpleqa-0368 | 1 | True | True | CORRECT | 1.243s |
| simpleqa-0376 | 1 | True | True | CORRECT | 0.967s |
| simpleqa-0379 | 1 | True | True | CORRECT | 1.145s |
| simpleqa-0404 | 1 | False | False | CORRECT | 1.091s |
| simpleqa-0409 | 1 | True | True | CORRECT | 1.415s |
| simpleqa-0454 | 1 | False | False | CORRECT | 1.032s |
| simpleqa-0512 | 1 | True | True | CORRECT | 1.628s |
| simpleqa-0516 | 1 | False | False | CORRECT | 1.326s |
| simpleqa-0522 | 1 | True | True | CORRECT | 2.138s |
| simpleqa-0553 | 1 | True | True | WRONG | 1.803s |
| simpleqa-0556 | 1 | True | True | CORRECT | 1.238s |
| simpleqa-0572 | 1 | False | False | CORRECT | 0.991s |
| simpleqa-0626 | 1 | True | True | CORRECT | 1.436s |
| simpleqa-0651 | 1 | True | True | CORRECT | 1.319s |
| simpleqa-0653 | 1 | True | True | CORRECT | 1.116s |
| simpleqa-0655 | 1 | True | True | WRONG | 1.148s |
| simpleqa-0662 | 1 | True | True | CORRECT | 1.002s |
| simpleqa-0663 | 1 | True | True | CORRECT | 1.136s |
| simpleqa-0667 | 1 | True | True | CORRECT | 0.792s |
| simpleqa-0669 | 1 | True | True | CORRECT | 1.256s |
| simpleqa-0671 | 1 | True | True | CORRECT | 1.17s |
| simpleqa-0677 | 1 | True | True | CORRECT | 1.193s |
| simpleqa-0682 | 1 | True | True | CORRECT | 0.974s |
| simpleqa-0722 | 1 | True | True | CORRECT | 1.053s |
| simpleqa-0738 | 1 | False | False | WRONG | 1.164s |
| simpleqa-0750 | 1 | True | True | CORRECT | 1.042s |
| simpleqa-0761 | 1 | False | False | CORRECT | 3.279s |
| simpleqa-0781 | 1 | True | True | CORRECT | 1.009s |
| simpleqa-0783 | 1 | True | True | CORRECT | 0.957s |
| simpleqa-0805 | 1 | True | True | CORRECT | 1.079s |
| simpleqa-0812 | 1 | True | True | CORRECT | 0.937s |
| simpleqa-0824 | 1 | True | True | CORRECT | 0.959s |
| simpleqa-0825 | 1 | True | True | CORRECT | 0.905s |
| simpleqa-0831 | 1 | True | True | CORRECT | 1.27s |
| simpleqa-0833 | 1 | True | True | CORRECT | 1.222s |
| simpleqa-0873 | 1 | True | True | CORRECT | 1.474s |
| simpleqa-0894 | 1 | True | True | CORRECT | 0.936s |
| simpleqa-0896 | 1 | True | True | CORRECT | 0.963s |
| simpleqa-0972 | 1 | False | False | CORRECT | 1.196s |
| simpleqa-0979 | 1 | True | True | CORRECT | 1.023s |
| simpleqa-1017 | 1 | True | True | CORRECT | 1.052s |
| simpleqa-1020 | 1 | True | True | WRONG | 1.142s |
| simpleqa-1025 | 1 | True | True | CORRECT | 0.965s |
| simpleqa-1028 | 1 | True | True | CORRECT | 1.233s |
| simpleqa-1135 | 1 | True | True | CORRECT | 1.566s |
| simpleqa-1142 | 1 | True | True | CORRECT | 1.019s |
| simpleqa-1263 | 1 | True | True | CORRECT | 0.98s |
| simpleqa-1270 | 1 | True | True | CORRECT | 1.144s |
| simpleqa-1271 | 1 | True | True | CORRECT | 0.883s |
| simpleqa-1302 | 1 | True | True | CORRECT | 1.31s |
| simpleqa-1317 | 1 | True | True | CORRECT | 1.047s |
| simpleqa-1359 | 1 | True | True | CORRECT | 0.985s |
| simpleqa-1415 | 1 | True | True | CORRECT | 1.065s |
| simpleqa-1437 | 1 | True | True | CORRECT | 0.945s |
| simpleqa-1438 | 1 | True | True | CORRECT | 1.028s |
| simpleqa-1480 | 1 | True | True | CORRECT | 1.166s |
| simpleqa-1490 | 1 | True | True | CORRECT | 1.02s |
| simpleqa-1501 | 1 | True | True | CORRECT | 1.355s |
| simpleqa-1504 | 1 | True | True | CORRECT | 0.931s |
| simpleqa-1510 | 1 | False | False | CORRECT | 0.963s |
| simpleqa-1514 | 1 | True | True | CORRECT | 0.93s |
| simpleqa-1518 | 1 | True | True | CORRECT | 0.954s |
| simpleqa-1525 | 1 | True | True | CORRECT | 1.205s |
| simpleqa-1540 | 1 | True | True | CORRECT | 0.988s |
| simpleqa-1548 | 1 | True | True | CORRECT | 1.377s |
| simpleqa-1579 | 1 | True | True | CORRECT | 1.037s |
| simpleqa-1583 | 1 | True | True | CORRECT | 1.055s |
| simpleqa-1615 | 1 | True | True | CORRECT | 0.919s |
| simpleqa-1627 | 1 | True | True | CORRECT | 0.944s |
| simpleqa-1636 | 1 | True | True | CORRECT | 1.137s |
| simpleqa-1642 | 1 | False | False | CORRECT | 1.52s |
| simpleqa-1644 | 1 | True | True | CORRECT | 1.122s |
| simpleqa-1708 | 1 | True | True | CORRECT | 1.434s |
| simpleqa-1787 | 1 | True | True | CORRECT | 1.102s |
| simpleqa-1795 | 1 | True | True | CORRECT | 1.407s |
| simpleqa-1808 | 1 | True | True | CORRECT | 1.143s |
| simpleqa-1839 | 1 | True | True | CORRECT | 1.088s |
| simpleqa-1851 | 1 | True | True | CORRECT | 1.74s |
| simpleqa-1867 | 1 | True | True | CORRECT | 0.931s |
| simpleqa-1884 | 1 | True | True | CORRECT | 1.018s |
| simpleqa-1892 | 1 | True | True | CORRECT | 1.669s |
| simpleqa-1927 | 1 | True | True | CORRECT | 1.27s |
| simpleqa-1928 | 1 | True | True | CORRECT | 1.055s |
| simpleqa-1930 | 1 | True | True | CORRECT | 1.065s |
| simpleqa-1944 | 1 | False | False | CORRECT | 1.004s |
| simpleqa-1951 | 1 | True | True | CORRECT | 0.938s |
| simpleqa-2042 | 1 | True | True | CORRECT | 0.933s |
| simpleqa-2081 | 1 | True | True | CORRECT | 0.952s |
| simpleqa-2118 | 1 | False | False | ABSTAIN | 1.35s |
| simpleqa-2130 | 1 | True | True | CORRECT | 1.038s |
| simpleqa-2134 | 1 | True | True | CORRECT | 1.058s |
| simpleqa-2148 | 1 | True | True | CORRECT | 0.983s |
| simpleqa-2163 | 1 | True | True | CORRECT | 1.059s |
| simpleqa-2191 | 1 | True | True | CORRECT | 0.923s |
| simpleqa-2204 | 1 | True | True | CORRECT | 0.878s |
| simpleqa-2295 | 1 | True | True | CORRECT | 1.18s |
| simpleqa-2351 | 1 | True | True | CORRECT | 1.151s |
| simpleqa-2411 | 1 | True | True | CORRECT | 0.961s |
| simpleqa-2441 | 1 | True | True | CORRECT | 0.938s |
| simpleqa-2451 | 1 | True | True | CORRECT | 1.107s |
| simpleqa-2453 | 1 | True | True | CORRECT | 1.209s |
| simpleqa-2462 | 1 | True | True | CORRECT | 0.97s |
| simpleqa-2517 | 1 | True | True | CORRECT | 0.997s |
| simpleqa-2521 | 1 | True | True | CORRECT | 1.028s |
| simpleqa-2539 | 1 | True | True | CORRECT | 1.262s |
| simpleqa-2553 | 1 | True | True | CORRECT | 0.915s |
| simpleqa-2564 | 1 | True | True | WRONG | 1.123s |
| simpleqa-2588 | 1 | True | True | CORRECT | 0.926s |
| simpleqa-2605 | 1 | True | True | CORRECT | 0.9s |
| simpleqa-2651 | 1 | True | True | CORRECT | 1.018s |
| simpleqa-2662 | 1 | True | True | CORRECT | 0.92s |
| simpleqa-2663 | 1 | True | True | WRONG | 1.288s |
| simpleqa-2681 | 1 | True | True | CORRECT | 0.979s |
| simpleqa-2728 | 1 | True | True | CORRECT | 0.969s |
| simpleqa-2773 | 1 | True | True | CORRECT | 1.205s |
| simpleqa-2781 | 1 | True | True | CORRECT | 1.089s |
| simpleqa-2786 | 1 | True | True | CORRECT | 0.923s |
| simpleqa-2804 | 1 | True | True | CORRECT | 1.087s |
| simpleqa-2844 | 1 | True | True | CORRECT | 1.069s |
| simpleqa-2849 | 1 | True | True | ABSTAIN | 0.963s |
| simpleqa-2859 | 1 | True | True | CORRECT | 1.155s |
| simpleqa-2875 | 1 | True | True | CORRECT | 1.064s |
| simpleqa-2889 | 1 | True | True | CORRECT | 1.43s |
| simpleqa-2914 | 1 | True | True | WRONG | 1.613s |
| simpleqa-2923 | 1 | True | True | CORRECT | 0.961s |
| simpleqa-2943 | 1 | True | True | CORRECT | 1.026s |
| simpleqa-2954 | 1 | True | True | CORRECT | 0.956s |
| simpleqa-2994 | 1 | True | True | WRONG | 1.092s |
| simpleqa-2995 | 1 | False | False | ABSTAIN | 0.791s |
| simpleqa-3010 | 1 | True | True | CORRECT | 0.935s |
| simpleqa-3022 | 1 | False | False | CORRECT | 1.028s |
| simpleqa-3092 | 1 | True | True | CORRECT | 0.943s |
| simpleqa-3103 | 1 | True | True | CORRECT | 0.916s |
| simpleqa-3107 | 1 | True | True | CORRECT | 3.368s |
| simpleqa-3127 | 1 | True | True | CORRECT | 1.38s |
| simpleqa-3140 | 1 | True | True | CORRECT | 0.863s |
| simpleqa-3159 | 1 | False | False | CORRECT | 1.405s |
| simpleqa-3186 | 1 | True | True | CORRECT | 1.02s |
| simpleqa-3200 | 1 | True | True | CORRECT | 1.14s |
| simpleqa-3220 | 1 | True | True | CORRECT | 0.982s |
| simpleqa-3237 | 1 | True | True | CORRECT | 1.02s |
| simpleqa-3271 | 1 | True | True | CORRECT | 1.099s |
| simpleqa-3282 | 1 | True | True | CORRECT | 4.202s |
| simpleqa-3295 | 1 | True | True | CORRECT | 0.987s |
| simpleqa-3343 | 1 | True | True | CORRECT | 1.01s |
| simpleqa-3379 | 1 | True | True | CORRECT | 1.128s |
| simpleqa-3389 | 1 | True | True | CORRECT | 1.008s |
| simpleqa-3411 | 1 | False | False | WRONG | 0.988s |
| simpleqa-3463 | 1 | True | True | CORRECT | 1.322s |
| simpleqa-3474 | 1 | True | True | CORRECT | 0.964s |
| simpleqa-3479 | 1 | True | True | CORRECT | 0.922s |
| simpleqa-3506 | 1 | True | True | CORRECT | 1.714s |
| simpleqa-3593 | 1 | True | True | WRONG | 1.234s |
| simpleqa-3620 | 1 | True | True | CORRECT | 1.412s |
| simpleqa-3630 | 1 | True | True | CORRECT | 0.924s |
| simpleqa-3642 | 1 | True | True | CORRECT | 1.37s |
| simpleqa-3644 | 1 | True | True | CORRECT | 1.001s |
| simpleqa-3697 | 1 | True | True | CORRECT | 1.106s |
| simpleqa-3728 | 1 | True | True | CORRECT | 1.171s |
| simpleqa-3772 | 1 | False | False | ABSTAIN | 1.269s |
| simpleqa-3793 | 1 | True | True | WRONG | 1.109s |
| simpleqa-3862 | 1 | True | True | CORRECT | 1.032s |
| simpleqa-3896 | 1 | True | True | CORRECT | 1.046s |
| simpleqa-3922 | 1 | True | True | CORRECT | 0.931s |
| simpleqa-3934 | 1 | True | True | CORRECT | 1.184s |
| simpleqa-3977 | 1 | True | True | CORRECT | 1.058s |
| simpleqa-3988 | 1 | True | True | CORRECT | 0.919s |
| simpleqa-4009 | 1 | True | True | CORRECT | 1.371s |
| simpleqa-4029 | 1 | False | False | CORRECT | 1.069s |
| simpleqa-4045 | 1 | True | True | CORRECT | 1.143s |
| simpleqa-4051 | 1 | True | True | CORRECT | 1.234s |
| simpleqa-4086 | 1 | True | True | CORRECT | 1.113s |
| simpleqa-4095 | 1 | True | True | CORRECT | 1.019s |
| simpleqa-4170 | 1 | True | True | CORRECT | 0.881s |
| simpleqa-4174 | 1 | True | True | CORRECT | 0.98s |
| simpleqa-4224 | 1 | True | True | CORRECT | 1.205s |
| simpleqa-4227 | 1 | True | True | CORRECT | 1.294s |
| simpleqa-4266 | 1 | True | True | CORRECT | 1.075s |
| simpleqa-4273 | 1 | True | True | CORRECT | 0.87s |
| simpleqa-4288 | 1 | True | True | WRONG | 1.179s |
| simpleqa-4290 | 1 | True | True | CORRECT | 1.55s |

## Misses (audit trail)

- simpleqa-0131 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-0404 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-0454 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-0516 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-0572 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-0738 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-0761 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-0972 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-1510 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-1642 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-1944 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-2118 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-2995 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-3022 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-3159 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-3411 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-3772 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-4029 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)

Grading is deterministic (benchlib/graders.py): no LLM judge ran for this summary.
