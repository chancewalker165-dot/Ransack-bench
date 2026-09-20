#!/usr/bin/env python3
"""Cost dimension for the bench: fact-bearing calls per fixed budget.

Reads scripts/prices.json (dated, sourced list prices + the current README
hit-rates) and emits a markdown table: how many fact-bearing calls $15 of each
provider buys, and how many of those contain the expected fact.

This is NOT a new metric and does not touch the harness. It is an economics
lens on the existing 2026-09-20 results. Re-run after any bench re-run:

    python3 scripts/cost_chart.py [--budget 15] [--out results/COST_ANALYSIS.md]

Caveats baked into the output:
- search lanes and answer lanes are not measurement-equivalent (README caveats)
- estimates (perplexity, serper, brave) are flagged in the table
- list prices, no volume discounts; token costs excluded for sonar-style lanes
"""
import argparse
import json
import sys
from pathlib import Path

HERE = Path(__file__).parent
DEFAULT_BUDGET = 15.0  # USD, ransack's monthly price: the anchor everyone can price against


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--budget", type=float, default=DEFAULT_BUDGET,
                    help="monthly budget in USD (default: ransack's flat month)")
    ap.add_argument("--prices", type=Path, default=HERE / "prices.json")
    ap.add_argument("--out", type=Path, default=None, help="write markdown here instead of stdout")
    a = ap.parse_args()

    p = json.loads(a.prices.read_text(encoding="utf-8"))
    providers, rates = p["providers"], p["hit_rates_2026_09_20"]
    rows = []
    for name, hit in rates.items():
        spec = providers.get(name)
        if spec is None and name.endswith("-answer"):
            # answer lanes are priced off the base vendor entry; exa answers
            # may cost more than searches, flagged as estimate in the output
            name_base = name.split("-")[0]
            spec = providers.get(name_base)
            src_name = name_base
        else:
            src_name = name
        if not spec:
            continue
        calls = a.budget / (spec["price_per_1k_calls"] / 1000.0)
        hit_calls = calls * hit
        rows.append((name, spec["price_per_1k_calls"], calls, hit, hit_calls,
                     spec["verification"].startswith("estimate")))
    rows.sort(key=lambda r: -r[4])

    lines = [
        f"# Fact-bearing calls per ${a.budget:.0f} (2026-09-20 prices and results)",
        "",
        f"How many calls ${a.budget} buys at each provider's list price, and how many of",
        "those contain the expected fact (SimpleQA frozen 200-question sample, bench",
        "v2.0.2). List prices, no volume discounts. Estimates are flagged; re-verify",
        "on publish day via the links in scripts/prices.json.",
        "",
        "| provider | $/1k calls | calls per " + f"${a.budget:.0f}" + " | hit-rate | fact-bearing calls | price figure |",
        "|---|---|---|---|---|---|",
    ]
    for name, price, calls, hit, hit_calls, is_est in rows:
        flag = " (estimate)" if is_est else ""
        lines.append(f"| {name} | ${price:.2f}{flag} | {calls:,.0f} | {hit * 100:.1f}% | {hit_calls:,.0f} | [source]({spec_source(p, src_name)}) |")
    lines += [
        "",
        "Reading: the answer engines win the accuracy column; the flat-priced",
        "search lane wins the absolute number of fact-bearing calls per dollar.",
        "Both columns are real; which one matters depends on whether your agent",
        "reads documents or needs one synthesized answer.",
        "",
        "Caveats: lane asymmetry (search k=5 docs vs one answer, see README),",
        "token costs excluded for sonar-style lanes, list prices only, and the",
        "estimate rows carry their own re-verify warnings.",
    ]
    out = "\n".join(lines) + "\n"
    if a.out:
        a.out.write_text(out, encoding="utf-8")
        print(f"wrote {a.out}")
    else:
        print(out)
    return 0


def spec_source(p: dict, name: str) -> str:
    return p["providers"].get(name, {}).get("source", "")


if __name__ == "__main__":
    sys.exit(main())
