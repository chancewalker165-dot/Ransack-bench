"""Search-API provider adapters over plain HTTP. Shapes verified against vendor
docs 2026-09-19 (see METHODOLOGY.md source register for the doc URLs)."""

from __future__ import annotations

import json

from .base import _http, _json_body, require_env


def _docs_from(items: list, title_key: str, url_key: str, text_key: str) -> list[dict]:
    return [{"title": str(i.get(title_key) or ""), "url": str(i.get(url_key) or ""),
             "text": str(i.get(text_key) or "")} for i in items]


class Tavily:
    """POST https://api.tavily.com/search, Authorization: Bearer.
    include_answer makes it answer-producing as well as a search lane."""

    name = "tavily"

    def ask(self, question: str, k: int) -> dict:
        key = require_env("TAVILY_API_KEY")
        _, _, raw = _http(
            "POST", "https://api.tavily.com/search",
            {"Content-Type": "application/json", "Authorization": f"Bearer {key}"},
            _json_body({"query": question, "max_results": k, "search_depth": "basic",
                        "include_answer": "basic"}),
        )
        data = json.loads(raw.decode("utf-8", "replace"))
        docs = _docs_from(data.get("results", []), "title", "url", "content")
        return {"answer": data.get("answer"), "documents": docs,
                "tokens_est": None, "server_latency_s": data.get("response_time"),
                "raw": data}


class Brave:
    """GET https://api.search.brave.com/res/v1/web/search, X-Subscription-Token."""

    name = "brave"

    def ask(self, question: str, k: int) -> dict:
        key = require_env("BRAVE_API_KEY")
        import urllib.parse
        url = ("https://api.search.brave.com/res/v1/web/search?q="
               + urllib.parse.quote(question) + f"&count={k}")
        _, _, raw = _http("GET", url, {"Accept": "application/json",
                                       "X-Subscription-Token": key})
        data = json.loads(raw.decode("utf-8", "replace"))
        items = (data.get("web") or {}).get("results", [])
        docs = _docs_from(items, "title", "url", "description")
        return {"answer": None, "documents": docs,
                "tokens_est": None, "server_latency_s": None, "raw": data}


class Serper:
    """POST https://google.serper.dev/search, X-API-KEY.
    (Header + q/num params are the widely documented convention; the response
    schema .organic[].title/link/snippet is verified against serper.dev's own
    embedded demo responses, 2026-09-19.)"""

    name = "serper"

    def ask(self, question: str, k: int) -> dict:
        key = require_env("SERPER_API_KEY")
        _, _, raw = _http(
            "POST", "https://google.serper.dev/search",
            {"Content-Type": "application/json", "X-API-KEY": key},
            _json_body({"q": question, "num": k}),
        )
        data = json.loads(raw.decode("utf-8", "replace"))
        docs = _docs_from(data.get("organic", []), "title", "link", "snippet")
        return {"answer": data.get("answerBox", {}).get("answer") if data.get("answerBox") else None,
                "documents": docs, "tokens_est": None, "server_latency_s": None, "raw": data}


class Exa:
    """POST https://api.exa.ai/search, x-api-key."""

    name = "exa"

    def ask(self, question: str, k: int) -> dict:
        key = require_env("EXA_API_KEY")
        _, _, raw = _http(
            "POST", "https://api.exa.ai/search",
            {"Content-Type": "application/json", "x-api-key": key},
            _json_body({"query": question, "numResults": k}),
        )
        data = json.loads(raw.decode("utf-8", "replace"))
        docs = _docs_from(data.get("results", []), "title", "url", "text")
        return {"answer": None, "documents": docs,
                "tokens_est": None, "server_latency_s": None, "raw": data}


class ExaAnswer:
    """POST https://api.exa.ai/answer, x-api-key; answer-producing lane
    (.answer + .citations[].title/url/text per docs, 2026-09-19)."""

    name = "exa-answer"

    def ask(self, question: str, k: int) -> dict:
        key = require_env("EXA_API_KEY")
        _, _, raw = _http(
            "POST", "https://api.exa.ai/answer",
            {"Content-Type": "application/json", "x-api-key": key},
            _json_body({"query": question, "text": True}),
        )
        data = json.loads(raw.decode("utf-8", "replace"))
        docs = _docs_from(data.get("citations", []), "title", "url", "text")
        return {"answer": data.get("answer") if isinstance(data.get("answer"), str) else json.dumps(data.get("answer")),
                "documents": docs, "tokens_est": None, "server_latency_s": None, "raw": data}


class Perplexity:
    """POST https://api.perplexity.ai/v1/sonar (current documented path),
    Bearer; answer-producing. Response: .choices[].message.content,
    .citations (URL strings), .search_results[] with title/url/snippet."""

    name = "perplexity"

    def ask(self, question: str, k: int) -> dict:
        key = require_env("PERPLEXITY_API_KEY")
        _, _, raw = _http(
            "POST", "https://api.perplexity.ai/v1/sonar",
            {"Content-Type": "application/json", "Authorization": f"Bearer {key}"},
            _json_body({"model": "sonar", "temperature": 0,
                        "messages": [{"role": "user", "content": question}]}),
        )
        data = json.loads(raw.decode("utf-8", "replace"))
        answer = data.get("choices", [{}])[0].get("message", {}).get("content", "")
        sr = data.get("search_results") or []
        docs = _docs_from(sr, "title", "url", "snippet") if sr else \
            [{"title": "", "url": str(u), "text": ""} for u in (data.get("citations") or [])]
        return {"answer": answer, "documents": docs,
                "tokens_est": (data.get("usage") or {}).get("total_tokens"),
                "server_latency_s": None, "raw": data}
