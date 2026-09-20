# Ransack-bench v2

A combined, re-runnable evaluation suite for web search APIs. It adopts the
public benchmarks the category already trusts (SimpleQA, FRAMES), adds a
no-search LLM control, grades deterministically with auditable spans, and
reports honest metrics: retrieval hit-rate for search lanes, answer accuracy
for answer-producing lanes, with Wilson confidence intervals on everything.

v1 graded its own product on 30 trivia questions and called the score a
benchmark. v2 exists so nobody has to trust anyone's grader: every sample is
frozen and reproducible, every run ships raw transcripts, and every provider
(competitors included) runs through the same harness. See
[BENCH_CHANGES.md](BENCH_CHANGES.md) and [METHODOLOGY.md](METHODOLOGY.md).

## Quickstart (60 seconds)

```bash
python3 bench.py list                    # datasets + providers
python3 bench.py validate                # schema-check every manifest
python3 bench.py run --dataset control_trivia --provider mock --limit 3   # offline smoke
```

Live runs need one env var per provider (see table below):

```bash
RANSACK_MCP_TOKEN=... python3 bench.py run --dataset frames --provider ransack --repeat 3
TAVILY_API_KEY=...  python3 bench.py run --dataset frames --provider tavily  --repeat 3
python3 bench.py compare results/<tavily-run-dir> results/<ransack-run-dir>
```

## Datasets

| Manifest | Questions | Grader | License | Role |
|---|---|---|---|---|
| `datasets/control_trivia.json` | 48 (all of v1's seed) | alias_exact | MIT (this repo) | sanity floor, labeled non-discriminative |
| `datasets/frames_sample_100.json` | 100 of 824, seed 20260919, source sha `b9a11b5df50b...` | alias_exact | Apache-2.0 (google/frames-benchmark) | multi-hop benchmark |
| `datasets/simpleqa_sample_200.json` | 200 of 4,326, seed 20260919, source sha `d1f858a88645...` | alias_exact + optional official judge | MIT (openai/simple-evals) | adversarial short-fact benchmark |

Sampling is deterministic: sorted ids + `random.Random(seed).sample`, committed
with the source file's sha256. Re-generate with `scripts/make_sample.py`;
full sources are fetched by `scripts/fetch_datasets.py` into `data/`
(gitignored, never redistributed unless the license says so).

## Providers

| Provider | Env | Metric it supports |
|---|---|---|
| `mock` | none (offline fixture) | pipeline smoke only |
| `ransack` (search lane, MCP surface) | `RANSACK_MCP_URL` (default https://ransack.tools), `RANSACK_MCP_TOKEN` | hit-rate |
| `ransack-research` (agentic lane) | same | hit-rate + answer accuracy |
| `nosearch` (no-search LLM control) | `OPENAI_API_KEY`, `NOSEARCH_MODEL`, `OPENAI_BASE_URL` | answer accuracy (the baseline that exposes weak seeds) |
| `tavily` | `TAVILY_API_KEY` | hit-rate (+ `answer` when returned) |
| `brave` | `BRAVE_API_KEY` | hit-rate |
| `serper` | `SERPER_API_KEY` | hit-rate |
| `exa` | `EXA_API_KEY` | hit-rate |
| `exa-answer` (the /answer lane) | `EXA_API_KEY` | hit-rate + answer accuracy |
| `perplexity` | `PERPLEXITY_API_KEY` | hit-rate + answer accuracy |

## Metrics, defined once

- **Retrieval hit-rate**: expected fact (or alias) present in the returned
  documents. This is what a search API sells; it is NOT answer accuracy.
- **Answer accuracy** (answer-producing providers only): the answer field
  graded CORRECT / WRONG / ABSTAIN. For SimpleQA the official grader prompt
  (vendored verbatim, MIT) runs as a cross-check when `OPENAI_API_KEY` is set.
- **Abstains are never correct**: "I don't know" is counted separately, the
  failure mode v1's containment grading hid.
- **CIs everywhere**: Wilson 95% on hit-rate and accuracy; repeats via `--repeat`.

Latency is measured client-side by the runner. Server-reported footers are
kept as `server_latency_s` for diagnostics only, never as the headline.

## Run dirs

Every run writes `results/<UTC ts>_<provider>_<dataset>[_<tag>]/`:
`run_config.json`, `transcript.jsonl` (untouched raw responses),
`results.jsonl` (verdicts + spans + latency), `summary.json`, `summary.md`.
Commit run dirs you want to publish; raw transcripts make grades auditable.

## Extending

- Add a provider: subclass in `bench/providers/`, return the normalized dict
  from `base.py`, register it in `providers/base.py` and `bench.py`.
- Add a dataset: build a full source JSON (`data/<name>_full.json` with
  `questions[]`), freeze a sample with `scripts/make_sample.py`, validate with
  `python3 bench.py validate`.
- Recency datasets must carry `verified_as_of` per question; `rotcheck.py`
  flags rot before a run, not after (the v1 H5 lesson).

## Known issue found while building

`https://ransack.tools/mcp` sits behind Cloudflare, which answers **1010**
("browser signature blocked") to scripts without a User-Agent; the bench sends
a proper UA. The MCP server then requires a bearer token (JSON-RPC -32001):
set `RANSACK_MCP_TOKEN`. Verified working end to end with a token on
2026-09-20 (see `results/` live runs). Note the lane is async: the research
tool returns a `taskId` and the bench polls `tasks_get` until completion.

## Legacy

v1 files (hand-run results, original seed, load tester) are preserved under
[legacy/](legacy/). `control_trivia.json` is their direct descendant, honestly
labeled. The load-test script targets a private token-gated endpoint and is
kept for archaeology, not use.
