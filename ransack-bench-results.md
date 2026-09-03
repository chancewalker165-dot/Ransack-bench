# ransack benchmark run v1 — results (2026-08-28)

Fixed 30-question seed (`ransack-bench-seed.json`) run against **ransack.tools** via the Pi MCP surface (`ransack_ransack` mode=search, format=markdown, verbose=true, crypto=false, max_results=5). Grading deterministic — every question has a known answer; verdict = does the returned output contain it.

**Headline: 29/30 CORRECT (96.7%), 1 PARTIAL (3.3%), 0 WRONG. Mean latency 3.2s, p50 2.9s, p95 5.4s. Zero errors, zero rate-limit hits.**

## Per-query results

| ID | Track | Question | Verdict | Latency | ~tokens | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| A1 | A | capital of Australia | ✅ CORRECT | 2.9s | 447 | Canberra, 4 sources incl. gov.au |
| A2 | A | tallest mountain on Earth | ✅ CORRECT | 4.7s | 495 | Mauna Kea vs Everest ambiguity surfaced (both) |
| A3 | A | writer of 1984 | ✅ CORRECT | 4.2s | 465 | George Orwell |
| A4 | A | chemical symbol for gold | ✅ CORRECT | 3.5s | 454 | Au, 5 sources |
| A5 | A | largest ocean | ✅ CORRECT | 5.2s | 397 | Pacific |
| A6 | A | planets in solar system | ✅ CORRECT | 5.0s | 472 | 8 (1 stale "9 planets" noise item) |
| A7 | A | WWII end year | ✅ CORRECT | 9.9s | 484 | 1945, 5 solid sources. Slowest query of run |
| A8 | A | first moonwalker | ✅ CORRECT | 2.7s | 449 | Neil Armstrong |
| A9 | A | water boiling point °C | ✅ CORRECT | 1.6s | 482 | 100°C + correct physics caveats |
| A10 | A | Japan currency | ✅ CORRECT | 3.4s | 466 | yen/JPY |
| B1 | B | DGX Spark TDP | ✅ CORRECT | 2.8s | 495 | 140W, incl. NVIDIA forum + official docs |
| B2 | B | Gemini 2.5 Pro context window | ✅ CORRECT | 1.9s | 424 | 1M tokens (3 sources; 1 consumer-UI caveat) |
| B3 | B | RTX 5090 VRAM | ✅ CORRECT | 5.0s | 690 | 32GB GDDR7 present — **but deal-injector + price-verify block fired on a non-price query** (finding #1) |
| B4 | B | Rust 1.0 year | ✅ CORRECT | 2.5s | 471 | 2015 (blog.rust-lang.org primary) |
| B5 | B | M4 Max max unified memory | ✅ CORRECT | 3.1s | 481 | 128GB (apple.com primary) |
| B6 | B | HTTPS default port | ✅ CORRECT | 1.8s | 473 | 443 |
| C1 | C | strait Australia–Tasmania | ✅ CORRECT | 2.0s | 500 | Bass Strait |
| C2 | C | Warsaw river → sea | ✅ CORRECT | 2.4s | 439 | Vistula → Baltic |
| C3 | C | language of flag (red circle on white) | ⚠️ PARTIAL | 4.7s | 488 | Japan identified (hop 1) but snippets never state official language = Japanese (finding #2) |
| C4 | C | 2016 Olympics host country | ✅ CORRECT | 4.4s | 464 | Brazil |
| C5 | C | Portugal's highest mountain | ✅ CORRECT | 5.6s | 455 | Pico 2,351m (Azores) + mainland Torre 1,993m — ambiguity handled |
| D1 | D | Super Bowl Feb 2025 winner | ✅ CORRECT | 3.0s | 443 | Eagles 40-22 (1 outlier snippet contradicted; 3 sources agree) |
| D2 | D | Microsoft Aug 2025 retirement | ✅ CORRECT | 4.3s | 440 | Bing Search APIs (learn.microsoft.com primary) |
| D3 | D | Tavily acquirer 2026 | ✅ CORRECT | 2.1s | 517 | Nebius $275M (nebius.com primary) |
| D4 | D | TTPD release year | ✅ CORRECT | 1.4s | 535 | 2024 |
| E1 | E | oldest continuously operating restaurant | ✅ CORRECT | 0.9s | 501 | Sobrino de Botín, 1725, Guinness-recorded |
| E2 | E | UK ccTLD | ✅ CORRECT | 1.4s | 502 | .uk |
| E3 | E | smallest country by area | ✅ CORRECT | 3.2s | 501 | Vatican City |
| E4 | E | telescope launched Dec 2021 | ✅ CORRECT | 1.8s | 451 | James Webb (JWST) |
| E5 | E | S in HTTPS | ✅ CORRECT | 2.5s | 431 | Secure |

## Aggregates

| Track | Correct | Partial | Wrong | Accuracy |
| --- | --- | --- | --- | --- |
| A simple-fact (SimpleQA-style) | 10 | 0 | 0 | 100% |
| B spec/technical | 6 | 0 | 0 | 100% |
| C multi-hop (FRAMES-style) | 4 | 1 | 0 | 80% |
| D recency (FreshQA-style) | 4 | 0 | 0 | 100% |
| E hard-to-find (BrowseComp-style) | 5 | 0 | 0 | 100% |
| **Total (30)** | **29** | **1** | **0** | **96.7%** |

**Latency stats (n=30):** mean 3.23s · p50 2.85s · p90 5.0s · p95 5.4s · max 9.9s (A7). Sub-second result in 1/30 (E1 @ 0.9s).
**Tokens:** ~397–690 per query (median ~475); B3's 690 is inflated by the price-verify block.
**Reliability:** 0 errors, 0 timeouts, 0 rate-limit rejections; footer headroom never dropped below 40/60 per-min.

## Track F: agentic lane contrast (execute_research vs search, same query)

| Lane | Latency | Result |
| --- | --- | --- |
| `ransack_ransack` mode=search (B1) | 2.8s | 5 raw results, 140W present in 2 |
| `ransack_execute_research` (time_budget=25, max_sources=4) | **5.25s** | Synthesized answer: exactly correct, disambiguates 140W chip-TDP vs 240W system budget, cites NVIDIA + docs; intent direct_qa (groq classifier), route [perplexity], 1 final source (PPLX fast-path won), coverage 0.6 / confidence 0.7 |

Takeaway: the agentic lane buys answer-groundedness + ambiguity handling at ~2x latency. Both cited sources correctly.

## Findings (feed the ransack backlog)

1. **Deal-injector false positive on B3** — "How much VRAM does the NVIDIA RTX 5090 have?" auto-appended `(site:reddit.com OR site:slickdeals.net OR site:dealnews.com)` and fired the 💰 PRICE VERIFICATION block ($1,999 MSRP cross-check) on a pure-spec question. The 32GB answer still surfaced, but ~215 extra tokens + 3 UNVERIFIED/UNCONFIRMED price rows is noise on non-commerce queries. Same family as the fixed `off-target` bug (server.py `_is_price_query`/`_is_commerce_intent`) — "RTX 5090" carries a price association. Candidate: only fire the injector when the query has an actual buy/purchase/deal signal, not GPU model names.
2. **C3 multi-hop partial** — flag-description → country (Japan) works; the results never close the second hop (official language = Japanese). This is the FRAMES-style gap: `search` returns the intermediate entity, synthesis engine (execute_research) would be needed to complete the chain. Suggests a real test-worthy difference between the search lane and the research lane on multi-hop queries.
3. **A2 / D1 ambiguity handling is good** — contested/ambiguous queries (Everest-vs-Mauna Kea, Eagles-vs-Chiefs outlier snippet) return both sides; majority consensus is reliable.
4. **Freshness verified live** — D2 (Bing Search APIs retired Aug 11 2025) and D3 (Nebius/Tavily, Feb 2026) only return correct answers if the index is current. ransack's recency track is clean.

## Next run (v1.1 candidates)

- Expand seed toward 100 Qs (Parallel-style methodology needs a 100-Q fixed subset to be comparable).
- Add the execute_research lane to every C-track (multi-hop) question — test whether the agentic lane closes the C3-style gap.
- Add 20 "price-laden" spec queries to quantify finding #1's blast radius.
- LLM-judge pass (deepseek-v4-flash via OpenRouter) on the same 30 Qs to cross-check the deterministic grades, per landscape §6.
