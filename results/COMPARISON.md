# Ransack-bench comparison - 2026-09-20 (judged)

Frozen seeded samples (seed 20260919), client-side latency, Wilson 95% CIs,
raw transcripts per run dir. All simpleqa rows n=200; frames rows n=100.
judged = official SimpleQA grader prompt on the provider's own answer
(judge model: z-ai/glm-5.3-flash via OpenRouter; gpt-4o would be stronger -
treat judge numbers as a cross-check, not a gold standard).
Tavily's published 93.3% used their own gpt-4.1 pipeline on the full 4,326
set: not directly comparable to this 200-question frozen sample.


## frames

# provider comparison

| provider | dataset | n | hit-rate | 95% CI | p50 | p95 | errors | ans-acc | judged |
|---|---|---|---|---|---|---|---|---|---|
| exa-answer | frames | 100 | 52.0% | [42.3%, 61.5%] | 1.159s | 1.543s | 0 | 45/100 | - |
| perplexity | frames | 100 | 50.0% | [40.4%, 59.6%] | 1.901s | 3.911s | 0 | 40/100 | - |
| nosearch | frames | 100 | 47.0% | [37.5%, 56.7%] | 4.432s | 48.455s | 0 | 47/98 | - |
| tavily | frames | 100 | 38.0% | [29.1%, 47.8%] | 2.698s | 5.015s | 0 | 24/100 | - |
| ransack-research | frames | 100 | 36.0% | [27.3%, 45.8%] | 21.324s | 29.551s | 0 | 26/100 | - |
| serper | frames | 100 | 24.0% | [16.7%, 33.2%] | 1.348s | 4.075s | 0 | - | - |
| ransack | frames | 100 | 20.0% | [13.3%, 28.9%] | 2.783s | 5.654s | 0 | - | - |
| brave | frames | 100 | 20.0% | [13.3%, 28.9%] | 0.623s | 0.755s | 0 | - | - |
| exa | frames | 100 | 17.0% | [10.9%, 25.5%] | 1.396s | 4.017s | 0 | - | - |

Hit-rate = expected fact present in returned documents (retrieval). ans-acc = exact composed answer present in the provider's own answer field (containment; the official judge cross-check needs OPENAI_API_KEY and was not run). Answer accuracy only exists for answer-producing lanes.


## simpleqa

# provider comparison

| provider | dataset | n | hit-rate | 95% CI | p50 | p95 | errors | ans-acc | judged |
|---|---|---|---|---|---|---|---|---|---|
| perplexity | simpleqa | 200 | 92.5% | [88.0%, 95.4%] | 1.5s | 2.995s | 0 | 187/200 | 185/200 |
| exa-answer | simpleqa | 200 | 91.0% | [86.2%, 94.2%] | 1.064s | 1.566s | 0 | 183/200 | 181/200 |
| tavily | simpleqa | 200 | 83.0% | [77.2%, 87.6%] | 2.159s | 4.057s | 0 | 163/200 | 163/200 |
| ransack | simpleqa | 200 | 74.5% | [68.0%, 80.0%] | 2.454s | 5.534s | 0 | - | - |
| serper | simpleqa | 200 | 70.5% | [63.8%, 76.4%] | 1.041s | 4.377s | 0 | - | - |
| brave | simpleqa | 200 | 70.0% | [63.3%, 75.9%] | 0.461s | 0.676s | 0 | - | - |
| nosearch | simpleqa | 200 | 39.0% | [32.5%, 45.9%] | 5.404s | 34.072s | 0 | 91/197 | 91/197 |

Hit-rate = expected fact present in returned documents (retrieval). ans-acc = exact composed answer present in the provider's own answer field (containment; the official judge cross-check needs OPENAI_API_KEY and was not run). Answer accuracy only exists for answer-producing lanes.


## control_trivia

# provider comparison

| provider | dataset | n | hit-rate | 95% CI | p50 | p95 | errors | ans-acc | judged |
|---|---|---|---|---|---|---|---|---|---|
| ransack | control_trivia | 10 | 100.0% | [72.2%, 100.0%] | 0.513s | 0.847s | 0 | - | - |

Hit-rate = expected fact present in returned documents (retrieval). ans-acc = exact composed answer present in the provider's own answer field (containment; the official judge cross-check needs OPENAI_API_KEY and was not run). Answer accuracy only exists for answer-producing lanes.
