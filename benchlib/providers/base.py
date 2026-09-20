"""Provider adapters. Each provider returns one normalized result dict.

Provider contract:
    ask(question: str, k: int) -> {
        "answer": str | None        # synthesized answer, if the product makes one
        "documents": [{title,url,text}]
        "tokens_est": int | None
        "server_latency_s": float | None   # vendor-reported, secondary telemetry only
        "raw": any                          # untouched response, goes to transcript.jsonl
    }
Raise ProviderError on failure; the runner records it and moves on.
"""

from __future__ import annotations

import json
import os
import urllib.error
import urllib.request


class ProviderError(RuntimeError):
    pass


def _http(method: str, url: str, headers: dict, body: bytes | None = None, timeout: float = 45.0):
    req = urllib.request.Request(url, data=body, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.status, dict(resp.headers), resp.read()
    except urllib.error.HTTPError as e:
        raise ProviderError(f"HTTP {e.code} from {url}: {e.read()[:200]!r}") from e
    except (urllib.error.URLError, TimeoutError, OSError) as e:
        raise ProviderError(f"network error for {url}: {e}") from e


def _json_body(payload) -> bytes:
    return json.dumps(payload).encode()


def require_env(name: str) -> str:
    val = os.environ.get(name, "")
    if not val:
        raise ProviderError(f"missing env var {name} for this provider")
    return val


def from_registry(name: str):
    """Instantiate a provider by registry name."""
    from . import mock, ransack_mcp, nosearch_llm, http_search

    registry = {
        "mock": mock.MockProvider,
        "ransack": ransack_mcp.RansackMCP,
        "nosearch": nosearch_llm.NoSearchLLM,
        "tavily": http_search.Tavily,
        "brave": http_search.Brave,
        "serper": http_search.Serper,
        "exa": http_search.Exa,
        "exa-answer": http_search.ExaAnswer,
        "perplexity": http_search.Perplexity,
    }
    if name not in registry:
        raise ProviderError(f"unknown provider {name!r}; known: {sorted(registry)}")
    return registry[name]()
