# Eval A: fetch ladder (ransack) vs plain fetch baseline

Grades: SUCCESS / HONEST_FAILURE / SHELL (content, no fact, no label) /
MISS (content, no fact, no label, full-length) / ERROR.

Entries whose fact anchor is not yet defined are EXCLUDED, not scored as
misses: an undefined fact is unmeasurable. They are listed at the end of
this summary and need the owner's browser pass (prereg option-4 gate).

| stratum | n | ransack S/HF/SHELL/MISS | baseline S/HF/SHELL/MISS |
|---|---|---|---|
| S1_plain_static | 10 | 7/0/0/3 | 5/0/0/5 |
| S2_tls_gated | 5 | 1/1/0/0 | 1/0/0/4 |
| S3_js_rendered | 6 | 5/0/0/1 | 4/0/0/2 |
| S4_bot_walled_retailer | 6 | 3/0/0/3 | 2/0/1/3 |
| S5_dead_or_404 | 10 | 0/9/0/1 | 0/0/2/8 |
| S6_paywalled | 6 | 2/0/0/4 | 1/0/0/5 |
| S7_archive_only | 1 | 0/1/0/0 | 0/0/0/1 |
