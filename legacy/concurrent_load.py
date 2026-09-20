#!/usr/bin/env python3
"""Concurrent-load harness for ransack.tools (Handoff 3 step 1).

Fires N concurrent POSTs at /api/bench-search (the real search() pipeline, no
per-IP cap) and reports client-side p50/p95/p99 latency + status-code breakdown +
total wall time. Polls /api/metrics before/after to surface server-side
in-flight peak + per-tool percentiles, so you can see WHERE it collapses
(embeddings vs SQLite vs limiter) under load — BEFORE optimizing blind.

Stdlib only (ThreadPoolExecutor + urllib). No deps, no key in the script —
the bench token comes from RANSACK_BENCH_TOKEN env or --token.

Usage:
  RANSACK_BENCH_TOKEN=secret python3 bench/concurrent_load.py --url https://ransack.tools --n 100
  python3 bench/concurrent_load.py --url http://localhost:8001 --n 50 --query "RTX 5090 VRAM"

Enable the endpoints on the server first: set RANSACK_BENCH_TOKEN in the Railway
env (or local env) and restart. Endpoints return 404 when the token is unset.
"""
import argparse, json, os, statistics, sys, time, urllib.request, urllib.error
from concurrent.futures import ThreadPoolExecutor, as_completed


def _post(url, token, query, max_results, timeout):
    body = json.dumps({"query": query, "max_results": max_results}).encode()
    req = urllib.request.Request(
        url.rstrip("/") + "/api/bench-search", data=body,
        headers={"Content-Type": "application/json", "X-Bench-Token": token})
    t0 = time.time()
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return time.time() - t0, r.status, r.read()
    except urllib.error.HTTPError as e:
        return time.time() - t0, e.code, e.read()
    except Exception as e:
        return time.time() - t0, 0, str(e).encode()


def _get(url, token, path, timeout=10):
    req = urllib.request.Request(
        url.rstrip("/") + path, headers={"X-Bench-Token": token})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return json.loads(r.read())
    except Exception:
        return None


def _pct(samples, p):
    if not samples:
        return None
    s = sorted(samples)
    k = max(0, min(len(s) - 1, int(round(p / 100 * (len(s) - 1)))))
    return round(s[k], 3)


def main():
    ap = argparse.ArgumentParser(description="Concurrent-load harness for ransack")
    ap.add_argument("--url", required=True, help="base URL, e.g. https://ransack.tools")
    ap.add_argument("--token", default=os.environ.get("RANSACK_BENCH_TOKEN", ""),
                    help="bench token (env RANSACK_BENCH_TOKEN)")
    ap.add_argument("--n", type=int, default=20, help="total requests")
    ap.add_argument("--workers", type=int, default=None,
                    help="max concurrent workers (default = n, all at once)")
    ap.add_argument("--query", default="What is the TDP of the NVIDIA DGX Spark?")
    ap.add_argument("--max-results", type=int, default=2)
    ap.add_argument("--timeout", type=float, default=35.0)
    ap.add_argument("--no-metrics", action="store_true", help="skip /api/metrics polling")
    args = ap.parse_args()

    if not args.token:
        print("error: --token or RANSACK_BENCH_TOKEN required", file=sys.stderr); sys.exit(2)
    workers = args.workers or args.n

    # Preflight: confirm endpoints are enabled.
    pre = _get(args.url, args.token, "/api/metrics")
    if pre is None:
        print(f"error: could not reach /api/metrics on {args.url} "
              f"(is RANSACK_BENCH_TOKEN set on the server?)", file=sys.stderr)
        sys.exit(1)

    print(f"→ firing {args.n} concurrent requests (workers={workers}) at {args.url}/api/bench-search")
    print(f"  query={args.query!r}  max_results={args.max_results}  timeout={args.timeout}s")
    print(f"  pre-flight metrics: inflight={pre.get('inflight')} peak={pre.get('inflight_peak')}")
    t_start = time.time()
    pairs = []  # (code, latency)
    with ThreadPoolExecutor(max_workers=workers) as ex:
        futs = [ex.submit(_post, args.url, args.token, args.query,
                          args.max_results, args.timeout) for _ in range(args.n)]
        for f in as_completed(futs):
            el, code, body = f.result()
            pairs.append((code, el))
            if code != 200:
                snippet = body[:120].decode("utf-8", "replace") if isinstance(body, bytes) else str(body)
                print(f"  ✗ status={code} elapsed={el:.2f}s {snippet}")
    wall = time.time() - t_start
    codes = {}
    for c, _ in pairs:
        codes[c] = codes.get(c, 0) + 1
    latencies = [el for _, el in pairs]
    ok_lat = [el for c, el in pairs if c == 200]
    print(f"\n─ results ({wall:.1f}s wall, {len(latencies)} samples) ─")
    print(f"  status codes: {codes}")
    if ok_lat:
        print(f"  OK latency  p50={_pct(ok_lat,50)}s  p95={_pct(ok_lat,95)}s  p99={_pct(ok_lat,99)}s")
        print(f"  OK latency  min={min(ok_lat):.3f}s  max={max(ok_lat):.3f}s  mean={statistics.mean(ok_lat):.3f}s")
    if latencies:
        print(f"  ALL latency p50={_pct(latencies,50)}s  p95={_pct(latencies,95)}s  p99={_pct(latencies,99)}s")
        print(f"  throughput: {len(latencies)/wall:.1f} req/s")

    if not args.no_metrics:
        post = _get(args.url, args.token, "/api/metrics")
        if post:
            print(f"\n─ server-side metrics ─")
            print(f"  inflight_now={post.get('inflight')}  inflight_peak={post.get('inflight_peak')}")
            print(f"  rate429_per_min={post.get('rate429_per_min')}  daily429={post.get('daily429')}")
            for t, m in (post.get("tools") or {}).items():
                print(f"  tool={t:<16} n={m.get('n'):>5} p50={m.get('p50')}s p95={m.get('p95')}s p99={m.get('p99')}s")


if __name__ == "__main__":
    main()
