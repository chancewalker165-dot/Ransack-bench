# BENCH_CHANGES

Every change to datasets, samples, or grading is recorded here. A frozen
sample that changes without an entry here is a broken benchmark.

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
