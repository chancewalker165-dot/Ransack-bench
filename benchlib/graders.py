"""Deterministic grading with span evidence.

Honesty rules this module enforces (v2 redesign of the v1 "contains it" rule):

1. For document-returning providers (search APIs) the primary metric is
   retrieval HIT: the expected fact or an alias appears in the returned
   documents. This is explicitly labeled hit-rate, not answer accuracy.
2. For answer-returning providers (sonar, answer endpoints, no-search LLM)
   the returned answer is additionally graded CORRECT / WRONG / ABSTAIN.
3. Abstentions never count as CORRECT; they are counted separately.
4. Every verdict records WHERE the match landed and a normalized context
   snippet, so any grade is auditable after the fact (v1 recorded nothing).

No LLM judge runs in this module. The optional SimpleQA judge lives in
bench/graders_judge.py and is only a published cross-check.
"""

from __future__ import annotations

import re
import unicodedata

# Phrases that signal an abstaining answer. Abstains are never CORRECT.
NEG_PATTERNS = [
    r"\bi (?:don't|do not|can't|cannot) know\b",
    r"\bnot sure\b",
    r"\b(?:unable|unable) to determine\b",
    r"\bcannot (?:determine|verify|find)\b",
    r"\bno (?:clear|definitive) answer\b",
    r"\binsufficient (?:information|evidence)\b",
    r"\bnot enough evidence\b",
    r"\bcannot be derived\b",
    r"\bunknown\b",
]

_NUMBERS = {
    "zero": "0", "one": "1", "two": "2", "three": "3", "four": "4",
    "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9",
    "ten": "10", "eleven": "11", "twelve": "12", "thirteen": "13",
    "fourteen": "14", "fifteen": "15", "sixteen": "16", "seventeen": "17",
    "eighteen": "18", "nineteen": "19", "twenty": "20",
}
_ARTICLES = {"the", "a", "an"}
_PUNCT_RE = re.compile(r"[^a-z0-9]+")
_WS_RE = re.compile(r"\s+")


def normalize(text: str) -> str:
    """Lowercase, strip accents/punctuation/articles, map number words."""
    s = unicodedata.normalize("NFKD", str(text)).encode("ascii", "ignore").decode()
    s = s.lower()
    s = _PUNCT_RE.sub(" ", s)
    tokens = [_NUMBERS.get(t, t) for t in s.split() if t and t not in _ARTICLES]
    return " ".join(_WS_RE.sub(" ", " ".join(tokens)).split())


def is_abstain(text: str) -> bool:
    t = str(text or "").lower()
    return any(re.search(p, t) for p in NEG_PATTERNS)


def _doc_text(doc: dict) -> str:
    return " ".join(str(doc.get(key) or "") for key in ("title", "url", "text", "content"))


def _find(candidate_norm: str, texts: list[tuple[str, str]]) -> tuple[bool, str, str]:
    """Return (found, where, context) for the first containment match."""
    if not candidate_norm:
        return False, "", ""
    for where, text in texts:
        norm = normalize(text)
        idx = norm.find(candidate_norm)
        if idx >= 0:
            lo, hi = max(0, idx - 50), min(len(norm), idx + len(candidate_norm) + 50)
            return True, where, norm[lo:hi]
    return False, "", ""


def grade_item(item: dict, result: dict) -> dict:
    """Grade one provider result against one seed question.

    Returns a dict with:
      hit              bool   - expected fact (or alias) present in output
      matched_alias    str    - which candidate string matched
      hit_where        str    - "answer" | "<doc url/title>" | ""
      hit_context      str    - normalized snippet around the match
      answer_verdict   str    - CORRECT / WRONG / ABSTAIN / "" (no answer field)
      abstain          bool
    """
    candidates = [item["expected"]] + list(item.get("aliases", []))

    texts: list[tuple[str, str]] = []
    answer = result.get("answer")
    if answer:
        texts.append(("answer", answer))
    for doc in result.get("documents", []):
        label = doc.get("url") or doc.get("title") or "doc"
        texts.append((str(label), _doc_text(doc)))

    matched_alias, hit_where, hit_context = "", "", ""
    hit = False
    for cand in candidates:
        ok, where, ctx = _find(normalize(cand), texts)
        if ok:
            hit, matched_alias, hit_where, hit_context = True, cand, where, ctx
            break

    out = {
        "hit": hit,
        "matched_alias": matched_alias if hit else "",
        "hit_where": hit_where,
        "hit_context": hit_context,
        "answer_verdict": "",
        "abstain": False,
    }

    if answer:
        abstain = is_abstain(answer)
        out["abstain"] = abstain
        if hit and hit_where == "answer":
            out["answer_verdict"] = "CORRECT"
        elif abstain:
            out["answer_verdict"] = "ABSTAIN"
        else:
            out["answer_verdict"] = "WRONG"
    return out
