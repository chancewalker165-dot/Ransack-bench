"""Manifest schema + validation for bench v2 datasets.

Two manifest modes:
- full      (default): "questions" is a list of frozen question objects.
- ids_only  : "sample_ids" lists frozen question ids; the full source dataset
              (fetched into data/ by scripts/fetch_datasets.py) is materialized
              locally and checked against "full_dataset_sha256". Used when the
              upstream license does not permit re-distribution of content.

Every question in a full manifest carries:
  id, question, expected, aliases[], and optionally
  verified_as_of (ISO date the expected answer was last checked against
  primary sources), source_urls[], unverified (bool), notes, recency (bool).

Datasets may set top-level "role" ("sanity_floor" or "benchmark") and
"non_discriminative" (true means: expect ~100% scores everywhere, exists to
catch pipeline breakage, not to rank providers).
"""

from __future__ import annotations

import re

GRADERS = ("alias_exact", "simpleqa_judge")
MODES = ("full", "ids_only")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def _check_date(val: str, where: str, errs: list) -> None:
    if not isinstance(val, str) or not DATE_RE.match(val):
        errs.append(f"{where}: expected ISO date (YYYY-MM-DD), got {val!r}")


def validate_manifest(m: dict) -> list[str]:
    """Return a list of schema errors (empty list = valid)."""
    errs: list[str] = []

    for key in ("dataset", "sample_id", "seed", "frozen_on", "source", "grader"):
        if key not in m:
            errs.append(f"missing top-level key: {key}")
    if errs:
        return errs

    if m["grader"] not in GRADERS:
        errs.append(f"grader must be one of {GRADERS}, got {m['grader']!r}")
    _check_date(m["frozen_on"], "frozen_on", errs)
    if not isinstance(m["seed"], int):
        errs.append("seed must be an int")

    src = m.get("source") or {}
    for key in ("url", "license", "fetched"):
        if key not in src:
            errs.append(f"source missing key: {key}")
    _check_date(src.get("fetched", ""), "source.fetched", errs)

    mode = m.get("mode", "full")
    if mode not in MODES:
        errs.append(f"mode must be one of {MODES}, got {mode!r}")
        return errs

    if mode == "full":
        qs = m.get("questions")
        if not isinstance(qs, list) or not qs:
            errs.append("mode=full requires a non-empty questions list")
            return errs
        ids = set()
        for q in qs:
            qid = q.get("id", "?")
            for key in ("id", "question", "expected"):
                if key not in q or not str(q.get(key, "")).strip():
                    errs.append(f"question {qid}: missing/empty {key}")
            if q.get("id") in ids:
                errs.append(f"duplicate question id: {q.get('id')}")
            ids.add(q.get("id"))
            if not isinstance(q.get("aliases", []), list):
                errs.append(f"question {qid}: aliases must be a list")
            if "verified_as_of" in q:
                _check_date(q["verified_as_of"], f"question {qid}.verified_as_of", errs)
            if "source_urls" in q and not isinstance(q["source_urls"], list):
                errs.append(f"question {qid}: source_urls must be a list")
    else:
        ids = m.get("sample_ids")
        if not isinstance(ids, list) or not ids:
            errs.append("mode=ids_only requires a non-empty sample_ids list")
        if not m.get("full_dataset_sha256"):
            errs.append("mode=ids_only requires full_dataset_sha256 of the fetched source file")

    return errs
