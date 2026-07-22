---
name: updating-iikocloud-sdk
description: Use when iiko Cloud Redoc or OpenAPI changes, upstream-check reports drift, or Codex must review and apply an iikoCloud SDK regeneration in this repository.
---

# Updating the iikoCloud SDK

Turn public upstream drift into a reviewed, reproducible SDK change without
silently breaking the existing public surface or bypassing live safety gates.

## Start with repository rules

1. Work in the user's active checkout and branch. Do not create a worktree.
2. Read `AGENTS.md`, `docs/troubleshooting.md`, the relevant sections of
   `docs/generation.md`, and `docs/known-upstream-issues.md` before touching the
   pipeline.
3. Inspect `git status --short --branch`. Preserve unrelated user changes.
4. Never print or copy `.env` values, API logins, private profiles, captures,
   receipts, mutation journals, or live identifiers.

An SDK update authorizes public schema inspection and offline repository work.
It does not authorize credentialed iiko calls, write/lifecycle tests, commits,
pushes, tags, or publication. Each requires a separate explicit request.
These authority rules take precedence over release-only steps in the quick
scenario in `docs/generation.md` unless the user explicitly requests them.

## Review drift before accepting it

Prepare the locked development environment, then run only the report command:

```bash
uv sync --frozen --group dev
uv run --frozen python -m tools.openapi_pipeline upstream-check
```

Read `build/reports/upstream-diff.md` and inspect the saved public candidate.
Record the exact added, changed, and removed operations and schemas. Do not use
`sync` as a substitute for this review: `upstream-check` is report-only, while
`sync` can replace tracked generated state.

Record the SHA-256 of `build/upstream/candidate.json` after review. Networked
`sync` currently fetches upstream again; it does not accept that saved file by
identity. This digest is therefore an acceptance check, not an implementation
detail to skip.

### Stop on unapproved removals

Absence from the current Redoc/OpenAPI document is not proof that an old iiko
endpoint stopped working and is never permission to remove it from this SDK.

- Never delete an operation ID, generated public method, model, fixture,
  safety entry, or read case solely because upstream stopped advertising it.
- A general request to update or regenerate the SDK is not explicit approval
  for a breaking removal.
- Require the user to approve each operation and every transitively removed
  public method/model/schema, or approve an exact reviewed removal manifest.
- If the repository cannot compose the new upstream document with retained
  legacy operations, do not run an accepting `sync`. Report the removals and
  state that legacy-retention support must be implemented and reviewed first,
  or that the user must explicitly approve the breaking removals.
- Do not claim that legacy retention already exists. Verify the implementation
  and its regression tests before relying on it.
- Do not improvise a retention layer during a routine drift refresh. Treat a
  missing retention mechanism as a separate design and implementation change
  unless the user explicitly expands the task.

Added and changed work may be analysed while a removal is blocked, but do not
promote a generated tree that drops the blocked public surface.

## Put corrections in the right layer

Never edit `openapi/upstream/iikocloud.openapi.json` or
`src/iikocloud_client/` by hand.

| Upstream condition | Reviewed repository change |
|---|---|
| Correct new operation or model | Usually no schema correction; add required safety/catalog/read coverage |
| Bad or unstable operation name | `openapi/operation-ids.yaml` |
| Colliding or generator-invalid model name | `openapi/model-name-overrides.yaml` |
| Wrong `type`, `required`, nullable, `oneOf`, or discriminator | Guarded action in `openapi/overlays/` plus a focused contract test |
| Upstream fixed a known defect | Remove only the now-stale correction after checking the new fragment and its test |

For every defect, first add a focused failing offline test that captures the
expected public contract. Overlay actions must use the exact JSONPath,
`expected-matches`, and canonical digest. A stale guard means “review upstream
again”, never “replace the hash blindly”. Use

```bash
uv run --frozen python -m tools.openapi_pipeline bootstrap
```

only to create ignored suggestions under `build/bootstrap/`; review and move
only justified entries into tracked registries or overlays.

For a new operation, inspect the actual repository contracts and add every
applicable operation-ID mapping, safety classification, verified/unverified
rate entry, request fixture, and read case. Do not invent request values or
mark a rate limit verified from guesswork.

## Generate only after review

Accept only when the final composed effective schema and generated public API
contain no unapproved removals. A removal in raw upstream is non-blocking only
when a reviewed, tested retention mechanism restores its entire public surface.
Then apply reviewed corrections and accept the public candidate atomically:

```bash
PYTHONDONTWRITEBYTECODE=1 \
uv run --frozen python -m tools.openapi_pipeline sync
```

Recheck the resulting operation/schema inventory and the complete Git diff.
Compare the promoted `openapi/upstream/iikocloud.openapi.json` SHA-256 with the
recorded reviewed-candidate SHA-256 before further edits or tests. If they
differ, the refetch raced the review: do not commit or run live checks; stop
and classify the new report. This post-check detects the current pipeline
limitation but does not make `sync` exact-candidate acceptance. Use
`sync --offline` only to regenerate from the already tracked snapshot; it
cannot accept a new public candidate.

Do not bump the package version merely to review drift. Versioning and release
publication are separate decisions.

## Run the offline gates

For a new UV cache, run the documented package-index-only cache priming step.
Then execute the current offline job commands from
`.github/workflows/python.yml` verbatim, including:

```bash
PYTHONDONTWRITEBYTECODE=1 uv run --frozen --offline \
  python -m tools.openapi_pipeline verify
PYTHONDONTWRITEBYTECODE=1 uv run --frozen --offline \
  python -m tools.openapi_pipeline verify-no-secrets
uv run --frozen --offline ruff check --no-cache tools tests
uv run --frozen --offline mypy tools/openapi_pipeline
uv build --offline
```

Run pytest using every fresh-process partition in
`.github/workflows/python.yml`. Do not replace that partition with one
monolithic `pytest -q`; the repository records a verified native-stack failure
for the monolithic form. Ordinary offline tests and CI must not select any live
marker. State which local Python version was actually used; do not claim the
3.10/3.12 CI matrix passed locally unless both environments were really run.

When a deterministic failure recurs and its workaround is verified, add a
sanitized entry to `docs/troubleshooting.md` in the same change. Never record
speculation or secret-bearing output.

## Treat live verification as a separate operation

Do not make a live iiko call unless the user explicitly requests it. If they
do, reread the current guarded commands in `docs/generation.md` and use the
smallest exact project entrypoint that covers the changed operation.

- Use only operations whose entry in `contracts/rate-limits.yaml` is marked
  `verified: true`.
- Run serially with `-n0` and preserve the persistent global minimum of 30
  seconds between any HTTP requests, including authentication, reads, and
  writes. Make no more than one call per operation in a run. Never replace the
  guard with manual `sleep` or delete its state.
- `uv --offline` blocks package-index access; it does not block iiko HTTP.
- Never use ad-hoc `curl`, parallel workers, automatic retry, or a second login
  to accelerate testing.
- On any `429`, stop the entire live run. Do not retry, continue, switch to
  `IIKO_API_KEY_2`, delete state, or reset the circuit without a later explicit
  investigated decision.
- Do not suggest `reset-circuit`: that reserved CLI name is not implemented.
- Capture only one explicitly selected operation through the guarded capture
  command. Keep sanitized output in ignored private storage and never stage it.

Write/lifecycle execution needs separate authorization after presenting the
exact test node, profile, target class, and satisfied preflight gates from
`docs/generation.md`; ask the user to confirm that concrete run. Collection-only
checks are offline. A real lifecycle must use the repository mutation journal
and its `finally` cleanup. `finally` attempts cleanup but cannot guarantee it;
an unfinished journal blocks success and must never be deleted manually.

## Report and hand off

Return a compact report containing:

1. added, changed, removed, and blocked operations/schemas by exact name;
2. each correction and why its chosen layer is correct;
3. generation and offline-gate results;
4. whether live checks were skipped or explicitly authorized, and their safe
   result without payloads or identifiers;
5. remaining blockers and `git status`.

Leave the reviewed diff unstaged by default. If the user explicitly asks for a
commit, rerun `verify-no-secrets`, stage only named reviewed files with
`git add -- <paths>`, inspect the staged diff, rerun `verify-no-secrets` against
the final staged blobs, and create one scoped commit. Never infer permission to
push, tag, or publish from permission to commit.

## Example decision

Suppose the report contains one new operation, one changed response property,
and one missing legacy operation. Add the new operation's reviewed contracts;
write a failing contract test and guarded overlay for the incorrect property;
list the missing legacy operation as blocked and preserve its public SDK
surface. Do not accept a `sync` that removes it. Continue generation only after
a tested retention mechanism exists or the user explicitly approves that exact
breaking removal. Do not run live checks or commit unless separately asked.

## Reject these shortcuts

| Shortcut | Required response |
|---|---|
| “Redoc removed it, so delete it” | Preserve it and request exact removal approval |
| “Let `sync` decide what changed” | Run and review `upstream-check` first |
| “The overlay hash changed; refresh it” | Re-evaluate the upstream fragment and correction |
| “Use key 2 after a 429” | Stop the entire run and keep the circuit closed |
| “`uv --offline` makes this non-live” | Check the selected command and pytest marker |
| “A full `pytest -q` passed” | Run the documented fresh-process partition |
| “Update implies commit and push” | Keep those as separate authority gates |
