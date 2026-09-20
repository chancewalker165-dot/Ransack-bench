# Pricing sources and verification status (2026-09-20)

Prices for the cost dimension. Verification tiers: **verified** = the vendor's
own page, fetched live this session with the quoted figure matching; **estimate**
= third-party or community figures, re-verify on publish day.

| provider | price used | tier | source | how verified |
|---|---|---|---|---|
| ransack | $15/mo flat = $1.00/1k at full use | owner canonical | ransack.tools/llms.txt | live fetch, 2026-09-20 |
| tavily | $0.008/credit | verified | tavily.com/pricing | verify-quote sha 1458baa07a15, 2026-09-20 |
| exa | $7.00/1k search | verified | exa.ai/versus/serper (vendor's own comparison page) | verify-quote sha 39758bd0a619, 2026-09-20 |
| perplexity | $5.00/1k Search API requests (token costs extra on sonar lanes) | estimate | docs.perplexity.ai pricing page | page is dynamic/tabbed; static quote NOT_FOUND 2026-09-20; third-party trackers say $5-$14/1k grounded |
| serper | $1.00/1k (volume ~$0.30/1k) | estimate | serper.dev/pricing | 404 via fetch ladder 2026-09-20; community figures |
| brave | $5.00/1k (credit-based) | estimate | brave.com/search/api | page confirms credit model + $5/mo free credits, no static per-1k figure |
| firecrawl | $7.60/1k searches | owner canonical | ransack.tools/llms.txt market context | live fetch, 2026-09-20 |

Rules for using these numbers publicly:

1. Re-verify every row on publish day; vendor pricing pages move (perplexity's
   page changed shape between the search snippet and the live fetch today).
2. Cite the vendor's own page as the source link, not a tracker.
3. Keep the estimate flag attached to any chart that uses an estimate row.
4. Perplexity sonar-style lanes have token costs on top of request prices; any
   cost table must say so or it is a false comparison.
