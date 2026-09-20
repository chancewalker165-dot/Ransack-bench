"""Ransack provider over the MCP streamable-HTTP surface (the real product path).

Env:
  RANSACK_MCP_URL     default https://ransack.tools  (MCP endpoint: <url>/mcp)
  RANSACK_MCP_TOKEN   bearer token if the server requires auth

- Tool names are discovered via tools/list because servers may register the
  search tool as "ransack" or "ransack_ransack".
- Latency is measured client-side by the runner. Any footer latency the server
  reports is captured as server_latency_s (secondary telemetry, never primary).
"""

from __future__ import annotations

import json
import os
import re

from .base import ProviderError, _http, _json_body

JSONRPC_HEADERS = {
    "Content-Type": "application/json",
    "Accept": "application/json, text/event-stream",
    # Without a non-empty User-Agent, Cloudflare in front of ransack.tools
    # answers 1010 (browser-signature block) before the MCP server sees us.
    "User-Agent": "RansackBench/2.0 (+https://github.com/chancewalker165-dot/Ransack-bench)",
}

TOOLS_RPC = {
    "jsonrpc": "2.0", "id": 1, "method": "initialize",
    "params": {
        "protocolVersion": "2024-11-05", "capabilities": {},
        "clientInfo": {"name": "ransack-bench", "version": "2.0.0"},
    },
}


def _parse_rpc_response(raw: bytes, content_type: str):
    """MCP servers may answer with plain JSON or an SSE stream; handle both.
    Notifications (no id) return an empty body: return None."""
    text = raw.decode("utf-8", "replace")
    if not text.strip():
        return None
    if "text/event-stream" in content_type:
        for line in text.splitlines():
            if line.startswith("data:"):
                payload = line[5:].strip()
                if not payload:
                    continue
                try:
                    return json.loads(payload)
                except json.JSONDecodeError:
                    continue
        raise ProviderError("SSE response contained no parsable data line")
    try:
        return json.loads(text)
    except json.JSONDecodeError as e:
        raise ProviderError(f"unparsable MCP response: {text[:200]!r}") from e


class RansackMCP:
    name = "ransack"

    def __init__(self):
        self.base = os.environ.get("RANSACK_MCP_URL", "https://ransack.tools").rstrip("/")
        self.token = os.environ.get("RANSACK_MCP_TOKEN", "")
        self.session_id: str | None = None
        self._search_tool: str | None = None

    def _headers(self) -> dict:
        h = dict(JSONRPC_HEADERS)
        if self.session_id:
            h["mcp-session-id"] = self.session_id
        if self.token:
            h["Authorization"] = f"Bearer {self.token}"
        return h

    def _rpc(self, payload: dict):
        _, hdrs, raw = _http("POST", self.base + "/mcp", self._headers(), _json_body(payload))
        sid = hdrs.get("mcp-session-id") or hdrs.get("Mcp-Session-Id")
        if sid:
            self.session_id = sid
        return _parse_rpc_response(raw, hdrs.get("Content-Type", ""))

    def _ensure_session(self):
        init = self._rpc(TOOLS_RPC)
        if init and "error" in init:
            raise ProviderError(f"MCP initialize failed: {init['error']}")
        # notifications/initialized has no id and expects no response body
        self._rpc({"jsonrpc": "2.0", "method": "notifications/initialized", "params": {}})

    def _discover_tools(self):
        listing = self._rpc({"jsonrpc": "2.0", "id": 2, "method": "tools/list", "params": {}})
        if listing and "error" in listing:
            raise ProviderError(f"tools/list failed: {listing['error']}")
        tools = (listing or {}).get("result", {}).get("tools") or []
        names = [t.get("name", "") for t in tools]
        for t in tools:
            n = t.get("name", "")
            if n in ("ransack", "ransack_ransack"):
                self._search_tool = n
                break
        if not self._search_tool:
            # fall back: a ransack-ish tool that is not one of the specialized
            # portal tools (permit search, youtube, memory, reports, tasks)
            specialized = ("permit", "youtube", "memory", "report", "task", "research")
            for t in tools:
                n = t.get("name", "")
                if "ransack" in n and not any(s in n for s in specialized):
                    self._search_tool = n
                    break
        if not self._search_tool:
            raise ProviderError(f"no search tool in tools/list: {names}")

    def ask(self, question: str, k: int) -> dict:
        if self.session_id is None:
            self._ensure_session()
            self._discover_tools()
        args = {"query": question, "mode": "search", "format": "markdown",
                "verbose": True, "crypto": False, "max_results": k}
        call = self._rpc({"jsonrpc": "2.0", "id": 3, "method": "tools/call",
                          "params": {"name": self._search_tool, "arguments": args}})
        if call and "error" in call:
            raise ProviderError(f"tools/call failed: {call['error']}")
        result = (call or {}).get("result", {})
        if result.get("isError"):
            raise ProviderError(f"tool error: {result.get('content')}")
        content = result.get("content") or []
        text = "\n".join(c.get("text", "") for c in content if isinstance(c, dict))

        tokens_est, server_latency = None, None
        m = re.search(r"~\s*(\d[\d,]*)\s*tokens", text)
        if m:
            tokens_est = int(m.group(1).replace(",", ""))
        m = re.search(r"\b(\d+(?:\.\d+)?)\s*s\b", text)
        if m:
            server_latency = float(m.group(1))

        documents = []
        # ransack markdown: a "[title](url)" line is followed by ">"-prefixed
        # snippet lines. Attach continuations to the doc they belong to,
        # otherwise the snippet text that carries answers is dropped.
        current = None
        for line in text.splitlines():
            links = re.findall(r"\[([^\]]+)\]\((https?://[^)\s]+)\)", line)
            if links:
                for title, url in links:
                    current = {"title": title.strip(), "url": url.strip(), "text": line.strip()}
                    documents.append(current)
            elif current is not None and line.strip():
                if line.lstrip().startswith(">") or not line.lstrip().startswith("#"):
                    current["text"] += " " + line.strip()
        if not documents:
            documents = [{"title": "", "url": "", "text": text}]

        return {"answer": None, "documents": documents[: k * 3],
                "tokens_est": tokens_est, "server_latency_s": server_latency,
                "raw": {"tool": self._search_tool, "text": text}}
