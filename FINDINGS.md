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
