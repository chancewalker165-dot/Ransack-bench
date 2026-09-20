"""Optional SimpleQA judge cross-check using the OFFICIAL grader prompt.

This is the only LLM-based grading in bench v2, and it is deliberately:
- opt-in per dataset (manifest grader = "simpleqa_judge")
- never the primary metric for search lanes (hit-rate is)
- a published, verbatim, attributed prompt (bench/grader_prompts/simpleqa_grader.txt)
  from openai/simple-evals (MIT), so anyone can audit exactly what the judge sees

Official mapping: CORRECT / INCORRECT / NOT_ATTEMPTED. We map
NOT_ATTEMPTED -> ABSTAIN (never counted as correct), CORRECT -> CORRECT,
INCORRECT -> WRONG.

Requires OPENAI_API_KEY (judge endpoint is OpenAI-compatible; override with
JUDGE_BASE_URL + JUDGE_MODEL).
"""

from __future__ import annotations

import json
import os
import re

from .providers.base import _http, _json_body, require_env

PROMPT_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "grader_prompts", "simpleqa_grader.txt")


def load_template() -> str:
    with open(PROMPT_FILE, encoding="utf-8") as fh:
        return fh.read()


def judge_grade(question: str, target: str, predicted_answer: str) -> str:
    base = os.environ.get("JUDGE_BASE_URL", os.environ.get("OPENAI_BASE_URL", "https://api.openai.com/v1")).rstrip("/")
    model = os.environ.get("JUDGE_MODEL", os.environ.get("NOSEARCH_MODEL", "gpt-4o"))
    key = require_env("OPENAI_API_KEY")
    prompt = load_template().format(
        question=question, target=target, predicted_answer=predicted_answer)
    _, _, raw = _http(
        "POST", base + "/chat/completions",
        {"Content-Type": "application/json", "Authorization": f"Bearer {key}"},
        _json_body({"model": model, "temperature": 0,
                    "messages": [{"role": "user", "content": prompt}]}),
    )
    data = json.loads(raw.decode("utf-8", "replace"))
    text = data.get("choices", [{}])[0].get("message", {}).get("content", "")
    m = re.search(r"\b(CORRECT|INCORRECT|NOT_ATTEMPTED)\b", text)
    if not m:
        return "JUDGE_ERROR"
    return {"CORRECT": "CORRECT", "INCORRECT": "WRONG", "NOT_ATTEMPTED": "ABSTAIN"}[m.group(1)]


def judge_available() -> bool:
    return bool(os.environ.get("OPENAI_API_KEY")) and os.path.exists(PROMPT_FILE)
