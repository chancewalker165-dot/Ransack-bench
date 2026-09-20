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


FORMAT_SUFFIX = ("\n\nEnd your reply with exactly one word on the last line: "
                 "CORRECT, INCORRECT, or NOT_ATTEMPTED.")


def judge_grade(question: str, target: str, predicted_answer: str) -> str:
    base = os.environ.get("JUDGE_BASE_URL", os.environ.get("OPENAI_BASE_URL", "https://api.openai.com/v1")).rstrip("/")
    model = os.environ.get("JUDGE_MODEL", os.environ.get("NOSEARCH_MODEL", "gpt-4o"))
    key = require_env("OPENAI_API_KEY")
    # The official template is used verbatim plus a one-line output-format
    # suffix (disclosed in METHODOLOGY.md): thinking models otherwise spend
    # their reply on reasoning and never emit the grade word in `content`.
    prompt = load_template().format(
        question=question, target=target, predicted_answer=predicted_answer) + FORMAT_SUFFIX
    _, _, raw = _http(
        "POST", base + "/chat/completions",
        {"Content-Type": "application/json", "Authorization": f"Bearer {key}"},
        _json_body({"model": model, "temperature": 0,
                    "messages": [{"role": "user", "content": prompt}]}),
    )
    data = json.loads(raw.decode("utf-8", "replace"))
    msg = data.get("choices", [{}])[0].get("message", {})
    verdicts = {"CORRECT": "CORRECT", "INCORRECT": "WRONG", "NOT_ATTEMPTED": "ABSTAIN"}
    content = msg.get("content") or ""
    m = re.search(r"\b(CORRECT|INCORRECT|NOT_ATTEMPTED)\b", content)
    if m:
        return verdicts[m.group(1)]
    # thinking models: the verdict often lands in the reasoning channel
    reasoning = msg.get("reasoning") or ""
    hits = re.findall(r"\b(CORRECT|INCORRECT|NOT_ATTEMPTED)\b", reasoning, re.I)
    if hits:
        return verdicts[hits[-1].upper()]
    return "JUDGE_ERROR"


def judge_available() -> bool:
    return bool(os.environ.get("OPENAI_API_KEY")) and os.path.exists(PROMPT_FILE)
