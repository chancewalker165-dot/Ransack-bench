#!/usr/bin/env python3
"""run_fetch_eval: EVAL A executor (prereg: docs/eval-a-fetch-ladder-prereg.md).

For each sample URL, runs two systems and grades both against the answer key:
  1. ransack fetch  - the real MCP fetch path (the ladder under test)
  2. plain urllib   - the no-ladder control

Grades (per system, per entry):
  SUCCESS         fact anchor found in returned content (or, for S5, explicit
                  failure with the correct status)
  HONEST_FAILURE  no fact, but an explicit label/status was returned
  SHELL           content returned, fact absent, no label, suspiciously short
  MISS            content returned, fact absent, no label

Output: results/fetch_eval_<ts>/{transcript.jsonl,results.jsonl,summary.md}
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from benchlib.graders import normalize  # noqa: E402
from benchlib.providers.base import _http, _json_body  # noqa: E484
from benchlib.providers.ransack_mcp import RansackMCP  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MANIFEST = os.path.join(ROOT, "datasets", "fetch_eval_sample_v1.json")
# Both lanes get the same content budget so the cap can never decide a verdict.
BASELINE_MAX_CHARS = 200_000
# Strata scored on failure honesty rather than fact retrieval, so they need no anchor:
# S5 (dead pages, graded on status and label) and S6 (paywalled news sections, where the
# prereg expects a label or status rather than success, and section-homepage content
# reshuffles hourly so a homepage anchor measures timing instead of the product).
LABEL_ONLY_STRATA = {"S5_dead_or_404", "S6_paywalled"}

# scripts run outside bench.py do not inherit its .env loading: do it here
import importlib.util as _ilu  # noqa: E402
_spec = _ilu.spec_from_file_location("_bench_cli", os.path.join(ROOT, "bench.py"))
_bench_cli = _ilu.module_from_spec(_spec)
_spec.loader.exec_module(_bench_cli)
_bench_cli._load_dotenv(ROOT)
LABEL_RE = re.compile(r"\[(bot wall|dead page|paywall|unreachable|render|archive|error|fetch timeout)[^\]]*\]", re.I)


def _call_tool(mcp: RansackMCP, args: dict, rid: int = 3, tool: str | None = None) -> dict:
    if mcp.session_id is None:
        mcp._ensure_session()
        mcp._discover_tools()
    call = mcp._rpc({"jsonrpc": "2.0", "id": rid, "method": "tools/call",
                     "params": {"name": tool or mcp._search_tool, "arguments": args}})
    if call and "error" in call:
        raise RuntimeError(f"tools/call error: {call['error']}")
    result = (call or {}).get("result", {})
    if result.get("isError"):
        raise RuntimeError(f"tool error: {result.get('content')}")
    return result


def _tasks_tool_name(mcp: RansackMCP) -> str:
    """The poll tool is registered under a namespaced name, so resolve it from
    tools/list instead of hardcoding (a wrong name would look like a failed fetch)."""
    cached = getattr(mcp, "_tasks_tool", None)
    if cached:
        return cached
    listing = mcp._rpc({"jsonrpc": "2.0", "id": 9, "method": "tools/list", "params": {}})
    names = [t.get("name", "") for t in (listing or {}).get("result", {}).get("tools", [])]
    for n in names:
        if "tasks_get" in n or n == "tasks_get":
            mcp._tasks_tool = n  # type: ignore[attr-defined]
            return n
    raise RuntimeError(f"no tasks_get tool in tools/list: {names}")


def _text_of(result: dict) -> str:
    return "\n".join(c.get("text", "") for c in result.get("content", []) if isinstance(c, dict))


def ransack_fetch(mcp: RansackMCP, url: str) -> dict:
    """Sync lane: the bounded default a caller gets (tool wall, 40s in prod)."""
    result = _call_tool(mcp, {"url": url, "mode": "fetch", "format": "markdown",
                              "max_chars": 200000})
    return {"text": _text_of(result), "tool": mcp._search_tool}


def ransack_fetch_background(mcp: RansackMCP, url: str, poll_cap_s: float = 240.0,
                             interval_s: float = 5.0) -> dict:
    """Full-ladder lane: mode=fetch with background=true runs the SAME ladder with a
    600s budget and hands back a taskId, so tiers the sync tool wall cuts short still
    run (server.py: background path, RANSACK_FETCH_TASK_WALL_S). Polling is capped so
    one pathological host cannot stall the whole run; a cap hit is recorded as a
    timeout, never as a success."""
    handle = _text_of(_call_tool(mcp, {"url": url, "mode": "fetch", "format": "markdown",
                                       "max_chars": 200000, "background": True}))
    try:
        task_id = json.loads(handle)["taskId"]
    except Exception:  # noqa: BLE001
        return {"text": handle, "tool": "ransack(background)"}
    poll_tool = _tasks_tool_name(mcp)
    deadline = time.time() + poll_cap_s
    while time.time() < deadline:
        time.sleep(interval_s)
        poll = _text_of(_call_tool(mcp, {"taskId": task_id}, rid=4, tool=poll_tool))
        try:
            d = json.loads(poll)
        except Exception:  # noqa: BLE001
            continue
        if d.get("status") == "completed":
            return {"text": str(d.get("result") or ""), "tool": "ransack(background)"}
        if d.get("status") in ("failed", "error"):
            return {"text": str(d.get("error") or "background task failed"),
                    "tool": "ransack(background)"}
    return {"text": f"[eval timeout: background task {task_id} not finished within "
                    f"{int(poll_cap_s)}s]", "tool": "ransack(background)", "poll_timeout": True}


def urllib_fetch(url: str, max_chars: int = BASELINE_MAX_CHARS) -> dict:
    req = urllib.request.Request(url, headers={"User-Agent": "RansackBenchEval/1.0 baseline"})
    try:
        with urllib.request.urlopen(req, timeout=25) as r:
            return {"text": r.read(max_chars).decode("utf-8", "replace"), "status": r.status}
    except urllib.error.HTTPError as e:
        return {"text": e.read(500).decode("utf-8", "replace"), "status": e.code}
    except Exception as e:  # noqa: BLE001
        return {"text": f"{type(e).__name__}: {e}"[:200], "status": -1}


def grade(entry: dict, content: str, status) -> dict:
    anchor = entry.get("fact_anchor")
    label = bool(LABEL_RE.search(content))
    short = len(content) < 500
    if anchor:
        hit = normalize(anchor) in normalize(content)
    else:
        hit = False
    if hit:
        verdict = "SUCCESS"
    elif label:
        # an explicit label is an honest outcome even without a transport status
        verdict = "HONEST_FAILURE"
    elif entry["expected_outcome"] == "explicit_failure_with_status" and content and short:
        verdict = "SHELL"
    elif content and short:
        verdict = "SHELL"
    else:
        verdict = "MISS"
    return {"verdict": verdict, "labeled": label, "content_chars": len(content),
            "status": status}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--lane", choices=("sync", "background"), default="sync",
                    help="sync = the bounded default (tool wall, 40s in prod); background = "
                         "mode=fetch background=true, the SAME ladder with a 600s budget, "
                         "polled via tasks_get. Hard pages need the background lane: the "
                         "sync wall kills a stealth-tier render mid-flight.")
    ap.add_argument("--poll-cap", type=float, default=240.0,
                    help="background lane only: max seconds to poll one URL")
    args = ap.parse_args()
    lane = args.lane

    manifest = json.load(open(MANIFEST))
    stamp = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
    outdir = os.path.join(ROOT, "results",
                          f"fetch_eval_{'bg_' if lane == 'background' else ''}{stamp}")
    os.makedirs(outdir, exist_ok=True)
    json.dump({"prereg": "docs/eval-a-fetch-ladder-prereg.md",
               "started_utc": stamp, "n": len(manifest["questions"]),
               "lane": lane, "poll_cap_s": args.poll_cap if lane == "background" else None},
              open(os.path.join(outdir, "run_config.json"), "w"), indent=2)

    tfile = open(os.path.join(outdir, "transcript.jsonl"), "w")
    rfile = open(os.path.join(outdir, "results.jsonl"), "w")
    mcp = RansackMCP()
    excluded: list[dict] = []

    for i, e in enumerate(manifest["questions"], 1):
        # Grade an entry only when its fact is DEFINED, and skip before spending any
        # call. Grading a fact that was never written down scores an unanchored entry
        # as a miss, the same defect class as the two grading bugs already corrected
        # offline (2026-09-20). S5 and S6 need no anchor: both are scored on failure
        # honesty (dead pages by status, paywalled news sections by label).
        if not e.get("fact_anchor") and e["stratum"] not in LABEL_ONLY_STRATA:
            excluded.append({"id": e["id"], "stratum": e["stratum"], "url": e["url"],
                             "reason": e.get("anchor_note") or "no fact_anchor"})
            print(f"[{i}/{len(manifest['questions'])}] {e['id']} {e['stratum'][:14]:14} "
                  f"EXCLUDED (no ground-truth anchor)", flush=True)
            continue

        # ransack lane
        t0 = time.perf_counter()
        err, rtext, rstatus = None, "", None
        try:
            r = (ransack_fetch_background(mcp, e["url"], poll_cap_s=args.poll_cap)
                 if lane == "background" else ransack_fetch(mcp, e["url"]))
            rtext, rstatus = r["text"], None
        except Exception as ex:  # noqa: BLE001
            err = f"{type(ex).__name__}: {ex}"[:150]
        r_latency = round(time.perf_counter() - t0, 2)

        # baseline lane (no ladder). Same content budget as the ransack lane: a smaller
        # read cap made late-page facts unreachable for the control and decided verdicts
        # (F-001/F-005 scored baseline MISS purely from truncation, 50k vs 200k).
        t0 = time.perf_counter()
        b = urllib_fetch(e["url"])
        b_latency = round(time.perf_counter() - t0, 2)

        rg = (grade(e, rtext, rstatus) if not err
              else {"verdict": "ERROR", "labeled": False, "content_chars": 0, "status": None})
        bg = grade(e, b["text"], b.get("status"))
        rec = {"id": e["id"], "stratum": e["stratum"], "url": e["url"],
               "ransack": {"latency_s": r_latency, "error": err, **rg},
               "baseline": {"latency_s": b_latency, "status": b.get("status"), **bg}}
        rfile.write(json.dumps(rec, default=str) + "\n")
        rfile.flush()
        if not err:
            tfile.write(json.dumps({"id": e["id"], "url": e["url"],
                                    "ransack_raw": rtext[:200000],
                                    "baseline_text": b["text"][:50000]}, default=str) + "\n")
            tfile.flush()
        print(f"[{i}/{len(manifest['questions'])}] {e['id']} {e['stratum'][:14]:14} "
              f"ransack={rg['verdict']:13} baseline={bg['verdict']:8} "
              f"{r_latency:.1f}s/{b_latency:.1f}s", flush=True)

    tfile.close()
    rfile.close()

    # aggregate
    recs = [json.loads(l) for l in open(os.path.join(outdir, "results.jsonl"))]
    strata = {}
    for r in recs:
        strata.setdefault(r["stratum"], []).append(r)
    lines = ["# Eval A: fetch ladder (ransack) vs plain fetch baseline", "",
             "Grades: SUCCESS / HONEST_FAILURE / SHELL (content, no fact, no label) /",
             "MISS (content, no fact, no label, full-length) / ERROR.", "",
             "Entries whose fact anchor is not yet defined are EXCLUDED, not scored as",
             "misses: an undefined fact is unmeasurable. They are listed at the end of",
             "this summary and need the owner's browser pass (prereg option-4 gate).", "",
             "| stratum | n | ransack S/HF/SHELL/MISS | baseline S/HF/SHELL/MISS |",
             "|---|---|---|---|"]
    for st in sorted(strata):
        rs = strata[st]

        def counts(key):
            c = {"SUCCESS": 0, "HONEST_FAILURE": 0, "SHELL": 0, "MISS": 0, "ERROR": 0}
            for x in rs:
                v = x[key]["verdict"]
                c[v] = c.get(v, 0) + 1
            return c
        cr, cb = counts("ransack"), counts("baseline")
        fmt = lambda c: f"{c['SUCCESS']}/{c['HONEST_FAILURE']}/{c['SHELL']}/{c['MISS']}"
        lines.append(f"| {st} | {len(rs)} | {fmt(cr)} | {fmt(cb)} |")
    open(os.path.join(outdir, "summary.md"), "w").write("\n".join(lines) + "\n")
    print("\n" + "\n".join(lines))
    if excluded:
        json.dump(excluded, open(os.path.join(outdir, "excluded.json"), "w"), indent=1)
        print(f"\nexcluded (no anchor, needs owner browser pass): {len(excluded)}")
        for x in excluded:
            print(f"  {x['id']} {x['stratum']:24} {x['url'][:70]}")
    print(f"\nrun dir: {outdir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
