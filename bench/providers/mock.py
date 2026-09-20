"""Deterministic offline provider for CI smoke tests. Never use for real runs."""

from __future__ import annotations


class MockProvider:
    name = "mock"

    def ask(self, question: str, k: int) -> dict:
        docs = [
            {"title": "mock result 1", "url": "https://example.invalid/1", "text": "generic fixture text"},
            {"title": "mock result 2", "url": "https://example.invalid/2", "text": "Canberra is mentioned here for pipeline testing"},
        ][: max(1, min(k, 2))]
        answer = "Canberra" if "capital of australia" in question.lower() else "mock answer"
        return {"answer": answer, "documents": docs, "tokens_est": 42,
                "server_latency_s": None, "raw": {"fixture": True, "question": question}}
