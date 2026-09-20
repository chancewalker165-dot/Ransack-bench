# FINDINGS

Dated, evidence-linked findings from bench runs. Every claim here is
reproducible from the referenced run dirs (results/, raw transcripts inside).

## 2026-09-20: exa-answer vs ransack-research on frames (n=100)

Sources: `20260920-030321_ransack-research_frames_suite`,
`20260920-034240_exa-answer_frames_suite`, `20260920-025450_ransack_frames_suite`
(ransack search lane), plus a token-level cross-tab of all three transcripts.

| metric | ransack-research | exa-answer |
|---|---|---|
| fact in own output (hit) | 36 | 52 |
| answer CORRECT | 26 | 45 |
| abstains | 2 | 0 |

Miss anatomy (the important part):

- All 64 research misses and all 48 exa misses have the expected fact ABSENT
  from the lane's own source text (0 near-misses). Neither lane loses on
  synthesis of what it retrieved; both lose on retrieval reach.
- On the 20 questions where the plain search lane DID find the fact:
  exa-answer converted 19/20 into a correct answer; ransack-research
  converted 11/20. When the fact is in front of the synthesizer, exa almost
  never drops it (95%) and ransack-research drops 45% of convertible cases.
- On the 80 questions the search lane missed: exa-answer still answered 26
  correctly (its internal retrieval reaches further), ransack-research 15.
- Head-to-head: exa wins 23 questions at the answer level; research wins 4.
- 42 questions are missed by BOTH lanes with the fact absent from both
  source sets; the search lane finds the fact for 0 of them. These are the
  hardest multi-hop chains.

### Backlog this implies (priority order)

1. **Synthesis conversion 55% -> 95% is the exa-class bar.** When a cited
   source contains the fact, the synthesized answer must not hedge or drop
   it. Worth ~9pp of answer accuracy on this sample alone.
2. **Retrieval reach for multi-hop.** exa-answer answers 26/80 questions
   whose facts ransack's own search lane cannot surface. The research lane
   needs deeper query reformulation / follow-up fetching rather than better
   summarization.
3. **Hedging audit.** The 2 abstains and the "not enough evidence" family
   partially overlap with problem 1: distinguish "source lacks the fact"
   (correct abstention) from "source has it but the synthesizer did not
   commit" (a bug by this finding's definition).

Caveat: "fact in source text" is normalized containment of the expected
answer, applied identically to both lanes. Phrasing variants could hide some
facts from the check for either lane equally; the lane-vs-lane comparison is
the point, not the absolute counts.

## 2026-09-20: rate-limit empirics (operational note)

During the simpleqa n=200 top-up, the ransack key hit a sustained 429 wall
after ~700 cumulative calls that day (172 consecutive rejections at 0.1s
each). Key facts observed:
- The wall was NOT the documented 60/min window (those calls were spaced
  2-3s apart); it persisted for minutes, then cleared.
- Timeline: cap hit ~04:03, same key fully working again by ~04:47. That
  points to an HOURLY cap on this key tier (roughly 400-600 calls/hour),
  not a daily one.
- The bench runner now backs off 20s once per question on 429; a longer
  sustained wall still needs either a higher tier or a scheduled run.

Owner TODO (only you can answer these): does execute_research's internal
sub-fetching count individually against the quota? What is the exact
hourly/daily number per tier? These belong in the API docs before launch.

## 2026-09-20: the no-search control lands (frames n=100)

Run: `20260920-052551_nosearch_frames_suite` (deepseek-v4.1-flash, no web).
Result: 47% hit-rate, answer accuracy in the same band as the search lanes.

Honest read: a strong 2026 model's parametric knowledge covers nearly half of
FRAMES-style questions without any search. Frames' discriminative power at
hit-rate level is therefore weaker than its reputation for this generation of
models; the meaningful separations are (a) answer accuracy on multi-hop
chains, (b) the 42-question hard tail both answer lanes miss, and (c)
SimpleQA-style adversarial facts. Bench design implication: datasets need
refreshing as model memory grows; static trivia (v1's error) and static
multi-hop both decay toward the no-search ceiling.

## 2026-09-20: judged results change the story (simpleqa n=200, frames n=100)

With the official SimpleQA grader prompt live (judge: z-ai/glm-5.3-flash via
OpenRouter):

- SimpleQA is properly discriminative: no-search control 39% hit / 46% judged
  vs search-answer lanes 70.5-92.5% hit / 81.5-92.5% judged. Search adds
  +25-50pp over parametric memory on this set. (Comparability caveat: Tavily's
  published 93.3% used gpt-4.1 extraction on the full 4,326 set.)
- The judge raises tavily's answer accuracy from 68% (containment) to 81.5%
  (163/200): containment undercounts paraphrased answers. For answer lanes,
  the judged column is the fair one.
- Frames, answer-accuracy: nosearch 47/98 (~48%) vs ransack-research 26/100.
  The research lane currently scores BELOW the no-search control on exact
  multi-hop answers. Combined with the conversion cross-tab above (11/20 vs
  exa's 19/20 on search-lane hits), the synthesis layer is the existential
  product priority, not a nice-to-have. The lane's differentiators that do
  hold up: citations, confidence telemetry, honest abstentions (2), and the
  latency price is paid for 0 errors at n=100.
