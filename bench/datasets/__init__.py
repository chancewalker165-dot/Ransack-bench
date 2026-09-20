"""Dataset loading + validation.

Manifests live in datasets/*.json. Two modes (see bench/schema.py):
- full: question content is committed (license permits).
- ids_only: only frozen sample ids are committed; content is materialized from
  the locally fetched full dataset in data/ and checked by sha256, so the
  freeze is reproducible without re-distributing licensed content.
"""

from __future__ import annotations

import glob
import hashlib
import json
import os

from ..schema import validate_manifest

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))  # repo root (this file lives in bench/datasets/)
DATASETS_DIR = os.path.join(ROOT, "datasets")
DATA_DIR = os.path.join(ROOT, "data")


def sha256_file(path: str) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 16), b""):
            h.update(chunk)
    return h.hexdigest()


def list_datasets() -> list[str]:
    return sorted(os.path.basename(p)[:-5] for p in glob.glob(DATASETS_DIR + "/*.json"))


def _materialize_ids_only(m: dict) -> dict:
    src = m.get("materialize_from") or ""
    path = os.path.join(DATA_DIR, src)
    if not os.path.exists(path):
        raise FileNotFoundError(
            f"dataset {m['dataset']!r} is ids_only: run scripts/fetch_datasets.py to get {path}")
    digest = sha256_file(path)
    if digest != m.get("full_dataset_sha256"):
        raise ValueError(
            f"full dataset sha mismatch for {m['dataset']!r}: manifest expects "
            f"{m.get('full_dataset_sha256')[:12]}, data/{src} is {digest[:12]}. "
            "Re-pin the manifest or re-fetch the pinned source.")
    full = json.load(open(path, encoding="utf-8"))
    by_id = {q["id"]: q for q in full.get("questions", [])}
    questions = []
    for qid in m["sample_ids"]:
        if qid not in by_id:
            raise ValueError(f"sample id {qid} not in materialized dataset {m['dataset']!r}")
        questions.append(by_id[qid])
    out = dict(m)
    out["mode"] = "full"
    out["questions"] = questions
    return out


def load_dataset(name: str) -> dict:
    path = name if os.path.exists(name) else os.path.join(DATASETS_DIR, name + ".json")
    if not os.path.exists(path):
        raise FileNotFoundError(f"unknown dataset {name!r}; known: {list_datasets()}")
    m = json.load(open(path, encoding="utf-8"))
    errs = validate_manifest(m)
    if errs:
        raise ValueError(f"manifest {path} invalid: " + "; ".join(errs))
    if m.get("mode", "full") == "ids_only":
        m = _materialize_ids_only(m)
    return m
