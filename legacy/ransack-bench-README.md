# ransack benchmark harness (v1, 2026-08-28)

Runs a fixed, hand-curated 30-question seed against ransack via the MCP surface
(`ransack_ransack` mode=search, format=markdown, verbose=true, crypto=false,
max_results=5). Every question has a known answer, so **grading is
deterministic** (no LLM judge in v1): CORRECT if the output contains the
expected fact, PARTIAL if related-but-not-exact, WRONG otherwise.

## Why this shape (ponytail)

- No new dependencies, no HF downloads, no network scripts: calls go through
  the Pi MCP tools (per the standing rule — never hit ransack.tools/mcp from a
  script).
- Latency + token count come free from the ransack footer on every response.
- The seed doubles as a regression truth set (the in-house "DGX-style"
  controlled QA set the landscape doc §6 recommends).

## Tracks

| Track | Qs | Mirrors |
| --- | --- | --- |
| A simple-fact | 10 | SimpleQA |
| B spec/technical | 6 | vendor demo queries (DGX Spark, RTX 5090, ...) |
| C multi-hop | 5 | FRAMES |
| D recency | 4 | FreshQA / LiveNewsBench |
| E hard-to-find | 5 | BrowseComp |

## Protocol

1. Query via `ransack_ransack` mode=search, verbose=true (footer has latency,
   ~tokens, per-min headroom -> rate-limit telemetry for free).
2. Record per query: verdict, latency (s), ~tokens, sources_used count, errors.
3. Aggregate into `ransack-bench-results.md` with per-track accuracy + p50/p95
   latency + error rate.
4. (Track F, single query) `execute_research` vs plain `search` on the same
   query for the agentic-lane latency/coverage contrast.

## Files

- `ransack-bench-seed.json` — the fixed 30-question seed + grading hints.
- `ransack-bench-results.md` — results of the first full run.
- `../LANSCAPE.md` — the benchmark landscape this harness was built from
  (`/home/egg/projects/ransack-benchmark-landscape-2026-08.md`).
