"""No-search LLM control lane: the baseline that exposes non-discriminative seeds.

An OpenAI-compatible chat completion with web search explicitly absent. If this
provider scores ~100% on a dataset, that dataset cannot rank search providers
and should be labeled a sanity floor (see METHODOLOGY.md).

Env: OPENAI_API_KEY, optional OPENAI_BASE_URL (default https://api.openai.com/v1),
optional NOSEARCH_MODEL (default gpt-4o-mini).
"""

from __future__ import annotations

import os

from .base import ProviderError, _http, _json_body, require_env

PROMPT = ("Answer the question with just the answer, no explanation. "
          "If you do not know, reply exactly: I don't know.")


class NoSearchLLM:
    name = "nosearch"

    def __init__(self):
        self.key = require_env("OPENAI_API_KEY")
        self.base = os.environ.get("OPENAI_BASE_URL", "https://api.openai.com/v1").rstrip("/")
        self.model = os.environ.get("NOSEARCH_MODEL", "gpt-4o-mini")

    def ask(self, question: str, k: int) -> dict:
        status, _, raw = _http(
            "POST", self.base + "/chat/completions",
            {"Content-Type": "application/json", "Authorization": f"Bearer {self.key}"},
            _json_body({"model": self.model, "temperature": 0,
                        "messages": [{"role": "user", "content": f"{PROMPT}\n\n{question}"}]}),
        )
        data = json.loads(raw.decode("utf-8", "replace"))
        msg = data.get("choices", [{}])[0].get("message", {})
        usage = data.get("usage", {}) or {}
        return {"answer": msg.get("content", ""), "documents": [],
                "tokens_est": usage.get("total_tokens"),
                "server_latency_s": None, "raw": data}
