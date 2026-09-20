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

## 2026-09-20: rate-limit truth from server code (correction)

Code-verified (server.py + ransack_db.py): per-minute /mcp sliding window is
120/min paid, 60/min trial, 300/min per-IP (in-memory per replica). Daily
quota per UTC day: trial 50/day, paid 500/day, Pro 10,000/day, Team
50,000/day; get_report and tasks_get are quota-exempt; "Daily quota exceeded"
= stop until UTC midnight.

The previously hypothesized "hourly cap (~400-600/hour)" is WITHDRAWN. The
sustained 44-minute 429 wall observed 2026-09-20 ~04:03 UTC does not match
either gate as coded (daily would persist until UTC midnight; the 60s window
recovers in 60s). Most plausible: a deploy/restart clearing in-memory limiter
state mid-wall, or a platform-level cap. Action: check Railway logs
04:03-04:47 UTC. Correction supersedes the earlier hourly-cap estimate.

---

Note: the research lane (execute_research) was removed from the suite and
marked for removal from the product on 2026-09-20; its failure analysis is
preserved in git history (FINDINGS.md revisions + the cross-tab commits).

## 2026-09-20: removal deployed and live-verified

execute_research removed from the MCP surface (ransack-server branch
remove-execute-research, merged to main, pushed 16:4x UTC). Live tools/list
verification at 17:00:28 UTC: execute_research absent, ransack search and all
other tools present. Product and benchmark now agree.
