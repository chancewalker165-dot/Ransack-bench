# legacy/

v1 artifacts, preserved as-is for provenance and archaeology:

- `ransack-bench-seed.json`: the original 30+18 question seed. Its content is
  now `datasets/control_trivia.json` with aliases and honest labeling.
- `ransack-bench-results.md` / `ransack-bench-evidence.json`: the hand-run
  v1 session. Kept as the canonical example of why a bench needs a runner,
  raw transcripts, and confidence intervals.
- `ransack-bench-README.md`: the original protocol doc (note the leaked local
  paths and the "never hit ransack.tools/mcp from a script" rule that made v1
  un-rerunnable by construction).
- `concurrent_load.py`: load tester for a private token-gated endpoint
  (`/api/bench-search`, bypasses customer rate caps). Not part of bench v2;
  load testing a production search API from a public repo needs a public,
  cap-respecting profile first.

Do not extend these. Build on bench.py.
