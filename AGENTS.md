# Repository Agent Safety Rules

Before changing or running the OpenAPI pipeline, read
`docs/troubleshooting.md` and reuse any verified workaround that matches the
current symptom.

- Never print, copy, commit, or include values from `.env`, API logins, access
  tokens, private profiles, captures, receipts, or mutation journals in tool
  output.
- Run live iiko calls only through the guarded project commands after their
  operation limits are marked verified.
- A `429` stops the entire live run. Do not retry and do not switch to another
  API login, including `IIKO_API_KEY_2`, until the circuit has been investigated
  and reset manually.
- Run automated test commands outside sandbox when the execution environment
  offers that choice. This does not authorize live HTTP calls.
- When a deterministic failure pattern recurs and a workaround is verified,
  add a sanitized entry to `docs/troubleshooting.md` in the same change set.
  Do not record speculation or secret-bearing output.

# Communication Style (owner's standing request)

Write to the repository owner in plain language, in Russian, so that a person
with an average technical background can follow. Do not use slang, buzzwords,
or ambiguous wording. Any unavoidable technical term (an identifier, a
mechanism name, an English word like "receipt" or "cleanup") must be explained
in the same sentence or immediately after it — what it is and what it does in
this repository. Do not leave ambiguous or double-meaning statements
unexplained. This applies to chat replies, reports, and status summaries.

