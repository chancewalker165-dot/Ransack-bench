# Ransack Bench

A reproducible evaluation harness for [ransack.tools](https://ransack.tools), a web search + research API for AI agents. The bench calls ransack through its real MCP surface (not a tuned internal endpoint) and grades it deterministically against a fixed, hand-curated question set.

**v1 headline: 29/30 CORRECT (96.7%), 1 PARTIAL, 0 WRONG. Mean latency 3.2s, p50 2.9s, p95 5.4s. Zero errors, zero rate-limit hits.**

## Why this shape

- Every question has a known answer, so grading is deterministic: CORRECT if the output contains the expected fact, PARTIAL if related-but-not-exact, WRONG otherwise. No LLM judge.
- Queries go through the same MCP tool an agent would use, so the bench measures the actual product path end to end.
- Latency and token counts come free from the response footer on every call.
- The fixed seed doubles as a regression truth set: any pipeline change is re-run against it, and a change that doesn't win the A/B gets reverted.

## Tracks

| Track | Qs | What it is | Mirrors |
|---|---|---|---|
| A | 10 | simple-fact ("capital of Australia") | SimpleQA |
| B | 6 | spec/technical (DGX Spark TDP, RTX 5090 VRAM, ports) | vendor demo queries |
| C | 5 | multi-hop ("river through Warsaw, which sea") | FRAMES |
| D | 4 | recency (2025/2026 events) | FreshQA / LiveNewsBench |
| E | 5 | hard-to-find/obscure | BrowseComp |
| F | 1 | agentic lane: `execute_research` vs plain `search` on the same query | n/a |

Per-track scoring makes segment-level accuracy visible (v1: 100% everywhere except C at 80%).

## Files

| File | What it is |
|---|---|
| `ransack-bench-seed.json` | the fixed 30-question seed + per-question grading hints |
| `ransack-bench-README.md` | the original protocol doc from the source repo |
| `ransack-bench-results.md` | v1 full run: per-question verdicts, latency, tokens, aggregates |
| `ransack-bench-evidence.json` | machine-readable per-query evidence for the v1 run |
| `concurrent_load.py` | stdlib-only concurrency harness: fires N parallel requests and reports client p50/p95/p99, status breakdown, throughput |

## Protocol

1. For each seed question, call ransack in search mode with `format=markdown`, `verbose=true` (footer carries latency, token estimate, per-minute rate-limit headroom), `max_results=5`.
2. Record per query: verdict, latency (s), token estimate, sources used count, errors.
3. Grade deterministically against the seed's expected answer and grading hints.
4. Aggregate into a results doc: per-track accuracy, p50/p95 latency, error rate.
5. Optionally run Track F: the same query through the agentic research lane for a latency/coverage contrast.

## Concurrency harness

`concurrent_load.py` is dependency-free (stdlib only). The bench token is supplied via env or flag, never stored in the repo:

```bash
RANSACK_BENCH_TOKEN=secret python3 concurrent_load.py --url https://ransack.tools --n 100
```

It fires N concurrent POSTs at the real search pipeline and polls the server-side metrics endpoint before/after to surface server p50/p95/p99, in-flight gauges, and 429 counters.

## Reproducibility notes

- The seed is fixed and versioned here; graders should tag which commit of the seed a run used.
- Latency figures are live-network numbers from a residential connection; treat absolute values as indicative, relative A/B deltas as the signal.
- Questions in track D (recency) have a shelf life: re-verify their expected answers before reusing this seed later.
