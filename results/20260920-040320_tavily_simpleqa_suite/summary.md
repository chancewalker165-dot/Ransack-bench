# bench run: tavily on simpleqa

- run: 20260920-040320 (git aea6ecd), sample `simpleqa_n200_seed20260919` frozen 2026-09-19
- calls: 200 (200 questions x 1 repeat(s)), errors: 0
- retrieval hit-rate: **82.0%** (95% CI [76.1%, 86.7%], Wilson)
- answer accuracy (answer-producing provider): **68.0%** (136/200 CORRECT), abstains: 0 (never counted as correct)
- judge was configured but did not run (no OPENAI_API_KEY): answer grades fall back to containment; judge cross-check skipped, and this is recorded
- latency (client-side): mean 2.332s, p50 2.114s, p95 3.992s, max 5.241s

## Per-question

| id | calls | hit_all | hit_any | verdicts | mean latency |
|---|---|---|---|---|---|
| simpleqa-0031 | 1 | True | True | CORRECT | 3.748s |
| simpleqa-0034 | 1 | True | True | CORRECT | 1.863s |
| simpleqa-0039 | 1 | True | True | CORRECT | 1.835s |
| simpleqa-0072 | 1 | True | True | WRONG | 1.827s |
| simpleqa-0095 | 1 | True | True | WRONG | 2.824s |
| simpleqa-0110 | 1 | False | False | WRONG | 2.304s |
| simpleqa-0117 | 1 | True | True | CORRECT | 2.348s |
| simpleqa-0131 | 1 | False | False | WRONG | 1.868s |
| simpleqa-0142 | 1 | True | True | CORRECT | 2.9s |
| simpleqa-0184 | 1 | True | True | WRONG | 1.897s |
| simpleqa-0189 | 1 | True | True | CORRECT | 2.983s |
| simpleqa-0192 | 1 | True | True | CORRECT | 1.872s |
| simpleqa-0204 | 1 | False | False | WRONG | 1.535s |
| simpleqa-0230 | 1 | False | False | WRONG | 4.329s |
| simpleqa-0260 | 1 | True | True | CORRECT | 3.053s |
| simpleqa-0272 | 1 | True | True | CORRECT | 3.877s |
| simpleqa-0297 | 1 | True | True | CORRECT | 3.336s |
| simpleqa-0298 | 1 | True | True | CORRECT | 1.836s |
| simpleqa-0340 | 1 | False | False | WRONG | 1.454s |
| simpleqa-0368 | 1 | True | True | CORRECT | 1.834s |
| simpleqa-0376 | 1 | True | True | WRONG | 3.015s |
| simpleqa-0379 | 1 | True | True | WRONG | 2.828s |
| simpleqa-0404 | 1 | False | False | WRONG | 3.673s |
| simpleqa-0409 | 1 | True | True | CORRECT | 3.98s |
| simpleqa-0454 | 1 | False | False | WRONG | 1.35s |
| simpleqa-0512 | 1 | True | True | CORRECT | 2.489s |
| simpleqa-0516 | 1 | False | False | WRONG | 5.035s |
| simpleqa-0522 | 1 | True | True | CORRECT | 1.549s |
| simpleqa-0553 | 1 | False | False | WRONG | 2.256s |
| simpleqa-0556 | 1 | True | True | WRONG | 2.28s |
| simpleqa-0572 | 1 | True | True | CORRECT | 1.648s |
| simpleqa-0626 | 1 | True | True | CORRECT | 1.383s |
| simpleqa-0651 | 1 | True | True | CORRECT | 3.093s |
| simpleqa-0653 | 1 | True | True | CORRECT | 2.651s |
| simpleqa-0655 | 1 | False | False | WRONG | 1.849s |
| simpleqa-0662 | 1 | True | True | CORRECT | 1.574s |
| simpleqa-0663 | 1 | True | True | CORRECT | 4.266s |
| simpleqa-0667 | 1 | True | True | WRONG | 2.247s |
| simpleqa-0669 | 1 | True | True | WRONG | 1.852s |
| simpleqa-0671 | 1 | True | True | CORRECT | 2.64s |
| simpleqa-0677 | 1 | True | True | CORRECT | 1.773s |
| simpleqa-0682 | 1 | True | True | CORRECT | 1.976s |
| simpleqa-0722 | 1 | True | True | WRONG | 2.191s |
| simpleqa-0738 | 1 | True | True | WRONG | 1.657s |
| simpleqa-0750 | 1 | True | True | CORRECT | 2.147s |
| simpleqa-0761 | 1 | True | True | WRONG | 1.942s |
| simpleqa-0781 | 1 | True | True | CORRECT | 1.92s |
| simpleqa-0783 | 1 | True | True | CORRECT | 1.701s |
| simpleqa-0805 | 1 | True | True | WRONG | 2.006s |
| simpleqa-0812 | 1 | True | True | WRONG | 2.528s |
| simpleqa-0824 | 1 | True | True | CORRECT | 2.15s |
| simpleqa-0825 | 1 | True | True | CORRECT | 1.69s |
| simpleqa-0831 | 1 | False | False | WRONG | 1.822s |
| simpleqa-0833 | 1 | True | True | CORRECT | 3.96s |
| simpleqa-0873 | 1 | True | True | WRONG | 2.639s |
| simpleqa-0894 | 1 | True | True | CORRECT | 2.354s |
| simpleqa-0896 | 1 | False | False | WRONG | 2.598s |
| simpleqa-0972 | 1 | False | False | WRONG | 2.071s |
| simpleqa-0979 | 1 | True | True | CORRECT | 1.537s |
| simpleqa-1017 | 1 | True | True | CORRECT | 2.023s |
| simpleqa-1020 | 1 | True | True | CORRECT | 2.27s |
| simpleqa-1025 | 1 | True | True | WRONG | 1.683s |
| simpleqa-1028 | 1 | True | True | CORRECT | 1.584s |
| simpleqa-1135 | 1 | True | True | CORRECT | 2.114s |
| simpleqa-1142 | 1 | False | False | WRONG | 2.929s |
| simpleqa-1263 | 1 | True | True | CORRECT | 2.144s |
| simpleqa-1270 | 1 | True | True | WRONG | 2.126s |
| simpleqa-1271 | 1 | True | True | CORRECT | 2.377s |
| simpleqa-1302 | 1 | True | True | WRONG | 4.655s |
| simpleqa-1317 | 1 | True | True | WRONG | 2.306s |
| simpleqa-1359 | 1 | True | True | CORRECT | 2.658s |
| simpleqa-1415 | 1 | True | True | CORRECT | 2.133s |
| simpleqa-1437 | 1 | True | True | CORRECT | 4.094s |
| simpleqa-1438 | 1 | True | True | CORRECT | 2.208s |
| simpleqa-1480 | 1 | True | True | CORRECT | 1.884s |
| simpleqa-1490 | 1 | True | True | CORRECT | 1.579s |
| simpleqa-1501 | 1 | True | True | CORRECT | 2.773s |
| simpleqa-1504 | 1 | True | True | CORRECT | 2.366s |
| simpleqa-1510 | 1 | False | False | WRONG | 3.932s |
| simpleqa-1514 | 1 | False | False | WRONG | 3.1s |
| simpleqa-1518 | 1 | True | True | CORRECT | 2.437s |
| simpleqa-1525 | 1 | True | True | CORRECT | 3.032s |
| simpleqa-1540 | 1 | False | False | WRONG | 1.973s |
| simpleqa-1548 | 1 | True | True | CORRECT | 2.51s |
| simpleqa-1579 | 1 | True | True | CORRECT | 1.967s |
| simpleqa-1583 | 1 | True | True | WRONG | 3.57s |
| simpleqa-1615 | 1 | True | True | CORRECT | 4.511s |
| simpleqa-1627 | 1 | True | True | CORRECT | 2.15s |
| simpleqa-1636 | 1 | True | True | CORRECT | 2.329s |
| simpleqa-1642 | 1 | False | False | WRONG | 2.327s |
| simpleqa-1644 | 1 | True | True | CORRECT | 2.541s |
| simpleqa-1708 | 1 | True | True | CORRECT | 2.293s |
| simpleqa-1787 | 1 | True | True | CORRECT | 1.835s |
| simpleqa-1795 | 1 | True | True | WRONG | 3.805s |
| simpleqa-1808 | 1 | True | True | CORRECT | 1.847s |
| simpleqa-1839 | 1 | True | True | CORRECT | 1.809s |
| simpleqa-1851 | 1 | False | False | WRONG | 2.397s |
| simpleqa-1867 | 1 | True | True | CORRECT | 3.204s |
| simpleqa-1884 | 1 | True | True | CORRECT | 2.451s |
| simpleqa-1892 | 1 | True | True | CORRECT | 2.474s |
| simpleqa-1927 | 1 | True | True | CORRECT | 1.939s |
| simpleqa-1928 | 1 | True | True | CORRECT | 1.858s |
| simpleqa-1930 | 1 | False | False | WRONG | 1.9s |
| simpleqa-1944 | 1 | False | False | WRONG | 2.162s |
| simpleqa-1951 | 1 | False | False | WRONG | 1.745s |
| simpleqa-2042 | 1 | True | True | WRONG | 1.611s |
| simpleqa-2081 | 1 | True | True | CORRECT | 1.608s |
| simpleqa-2118 | 1 | False | False | WRONG | 2.011s |
| simpleqa-2130 | 1 | True | True | CORRECT | 3.916s |
| simpleqa-2134 | 1 | True | True | CORRECT | 2.221s |
| simpleqa-2148 | 1 | True | True | CORRECT | 2.779s |
| simpleqa-2163 | 1 | True | True | WRONG | 1.629s |
| simpleqa-2191 | 1 | True | True | CORRECT | 1.736s |
| simpleqa-2204 | 1 | True | True | WRONG | 1.77s |
| simpleqa-2295 | 1 | False | False | WRONG | 2.335s |
| simpleqa-2351 | 1 | True | True | CORRECT | 1.729s |
| simpleqa-2411 | 1 | True | True | CORRECT | 1.642s |
| simpleqa-2441 | 1 | True | True | CORRECT | 1.774s |
| simpleqa-2451 | 1 | False | False | WRONG | 2.606s |
| simpleqa-2453 | 1 | True | True | CORRECT | 1.825s |
| simpleqa-2462 | 1 | True | True | CORRECT | 1.84s |
| simpleqa-2517 | 1 | True | True | CORRECT | 2.503s |
| simpleqa-2521 | 1 | True | True | WRONG | 1.649s |
| simpleqa-2539 | 1 | True | True | CORRECT | 1.508s |
| simpleqa-2553 | 1 | True | True | CORRECT | 2.398s |
| simpleqa-2564 | 1 | False | False | WRONG | 2.449s |
| simpleqa-2588 | 1 | True | True | CORRECT | 1.717s |
| simpleqa-2605 | 1 | True | True | CORRECT | 2.689s |
| simpleqa-2651 | 1 | True | True | CORRECT | 1.774s |
| simpleqa-2662 | 1 | True | True | WRONG | 1.464s |
| simpleqa-2663 | 1 | True | True | CORRECT | 1.754s |
| simpleqa-2681 | 1 | True | True | CORRECT | 1.668s |
| simpleqa-2728 | 1 | True | True | CORRECT | 1.596s |
| simpleqa-2773 | 1 | False | False | WRONG | 2.024s |
| simpleqa-2781 | 1 | True | True | CORRECT | 1.591s |
| simpleqa-2786 | 1 | True | True | CORRECT | 1.559s |
| simpleqa-2804 | 1 | True | True | CORRECT | 2.609s |
| simpleqa-2844 | 1 | True | True | CORRECT | 4.286s |
| simpleqa-2849 | 1 | False | False | WRONG | 5.241s |
| simpleqa-2859 | 1 | True | True | CORRECT | 2.096s |
| simpleqa-2875 | 1 | True | True | CORRECT | 2.987s |
| simpleqa-2889 | 1 | True | True | CORRECT | 1.996s |
| simpleqa-2914 | 1 | True | True | CORRECT | 1.769s |
| simpleqa-2923 | 1 | True | True | CORRECT | 2.046s |
| simpleqa-2943 | 1 | True | True | WRONG | 3.296s |
| simpleqa-2954 | 1 | True | True | CORRECT | 1.902s |
| simpleqa-2994 | 1 | True | True | CORRECT | 1.613s |
| simpleqa-2995 | 1 | True | True | CORRECT | 1.998s |
| simpleqa-3010 | 1 | True | True | CORRECT | 2.346s |
| simpleqa-3022 | 1 | True | True | CORRECT | 4.068s |
| simpleqa-3092 | 1 | True | True | CORRECT | 3.078s |
| simpleqa-3103 | 1 | True | True | CORRECT | 2.605s |
| simpleqa-3107 | 1 | True | True | CORRECT | 2.708s |
| simpleqa-3127 | 1 | True | True | CORRECT | 1.808s |
| simpleqa-3140 | 1 | True | True | CORRECT | 1.507s |
| simpleqa-3159 | 1 | False | False | WRONG | 2.018s |
| simpleqa-3186 | 1 | True | True | CORRECT | 2.072s |
| simpleqa-3200 | 1 | True | True | CORRECT | 1.974s |
| simpleqa-3220 | 1 | True | True | CORRECT | 1.948s |
| simpleqa-3237 | 1 | True | True | CORRECT | 1.594s |
| simpleqa-3271 | 1 | True | True | CORRECT | 2.616s |
| simpleqa-3282 | 1 | True | True | CORRECT | 2.343s |
| simpleqa-3295 | 1 | True | True | CORRECT | 2.219s |
| simpleqa-3343 | 1 | True | True | CORRECT | 1.558s |
| simpleqa-3379 | 1 | True | True | CORRECT | 1.753s |
| simpleqa-3389 | 1 | True | True | CORRECT | 2.924s |
| simpleqa-3411 | 1 | False | False | WRONG | 2.529s |
| simpleqa-3463 | 1 | True | True | CORRECT | 1.595s |
| simpleqa-3474 | 1 | True | True | WRONG | 2.7s |
| simpleqa-3479 | 1 | True | True | CORRECT | 1.832s |
| simpleqa-3506 | 1 | False | False | WRONG | 2.208s |
| simpleqa-3593 | 1 | True | True | CORRECT | 1.504s |
| simpleqa-3620 | 1 | True | True | CORRECT | 3.058s |
| simpleqa-3630 | 1 | True | True | CORRECT | 1.81s |
| simpleqa-3642 | 1 | True | True | CORRECT | 2.639s |
| simpleqa-3644 | 1 | True | True | CORRECT | 1.663s |
| simpleqa-3697 | 1 | True | True | CORRECT | 1.639s |
| simpleqa-3728 | 1 | True | True | CORRECT | 3.992s |
| simpleqa-3772 | 1 | False | False | WRONG | 4.742s |
| simpleqa-3793 | 1 | True | True | CORRECT | 1.853s |
| simpleqa-3862 | 1 | True | True | CORRECT | 1.908s |
| simpleqa-3896 | 1 | True | True | CORRECT | 3.968s |
| simpleqa-3922 | 1 | True | True | CORRECT | 2.938s |
| simpleqa-3934 | 1 | True | True | CORRECT | 1.726s |
| simpleqa-3977 | 1 | True | True | CORRECT | 2.636s |
| simpleqa-3988 | 1 | True | True | CORRECT | 2.47s |
| simpleqa-4009 | 1 | False | False | WRONG | 1.683s |
| simpleqa-4029 | 1 | False | False | WRONG | 1.536s |
| simpleqa-4045 | 1 | True | True | CORRECT | 1.722s |
| simpleqa-4051 | 1 | True | True | CORRECT | 1.401s |
| simpleqa-4086 | 1 | True | True | CORRECT | 1.626s |
| simpleqa-4095 | 1 | True | True | CORRECT | 1.617s |
| simpleqa-4170 | 1 | True | True | CORRECT | 1.617s |
| simpleqa-4174 | 1 | True | True | CORRECT | 1.902s |
| simpleqa-4224 | 1 | True | True | CORRECT | 2.46s |
| simpleqa-4227 | 1 | True | True | CORRECT | 2.893s |
| simpleqa-4266 | 1 | True | True | CORRECT | 2.48s |
| simpleqa-4273 | 1 | True | True | WRONG | 2.271s |
| simpleqa-4288 | 1 | False | False | WRONG | 1.55s |
| simpleqa-4290 | 1 | False | False | WRONG | 2.107s |

## Misses (audit trail)

- simpleqa-0110 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-0131 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-0204 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-0230 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-0340 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-0404 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-0454 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-0516 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-0553 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-0655 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-0831 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-0896 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-0972 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-1142 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-1510 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-1514 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-1540 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-1642 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-1851 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-1930 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-1944 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-1951 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-2118 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-2295 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-2451 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-2564 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-2773 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-2849 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-3159 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-3411 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-3506 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-3772 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-4009 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-4029 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-4288 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)
- simpleqa-4290 rep1: no candidate matched (see results.jsonl + transcript.jsonl for spans)

Grading is deterministic (benchlib/graders.py): no LLM judge ran for this summary.
