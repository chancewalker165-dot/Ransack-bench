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

## 2026-09-20: EVAL A complete run (44 of 62 graded, 18 excluded)

Run: `results/fetch_eval_20260920-233546`. Sample, strata and question set are
unchanged from the pre-registered v1 manifest; the anchor pass, the S1 anchor
kind, the exclusion rule and the baseline cap are all recorded in BENCH_CHANGES
2.0.3. Grades are SUCCESS (anchor found) / HONEST_FAILURE (labeled, no content) /
SHELL (content returned, no fact, no label) / MISS (full-length content, no fact, no label).

| stratum | n | ransack S/HF/SHELL/MISS | baseline S/HF/SHELL/MISS |
|---|---|---|---|
| S1 plain static | 10 | 7/0/0/3 | 5/0/0/5 |
| S2 tls gated | 5 | 1/1/0/3 | 1/0/0/4 |
| S3 js rendered | 6 | 5/0/0/1 | 4/0/0/2 |
| S4 bot walled retailer | 6 | 1/2/0/3 | 2/0/1/3 |
| S5 dead or 404 | 10 | 0/9/0/1 | 0/0/2/8 |
| S6 paywalled | 6 | 1/1/0/4 | 2/0/0/4 |
| S7 archive only | 1 | 0/1/0/0 | 0/0/0/1 |
| **total** | **44** | **15/14/0/15** | **14/0/3/27** |

**What this measures.** Fact-success is a tie (15 vs 14). The ladder's measurable
advantage is honesty on failure: 14 labeled failures against 0 for the control,
and 0 dishonest shells against 3 (two of which are dead pages served as page
content). Dead-page labeling is the strongest single result: 9 of 10 dead URLs
were labeled with their true status versus 0 of 10 for the control.

**Honest limits of this run.** (1) Hard-strata n is 5 or 6 after exclusions, so
those rates carry wide intervals and none of them is a publishable percentage on
its own. (2) 18 of 62 entries are excluded for want of a ground-truth fact (JS
login SPAs, retailer homepages, paywalled homepages, one archive-only page); they
need the owner's browser pass. (3) 24 of the 34 anchors were captured with the same
plain-urllib client the control uses, so the control has home-field advantage on
those entries and any ladder edge is understated. (4) Anchors are containment
checks: MISS means "no anchor string in the returned text", which for a stealth-tier
win can also mean the sentence was reflowed, not that content is missing; every
transcript is in the run dir so the distinction can be checked.

Two product bugs found by the earlier Eval A run are fixed and live: hard fetches
now return a labeled failure inside the tool wall instead of a transport error
(commit f48785d), and fetch output carries the page title again, which the
clean-output scrub had been deleting for every default caller (commit 196d4ac,
live-verified 4/4 pages versus a same-day 0/4 baseline).

## 2026-09-20: EVAL A first run (fetch ladder, 62 URLs, preregistered)

Run: `results/fetch_eval_20260920-203417`. Pre-registered sample
(`datasets/fetch_eval_sample_v1.json`, seed 20260920) committed before any
call; 8 entries owner-verified by browser pass. Two grading defects were
caught and corrected offline from transcripts (no re-runs needed):
(1) the grader checked the explicit-failure status before the label, hiding
labels on statusless MCP calls; (2) S1 anchors were page titles, which
markdown conversion drops. Corrected results (ransack S/HF/SHELL/MISS/ERROR
vs plain-urllib baseline):

- S1 plain static: 3/2/0/5/0 vs baseline 10/0/0/0/0. The MISSes are an anchor
  artifact: transcripts show full content delivered (e.g. 20,923 chars of the
  w3.org page); the anchor was the title, which markdown drops.
- S5 dead/404: 10/10 HONEST_FAILURE. Every dead URL was labeled
  `[dead page: HTTP 404]` while the plain baseline returned soft-404 page
  content 8/10. The labeling-honesty claim IS verified for dead pages.
- S2 tls-gated: 2 of 10 calls hit the 45s client timeout (server ladder ran
  out of wall and the MCP call errored instead of returning a labeled
  failure). Product fix: return a labeled failure inside the budget.
- S3 js-rendered / S4 bot-walled / S6 paywalled / S7 archive: fact-success is
  UNMEASURED (anchors not yet provided; owner pass was partial). Labels fired
  rarely; MISS means "content returned, no anchor to check", not "failed".

Two product bugs this eval found in one run: (a) hard fetches time the whole
MCP call out at ~45s instead of returning a labeled failure; (b) fetch output
does not carry the page title, which makes title-based verification impossible
for agents. The make-or-break question (fact-success on hard strata) stays
open until anchors exist for the flagged entries.
