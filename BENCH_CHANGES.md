# BENCH_CHANGES

Every change to datasets, samples, or grading is recorded here. A frozen
sample that changes without an entry here is a broken benchmark.

## 2.0.3 - 2026-09-20 (Eval A anchor pass and two harness defects)

No sample URL, stratum, or question was changed. Three grading-side changes:

1. **Fact anchors filled for the hard strata.** `scripts/fill_fact_anchors.py`
   (new) implements the prereg's ground-truth protocol: plain urllib first, then
   the Wayback snapshot via the CDX API restricted to `statuscode:200` (so an
   archived challenge page cannot masquerade as the page under test). Anchors are
   captured independently of ransack. 34 of the 52 anchorable entries now have an
   anchor (24 captured live, 10 from Wayback); 18 remain `fact_anchor: null` for
   the owner's browser pass. The 10 S5 dead-or-404 entries need no anchor: they
   are scored on status and label honesty.
2. **S1 anchor KIND changed from page `<title>` to body prose.** Titles are not a
   gradeable ground truth: the same page exposes different title text in the
   `<title>` tag, `og:title`, and the product's own title extraction, so a title
   anchor fails on a page whose content arrived intact. Worked example: F-001's
   anchor was `curl - How To Use` while the delivered page carried
   `Title: curl man page`, and the transcript shows full content. Disclosed
   before/after on the same 44 graded entries: S1 ransack 3/10 and baseline 10/10
   with title anchors, S1 ransack 7/10 and baseline 5/10 with body anchors. The
   change makes S1 consistent with every other stratum and removes a known
   artifact; it is not a tuning pass, and both numbers are recorded here.
3. **Two harness defects fixed in `scripts/run_fetch_eval.py`.** (a) An entry with
   no anchor is now EXCLUDED rather than scored as a miss, because grading a fact
   that was never defined is the same defect class as the two grading bugs
   corrected on 2026-09-20; excluded ids are written to `excluded.json` and listed
   in the summary. S5 is exempt (no anchor needed). (b) The baseline lane's read
   cap was raised from 50,000 to 200,000 chars to match the ransack lane: F-001 and
   F-005 scored baseline MISS purely from truncation, so the cap was deciding
   verdicts instead of the ladder.

Run with these changes: `results/fetch_eval_20260920-233546` (44 graded, 18
excluded). Full table in FINDINGS.md.

## 2.0.0 - 2026-09-19

Full redesign (breaking). v1 was a 30-question self-graded trivia quiz with
containment grading, server-reported latency, and no baselines. v2:

- **Suite, not seed.** control_trivia (v1's 48 questions, carried over and
  honestly labeled a non-discriminative sanity floor), frames_sample_100
  (Apache-2.0, frozen seed 20260919), simpleqa_sample_200 (MIT, frozen seed
  20260919, official judge cross-check).
- **Two metrics, never conflated.** Retrieval hit-rate (search lanes) vs
  answer accuracy (answer-producing lanes). Abstains never count as correct.
- **Deterministic grading with span evidence** in bench/graders.py: matched
  alias, location, and normalized context recorded per verdict. No LLM judge
  for the primary metric; the SimpleQA official prompt (vendored verbatim,
  MIT) runs as an opt-in cross-check only.
- **Real runner.** bench.py: client-side latency, repeats, Wilson 95% CIs,
  per-run dirs with run_config.json + transcript.jsonl (raw responses) +
  results.jsonl + summary.json + summary.md, and cross-provider compare.
- **Baseline lane.** nosearch (no-search LLM) exposes non-discriminative
  seeds; if it scores ~100%, the dataset cannot rank providers.
- **Seed hygiene.** Manifest schema + validate command; rotcheck.py flags
  stale/unverified recency answers before runs (the v1 H5 lesson: that seed's
  expected answer was corrected after the run).
- **Frozen samples are sha-pinned** to fetched source files
  (scripts/fetch_datasets.py, scripts/make_sample.py); refetch drift breaks
  loudly instead of silently.
- **Load testing removed from scope.** v1's script measured a private
  token-gated endpoint bypassing customer rate caps; kept in legacy/ unused.
- v1 files preserved under legacy/ untouched.

Known issue surfaced during the rebuild: ransack.tools/mcp sits behind
Cloudflare (1010 to UA-less scripts) and requires a bearer token
(JSON-RPC -32001). Set RANSACK_MCP_TOKEN; server operators should document
the scripted-client path.

## 1.x - 2026-08/09 (legacy)

v1 seed, hand-run results, evidence excerpts, load tester. See legacy/ and
the git history before this file existed. v1's "96.7%" headline is retained
only as an example of why confidence intervals matter (n=30 single run:
Wilson 95% CI [83.3%, 99.4%]).
