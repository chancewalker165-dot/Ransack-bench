# Ransack-bench comparison - 2026-09-20

Frozen seeded samples (seed 20260919), client-side latency, Wilson 95% CIs,
raw transcripts per run dir. simpleqa rows at n=200 where marked.
Caveats: (1) perplexity frames row rate-limited (50 err/100);
(2) no-search baseline + SimpleQA judge need OPENAI_API_KEY, not yet run;
(3) ransack simpleqa row is n=100: the n=200 attempt hit the key's usage cap
(172 x 429) - the runner now backs off once per question on 429.


## frames

# provider comparison

| provider | dataset | n | hit-rate | 95% CI | p50 | p95 | errors | ans-acc |
|---|---|---|---|---|---|---|---|---|
| exa-answer | frames | 100 | 52.0% | [42.3%, 61.5%] | 1.159s | 1.543s | 0 | 45/100 |
| tavily | frames | 100 | 38.0% | [29.1%, 47.8%] | 2.698s | 5.015s | 0 | 24/100 |
| perplexity | frames | 100 | 38.0% | [25.9%, 51.8%] | 1.838s | 4.316s | 50 | 13/50 |
| ransack-research | frames | 100 | 36.0% | [27.3%, 45.8%] | 21.324s | 29.551s | 0 | 26/100 |
| serper | frames | 100 | 24.0% | [16.7%, 33.2%] | 1.348s | 4.075s | 0 | - |
| ransack | frames | 100 | 20.0% | [13.3%, 28.9%] | 2.783s | 5.654s | 0 | - |
| brave | frames | 100 | 20.0% | [13.3%, 28.9%] | 0.623s | 0.755s | 0 | - |
| exa | frames | 100 | 17.0% | [10.9%, 25.5%] | 1.396s | 4.017s | 0 | - |

Hit-rate = expected fact present in returned documents (retrieval). ans-acc = exact composed answer present in the provider's own answer field (containment; the official judge cross-check needs OPENAI_API_KEY and was not run). Answer accuracy only exists for answer-producing lanes.


## simpleqa

# provider comparison

| provider | dataset | n | hit-rate | 95% CI | p50 | p95 | errors | ans-acc |
|---|---|---|---|---|---|---|---|---|
| tavily | simpleqa | 200 | 82.0% | [76.1%, 86.7%] | 2.114s | 3.992s | 0 | 136/200 |
| serper | simpleqa | 200 | 70.5% | [63.8%, 76.4%] | 1.041s | 4.377s | 0 | - |
| brave | simpleqa | 200 | 70.0% | [63.3%, 75.9%] | 0.461s | 0.676s | 0 | - |
| ransack | simpleqa | 100 | 66.0% | [56.3%, 74.5%] | 2.263s | 5.249s | 0 | - |

Hit-rate = expected fact present in returned documents (retrieval). ans-acc = exact composed answer present in the provider's own answer field (containment; the official judge cross-check needs OPENAI_API_KEY and was not run). Answer accuracy only exists for answer-producing lanes.


## control_trivia

# provider comparison

| provider | dataset | n | hit-rate | 95% CI | p50 | p95 | errors | ans-acc |
|---|---|---|---|---|---|---|---|---|
| ransack | control_trivia | 10 | 100.0% | [72.2%, 100.0%] | 0.513s | 0.847s | 0 | - |

Hit-rate = expected fact present in returned documents (retrieval). ans-acc = exact composed answer present in the provider's own answer field (containment; the official judge cross-check needs OPENAI_API_KEY and was not run). Answer accuracy only exists for answer-producing lanes.
