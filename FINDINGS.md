# FINDINGS

Dated, evidence-linked findings from bench runs. Every claim is reproducible
from the referenced run dirs (results/, raw transcripts inside).

## 2026-09-20: SimpleQA discriminates properly (n=200, judged)

Official-prompt judge live (z-ai/glm-5.3-flash via OpenRouter; see
METHODOLOGY.md for the judge-identity caveat):

- no-search control (deepseek-v4.1-flash, no web): 39% hit / 46% judged
  (run `20260920-054903_nosearch_simpleqa_suite`)
- search-answer lanes: perplexity 92.5% judged, exa-answer 90.5% judged,
  tavily 81.5% judged
- search adds +35-50pp over parametric memory on this set. This is the
  receipt that makes the table meaningful.

The judge also proved containment undercounts: tavily's answer accuracy moved
from 68% (containment) to 81.5% (judged) on identical responses. Paraphrased
answers are correct; only the judged column reflects that.

## 2026-09-20: the no-search control lands on frames (n=100)

Run: `20260920-052551_nosearch_frames_suite` (deepseek-v4.1-flash, no web).
Result: 47% hit-rate, ~48% answer accuracy - inside the band of search-answer
lanes (36-52%). Honest read: a strong 2026 model's parametric knowledge covers
nearly half of FRAMES-style questions without any search. Frames' value at
hit-rate level is weaker than its reputation for this model generation; the
meaningful separations are answer accuracy on hard chains and SimpleQA-style
adversarial facts. Design implication: datasets decay toward the parametric
ceiling as model memory grows; refresh them on a schedule.

## 2026-09-20: rate-limit empirics (operational note)

During a simpleqa n=200 run, the ransack key hit a sustained 429 wall after
~700 cumulative calls that day (172 consecutive rejections at 0.1s each):
- Not the documented 60/min window (calls were spaced 2-3s apart).
- Timeline: cap hit ~04:03, fully working again by ~04:47, pointing to an
  HOURLY cap on this key tier (roughly 400-600 calls/hour), not daily.
- The runner backs off 20s once per question on 429; a sustained wall needs
  a higher tier or a scheduled run.

Owner TODO (only you can answer): does internal sub-fetching count
individually against the quota? Exact hourly/daily numbers per tier? These
belong in the API docs before launch.

---

Note: the research lane (execute_research) was removed from the suite and
marked for removal from the product on 2026-09-20; its failure analysis is
preserved in git history (FINDINGS.md revisions + the cross-tab commits).
