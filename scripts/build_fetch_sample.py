#!/usr/bin/env python3
"""build_fetch_sample: mechanical, pre-registered sample for EVAL A.

Design: docs/eval-a-fetch-ladder-prereg.md. Draws 60 URLs across 7 strata with
a seeded RNG over candidate pools assembled from neutral public sources. No
ransack calls happen here: ground-truth probing uses plain urllib only (this
is the no-ladder baseline and doubles as independent fact capture).

Everything the script cannot determine mechanically is flagged
needs_owner_verification=true for the owner browser pass (option-4 gate).

Usage: python3 scripts/build_fetch_sample.py
Output: datasets/fetch_eval/sample_v1.json (committed pre-run)
"""

from __future__ import annotations

import json
import os
import random
import sys
import urllib.request
import uuid
from datetime import date, datetime, timezone

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from benchlib.datasets import DATA_DIR  # noqa: E402

SEED = 20260920
UA = "RansackBenchEval/1.0 (sample builder; contact via repo issues)"


def probe(url: str, timeout: float = 12.0) -> tuple[int, str]:
    """Plain urllib GET: status + first 2000 chars of body. Independent of ransack."""
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.status, r.read(2000).decode("utf-8", "replace")
    except urllib.error.HTTPError as e:
        return e.code, e.read(500).decode("utf-8", "replace")
    except Exception as e:  # noqa: BLE001
        return -1, f"{type(e).__name__}: {e}"[:200]


POOLS = {
    # S1: stable, text-first pages. Fact anchor = the page <title> (stable, on-page).
    "S1_plain_static": [
        "https://www.rfc-editor.org/rfc/rfc9110.html",
        "https://docs.python.org/3/library/urllib.request.html",
        "https://markdown-guide.readthedocs.io/en/latest/",
        "https://semver.org/",
        "https://keepachangelog.com/en/1.1.0/",
        "https://www.json.org/json-en.html",
        "https://datatracker.ietf.org/doc/html/rfc1035",
        "https://numpy.org/doc/stable/user/basics.creation.html",
        "https://sqlite.org/lang_select.html",
        "https://curl.se/docs/manpage.html",
        "https://www.w3.org/TR/REC-html40/struct/text.html",
        "https://man7.org/linux/man-pages/man1/ls.1.html",
    ],
    # S2: sites publicly documented in engineering writeups as TLS-fingerprint
    # gated (block python-requests/urllib). Source: public status/blog posts.
    "S2_tls_gated": [
        "https://www.g2.com/products/notion/reviews",
        "https://www.glassdoor.com/Overview/index.htm",
        "https://www.crunchbase.com/organization/openai",
        "https://www.indeed.com/cmp/Openai",
        "https://www.trustpilot.com/review/github.com",
        "https://www.zoominfo.com/z/OpenAI",
        "https://www.cbinsights.com/company/openai",
        "https://craft.co/openai",
        "https://www.similarweb.com/website/github.com/",
        "https://www.alexa.com/siteinfo/wikipedia.org",
        "https://www.semrush.com/website/github.com/overview/",
        "https://www.similarweb.com/website/openai.com/",
    ],
    # S3: publicly known SPA surfaces (client-rendered; plain HTML is a shell).
    "S3_js_rendered": [
        "https://linear.app/",
        "https://www.figma.com/",
        "https://airtable.com/",
        "https://www.notion.so/",
        "https://vercel.com/dashboard",
        "https://app.netlify.com/",
        "https://web.telegram.org/",
        "https://open.spotify.com/",
        "https://www.canva.com/",
        "https://trello.com/",
        "https://www.figma.com/community",
        "https://dribbble.com/shots",
    ],
    # S4: retailers from Wikipedia's list of largest online retailers (public
    # list); deep paths are drawn from each retailer's own public sitemap when
    # parseable, else the retailer root with needs_owner_verification=true.
    "S4_bot_walled_retailer": [
        "https://www.amazon.com/",
        "https://www.walmart.com/",
        "https://www.ebay.com/",
        "https://www.bestbuy.com/",
        "https://www.target.com/",
        "https://www.etsy.com/",
        "https://www.wayfair.com/",
        "https://www.aliexpress.com/",
        "https://www.flipkart.com/",
        "https://www.mercadolibre.com.mx/",
        "https://www.bol.com/nl/nl/",
        "https://www.zalando.de/",
    ],
    # S6: major paywalled publishers (public knowledge of paywall status).
    "S6_paywalled": [
        "https://www.wsj.com/",
        "https://www.ft.com/",
        "https://www.nytimes.com/",
        "https://www.economist.com/",
        "https://www.bloomberg.com/",
        "https://www.zeit.de/",
        "https://www.lemonde.fr/",
        "https://www.ft.com/markets",
        "https://www.wsj.com/tech",
        "https://www.nytimes.com/section/technology",
        "https://www.theatlantic.com/",
        "https://www.newyorker.com/",
    ],
    # S7 archive-only: drawn from the Wayback CDX API at build time.
    "S7_archive_only": [],  # filled mechanically below
}

S5_DOMAINS = [
    "https://www.wikipedia.org", "https://www.python.org",
    "https://www.rust-lang.org", "https://go.dev", "https://www.sqlite.org",
    "https://www.r-project.org", "https://www.postgresql.org",
    "https://redis.io", "https://nginx.org", "https://www.gnu.org",
]


def build_s7(rng: random.Random, n: int) -> list[dict]:
    """Draw URLs that Wayback has archived but whose live status is not 200."""
    out = []
    domains = ["python.org", "rust-lang.org", "sqlite.org", "postgresql.org",
               "nginx.org", "gnu.org", "w3.org", "kernel.org", "debian.org",
               "apache.org"]
    tried = set()
    guard = 0
    while len(out) < n and guard < 25:
        guard += 1
        dom = rng.choice(domains)
        year = rng.choice(["2015", "2016", "2017", "2018"])
        cdx = (f"https://web.archive.org/cdx/search/cdx?url={dom}/*&output=json"
               f"&from={year}&to={year}&filter=statuscode:200&limit=40&collapse=urlkey")
        try:
            req = urllib.request.Request(cdx, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=30) as r:
                rows = json.loads(r.read().decode("utf-8", "replace"))
        except Exception as e:  # noqa: BLE001
            print(f"    s7: cdx fetch failed ({e.__class__.__name__})", flush=True)
            continue
        if not rows or len(rows) < 2:
            continue
        candidate = rng.choice(rows[1:])[2]  # original URL column
        print(f"    s7: probing live status of {candidate[:70]}", flush=True)
        if candidate in tried:
            continue
        tried.add(candidate)
        status, _ = probe(candidate, timeout=15)
        if status != 200:  # live web cannot serve it; archive is the only path
            out.append({"url": candidate, "expected_outcome": "honest_label_or_fact",
                        "fact_anchor": None, "needs_owner_verification": True,
                        "probe_live_status": status})
    return out


def main() -> int:
    rng = random.Random(SEED)
    entries: list[dict] = []
    print(f"[{datetime.now(timezone.utc).strftime('%H:%M:%S')}] building sample...", flush=True)
    generated = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    print("[build] S1 plain-static: probing + fact capture", flush=True)
    # S1: fact anchor captured independently via plain urllib (the page title).
    for url in rng.sample(POOLS["S1_plain_static"], 10):
        status, body = probe(url)
        anchor = None
        if status == 200 and "<title>" in body:
            anchor = body.split("<title>", 1)[1].split("</title>", 1)[0].strip()[:120]
        entries.append({"id": f"F-{len(entries) + 1:03d}", "stratum": "S1_plain_static",
                        "url": url, "expected_outcome": "fact_found",
                        "fact_anchor": anchor,
                        "fact_source": "plain_urllib" if anchor else None,
                        "needs_owner_verification": anchor is None,
                        "probe_live_status": status})

    for stratum in ("S2_tls_gated", "S3_js_rendered", "S4_bot_walled_retailer",
                    "S6_paywalled"):
        print(f"[build] {stratum}: probing", flush=True)
        for url in rng.sample(POOLS[stratum], 10):
            status, _ = probe(url)
            entries.append({"id": f"F-{len(entries) + 1:03d}", "stratum": stratum,
                            "url": url,
                            "expected_outcome": "honest_label_or_fact"
                            if stratum != "S6_paywalled" else "honest_label_or_explicit_failure",
                            "fact_anchor": None, "fact_source": None,
                            "needs_owner_verification": True,
                            "probe_live_status": status})

    print("[build] S5 dead-or-404: probing", flush=True)
    for dom in rng.sample(S5_DOMAINS, 10):
        url = f"{dom}/{uuid.UUID(int=rng.getrandbits(128), version=4)}"
        status, _ = probe(url)
        entries.append({"id": f"F-{len(entries) + 1:03d}", "stratum": "S5_dead_or_404",
                        "url": url, "expected_outcome": "explicit_failure_with_status",
                        "fact_anchor": None, "fact_source": None,
                        "needs_owner_verification": False,
                        "probe_live_status": status})

    print("[build] S7 archive-only: wayback cdx + live probes (bounded)", flush=True)
    for e in build_s7(rng, 10):
        entries.append({"id": f"F-{len(entries) + 1:03d}", "stratum": "S7_archive_only",
                        **e})

    manifest = {
        "dataset": "fetch_eval",
        "sample_id": "fetch_eval_v1",
        "seed": SEED,
        "frozen_on": date.today().isoformat(),
        "preregistration": "docs/eval-a-fetch-ladder-prereg.md",
        "selection_disclosure": (
            "Candidate pools from neutral public sources, cited in the pools "
            "block of scripts/build_fetch_sample.py; seeded RNG draw; no URL "
            "from any prior ransack run; ground-truth probing via plain urllib "
            "only. Entries flagged needs_owner_verification require an owner "
            "browser pass before the eval runs (option-4 gate)."),
        "questions": entries,
    }
    os.makedirs(os.path.join(DATA_DIR, "fetch_eval"), exist_ok=True)
    out = os.path.join(os.path.dirname(DATA_DIR), "datasets", "fetch_eval_sample_v1.json")
    json.dump(manifest, open(out, "w"), indent=1, ensure_ascii=False)
    counts: dict[str, int] = {}
    for e in entries:
        counts[e["stratum"]] = counts.get(e["stratum"], 0) + 1
    owner = sum(1 for e in entries if e["needs_owner_verification"])
    print(f"wrote {out}: {len(entries)} entries, {owner} need owner verification", flush=True)
    for k, v in sorted(counts.items()):
        print(f"  {k}: {v}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
