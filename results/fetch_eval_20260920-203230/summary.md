# Eval A: fetch ladder (ransack) vs plain fetch baseline

Grades: SUCCESS / HONEST_FAILURE / SHELL (content, no fact, no label) /
MISS (content, no fact, no label, full-length) / ERROR.

| stratum | n | ransack S/HF/SHELL/MISS | baseline S/HF/SHELL/MISS |
|---|---|---|---|
| S1_plain_static | 10 | 0/0/0/0 | 10/0/0/0 |
| S2_tls_gated | 10 | 0/0/0/0 | 0/0/0/10 |
| S3_js_rendered | 10 | 0/0/0/0 | 0/0/1/9 |
| S4_bot_walled_retailer | 10 | 0/0/0/0 | 0/0/1/9 |
| S5_dead_or_404 | 10 | 0/0/0/0 | 1/0/9/0 |
| S6_paywalled | 10 | 0/0/0/0 | 0/0/0/10 |
| S7_archive_only | 2 | 0/0/0/0 | 0/0/0/2 |
