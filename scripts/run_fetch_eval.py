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

# scripts run outside bench.py do not inherit its .env loading: do it here
import importlib.util as _ilu  # noqa: E402
_spec = _ilu.spec_from_file_location("_bench_cli", os.path.join(ROOT, "bench.py"))
_bench_cli = _ilu.module_from_spec(_spec)
_spec.loader.exec_module(_bench_cli)
_bench_cli._load_dotenv(ROOT)
LABEL_RE = re.compile(r"\[(bot wall|dead page|paywall|unreachable|render|archive|error)[^\]]*\]|HTTP \d{3}", re.I)


def ransack_fetch(mcp: RansackMCP, url: str) -> dict:
    if mcp.session_id is None:
        mcp._ensure_session()
        mcp._discover_tools()
    call = mcp._rpc({"jsonrpc": "2.0", "id": 3, "method": "tools/call",
                     "params": {"name": mcp._search_tool,
                                "arguments": {"url": url, "mode": "fetch",
                                              "format": "markdown", "max_chars": 200000}}})
    if call and "error" in call:
        raise RuntimeError(f"tools/call error: {call['error']}")
    result = (call or {}).get("result", {})
    if result.get("isError"):
        raise RuntimeError(f"tool error: {result.get('content')}")
    text = "\n".join(c.get("text", "") for c in result.get("content", []) if isinstance(c, dict))
    return {"text": text, "tool": mcp._search_tool}


def urllib_fetch(url: str, max_chars: int = 50000) -> dict:
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
    manifest = json.load(open(MANIFEST))
    stamp = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
    outdir = os.path.join(ROOT, "results", f"fetch_eval_{stamp}")
    os.makedirs(outdir, exist_ok=True)
    json.dump({"prereg": "docs/eval-a-fetch-ladder-prereg.md",
               "started_utc": stamp, "n": len(manifest["questions"])},
              open(os.path.join(outdir, "run_config.json"), "w"), indent=2)

    tfile = open(os.path.join(outdir, "transcript.jsonl"), "w")
    rfile = open(os.path.join(outdir, "results.jsonl"), "w")
    mcp = RansackMCP()

    for i, e in enumerate(manifest["questions"], 1):
        # ransack lane
        t0 = time.perf_counter()
        err, rtext, rstatus = None, "", None
        try:
            r = ransack_fetch(mcp, e["url"])
            rtext, rstatus = r["text"], None
        except Exception as ex:  # noqa: BLE001
            err = f"{type(ex).__name__}: {ex}"[:150]
        r_latency = round(time.perf_counter() - t0, 2)

        # baseline lane (no ladder)
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
    print(f"\nrun dir: {outdir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
