# Ransack-bench comparison - 2026-09-20

All runs n=100 questions from frozen seeded samples (seed 20260919), commit-pinned,
client-side latency, Wilson 95% CIs, raw transcripts in each run dir.
Known caveats: (1) perplexity hit rate limiting (50 calls errored, its row understates);
(2) the no-search baseline lane needs OPENAI_API_KEY and did not run;
(3) the SimpleQA official judge cross-check needs OPENAI_API_KEY and did not run;
answer grades for answer lanes are containment-based until then.


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
| tavily | simpleqa | 100 | 77.0% | [67.8%, 84.2%] | 2.322s | 4.043s | 0 | 57/100 |
| brave | simpleqa | 100 | 68.0% | [58.3%, 76.3%] | 0.587s | 0.686s | 0 | - |
| ransack | simpleqa | 100 | 66.0% | [56.3%, 74.5%] | 2.263s | 5.249s | 0 | - |
| serper | simpleqa | 100 | 66.0% | [56.3%, 74.5%] | 1.027s | 3.05s | 0 | - |

Hit-rate = expected fact present in returned documents (retrieval). ans-acc = exact composed answer present in the provider's own answer field (containment; the official judge cross-check needs OPENAI_API_KEY and was not run). Answer accuracy only exists for answer-producing lanes.


## control_trivia

# provider comparison

| provider | dataset | n | hit-rate | 95% CI | p50 | p95 | errors | ans-acc |
|---|---|---|---|---|---|---|---|---|
| ransack | control_trivia | 10 | 100.0% | [72.2%, 100.0%] | 0.513s | 0.847s | 0 | - |

Hit-rate = expected fact present in returned documents (retrieval). ans-acc = exact composed answer present in the provider's own answer field (containment; the official judge cross-check needs OPENAI_API_KEY and was not run). Answer accuracy only exists for answer-producing lanes.
