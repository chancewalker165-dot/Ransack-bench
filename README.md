# Ransack-bench v2

> [Why I built this](WHY.md): one MCP for an agent's web research instead of five half-tools.

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

## Quickstart (two commands)

**1. Write your keys once** (copy this, replace the `[BRACKETS]` you have, delete lines you don't; `.env` is gitignored and placeholders are skipped):

```bash
cd Ransack-bench
cat > .env <<'EOF'
RANSACK_MCP_TOKEN=[RANSACK_TOKEN]
OPENAI_API_KEY=[OPENAI_KEY]
TAVILY_API_KEY=[TAVILY_KEY]
BRAVE_API_KEY=[BRAVE_KEY]
SERPER_API_KEY=[SERPER_KEY]
EXA_API_KEY=[EXA_KEY]
PERPLEXITY_API_KEY=[PERPLEXITY_KEY]
EOF
chmod 600 .env
```

**2. Run the whole suite** (auto-loads `.env`, skips providers with missing keys, runs the priority plan, writes `results/COMPARISON.md`):

```bash
python3 bench.py suite            # confirm with y; add --yes to skip the prompt
```

Useful variants: `--limit 25` for a fast first pass, `--providers ransack tavily` to restrict, `--repeat 3` for tighter CIs (note: identical re-queries can be cache-warm; see METHODOLOGY.md).

Single runs still work exactly as before:

```bash
python3 bench.py list                    # datasets + providers
python3 bench.py validate                # schema-check every manifest
python3 bench.py run --dataset frames --provider ransack --limit 10
python3 bench.py compare results/<dirA> results/<dirB>
```

## Results (2026-09-20)

This README is the source of truth; dated run dirs live in `results/` with raw
transcripts. Reproduce with `python3 bench.py suite --yes` and your own keys;
if your numbers differ, open an issue with your run dir.

## simpleqa

**Read this first: ransack is structurally a different product on this table.**
It is a search lane that returns documents, not a synthesized answer, so it has
no judged column; hit-rate is its comparable metric. The ans-acc and judged
columns measure answer engines. Saying it here so nobody has to gotcha it.

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

Hit-rate = expected fact present in returned documents (retrieval). ans-acc = containment of the expected answer in the provider's own answer field. judged = official SimpleQA grader prompt on that answer (where the manifest declares the judge). Answer accuracy only exists for answer-producing lanes.



Full caveats: judge model is flash-tier glm-5.3-flash via OpenRouter on the
verbatim official prompt (a stronger judge tightens numbers; `scripts/rejudge.py`
re-grades every simpleqa run with zero provider calls - ranking-robustness
re-checks are cheap and welcome). Tavily's published 93.3% used their own
gpt-4.1 pipeline on the full 4,326-question set: not the same eval as this
frozen 200-question sample.

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

- Add a provider: subclass in `benchlib/providers/`, return the normalized dict
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
2026-09-20 (see `results/` live runs).

## Legacy

v1 files (hand-run results, original seed, load tester) are preserved under
[legacy/](legacy/). `control_trivia.json` is their direct descendant, honestly
labeled. The load-test script targets a private token-gated endpoint and is
kept for archaeology, not use.
