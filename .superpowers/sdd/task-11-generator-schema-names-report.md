# Task 11 generator schema-name normalization report

## Outcome

The existing reviewed model-name registry now physically normalizes only
generator-invalid `components.schemas` keys before strict validation. The same
stage is used by bootstrap acceptance, committed corrections, and reviewed
candidate composition. Strict OpenAPI Generator validation remains enabled.

## TDD evidence

- RED: `pytest -q tests/pipeline/test_naming.py -k generator_invalid` failed
  8 tests because the requested pure helper did not exist.
- RED: the two pipeline-path regressions and the reviewed-candidate regression
  failed because the invalid source key remained in the effective document.
- RED follow-up: two focused regressions proved that a percent-encoded fragment
  marker and literal `$ref`-shaped JSON under schema data/vendor extensions were
  being rewritten as semantic references.
- GREEN: the complete affected files passed in separate offline processes:
  40 naming tests, 38 pipeline tests, and 15 reviewed-candidate tests. Reference
  rewriting now consumes the existing path/context-aware structural-reference
  iterator, while real refs below a property named `example` and the `default`
  response key remain covered.
- Public offline composition reported 10 renamed keys, 11 rewritten exact local
  references, 0 remaining old references, and 0 invalid effective schema keys.
- Exact source Ruff and mypy checks passed. The existing broad test-file mypy
  baseline still reports unrelated historical typing findings, so it was not
  weakened or bulk-edited in this task.

## Changed files

- `tools/openapi_pipeline/naming.py`
- `tools/openapi_pipeline/pipeline.py`
- `tests/pipeline/test_naming.py`
- `tests/pipeline/test_pipeline.py`
- `tests/pipeline/test_reviewed_candidate.py`
- `.superpowers/sdd/task-11-generator-schema-names-report.md`

## Commit

Initial implementation: `1c27585 fix: normalize generator-invalid schema names`.
One focused follow-up commit covers the two final review findings; its object ID
is recorded in the controller handoff because a commit cannot contain its own
hash.

## Concerns

Docker validation, generation, bootstrap acceptance, private data, and live API
operations were intentionally not run. The controller owns the pinned Docker
validation and any resulting verified troubleshooting-ledger entry after
reviewing this commit.
