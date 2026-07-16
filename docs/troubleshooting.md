# Pipeline Troubleshooting Ledger

Read this file before running generation or live commands. Add an entry only
after the root cause and workaround are verified. Sanitize commands and output;
never include `.env` values, API logins, tokens, private payloads, or raw
captures.

| Date | Sanitized command/context | Symptom | Root cause | Safe workaround | Prevention | Verification |
|---|---|---|---|---|---|---|
| 2026-07-16 | `uv run pytest -q` in a fresh checkout, without live arguments | `pytest` executable could not be spawned | The generated project declared Poetry dev dependencies, but no PEP 735 `dependency-groups.dev` for `uv sync` | Use an isolated `uvx` pytest only to observe TDD RED, then add and sync the explicit dev group | Keep test tooling in `[dependency-groups].dev` and use `uv sync --frozen --group dev` in CI | `uv sync --group dev` installed pytest and the focused Task 1 suite passed |
| 2026-07-16 | `uv sync --group dev` after adding pytest 9 | Resolver rejected the Python 3.9 split although the active interpreter was 3.12 | `uv` resolves every version admitted by `project.requires-python`; pytest 9 requires Python 3.10+ while the legacy metadata admitted 3.9 | Raise `project.requires-python` to the already selected SDK minimum, Python 3.10 | Keep runtime support metadata aligned with generator and development-tool requirements | Resolution completed with 53 packages and the focused Task 1 suite passed |
| 2026-07-16 | Cached `sdd-workspace` and `task-brief` helper scripts invoked directly | `Permission denied` before helper startup | The cached scripts had mode `0644` despite bash shebangs, so direct execution lacked execute permission | Invoke each helper as `bash SCRIPT ...`; after `bash sdd-workspace ...`, invoke `bash task-brief ... OUTPUT_PATH` explicitly because the workspace helper's nested direct call has the same mode assumption | Avoid direct execution of cached SDD helpers and always pass an explicit task-brief output path | `stat` confirmed mode `0644`; explicit `bash` invocations created the workspace metadata and task brief |
