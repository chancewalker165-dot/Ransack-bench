# METHODOLOGY

Version 2.0.0, written 2026-09-19. This page exists so a stranger can
reproduce every number this repo publishes without trusting the authors.

## What we measure

Two metrics, never conflated:

1. **Retrieval hit-rate** (all providers): the expected fact, or a listed
   alias, appears (normalized containment) in the provider's returned
   documents or answer text. For search APIs this is the product. Recorded
   with a matched alias, where it matched, and a normalized context snippet,
   so any verdict can be re-checked from `transcript.jsonl`.
2. **Answer accuracy** (only providers that return a synthesized answer):
   the answer field graded CORRECT / WRONG / ABSTAIN. Abstentions ("I don't
   know", "cannot determine") are never counted as correct and are reported
   separately. v1's containment rule scored fence-sitting as correct; that
   hole is closed by construction.

Deterministic grading lives in `bench/graders.py` (no LLM). For SimpleQA the
official grader prompt from openai/simple-evals (MIT) is vendored verbatim in
`bench/grader_prompts/` and runs as a published cross-check when
`OPENAI_API_KEY` is present; runs without the key are labeled as fallback and
skipped-judge is recorded rather than hidden.

## Sampling and freezing

- Full source datasets are fetched into `data/` by `scripts/fetch_datasets.py`
  (gitignored). The fetched file's sha256 is recorded.
- Samples are frozen by `scripts/make_sample.py`: sort question ids, select
  with `random.Random(seed).sample`, commit the chosen ids + questions + the
  source sha256 + the seed. Same seed + same sha = same sample forever.
- Changing a sample requires a new `sample_id` and a `BENCH_CHANGES.md` entry.
  Never edit a frozen manifest in place; that was the v1 failure mode (v2
  tracks and H5's expected answer were edited after the results existed).

## Datasets in v2.0.0

| Dataset | Source | License | Size | Grader |
|---|---|---|---|---|
| control_trivia | this repo (v1 seed carried over) | MIT | 48 | alias_exact |
| frames | [google/frames-benchmark](https://huggingface.co/datasets/google/frames-benchmark), split `test`, 824 rows via datasets-server [tool: fetched 2026-09-19] | Apache-2.0 (dataset card metadata, [tool: HF api 2026-09-19]) | 100 of 824 | alias_exact |
| simpleqa | [simple_qa_test_set.csv](https://openaipublic.blob.core.windows.net/simple-evals/simple_qa_test_set.csv), the exact URL simple-evals' own code downloads [tool: fetched 2026-09-19] | MIT (openai/simple-evals) | 200 of 4,326 | alias_exact + official judge cross-check |

The v1 seed ships as `control_trivia` with honest labeling: it is a sanity
floor. A no-search LLM (the `nosearch` provider) answers most of it without
any web access; if that control scores high on any dataset, that dataset is
not allowed to rank providers. That is the exact failure v1 hid.

## Measurement rules

- Latency is client-side (`time.perf_counter` around the provider call).
  Server-reported footers are stored as `server_latency_s` and never quoted
  as the headline. v1 quoted server self-reporting; that stops here.
  Cache caveat, observed live 2026-09-20: identical repeated queries can be
  served cache-warm (server footer showed 0.0s on a re-run). For
  latency-sensitive comparisons, vary phrasing or run each query once.
- Repeats: `--repeat N` asks each question N times; summary reports per-call
  hit-rate plus per-question all-hit / any-hit.
- Statistics: Wilson 95% intervals on every rate. n=30 single-run headlines
  like v1's "96.7%" are not publishable without one (v1's real interval was
  [83.3%, 99.4%]).
- Errors are recorded per call and reported; a run never aborts on a provider
  error.
- Load testing is out of scope for this repo: v1's script measured a private
  token-gated endpoint that bypasses customer-facing rate caps. It is
  preserved in `legacy/` for archaeology only.

## Run lifecycle

1. `python3 bench.py validate` (CI runs this on every push)
2. `python3 rotcheck.py --strict` for datasets with recency questions
3. `python3 bench.py run --dataset ... --provider ... --repeat 3`
4. `summary.md` + raw transcripts land in a dated run dir; publish the dir
   as-is, misses included
5. `python3 bench.py compare results/<dirA> results/<dirB>` for cross-provider
   tables; publish losses with wins

## Roadmap (in order, per the 2026-09 review)

- FreshQA fast-changing slice (freshness, with rotcheck enforcement)
- BrowseComp fixed 50-Q sample (monthly; expensive lane)
- CRAG robustness slice (missing/misleading documents)
- DeepResearch Bench English subset for the `ransack-research` lane
- xbench / GAIA leaderboard submissions (channel, not harness)
- Judge cross-checks extended beyond SimpleQA with published prompts

## Source register

| # | Source | Verified | Fetched |
|---|--------|----------|---------|
| 1 | https://huggingface.co/datasets/google/frames-benchmark | VERIFIED (verify-quote, 2026-09-19, sha a9b20beac7b3) - 824 multi-hop questions | 2026-09-19 |
| 2 | https://arxiv.org/html/2411.04368v1 | VERIFIED (verify-quote, 2026-09-19, sha 09643f01731b) - SimpleQA 4,326 questions | 2026-09-19 |
| 3 | https://github.com/openai/simple-evals | VERIFIED (verify-quote, 2026-09-19, sha dda6e5f49978) - MIT license | 2026-09-19 |

Facts pulled during this build by direct tool calls, tagged [tool:] above:
FRAMES license + split (HF api + datasets-server), SimpleQA CSV URL and shape
(simpleqa_eval.py source + CSV download), v1 seed contents (in-repo).
