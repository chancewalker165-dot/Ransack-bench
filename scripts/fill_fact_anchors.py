#!/usr/bin/env python3
"""Fill the ground-truth `fact_anchor` values for Eval A's hard strata.

Pre-registration: docs/eval-a-fetch-ladder-prereg.md. That document specifies how
anchors are captured, and this script implements exactly that protocol:

  1. plain urllib fetch of the live URL (the same client the no-ladder baseline
     uses, i.e. independent of ransack's ladder), then
  2. for S7 archive-only, and whenever the live fetch yields no real content, the
     Wayback snapshot of the URL.

A candidate anchor is a verbatim run of body prose from the captured page, so it
survives ransack's markdown conversion (the earlier S1 anchors were page titles,
which markdown drops: FINDINGS.md records that artifact). Paywalled entries get
the page identity (title) instead, because their body is behind the wall by
definition and the prereg expects a label or status, not success.

Entries where neither source yields real content keep fact_anchor=None and stay
flagged for the owner's browser pass. Nothing here is captured from ransack.

Usage:
  python3 scripts/fill_fact_anchors.py --dry-run   # preview, writes nothing
  python3 scripts/fill_fact_anchors.py             # writes the manifest
"""
from __future__ import annotations

import argparse
import html as html_mod
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from benchlib.graders import normalize  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MANIFEST = os.path.join(ROOT, "datasets", "fetch_eval_sample_v1.json")
UA = "RansackBenchEval/1.0 (anchor pass; independent of ransack)"
NEEDS_ANCHOR_SKIP = {"S5_dead_or_404"}  # scored on explicit failure, no fact exists
PAYWALLED = "S6_paywalled"

# A challenge/error page is not content: never mine an anchor out of one.
SHELL_MARKERS = (
    "just a moment", "attention required", "enable javascript", "enable js",
    "checking your browser", "verify you are human", "access denied",
    "are you a robot", "ddos protection", "cf-browser-verification",
    "please turn javascript on", "captcha", "request blocked",
    "you have been blocked", "unusual traffic", "temporarily blocked",
    "possible abuse", "security verification", "unsupported browser",
    "browser or operating system is out of date", "no longer supported",
    "challenge validation", "please inform the site owner", "broken link",
    "temporarily closed",
)
REAL_MIN_TEXT_CHARS = 600
ANCHOR_MIN_WORDS = 8
ANCHOR_MAX_CHARS = 160
# An anchor is prose, not source code or a browser notice.
_NON_PROSE_RE = re.compile(r"[{};=<>]|\bconst\b|\bfunction\b|\bvar\b|\bwindow\.[a-z]")


def valid_anchor(anchor: str | None, confidence: str) -> bool:
    """An anchor must survive normalize() (containment is on normalized tokens)
    and must look like the page's own content, not code, a wall notice, or capture
    garbage."""
    if not anchor:
        return False
    a = " ".join(anchor.split())
    if len(a) < 12 or _NON_PROSE_RE.search(a):
        return False
    printable = sum(1 for c in a if c.isprintable())
    if printable < len(a) * 0.95 or "\ufffd" in a:
        return False  # encoding artifact, not ground truth
    if re.match(r"^https?://", a) or re.match(r"^[\w.-]+\.(com|net|org|de|uk|nl)(\b|$)", a, re.I):
        return False  # a bare URL/domain is not page content
    norm = normalize(a)
    min_tokens = 5 if confidence == "title_only" else 6
    if len(norm.split()) < min_tokens:
        return False
    return not any(m in a.lower() for m in SHELL_MARKERS)


def _get(url: str, timeout: float = 25.0, cap: int = 400_000) -> tuple[int, str, str]:
    """Plain urllib GET. Returns (status, body, final_url). Independent of ransack."""
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return int(getattr(r, "status", 200)), r.read(cap).decode("utf-8", "replace"), r.geturl()
    except urllib.error.HTTPError as e:
        return int(e.code), e.read(cap).decode("utf-8", "replace"), url
    except Exception as e:  # noqa: BLE001
        return -1, f"{type(e).__name__}: {e}"[:200], url


def html_to_text(raw: str) -> str:
    """Minimal HTML to text. No third-party extractor: the anchor must exist on the
    page, so the simplest reader is also the least circular."""
    h = re.sub(r"(?is)<(script|style|noscript|svg|template)[^>]*>.*?</\1>", " ", raw)
    h = re.sub(r"(?is)<br[^>]*>|</p>|</div>|</li>|</h[1-6]>|</tr>", "\n", h)
    h = re.sub(r"(?s)<[^>]+>", " ", h)
    h = html_mod.unescape(h)
    h = re.sub(r"[ \t\xa0]+", " ", h)
    h = re.sub(r"\n\s*\n+", "\n", h)
    return h.strip()


def is_real_content(text: str) -> bool:
    return len(text) >= REAL_MIN_TEXT_CHARS and not any(m in text.lower() for m in SHELL_MARKERS)


def extract_title(raw: str) -> str | None:
    m = re.search(r'(?is)<meta[^>]+property=["\']og:title["\'][^>]*content=["\']([^"\']+)', raw)
    if not m:
        m = re.search(r"(?is)<title[^>]*>(.*?)</title>", raw)
    if not m:
        return None
    t = re.sub(r"\s+", " ", html_mod.unescape(m.group(1))).strip()
    t = re.sub(r"\s*[|\-–—]\s*[^|\-–—]{0,40}$", "", t).strip()  # drop "Title | Site"
    return t[:ANCHOR_MAX_CHARS] or None


_BOILER_STARTS = ("cookie", "we use cookies", "sign in", "log in", "subscribe",
                  "accept all", "this site uses", "skip to", "menu", "search",
                  "your browser", "javascript", "enable")
# A Wayback/error page is not the page under test.
_ERROR_TEXT = ("we are sorry", "can't be found", "could not be found",
               "page not found", "does not exist", "has been removed")
_NAV_HINT_RE = re.compile(r"\b(skip to main content|registry & wish list|shopping cart|sign up for|newsletter)\b", re.I)


def anchor_kind_penalty(anchor: str) -> int:
    """Penalise masthead/nav pickups so real prose wins the score comparison."""
    pen = 0
    if _NAV_HINT_RE.search(anchor):
        pen += 8
    caps = sum(1 for w in anchor.split() if w[:1].isupper())
    if caps >= len(anchor.split()) * 0.6:  # Title Case masthead
        pen += 4
    return pen


def pick_body_anchor(text: str) -> str | None:
    """Best-scoring prose sentence: long, distinctive, not nav or a block notice.
    Deterministic (highest word count wins, ties break toward the earlier line), so
    the same capture always yields the same anchor."""
    best, best_score = None, 0
    for para in text.split("\n"):
        p = para.strip()
        if len(p) < 40:
            continue
        for sent in re.split(r"(?<=[.!?])\s+", p):
            s = " ".join(sent.split())
            if not (ANCHOR_MIN_WORDS <= len(s.split()) and len(s) <= ANCHOR_MAX_CHARS):
                continue
            if s.lower().startswith(_BOILER_STARTS):
                continue
            if sum(c.isdigit() for c in s) > len(s) * 0.3:  # not a table of numbers
                continue
            if any(m in s.lower() for m in _ERROR_TEXT):
                continue
            score = len(s.split()) - anchor_kind_penalty(s)
            if score > best_score:
                best, best_score = s, score
    return best


def wayback_snapshot(url: str) -> tuple[str | None, str | None]:
    """(snapshot_url, timestamp) for the newest archived copy, or (None, None).

    Uses the CDX API rather than the availability API: CDX can be restricted to
    statuscode:200 snapshots, which keeps a wayback copy of a challenge page from
    being mistaken for the page under test."""
    cdx = ("https://web.archive.org/cdx/search/cdx?url=" + urllib.parse.quote(url, safe="")
           + "&output=json&filter=statuscode:200&limit=5&collapse=digest")
    status, body, _ = _get(cdx, timeout=30, cap=200_000)
    if status != 200 or not body.strip():
        return None, None
    try:
        rows = json.loads(body)
    except Exception:  # noqa: BLE001
        return None, None
    if not rows or len(rows) < 2:
        return None, None
    row = rows[-1]  # newest matching snapshot
    ts, original = str(row[1]), row[2]
    return f"https://web.archive.org/web/{ts}id_/{original}", ts


def capture(entry: dict) -> dict:
    """Fill the anchor for one entry. Returns the fields to merge into the manifest.

    Order: live plain fetch, then the Wayback snapshot; an entry is only left
    unflagged when its anchor passes valid_anchor(). Title-only anchors are
    accepted for paywalled entries (identity, not the article body), which the
    prereg explicitly does not expect to be retrievable."""
    url = entry["url"]
    stratum = entry["stratum"]
    utc = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    attempts = []

    def body_or_title(raw: str, source: str) -> dict | None:
        text = html_to_text(raw) if "<" in raw[:2000] else raw
        attempts.append(f"{source} chars={len(text)}")
        if is_real_content(text):
            anchor = pick_body_anchor(text)
            if valid_anchor(anchor, "body_text"):
                return {"fact_anchor": anchor, "fact_source": source,
                        "anchor_confidence": "body_text", "anchor_captured_utc": utc,
                        "anchor_note": None}
        if stratum == PAYWALLED or "wayback" in source:
            title = extract_title(raw)
            if valid_anchor(title, "title_only"):
                note = ("paywalled: body is behind the wall by design; identity anchor only, "
                        "prereg expects a label or status here" if stratum == PAYWALLED
                        else "snapshot yielded no body prose; identity anchor only")
                return {"fact_anchor": title, "fact_source": source,
                        "anchor_confidence": "title_only", "anchor_captured_utc": utc,
                        "anchor_note": note}
        return None

    status, raw, _ = _get(url)
    attempts.append(f"live status={status}")
    hit = body_or_title(raw, "plain_urllib")
    if hit:
        return hit

    snap, ts = wayback_snapshot(url)
    if snap:
        _, s_raw, _ = _get(snap)
        hit = body_or_title(s_raw, f"wayback:{ts}")
        if hit:
            return hit
    else:
        attempts.append("wayback: no statuscode:200 snapshot")

    return {"fact_anchor": None, "fact_source": None, "anchor_confidence": None,
            "anchor_captured_utc": utc,
            "anchor_note": "no real content capturable independently; needs owner "
                           "browser pass. " + "; ".join(attempts)}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true", help="preview without writing")
    ap.add_argument("--redo-stratum", default=None,
                    help="re-capture anchors for a whole stratum (e.g. S1_plain_static). "
                         "Used to replace anchor KINDS that cannot be graded: S1 was "
                         "captured as page <title>, whose text varies between the tag, "
                         "og:title and the product's own title extraction, so a title "
                         "anchor fails on a page whose content arrived intact.")
    args = ap.parse_args()

    doc = json.load(open(MANIFEST))
    if args.redo_stratum:
        targets = [e for e in doc["questions"] if e["stratum"] == args.redo_stratum]
    else:
        targets = [e for e in doc["questions"]
                   if e.get("fact_anchor") is None and e["stratum"] not in NEEDS_ANCHOR_SKIP]
    print(f"{len(targets)} entries need an anchor\n", flush=True)

    filled, missing = 0, []
    for e in targets:
        prev = e.get("fact_anchor")
        fields = capture(e)
        ok = bool(fields["fact_anchor"])
        if args.redo_stratum and not ok and prev and valid_anchor(prev, e.get("anchor_confidence") or "body_text"):
            # never erase existing ground truth because one live capture failed
            fields.update({"fact_anchor": prev, "fact_source": e.get("fact_source"),
                           "anchor_confidence": e.get("anchor_confidence") or "legacy_title",
                           "anchor_note": "redo pass captured nothing on this run; "
                                          "previous anchor kept"})
            ok = True
        if ok and prev and prev != fields["fact_anchor"]:
            fields["anchor_prev"] = prev
            fields["anchor_prev_source"] = e.get("fact_source")
        # invariant: a body anchor must survive the grading normalization
        if ok and fields["anchor_confidence"] == "body_text":
            assert valid_anchor(fields["fact_anchor"], "body_text"), fields["fact_anchor"]
        e.update(fields)
        filled += ok
        if not ok:
            missing.append(e["id"])
        print(f"{e['id']} {e['stratum']:22} {'OK ' if ok else 'MISS'} "
              f"{fields['anchor_confidence'] or '-':11} "
              f"{(fields['fact_anchor'] or fields['anchor_note'] or '')[:78]!r}", flush=True)
        time.sleep(0.4)

    print(f"\nfilled {filled}/{len(targets)}; still missing: {missing or 'none'}")
    if args.dry_run:
        print("dry run: manifest NOT written")
        return 0
    json.dump(doc, open(MANIFEST, "w"), indent=1, ensure_ascii=False)
    print(f"manifest written: {MANIFEST}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())