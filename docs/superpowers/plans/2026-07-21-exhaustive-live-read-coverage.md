# Exhaustive Guarded Live Read Coverage Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a fail-closed, exhaustive and sequential live-read verification path for all 91 reviewed non-mutating operations in the current 225-operation iiko Cloud effective OpenAPI document.

**Architecture:** Keep semantic classification, executable HTTP allowlisting, test cadence/server limits, and typed `ReadCase` code as four independent permissions. A deterministic dependency planner runs one authenticated generated-SDK session, keeps discovered targets only in process memory, records credential-free private outcomes, and stops globally on any unsafe transport, deserialization, rate-state, receipt, or `429` condition. Operations that need an entity unavailable from the profile or another read return a reviewed `no_live_target` result before rate acquisition and HTTP.

**Tech Stack:** Python 3.10+, Pydantic 2, PyYAML, pytest 9, pytest-asyncio, generated async `iikocloud_client`, existing `LiveRateGuard`/`SafeLiveSession`/capture/receipt infrastructure, Ruff, mypy, uv.

## Global Constraints

- Work only in `/home/ivan/programming/Iikocloud-py-sdk` on the active `feat/iikocloud-generation-pipeline` branch; do not create or use a Git worktree.
- Run every shell command directly in the host environment, never in a Codex sandbox. `uv run --offline` means dependency resolution is offline; it does not sandbox the process and does not suppress iiko HTTP.
- Read `docs/troubleshooting.md` before pipeline changes and reuse its verified workarounds. Run commands with `PYTHONDONTWRITEBYTECODE=1`; split long offline pytest suites into fresh processes if the documented monolithic-run crash pattern recurs.
- Never read or print `.env`, private profiles, API logins, access tokens, private captures, receipts, reports, identifiers, or mutation journals in tool output.
- No task before Task 20 may make live HTTP calls. Offline tests must use fake clocks, fake transports, synthetic generated models, and temporary directories.
- Every live HTTP request, including authentication, is serialized through one held canonical process lock and one persistent `LiveRateGuard`; the global interval is at least 30 seconds and a known stricter operation interval wins.
- Each operation may be acquired at most once per run. There is no automatic retry, parallel HTTP, cleanup request, or fallback to `IIKO_API_KEY_2`.
- Any `429`, including during authentication, stops the entire run, opens the profile-global persistent circuit, leaves the receipt incomplete, and forbids retry or API-login switching until a human investigates and resets the circuit.
- The full-read stage executes no create, update, delete, action, irreversible, compensating, or cleanup operation.
- Generated files under `src/iikocloud_client/api/` and `src/iikocloud_client/models/` are never hand-edited. Confirmed schema defects go through operation-ID overrides, guarded overlays, model-name overrides, synthetic fixtures, and complete regeneration.
- Private reports and captures stay below ignored `private/` roots with directories mode `0700`, files mode `0600`, one owner, one hard link, no symlink traversal, no overwrite of an unrelated artifact, and atomic publication.
- A report never contains request/response bodies, headers, URLs with query strings, raw exception text, API logins, tokens, UUID targets, phone/email values, customer/order/menu content, or profile values.
- If a deterministic failure pattern recurs and a workaround is verified, add a sanitized entry to `docs/troubleshooting.md` in the same change set. Do not record speculation.
- Lifecycle tests, automatic write execution, owned test-entity creation, compensation stacks, mutation-journal expansion, and the repository-local update skill are separate later plans.

---

## Scope and file map

This is one cohesive deliverable: the catalog, rate contract, typed cases, planner, runner, report, pytest gates, and final guarded run are mutually dependent. Lifecycle/write orchestration remains a separate subsystem and is not folded into this plan.

### New hand-owned files

| Path | Responsibility |
|---|---|
| `contracts/operation-safety.yaml` | Human-reviewed `effect` and `live_policy` for exactly 225 effective operation IDs. |
| `tools/openapi_pipeline/live/contract_io.py` | Strict bounded UTF-8 YAML loading, duplicate-key rejection, exact-key and safe-string helpers shared by live contracts. |
| `tools/openapi_pipeline/live/safety.py` | Safety enums/catalog parsing, policy-matrix validation, OpenAPI parity, and canonical catalog hash. |
| `tools/openapi_pipeline/live/read_case.py` | Immutable bindings/cases, safe context, `NO_REQUEST`, no-target/failure reason enums, and generated request construction. |
| `tools/openapi_pipeline/live/read_planner.py` | Registry validation, deterministic DAG ordering, dependency closure, and canonical registry descriptor hash. |
| `tools/openapi_pipeline/live/read_report.py` | Strict credential-free report model and private atomic report writer. |
| `tools/openapi_pipeline/live/read_runner.py` | Sequential case coordinator and continuation/abort policy. |
| `tests/integration/read/cases/__init__.py` | Exact 91-case registry assembled from domain modules. |
| `tests/integration/read/cases/foundation.py` | Organizations, terminals, dictionaries, marketing, command, webhook cases. |
| `tests/integration/read/cases/addresses.py` | Region/city/street cases. |
| `tests/integration/read/cases/menu.py` | Nomenclature, combo, stop-list and external-menu cases. |
| `tests/integration/read/cases/deliveries.py` | Delivery retrieval/restriction/draft cases. |
| `tests/integration/read/cases/reserves_orders.py` | Reserve, restaurant-section and table-order cases. |
| `tests/integration/read/cases/employees.py` | Courier, employee and personal-session read cases. |
| `tests/integration/read/cases/loyalty.py` | Loyalty, customer, coupon, message and report read cases. |
| `tests/integration/read/cases/finance.py` | Finance lists/gets/transaction cases. |
| `tests/integration/read/cases/inventory.py` | Inventory lists/gets/counteragent/cost-price cases. |
| `tests/integration/read/test_all_reads.py` | Exact full-run orchestration test. |
| `tests/integration/read/test_selected_read.py` | Exact one-operation diagnostic/capture entrypoint plus required dependency closure. |
| `tests/live_support/test_operation_safety.py` | Strict safety-catalog and 225-operation parity tests. |
| `tests/live_support/test_read_case.py` | Binding/context/request/no-target unit tests. |
| `tests/live_support/test_read_planner.py` | DAG, registry parity, closure and stable-order tests. |
| `tests/live_support/test_read_report.py` | Report schema, leakage, permissions and filesystem attack tests. |
| `tests/live_support/test_read_runner.py` | Fake-transport runner success/failure/abort tests. |
| `tests/live_support/read_cases/test_foundation.py` | Offline foundation/address case contract tests. |
| `tests/live_support/read_cases/test_menu.py` | Offline menu case contract tests. |
| `tests/live_support/read_cases/test_deliveries.py` | Offline delivery/draft case contract tests. |
| `tests/live_support/read_cases/test_reserves_orders.py` | Offline reserve/table-order case contract tests. |
| `tests/live_support/read_cases/test_employees.py` | Offline employee case contract tests. |
| `tests/live_support/read_cases/test_loyalty.py` | Offline loyalty/customer case contract tests. |
| `tests/live_support/read_cases/test_finance.py` | Offline finance case contract tests. |
| `tests/live_support/read_cases/test_inventory.py` | Offline inventory case contract tests. |

### Existing files changed

| Path | Change |
|---|---|
| `contracts/live-operations.yaml` | Add exact method/path entries for all 91 reviewed reads; retain current guarded write entries without enabling them. |
| `contracts/rate-limits.yaml` | Migrate to version 2 with separate reviewed `test_budget` and optional documented `server_limit`. |
| `src/iikocloud_client/_contracts/rate-limits.yaml` | Exact packaged copy of the canonical version-2 rate contract. |
| `tools/openapi_pipeline/paths.py` | Add exact safety/live/rate contract paths. |
| `tools/openapi_pipeline/pipeline.py` | Require safety-catalog/OpenAPI parity in real sync and verify validation. |
| `tools/openapi_pipeline/live/rates.py` | Parse version 2 and compute the maximum safe interval. |
| `tools/openapi_pipeline/live/profile.py` | Allow a read-only profile to resolve a terminal-group target without resolving a write product. |
| `tools/openapi_pipeline/live/generated.py` | Replace caller-supplied arbitrary read callbacks with exact generated bindings; normalize failures; return status/duration. |
| `tools/openapi_pipeline/live/pytest_support.py` | Preflight the selected plan/catalog/contracts before private/env/network access. |
| `tools/openapi_pipeline/live/receipt.py` | Bind receipts to a hash of all three live contracts and require the report gate for exhaustive reads. |
| `tools/openapi_pipeline/publish.py` | Select only a completed receipt matching the current live-contract hash. |
| `tools/openapi_pipeline/live/__init__.py` | Export stable live-read types only. |
| `tests/conftest.py` | Add full/selected gates, report and capture wiring, seed context, and teardown completion requirements. |
| `tests/integration/read/test_organizations.py` | Route the smoke canary through the bound generated call API. |
| `tests/live_support/test_rates.py` | Version-2 parsing and interval tests. |
| `tests/live_support/test_profile.py` | Read terminal/write-product separation tests. |
| `tests/live_support/test_generated_adapter.py` | Bound endpoint, normalized error, capture and one-call tests. |
| `tests/live_support/test_live_sdk_fixture.py` | Fixture/report/capture lifecycle tests. |
| `tests/live_support/test_pytest_gates.py` | Exact full/selected invocation and pre-private preflight tests. |
| `tests/live_support/test_receipt.py` | Live-contract hash and report completion tests. |
| `tests/live_support/test_write_gates.py` | Keep existing write behavior compatible with rate version 2. |
| `tests/live_support/test_session.py` | Rate version-2 fixtures and `429` invariants. |
| `tests/live_support/test_circuit.py` | Rate version-2 fixtures and global circuit checks. |
| `tests/pipeline/test_generator.py` | Assert the packaged rate copy remains exact. |
| `tests/pipeline/test_ci_workflows.py` | Assert selected-read marker exclusion and no live CI command. |
| `tests/publish/test_publish.py` | Require current live-contract hash when selecting a completed receipt. |
| `pyproject.toml` | Register and default-exclude `live_read_selected`. |
| `docs/generation.md` | Full/selected commands, flag meanings, duration, statuses, `429`, and triage instructions. |
| `private/README.md` | Private report/capture locations and safe profile target semantics. |
| `config/live-profile.example.toml` | Explain optional read terminal and write-only product fields. |

## Stable interfaces used by all tasks

The following names are fixed for the plan. Later tasks must import these exact names rather than introduce competing variants.

```python
# tools/openapi_pipeline/live/safety.py
class OperationEffect(str, Enum):
    AUTH = "auth"
    READ = "read"
    CREATE = "create"
    UPDATE = "update"
    DELETE = "delete"
    ACTION = "action"
    IRREVERSIBLE = "irreversible"
    UNKNOWN = "unknown"

class LivePolicy(str, Enum):
    AUTOMATIC = "automatic"
    LIFECYCLE_ONLY = "lifecycle_only"
    MANUAL_ONLY = "manual_only"
    BLOCKED = "blocked"

@dataclass(frozen=True, slots=True)
class SafetyOperation:
    operation_id: str
    effect: OperationEffect
    live_policy: LivePolicy
    reason: str

@dataclass(frozen=True, slots=True)
class OperationSafetyCatalog:
    operations: Mapping[str, SafetyOperation]
    sha256: str
```

Its exact callable surface is `load(path: Path) -> OperationSafetyCatalog`, `assert_matches_openapi(document: dict[str, Any]) -> None`, `require_automatic_read(operation_id: str) -> SafetyOperation`, and the `automatic_read_ids: tuple[str, ...]` property.

```python
# tools/openapi_pipeline/live/read_case.py
class NoLiveTargetCode(str, Enum):
    CITY = "city_unavailable"
    STREET = "street_unavailable"
    TERMINAL_GROUP = "terminal_group_unavailable"
    PRODUCT = "product_unavailable"
    COMBO = "combo_unavailable"
    DELIVERY = "delivery_unavailable"
    DELIVERY_PHONE = "delivery_phone_unavailable"
    DELIVERY_REVISION = "delivery_revision_unavailable"
    DRAFT = "draft_unavailable"
    RESERVE = "reserve_unavailable"
    RESTAURANT_SECTION = "restaurant_section_unavailable"
    TABLE = "table_unavailable"
    TABLE_ORDER = "table_order_unavailable"
    EMPLOYEE = "employee_unavailable"
    EMPLOYEE_ROLE = "employee_role_unavailable"
    SMS = "sms_unavailable"
    COMMAND = "command_unavailable"
    COUPON_SERIES = "coupon_series_unavailable"
    COUPON = "coupon_unavailable"
    CUSTOMER = "customer_unavailable"
    DOCUMENT = "document_unavailable"
    ACCOUNT = "account_unavailable"
    STORE = "store_unavailable"

class ReadFailureCode(str, Enum):
    DEPENDENCY_FAILED = "dependency_failed"
    ASSERTION_FAILED = "assertion_failed"
    EXTRACTOR_FAILED = "extractor_failed"
    INVOCATION_FAILED = "invocation_failed"
    HTTP_ERROR = "http_error"
    TRANSPORT_ERROR = "transport_error"
    RATE_GUARD_FAILED = "rate_guard_failed"
    RECEIPT_FAILED = "receipt_failed"
    REPORT_FAILED = "report_failed"
    CAPTURE_FAILED = "capture_failed"
    CANCELLED = "cancelled"
    SAFETY_INVARIANT = "safety_invariant"

@dataclass(frozen=True, slots=True)
class GeneratedReadBinding:
    api_module: str
    api_class: str
    method_name: str
    request_module: str | None
    request_class: str | None
    request_keyword: str | None

@dataclass(frozen=True, slots=True)
class NoRequest:
    pass

NO_REQUEST = NoRequest()

@dataclass(frozen=True, slots=True)
class ReadCase:
    operation_id: str
    revision: int
    depends_on: tuple[str, ...]
    requires: tuple[str, ...]
    provides: tuple[str, ...]
    allowed_no_target_codes: frozenset[NoLiveTargetCode]
    binding: GeneratedReadBinding
    build_values: Callable[[ContextView], Mapping[str, object] | NoRequest]
    validate_response: Callable[[object, ContextView], None]
    extract: Callable[[object, ContextView], Mapping[str, object]]
```

`GeneratedReadBinding.method_name` is always exactly `<operation_id>_with_http_info`. A no-body operation has all three request fields set to `None` and `build_values` returns the immutable `NO_REQUEST`. A body operation uses the exact request model and keyword in Appendix B; the runner builds it with `model_validate`, so arbitrary JSON never reaches the generated API method.

`ReadContext.seed(values: Mapping[str, object]) -> ReadContext` copies values without exposing them in repr. `ReadContext.view(keys: tuple[str, ...]) -> ContextView` exposes only declared keys; absent declared keys remain absent so a builder can choose among multiple read-only providers and emit a fixed no-target code. `ReadContext.apply(case: ReadCase, extracted: Mapping[str, object]) -> None` accepts only keys declared in `case.provides`. The fixed `READ_SEED_KEYS` are `profile_organization_id`, `profile_external_menu_id`, `profile_terminal_group_id`, `date_yyyy_mm_dd`, `period_from_yyyy_mm_dd`, `period_to_yyyy_mm_dd`, `window_from_local`, and `window_to_local`.

```python
# tools/openapi_pipeline/live/read_planner.py
@dataclass(frozen=True, slots=True)
class ReadPlan:
    cases: tuple[ReadCase, ...]
    ordered_operation_ids: tuple[str, ...]
    registry_sha256: str
```

Its exact constructors are `ReadPlan.build(cases: Iterable[ReadCase]) -> ReadPlan` and `dependency_closure(operation_id: str) -> ReadPlan`.

```python
# tools/openapi_pipeline/live/read_report.py outcome types
class ReadStatus(str, Enum):
    PASSED = "passed"
    NO_LIVE_TARGET = "no_live_target"
    FAILED = "failed"
    ABORTED = "aborted"

@dataclass(frozen=True, slots=True)
class ReadOutcome:
    operation_id: str
    method: str
    path: str
    status: ReadStatus
    reason: str | None
    http_status: int | None
    duration_ms: int | None

# tools/openapi_pipeline/live/read_runner.py summary type
@dataclass(frozen=True, slots=True)
class ReadRunSummary:
    outcomes: tuple[ReadOutcome, ...]
    passed: int
    no_live_target: int
    failed: int
    aborted: int
    success: bool
```

The exact coroutine signature is:

```text
run_read_plan(
    plan: ReadPlan,
    *,
    context: ReadContext,
    sdk: GeneratedLiveSdk,
    operation_contract: Mapping[str, LiveOperation],
    report: ReadReportWriter,
) -> Awaitable[ReadRunSummary]
```

### Task 1: Add the strict exhaustive operation-safety catalog

**Files:**
- Create: `tools/openapi_pipeline/live/contract_io.py`
- Create: `tools/openapi_pipeline/live/safety.py`
- Create: `contracts/operation-safety.yaml`
- Create: `tests/live_support/test_operation_safety.py`
- Modify: `tools/openapi_pipeline/paths.py`
- Modify: `tools/openapi_pipeline/pipeline.py`
- Modify: `tests/pipeline/test_pipeline.py`

**Interfaces:**
- Consumes: `build/openapi/effective.json`, `tools.openapi_pipeline.io.canonical_json_bytes`, `sha256_bytes`.
- Produces: `OperationSafetyCatalog.load(path)`, `assert_matches_openapi(document)`, `automatic_read_ids`, and `RepoPaths.operation_safety`.

- [ ] **Step 1: Write strict-parser and policy-matrix tests**

Add tests that use this minimal valid mapping and mutate one invariant at a time:

```python
VALID = {
    "version": 1,
    "operations": {
        "authenticate": {
            "effect": "auth",
            "live_policy": "automatic",
            "reason": "current single-session token endpoint",
        },
        "get_organizations": {
            "effect": "read",
            "live_policy": "automatic",
            "reason": "reviewed non-mutating organization query",
        },
        "create_delivery_order": {
            "effect": "create",
            "live_policy": "lifecycle_only",
            "reason": "requires an owned order and compensation",
        },
        "authenticate_v2": {
            "effect": "auth",
            "live_policy": "blocked",
            "reason": "requires a separate session contract migration",
        },
    },
}
```

Cover: invalid UTF-8; file over 1 MiB; YAML duplicate key; root/entry extra or missing key; unsafe operation ID; invalid enum; empty/control-character/UUID/email/token-like reason; `unknown` with non-`blocked`; `automatic` on create/update/delete/action/irreversible; auth automatic on anything except `authenticate`; immutable returned mapping; stable canonical hash; duplicate/missing/extra OpenAPI operation IDs.

- [ ] **Step 2: Run the focused test and verify RED**

Run:

```bash
PYTHONDONTWRITEBYTECODE=1 uv run --frozen --offline pytest -q \
  tests/live_support/test_operation_safety.py
```

Expected: collection fails because `tools.openapi_pipeline.live.safety` does not exist.

- [ ] **Step 3: Implement strict contract I/O and catalog parsing**

Implement `load_yaml_mapping(path, *, label, maximum_bytes)`, `exact_keys`, `safe_identifier`, `safe_source`, and `safe_review_reason` in `contract_io.py`. `safe_source` accepts 1–256 trimmed printable characters. `safe_review_reason` applies the same length/printability rules and additionally rejects UUID, email, bearer/JWT, API-key/token assignment, newline, and control-character patterns.

Implement the stable interfaces above in `safety.py`. Build the OpenAPI operation-ID set only from the eight HTTP methods in `inventory.HTTP_METHODS`, reject duplicate or missing IDs, compare exact sets, and calculate `sha256` from canonical JSON of the parsed version and sorted entries rather than YAML formatting.

- [ ] **Step 4: Populate all 225 reviewed entries**

Create `contracts/operation-safety.yaml` from the exact classification ledger in Appendix A. Use one explicit mapping entry per operation; do not use YAML anchors, merge keys, inferred prefixes, HTTP verbs, tags, or restriction-group names. All 91 operations in Appendix B are `effect: read`, `live_policy: automatic`. Use `authenticate/auth/automatic`, `authenticate_v2/auth/blocked`, and the exact write partitions in Appendix A.

- [ ] **Step 5: Gate real pipeline validation**

Add:

```python
def _validate_effective_for_pipeline(paths: RepoPaths, document: dict[str, Any]) -> None:
    ensure_valid_effective_schema(document, require_iikocloud_contracts=True)
    OperationSafetyCatalog.load(paths.operation_safety).assert_matches_openapi(document)
```

Wire it only as the `validate` callback returned by `default_dependencies`, so injected synthetic `PipelineDependencies` tests stay isolated while real `sync` and `verify` fail before generation when upstream adds, removes, renames, or duplicates an operation.

- [ ] **Step 6: Verify count/parity and commit**

Run:

```bash
PYTHONDONTWRITEBYTECODE=1 uv run --frozen --offline pytest -q \
  tests/live_support/test_operation_safety.py tests/pipeline/test_pipeline.py
PYTHONDONTWRITEBYTECODE=1 uv run --frozen --offline python - <<'PY'
import json
from pathlib import Path
from tools.openapi_pipeline.live.safety import OperationSafetyCatalog

document = json.loads(Path("build/openapi/effective.json").read_text(encoding="utf-8"))
catalog = OperationSafetyCatalog.load(Path("contracts/operation-safety.yaml"))
catalog.assert_matches_openapi(document)
assert len(catalog.operations) == 225
assert len(catalog.automatic_read_ids) == 91
print("operation-safety: 225 total, 91 automatic reads")
PY
```

Expected: both pytest files pass and the script prints only the two public counts.

Commit:

```bash
git add contracts/operation-safety.yaml tools/openapi_pipeline/live/contract_io.py \
  tools/openapi_pipeline/live/safety.py tools/openapi_pipeline/paths.py \
  tools/openapi_pipeline/pipeline.py tests/live_support/test_operation_safety.py \
  tests/pipeline/test_pipeline.py
git commit -m "feat: classify every iiko operation for live safety"
```

### Task 2: Separate reviewed test cadence from documented server limits

**Files:**
- Modify: `tools/openapi_pipeline/live/rates.py`
- Modify: `contracts/rate-limits.yaml`
- Modify: `src/iikocloud_client/_contracts/rate-limits.yaml`
- Modify: `contracts/live-operations.yaml`
- Modify: `tests/live_support/test_rates.py`
- Modify: `tests/live_support/test_circuit.py`
- Modify: `tests/live_support/test_session.py`
- Modify: `tests/live_support/test_write_gates.py`
- Modify: `tests/pipeline/test_generator.py`

**Interfaces:**
- Consumes: `OperationSafetyCatalog.automatic_read_ids`, current live operation contract, existing `RatePolicy` and `LiveRateGuard`.
- Produces: version-2 `RateCatalog`, `TestBudget`, optional `ServerLimit`, unchanged `OperationBudget(operation_id, safe_interval_seconds, max_calls_per_run)`, and sorted `RateCatalog.operation_ids: tuple[str, ...]` for parity checks.

- [ ] **Step 1: Rewrite rate tests for the exact version-2 shape**

Use this canonical fixture:

```python
RATE_V2 = {
    "version": 2,
    "defaults": {
        "utilization": 0.20,
        "global_min_interval_seconds": 30,
        "max_calls_per_operation_per_run": 1,
    },
    "operations": {
        "get_nomenclature": {
            "test_budget": {
                "min_interval_seconds": 30,
                "source": "user-approved-global-read-cadence-2026-07-21",
                "verified": True,
            },
            "server_limit": None,
        },
        "get_external_menus": {
            "test_budget": {
                "min_interval_seconds": 30,
                "source": "user-approved-global-read-cadence-2026-07-21",
                "verified": True,
            },
            "server_limit": {
                "calls": 1,
                "per_seconds": 1800,
                "source": "existing-manager-configuration",
                "verified": True,
            },
        },
    },
}
```

Assert 30 seconds for `get_nomenclature`, 9000 seconds for `get_external_menus`, rejection of version 1, missing/unverified test budget, unverified/non-object server limit, test interval below 30, utilization above 0.20, max calls other than one, NaN/infinity/bool numerics, unknown keys, duplicate YAML keys, and unknown operation IDs.

- [ ] **Step 2: Run the focused tests and verify RED**

Run:

```bash
PYTHONDONTWRITEBYTECODE=1 uv run --frozen --offline pytest -q \
  tests/live_support/test_rates.py tests/live_support/test_circuit.py
```

Expected: rate tests fail because the current parser requires version 1 and a single `server_limit/source/verified` entry.

- [ ] **Step 3: Implement version-2 parsing and interval calculation**

Use `contract_io.load_yaml_mapping`, `exact_keys`, `safe_identifier`, and the shared bounded safe-source validator rather than retaining a second YAML loader in `rates.py`. Use exact immutable data:

```python
@dataclass(frozen=True, slots=True)
class TestBudget:
    min_interval_seconds: float
    source: str
    verified: bool

@dataclass(frozen=True, slots=True)
class ServerLimit:
    calls: int
    per_seconds: float
    source: str
    verified: bool

@dataclass(frozen=True, slots=True)
class _CatalogOperation:
    test_budget: TestBudget
    server_limit: ServerLimit | None
```

`operation_budget` must reject a non-verified test budget and any present non-verified server limit. Calculate:

```python
server_interval = (
    math.ceil(server_limit.per_seconds / server_limit.calls / policy.utilization)
    if server_limit is not None
    else 0
)
safe_interval_seconds = max(
    policy.global_min_interval_seconds,
    test_budget.min_interval_seconds,
    server_interval,
)
```

Do not derive a numeric server limit from OpenAPI prose or `Restriction group`.

- [ ] **Step 4: Expand the executable read allowlist and rate entries**

Add every Appendix B operation to `contracts/live-operations.yaml` with the exact effective method/path and `kind: read`, `cleanup: null`. The file then contains 94 entries: `authenticate`, 91 reads, and the existing `add_products_to_stop_list`/`remove_products_from_stop_list` write pair. `authenticate_v2` remains absent.

Add rate entries for `authenticate` and all 91 reads. Every read gets the reviewed 30-second `test_budget`. Preserve only these separately reviewed server limits:

```text
authenticate                 1 / 5 seconds     -> effective 30 seconds
get_organizations            1 / 10 seconds    -> effective 50 seconds
get_terminal_groups          10 / 60 seconds   -> effective 30 seconds
get_external_menus           1 / 1800 seconds  -> effective 9000 seconds
get_external_menu_by_id      5 / 60 seconds    -> effective 60 seconds
```

All other reads use `server_limit: null`; this records that the server limit is unknown rather than claiming the 30-second test cadence is a server limit. Keep the two stop-list write budgets unverified so this task cannot enable write execution. Copy the canonical YAML byte-for-byte to `src/iikocloud_client/_contracts/rate-limits.yaml`.

- [ ] **Step 5: Update all synthetic rate fixtures and verify GREEN**

Run in fresh processes:

```bash
PYTHONDONTWRITEBYTECODE=1 uv run --frozen --offline pytest -q \
  tests/live_support/test_rates.py tests/live_support/test_circuit.py \
  tests/live_support/test_session.py
PYTHONDONTWRITEBYTECODE=1 uv run --frozen --offline pytest -q \
  tests/live_support/test_write_gates.py tests/pipeline/test_generator.py
```

Expected: all tests pass; no live marker is selected and no HTTP occurs.

- [ ] **Step 6: Commit the cadence contract**

```bash
git add contracts/live-operations.yaml contracts/rate-limits.yaml \
  src/iikocloud_client/_contracts/rate-limits.yaml \
  tools/openapi_pipeline/live/rates.py tests/live_support/test_rates.py \
  tests/live_support/test_circuit.py tests/live_support/test_session.py \
  tests/live_support/test_write_gates.py tests/pipeline/test_generator.py
git commit -m "feat: budget every guarded live read"
```

### Task 3: Resolve a terminal target for read-only profiles

**Files:**
- Modify: `tools/openapi_pipeline/live/profile.py`
- Modify: `tests/live_support/test_profile.py`
- Modify: `config/live-profile.example.toml`
- Modify: `private/README.md`

**Interfaces:**
- Consumes: existing strict private profile and `.env` readers.
- Produces: unchanged `ResolvedLiveProfile`, with `terminal_group_id` available when `allow_write=false` and the optional terminal env name is configured; `write_product_id` remains `None` unless `allow_write=true`.

- [ ] **Step 1: Add failing read/write target separation tests**

Cover these exact cases without reading the repository `.env`:

```text
allow_write=false + terminal env only       -> terminal loaded, product None
allow_write=false + terminal and product    -> terminal loaded, product env not required/read
allow_write=false + product without terminal -> rejected
allow_write=true  + terminal and product    -> both loaded
allow_write=true  + either field missing    -> rejected
discovery profile with terminal name        -> name validated, value not loaded
```

- [ ] **Step 2: Run and verify RED**

```bash
PYTHONDONTWRITEBYTECODE=1 uv run --frozen --offline pytest -q \
  tests/live_support/test_profile.py
```

Expected: the terminal-only read profile is rejected by the current pair requirement, and a read-only profile resolves `terminal_group_id=None`.

- [ ] **Step 3: Implement minimal profile semantics**

Replace the pair check with:

```python
if "write_product_id_env" in value and "terminal_group_id_env" not in value:
    raise SafetyError("Live profile write product requires a terminal group field")
```

In `load_profile`, always resolve `terminal_group_id` when its env name exists. Resolve `write_product_id` only when `allow_write is True`; a write-enabled profile still requires and resolves both. Never log either value.

- [ ] **Step 4: Document and verify**

Explain in the example and private README that the terminal is a read target used by terminal/stop-list/employee checks, while the product is a dedicated write-only target and is ignored when writes are disabled.

Run:

```bash
PYTHONDONTWRITEBYTECODE=1 uv run --frozen --offline pytest -q \
  tests/live_support/test_profile.py tests/live_support/test_write_gates.py
```

Expected: both files pass.

- [ ] **Step 5: Commit**

```bash
git add tools/openapi_pipeline/live/profile.py tests/live_support/test_profile.py \
  config/live-profile.example.toml private/README.md
git commit -m "feat: allow terminal targets in read-only profiles"
```

### Task 4: Add immutable ReadCase, binding, context, and safe reason types

**Files:**
- Create: `tools/openapi_pipeline/live/read_case.py`
- Create: `tests/live_support/test_read_case.py`
- Modify: `tools/openapi_pipeline/live/__init__.py`

**Interfaces:**
- Consumes: generated Pydantic request models only through `GeneratedReadBinding.resolve()`.
- Produces: all names in the stable `read_case.py` interface, plus `ReadContext`, `ContextView`, `NoLiveTarget`, `ReadAssertionFailure`, `ReadExtractorFailure`, and `build_generated_request`.

- [ ] **Step 1: Write failing context and binding tests**

Tests must prove:

```python
context = ReadContext.seed({"organization_id": object(), "terminal_group_id": object()})
view = context.view(("organization_id",))
assert tuple(view) == ("organization_id",)
assert "terminal_group_id" not in view
assert "object" not in repr(context)
assert "object" not in repr(view)
```

Also cover duplicate/unsafe keys, undeclared access, undeclared extractor output, overwrite attempts, non-positive revision, duplicate requires/provides/dependencies, unsafe method/module/class names, request triple all-null versus all-present, exact `<operation_id>_with_http_info`, immutable `NO_REQUEST`, and fixed-code exceptions whose `str()` never includes supplied live values.

- [ ] **Step 2: Run and verify RED**

```bash
PYTHONDONTWRITEBYTECODE=1 uv run --frozen --offline pytest -q \
  tests/live_support/test_read_case.py
```

Expected: import fails because `read_case.py` does not exist.

- [ ] **Step 3: Implement safe context and exceptions**

`ReadContext` owns a private mutable dictionary with `repr=False`; `ContextView` exposes only declared keys through a `MappingProxyType`; neither type serializes values. `ReadContext.apply(case, extracted)` rejects undeclared keys and overwrites except when the new value equals the existing immutable value.

Implement exceptions with code-only messages:

```python
class NoLiveTarget(Exception):
    def __init__(self, code: NoLiveTargetCode) -> None:
        self.code = code
        super().__init__(code.value)

class ReadAssertionFailure(Exception):
    def __init__(self) -> None:
        super().__init__(ReadFailureCode.ASSERTION_FAILED.value)

class ReadExtractorFailure(Exception):
    def __init__(self) -> None:
        super().__init__(ReadFailureCode.EXTRACTOR_FAILED.value)
```

Do not accept free-form exception messages.

- [ ] **Step 4: Implement exact lazy generated bindings**

`GeneratedReadBinding.resolve()` imports only module names beginning with `iikocloud_client.api.` and `iikocloud_client.models.`, obtains the declared classes, checks the API method exists, and checks the request keyword exists in `inspect.signature(method)`. `build_generated_request(binding, values)` returns `None` only for `NO_REQUEST`; otherwise it calls the resolved Pydantic class's `model_validate(dict(values))` and converts every exception into `SafetyError("Generated read request validation failed")` without payload or exception text.

- [ ] **Step 5: Verify and commit**

```bash
PYTHONDONTWRITEBYTECODE=1 uv run --frozen --offline pytest -q \
  tests/live_support/test_read_case.py
PYTHONDONTWRITEBYTECODE=1 uv run --frozen --offline mypy \
  tools/openapi_pipeline/live/read_case.py
```

Expected: tests and mypy pass.

```bash
git add tools/openapi_pipeline/live/read_case.py \
  tools/openapi_pipeline/live/__init__.py tests/live_support/test_read_case.py
git commit -m "feat: define typed live read cases"
```

### Task 5: Build the deterministic dependency planner

**Files:**
- Create: `tools/openapi_pipeline/live/read_planner.py`
- Create: `tests/live_support/test_read_planner.py`
- Modify: `tools/openapi_pipeline/live/__init__.py`

**Interfaces:**
- Consumes: immutable `ReadCase` values.
- Produces: `ReadPlan.build(cases)`, `dependency_closure(operation_id)`, `case_for(operation_id)`, and `registry_sha256`.

- [ ] **Step 1: Write failing DAG and descriptor tests**

Build synthetic cases `root`, `alpha`, `beta`, `leaf` with dependencies `alpha -> root`, `beta -> root`, `leaf -> alpha,beta`. Assert stable order `root,alpha,beta,leaf`, regardless of input order. Cover duplicate IDs, missing dependency, self-dependency, cycle, dependency that does not provide a required key, duplicate context provider, unknown closure target, and closure containing only the selected operation plus transitive dependencies.

The descriptor hash input is exact canonical JSON:

```python
{
    "version": 1,
    "cases": [
        {
            "operation_id": case.operation_id,
            "revision": case.revision,
            "depends_on": list(case.depends_on),
            "requires": list(case.requires),
            "provides": list(case.provides),
            "allowed_no_target_codes": sorted(code.value for code in case.allowed_no_target_codes),
            "binding": asdict(case.binding),
        }
        for case in cases_sorted_by_operation_id
    ],
}
```

- [ ] **Step 2: Run and verify RED**

```bash
PYTHONDONTWRITEBYTECODE=1 uv run --frozen --offline pytest -q \
  tests/live_support/test_read_planner.py
```

Expected: import fails because `read_planner.py` does not exist.

- [ ] **Step 3: Implement stable layered topological ordering**

Use Kahn's algorithm. At each layer, sort ready operation IDs lexicographically before appending them. For every name in `case.requires`, require that it is in `READ_SEED_KEYS` or is declared by exactly one transitive dependency's `provides`; a key may be absent at runtime, and the builder then chooses another declared provider or raises its reviewed no-target code. Reject all invalid graph/context relationships during `ReadPlan.build`, before profile or network access. Freeze the case lookup and calculate `registry_sha256` from the descriptor above.

- [ ] **Step 4: Implement dependency closure**

`dependency_closure` must retain original topological order and the original registry hash descriptor must be recalculated for the subset. The selected-read runner later adds `get_organizations` as a required canary before requesting the closure when it is otherwise absent.

- [ ] **Step 5: Verify and commit**

```bash
PYTHONDONTWRITEBYTECODE=1 uv run --frozen --offline pytest -q \
  tests/live_support/test_read_case.py tests/live_support/test_read_planner.py
PYTHONDONTWRITEBYTECODE=1 uv run --frozen --offline mypy \
  tools/openapi_pipeline/live/read_case.py tools/openapi_pipeline/live/read_planner.py
```

Expected: all checks pass.

```bash
git add tools/openapi_pipeline/live/read_planner.py \
  tools/openapi_pipeline/live/__init__.py tests/live_support/test_read_planner.py
git commit -m "feat: plan live reads by safe dependencies"
```

### Task 6: Close arbitrary callback substitution in the generated SDK adapter

**Files:**
- Modify: `tools/openapi_pipeline/live/generated.py`
- Modify: `tests/live_support/test_generated_adapter.py`
- Modify: `tests/live_support/test_generated_cleanup.py`
- Modify: `tests/integration/read/test_organizations.py`

**Interfaces:**
- Consumes: `GeneratedReadBinding`, generated `ApiResponse`, exact `LiveOperation` contract, existing guard/state/receipt/capture.
- Produces: `GeneratedCallResult[T]`, code-only `GeneratedCallFailure`, and `GeneratedLiveSdk.call_bound_read(operation_id, binding, request_model)`; arbitrary read callbacks are no longer public.

- [ ] **Step 1: Add failing substitution and safe-error tests**

Add a fake generated API with both approved and wrong methods. Prove all of these fail before `guard.acquire`:

```text
operation_id does not match binding.method_name
API class does not own the exact method
request keyword differs from the generated signature
operation is absent from live-operations
operation kind is not read
binding request model differs from the resolved request class
```

Add fake responses for 200, 400, 429, cancellation, transport exception, non-`ApiResponse`, and a capture failure. Assert returned/status behavior and that every raised message is a fixed safe string with no fake response body, URL, token, UUID, or exception detail.

- [ ] **Step 2: Run and verify RED**

```bash
PYTHONDONTWRITEBYTECODE=1 uv run --frozen --offline pytest -q \
  tests/live_support/test_generated_adapter.py \
  tests/live_support/test_generated_cleanup.py
```

Expected: substitution tests fail because `call_generated` currently accepts any caller-supplied callback for a claimed operation ID.

- [ ] **Step 3: Add the bound result and invocation API**

Implement:

```python
@dataclass(frozen=True, slots=True)
class GeneratedCallResult(Generic[T]):
    data: T
    status_code: int
    duration_ms: int

class GeneratedCallFailure(SafetyError):
    def __init__(self, code: ReadFailureCode, status_code: int | None = None) -> None:
        self.code = code
        self.status_code = status_code
        super().__init__(code.value)

async def call_bound_read(
    self,
    operation_id: str,
    binding: GeneratedReadBinding,
    request_model: object | None,
) -> GeneratedCallResult[object]:
    operation = self.operation_contract.get(operation_id)
    if operation is None or operation.kind != "read":
        raise SafetyError("Generated read operation is not allowlisted")
    if binding.method_name != f"{operation_id}_with_http_info":
        raise SafetyError("Generated read binding does not match operation ID")
    api_type, request_type, method = binding.resolve()
    # Validate request_model type/NO_REQUEST contract, then invoke only `method`.
```

The constructor now receives the exact immutable `operation_contract`. Instantiate `api_type(self.api_client)` inside the adapter and construct kwargs only from the binding's single request keyword plus `_request_timeout=(10.0, 30.0)`. No caller supplies a callable.

- [ ] **Step 4: Normalize the internal call path**

Keep one private `_call_generated` method for the bound read method and the already hard-coded stop-list cleanup. Measure monotonic duration, record the operation before HTTP, accept only `ApiResponse` with status 200–299, and return `GeneratedCallResult`.

On `ApiException`, record a normalized integer status, open the existing circuit on 429, mark the adapter unusable for every HTTP/transport/deserialization/capture failure, and raise `GeneratedCallFailure` with the matching fixed code/status and no exception chaining. Its public string is only the code. Internal fixed diagnostics may use only these messages and never raw details:

```text
iiko returned 429; live circuit opened
Generated SDK returned a non-success HTTP status
Generated SDK invocation failed without a retry
Generated SDK invocation returned an invalid response
Generated SDK capture failed after response without a retry
```

`CancelledError` is re-raised after marking the adapter unusable. A validator/extractor failure is not handled here because it occurs after a valid 2xx/deserialization and may permit independent branches to continue.

- [ ] **Step 5: Capture only the explicitly selected matching operation**

When a `LiveCapture` exists, call it only if `capture.selected_operation == operation_id`; do not call `assert_selected` for non-selected dependency/canary reads. Include exact allowlisted `method`, `path`, `status`, and duration metadata. Auth remains outside the generated capture path.

- [ ] **Step 6: Migrate the organization smoke canary and cleanup internals**

Change the smoke test to construct the Appendix B binding for `get_organizations` and call `call_bound_read`. Keep cleanup callable inaccessible to read cases; `execute_cleanup` invokes the existing exact `MenuApi.remove_products_from_stop_list_with_http_info` through the private primitive.

- [ ] **Step 7: Verify and commit**

```bash
PYTHONDONTWRITEBYTECODE=1 uv run --frozen --offline pytest -q \
  tests/live_support/test_generated_adapter.py \
  tests/live_support/test_generated_cleanup.py \
  tests/integration/read/test_organizations.py --collect-only
PYTHONDONTWRITEBYTECODE=1 uv run --frozen --offline mypy \
  tools/openapi_pipeline/live/generated.py
```

Expected: all offline tests pass and collection reports one skipped live smoke test when no profile is supplied.

```bash
git add tools/openapi_pipeline/live/generated.py \
  tests/live_support/test_generated_adapter.py \
  tests/live_support/test_generated_cleanup.py \
  tests/integration/read/test_organizations.py
git commit -m "fix: bind live reads to exact generated methods"
```

### Task 7: Add a credential-free private read report and contract-bound receipt

**Files:**
- Create: `tools/openapi_pipeline/live/read_report.py`
- Create: `tests/live_support/test_read_report.py`
- Modify: `tools/openapi_pipeline/live/receipt.py`
- Modify: `tools/openapi_pipeline/live/pytest_support.py`
- Modify: `tools/openapi_pipeline/publish.py`
- Modify: `tests/live_support/test_receipt.py`
- Modify: `tests/live_support/test_pytest_gates.py`
- Modify: `tests/publish/test_publish.py`

**Interfaces:**
- Consumes: `ReadOutcome`, run ID, profile fingerprint, effective/generated hashes, safety/live/rate contract bytes, registry hash.
- Produces: `LiveArtifactHashes.live_contracts_sha256`, `ReadStatus`, `ReadOutcome`, `ReadReport`, `ReadReportWriter.create`, `append(outcome)`, `finish(success)`, and `load_and_verify()`.

- [ ] **Step 1: Write failing report schema and attack tests**

Use this exact JSON shape:

```python
{
    "version": 1,
    "run_id": "20260721T120000Z-a1b2c3d4",
    "profile_fingerprint": "a" * 64,
    "effective_schema_sha256": "b" * 64,
    "generated_tree_sha256": "c" * 64,
    "live_contracts_sha256": "d" * 64,
    "registry_sha256": "e" * 64,
    "started_at": "2026-07-21T12:00:00Z",
    "finished_at": None,
    "completed": False,
    "outcomes": [],
    "counts": {"passed": 0, "no_live_target": 0, "failed": 0, "aborted": 0},
}
```

Test canonical JSON, duplicate-key rejection, exact fields, enum/reason compatibility, no duplicate operation outcome, safe method/path, 100–599 optional status, non-negative integer duration, counts, completion, file size, directory/file modes, owner, hard link, symlink ancestry/leaf, path escape, pre-existing unrelated file, concurrent replacement, atomic update, and reopen verification.

Scan the final bytes and assert absence of a synthetic API login, bearer token, UUID, email, phone, customer name, request body, response body, raw exception, `Authorization`, and query string.

- [ ] **Step 2: Run and verify RED**

```bash
PYTHONDONTWRITEBYTECODE=1 uv run --frozen --offline pytest -q \
  tests/live_support/test_read_report.py tests/live_support/test_receipt.py
```

Expected: report import fails and receipts lack the live-contract hash.

- [ ] **Step 3: Bind artifacts and receipts to all live contracts**

Extend `LiveArtifactHashes` and `LiveReceipt` with `live_contracts_sha256`. Calculate it in `verify_live_artifacts` as canonical JSON over SHA-256 values of the validated raw bytes of:

```text
contracts/operation-safety.yaml
contracts/live-operations.yaml
contracts/rate-limits.yaml
```

The strict parsers must successfully load all three before hashing. Update receipt JSON fields, `matches`, initialization, completion, publish selection, and tests. Old receipts lacking the field become invalid rather than being silently accepted.

- [ ] **Step 4: Implement the report writer**

Create `private/reports/live-read/<run-id>.json` under already validated private ancestry. `create` rejects an existing leaf and writes the initial report mode `0600`. Each update verifies the current file still matches the writer's last canonical bytes and safe metadata before `write_json_atomic`, then reopens and validates the new canonical content. `finish(success=True)` is legal only with at least one `passed`, no `failed`/`aborted`, and counts matching outcomes.

Reason rules are exact:

```text
passed          -> reason is null
no_live_target  -> one NoLiveTargetCode value
failed          -> ASSERTION_FAILED or EXTRACTOR_FAILED
aborted         -> one ReadFailureCode other than assertion/extractor
```

- [ ] **Step 5: Require a verified completed report for full/selected receipt completion**

Extend the pytest run context with `read_report_path` and `read_report_completed`. For exhaustive/selected runs, `finalize_live_receipt` receives `read_report_completed=True` only after `load_and_verify()` confirms matching run/profile/artifact hashes and a successful report. Smoke and existing explicitly selected write tests retain their current receipt semantics; this task must not enable writes.

- [ ] **Step 6: Verify and commit**

```bash
PYTHONDONTWRITEBYTECODE=1 uv run --frozen --offline pytest -q \
  tests/live_support/test_read_report.py tests/live_support/test_receipt.py \
  tests/live_support/test_pytest_gates.py
PYTHONDONTWRITEBYTECODE=1 uv run --frozen --offline pytest -q \
  tests/publish/test_publish.py
```

Expected: all tests pass.

```bash
git add tools/openapi_pipeline/live/read_report.py \
  tools/openapi_pipeline/live/receipt.py \
  tools/openapi_pipeline/live/pytest_support.py \
  tools/openapi_pipeline/publish.py \
  tests/live_support/test_read_report.py tests/live_support/test_receipt.py \
  tests/live_support/test_pytest_gates.py tests/publish/test_publish.py
git commit -m "feat: record private live read outcomes"
```

### Task 8: Implement the sequential read runner and abort policy

**Files:**
- Create: `tools/openapi_pipeline/live/read_runner.py`
- Create: `tests/live_support/test_read_runner.py`
- Modify: `tools/openapi_pipeline/live/__init__.py`

**Interfaces:**
- Consumes: `ReadPlan`, `ReadContext`, `ReadStatus`, `ReadOutcome`, `GeneratedLiveSdk.call_bound_read`, operation contract, report writer.
- Produces: `run_read_plan -> ReadRunSummary` and the exact status policy in the approved design.

- [ ] **Step 1: Write fake-SDK runner tests**

Cover these complete state transitions:

| Case result | Current outcome | Independent next branch | Dependents | Report completion |
|---|---|---|---|---|
| valid 2xx + validation + extraction | `passed` | runs | runs if context exists | possible |
| declared missing target before build | `no_live_target` | runs | `no_live_target` if its own target is absent | possible |
| validator failure after valid 2xx | `failed/assertion_failed` | runs | `aborted/dependency_failed` | false |
| extractor failure after valid 2xx | `failed/extractor_failed` | runs | `aborted/dependency_failed` | false |
| request model validation failure | `aborted/safety_invariant` | no further HTTP | aborted | false |
| deserialization/invocation/HTTP/timeout | `aborted` | no further HTTP | aborted | false |
| `429` | `aborted/http_error` | no further HTTP | aborted | false |
| cancellation | current and remaining `aborted/cancelled` | no further HTTP | aborted | false |
| rate/state/receipt/report failure | `aborted` | no further HTTP | aborted | false |

Assert `NoLiveTarget` occurs before SDK call and therefore before rate acquisition, each operation is invoked zero or one time, context values never appear in repr/outcomes/report, and summary success requires at least one passed case plus only passed/no-target outcomes.

- [ ] **Step 2: Run and verify RED**

```bash
PYTHONDONTWRITEBYTECODE=1 uv run --frozen --offline pytest -q \
  tests/live_support/test_read_runner.py
```

Expected: import fails because `read_runner.py` does not exist.

- [ ] **Step 3: Implement request/build/invoke/validate/extract order**

For each planned case:

```python
view = context.view(case.requires)
values = case.build_values(view)           # may raise reviewed NoLiveTarget
request = build_generated_request(case.binding, values)
result = await sdk.call_bound_read(case.operation_id, case.binding, request)
case.validate_response(result.data, view)  # catch and normalize, never stringify data/error
extracted = case.extract(result.data, view)
context.apply(case, extracted)
```

Before each case, inspect prior outcomes for failed dependencies. Append exactly one terminal outcome per case and update the report after each. After a global abort, append fixed-code `aborted` outcomes for every unvisited case without building a request or acquiring a rate budget.

- [ ] **Step 4: Implement safe continuation boundaries**

Only `ReadAssertionFailure` and `ReadExtractorFailure` after a valid generated 2xx allow independent branches to continue. `GeneratedCallFailure` contributes only its enum code and normalized status. Every other exception is normalized to a fixed `ReadFailureCode`, marks the global run aborted, and never includes `str(error)` or `repr(error)` in a report, assertion message, or print.

- [ ] **Step 5: Verify and commit**

```bash
PYTHONDONTWRITEBYTECODE=1 uv run --frozen --offline pytest -q \
  tests/live_support/test_read_case.py tests/live_support/test_read_planner.py \
  tests/live_support/test_read_report.py tests/live_support/test_read_runner.py
PYTHONDONTWRITEBYTECODE=1 uv run --frozen --offline mypy \
  tools/openapi_pipeline/live/read_case.py \
  tools/openapi_pipeline/live/read_planner.py \
  tools/openapi_pipeline/live/read_report.py \
  tools/openapi_pipeline/live/read_runner.py
```

Expected: tests and mypy pass.

```bash
git add tools/openapi_pipeline/live/read_runner.py \
  tools/openapi_pipeline/live/__init__.py tests/live_support/test_read_runner.py
git commit -m "feat: run live reads sequentially and fail closed"
```

### Task 9: Add exact pytest gates, report fixtures, and selected-operation capture

**Files:**
- Modify: `tests/conftest.py`
- Modify: `tools/openapi_pipeline/live/pytest_support.py`
- Modify: `tests/live_support/test_pytest_gates.py`
- Modify: `tests/live_support/test_live_sdk_fixture.py`
- Modify: `tests/capture/test_session_capture.py`
- Modify: `tests/pipeline/test_ci_workflows.py`
- Modify: `pyproject.toml`
- Create: `tests/integration/read/test_all_reads.py`
- Create: `tests/integration/read/test_selected_read.py`

**Interfaces:**
- Consumes: full `ReadPlan`, safety/rate/live catalogs, profile, one session/adapter, `CaptureWriter`, `LiveCapture`, report writer.
- Produces: `live_read_full` exact command, new `live_read_selected` exact command, fixtures `live_read_plan`, `live_read_context`, `live_read_report`, and capture-aware `live_sdk`.

- [ ] **Step 1: Write subprocess gate tests before fixture changes**

Assert these invocations fail during collection before private/profile/env/network access:

```text
live_read_full without -n0
live_read_full without exact tests/integration/read/test_all_reads.py
live_read_full with any second path, live_write marker, --allow-live-write, or capture flag
live_read_selected without -n0
live_read_selected without exact tests/integration/read/test_selected_read.py
only one of --capture-http / --capture-operation
unknown, auth, non-read, non-automatic, unallowlisted, unbudgeted, or unregistered capture operation
capture flags on the full runner
xdist worker environment for either read mode
```

Assert ordinary `pytest --collect-only`, `pytest --help`, and default CI collection neither reads private/env nor initializes a live report/capture/socket.

- [ ] **Step 2: Run and verify RED**

```bash
PYTHONDONTWRITEBYTECODE=1 uv run --frozen --offline pytest -q \
  tests/live_support/test_pytest_gates.py \
  tests/live_support/test_live_sdk_fixture.py \
  tests/pipeline/test_ci_workflows.py
```

Expected: selected marker/path gates and capture/report wiring tests fail.

- [ ] **Step 3: Register and default-exclude the selected marker**

Add:

```toml
"live_read_selected: one explicit guarded live read plus dependency closure",
```

and include `not live_read_selected` in pytest `addopts`. Add the marker to `_LIVE_MARKERS`. CI must continue to contain no command that selects any live marker.

- [ ] **Step 4: Validate the full static plan before private access**

`prepare_live_preflight` now accepts the selected `ReadPlan` and mode. Before `profile_path_for_name` or `.env` access it must:

1. require exact path/marker/`-n0` arguments;
2. verify the generated package origin is exactly the current checkout's `src/iikocloud_client`;
3. verify generated/effective artifacts and all three live contracts;
4. assert safety catalog exact OpenAPI parity;
5. assert every planned operation is an automatic read;
6. assert exact read-set parity among 91 safety automatic reads, 91 `kind: read` allowlist entries, 91 executable rate budgets, and the 91-case full registry;
7. resolve every generated binding and reject a method/request mismatch;
8. reject capture flags in full mode;
9. in selected mode, validate one exact operation and take its dependency closure plus `get_organizations` canary.

- [ ] **Step 5: Seed context only after lock/profile validation**

Require the selected organization to be present in `allowed_organization_ids`. Seed only these keys, all with hidden repr:

```text
profile_organization_id
profile_external_menu_id
profile_terminal_group_id (only when present)
date_yyyy_mm_dd
period_from_yyyy_mm_dd
period_to_yyyy_mm_dd
window_from_local
window_to_local
```

`get_organizations`, `get_external_menus`, and `get_terminal_groups` validate profile targets before publishing the usable `organization_id`, `external_menu_id`, and `terminal_group_id` keys.

- [ ] **Step 6: Wire reports and single-operation capture**

Create the report after acquiring the canonical lock and resolving the profile but before authentication. Build `RedactionHints.for_operation(effective_schema, selected_id)` before private capture creation. Construct `CaptureWriter(private/captures, known_secrets=(profile.api_login,))`; after auth, add the access token through `capture.add_known_secret` before yielding `live_sdk`. Pass capture only to the generated adapter, never the auth session.

The selected runner executes its canary/dependency closure, but only the exact selected operation is captured. A full run always refuses capture flags.

- [ ] **Step 7: Implement the two orchestration tests**

`test_all_reads.py`:

```python
@pytest.mark.live_read_full
@pytest.mark.asyncio(loop_scope="session")
async def test_all_reviewed_reads(live_read_harness: LiveReadHarness) -> None:
    summary = await live_read_harness.run()
    if not summary.success:
        pytest.fail("live_read_full did not satisfy the safe outcome contract", pytrace=False)
```

`test_selected_read.py` uses the same body and `live_read_selected`; its fixture supplies the closure plan. Neither test prints response/context values.

- [ ] **Step 8: Verify all gates offline and commit**

```bash
PYTHONDONTWRITEBYTECODE=1 uv run --frozen --offline pytest -q \
  tests/live_support/test_pytest_gates.py \
  tests/live_support/test_live_sdk_fixture.py
PYTHONDONTWRITEBYTECODE=1 uv run --frozen --offline pytest -q \
  tests/capture/test_session_capture.py tests/pipeline/test_ci_workflows.py
PYTHONDONTWRITEBYTECODE=1 uv run --frozen --offline pytest -q \
  tests/integration/read/test_all_reads.py \
  tests/integration/read/test_selected_read.py --collect-only
```

Expected: all offline tests pass; collect-only finds two live tests and performs no private/env/network access.

```bash
git add tests/conftest.py tools/openapi_pipeline/live/pytest_support.py \
  tests/live_support/test_pytest_gates.py \
  tests/live_support/test_live_sdk_fixture.py \
  tests/capture/test_session_capture.py tests/pipeline/test_ci_workflows.py \
  tests/integration/read/test_all_reads.py \
  tests/integration/read/test_selected_read.py pyproject.toml
git commit -m "feat: gate exhaustive and selected live reads"
```

### Task 10: Implement organization, terminal, dictionary, address, command, and webhook cases

**Files:**
- Create: `tests/integration/read/cases/foundation.py`
- Create: `tests/integration/read/cases/addresses.py`
- Create: `tests/live_support/read_cases/test_foundation.py`

**Interfaces:**
- Consumes: stable ReadCase helpers, profile seed keys, Appendix B bindings.
- Produces: 18 cases and context keys `organization_id`, `terminal_group_id`, `city_id`, `street_id`.

- [ ] **Step 1: Write the exact registry-set test**

Assert equality with this set, not a count-only assertion:

```python
FOUNDATION_IDS = {
    "get_cancel_causes",
    "get_cities",
    "get_command_status",
    "get_delivery_order_types",
    "get_discounts",
    "get_marketing_sources",
    "get_organization_settings",
    "get_organizations",
    "get_payment_types",
    "get_regions",
    "get_removal_types",
    "get_terminal_groups",
    "check_terminal_groups_availability",
    "get_tips_types",
    "get_webhook_settings",
    "list_organizations",
    "get_streets_by_city",
    "get_streets_by_id",
}
```

Use synthetic generated responses to test target validation, empty city/street collections, no-body operations, hidden webhook payloads, and fixed `command_unavailable` before SDK invocation.

- [ ] **Step 2: Run and verify RED**

```bash
PYTHONDONTWRITEBYTECODE=1 uv run --frozen --offline pytest -q \
  tests/live_support/read_cases/test_foundation.py
```

Expected: modules do not exist.

- [ ] **Step 3: Implement foundation dependencies and bounded requests**

Use exact dependency rules:

```text
get_organizations: profile_organization_id -> organization_id after response contains it
all organization-scoped foundation reads: depend on get_organizations, require organization_id
get_terminal_groups: also validate optional profile_terminal_group_id -> terminal_group_id
check_terminal_groups_availability: require terminal_group_id or terminal_group_unavailable
get_command_status: command_unavailable (no read-only provider in this stage)
list_organizations/get_tips_types: NO_REQUEST
get_webhook_settings: validate only response model/type; never extract or report authToken
get_cities: extract first explicit city id -> city_id
get_streets_by_city: depend on get_cities, require city_id, extract first street id -> street_id
get_streets_by_id: depend on get_streets_by_city, require street_id
```

Every multi-organization request contains exactly `[organization_id]`; `get_organizations` sets `includeDisabled=False` and `returnAdditionalInfo=False`; terminal requests set `includeDisabled=False`. Validators raise only `ReadAssertionFailure()`.

- [ ] **Step 4: Verify bindings/models/extraction and commit**

```bash
PYTHONDONTWRITEBYTECODE=1 uv run --frozen --offline pytest -q \
  tests/live_support/read_cases/test_foundation.py
PYTHONDONTWRITEBYTECODE=1 uv run --frozen --offline ruff check \
  tests/integration/read/cases/foundation.py \
  tests/integration/read/cases/addresses.py \
  tests/live_support/read_cases/test_foundation.py
```

Expected: 18 exact cases pass all offline request and response tests.

```bash
git add tests/integration/read/cases/foundation.py \
  tests/integration/read/cases/addresses.py \
  tests/live_support/read_cases/test_foundation.py
git commit -m "test: cover foundational iiko reads"
```

### Task 11: Implement menu, combo, stop-list, and external-menu read cases

**Files:**
- Create: `tests/integration/read/cases/menu.py`
- Create: `tests/live_support/read_cases/test_menu.py`

**Interfaces:**
- Consumes: `organization_id`, validated optional `terminal_group_id`, profile external-menu target, Appendix B bindings.
- Produces: seven cases and keys `product_id`, `product_price`, the internal immutable `nomenclature_prices` lookup, `combo_items`, and `external_menu_id`.

- [ ] **Step 1: Write the exact case-set and dependency tests**

```python
MENU_IDS = {
    "calculate_combo_price",
    "check_products_in_stop_list",
    "get_combos_info",
    "get_external_menu_by_id",
    "get_external_menus",
    "get_nomenclature",
    "get_stop_lists",
}
```

Test generated model aliases, selected external-menu validation, empty nomenclature/combo results, missing product/terminal/combo codes before SDK invocation, and validators that never include product/menu data in failure text.

- [ ] **Step 2: Run and verify RED**

```bash
PYTHONDONTWRITEBYTECODE=1 uv run --frozen --offline pytest -q \
  tests/live_support/read_cases/test_menu.py
```

Expected: menu case module does not exist.

- [ ] **Step 3: Implement exact requests and providers**

```text
get_nomenclature:
  request organizationId and startRevision=0;
  extract the first non-deleted purchasable product UUID and its numeric price
  when present, plus an immutable lookup of every unambiguous purchasable
  product-size price needed only for later combo construction.

get_combos_info:
  depend on get_nomenclature and request organizationId;
  extract the first active specification with a source action and non-empty
  groups only when one product from every group has an exact response-derived
  nomenclature price; build generated product order items with one shared fresh
  client-side comboId, otherwise publish no combo_items.

calculate_combo_price:
  depend on get_combos_info and get_nomenclature;
  use only generated order-item models derived from those responses;
  return combo_unavailable before rate acquisition when no complete combo exists.

get_stop_lists:
  request exactly [organization_id], returnSize=True, and at most the validated terminal group filter.

check_products_in_stop_list:
  depend on get_nomenclature and get_terminal_groups;
  require one product and validated terminal group;
  send exactly one generated DeliveryOrderCreateProductItem with the
  `type="Product"` discriminator through CheckStopListRequest.items.

get_external_menus:
  NO_REQUEST;
  confirm profile_external_menu_id occurs in the returned collection before providing external_menu_id.

get_external_menu_by_id:
  depend on get_external_menus;
  request exactly one organization and the validated external menu ID, asyncMode=False.
```

- [ ] **Step 4: Verify and commit**

```bash
PYTHONDONTWRITEBYTECODE=1 uv run --frozen --offline pytest -q \
  tests/live_support/read_cases/test_menu.py
PYTHONDONTWRITEBYTECODE=1 uv run --frozen --offline ruff check \
  tests/integration/read/cases/menu.py \
  tests/live_support/read_cases/test_menu.py
```

Expected: seven exact cases pass offline.

```bash
git add tests/integration/read/cases/menu.py \
  tests/live_support/read_cases/test_menu.py
git commit -m "test: cover iiko menu reads"
```

### Task 12: Implement delivery retrieval, restrictions, and draft cases

**Files:**
- Create: `tests/integration/read/cases/deliveries.py`
- Create: `tests/live_support/read_cases/test_deliveries.py`

**Interfaces:**
- Consumes: `organization_id`, bounded seed windows, optional product data, Appendix B bindings.
- Produces: ten cases and uniquely named keys `search_delivery_id`, `status_delivery_id`, `search_delivery_phone`, `status_delivery_phone`, `search_delivery_revision`, `status_delivery_revision`, `search_delivery_customer_id`, `status_delivery_customer_id`, `draft_id`.

- [ ] **Step 1: Write the exact case-set test**

```python
DELIVERY_IDS = {
    "get_allowed_delivery_restrictions",
    "get_deliveries_by_delivery_date_and_phone",
    "get_deliveries_by_delivery_date_and_status",
    "get_deliveries_by_id",
    "get_deliveries_by_revision",
    "get_delivery_draft_by_id",
    "get_delivery_drafts_by_filter",
    "get_delivery_history_by_delivery_date_and_phone",
    "get_delivery_restrictions",
    "search_deliveries",
}
```

Test a non-empty synthetic order response and each empty-provider branch. Assert phone/customer/order values remain only in hidden context and never appear in exception strings, outcomes, or repr.

- [ ] **Step 2: Run and verify RED**

```bash
PYTHONDONTWRITEBYTECODE=1 uv run --frozen --offline pytest -q \
  tests/live_support/read_cases/test_deliveries.py
```

Expected: delivery case module does not exist.

- [ ] **Step 3: Implement bounded foundation queries**

`search_deliveries` uses exactly one organization, the exact seeded bounded local
window, `rowsCount=1`, schema-supported `CompleteBefore` plus `Ascending`
ordering, and no free-text filter. Equal `CompleteBefore` values remain
server-ordered because the schema exposes no stable tie-break field.
`get_deliveries_by_delivery_date_and_status` uses the same exact seeded window
and no status expansion; its generated request exposes neither a row limit nor
sorting fields. Each provider uses its own `search_*` or `status_*` keys for
order ID, phone, customer ID, and revision; only response-provided values are
copied into hidden context.

`get_delivery_drafts_by_filter` uses the same organization/window with `offset=0`, `limit=1`; it provides `draft_id` only when present. `get_delivery_restrictions` uses exactly one organization. `get_allowed_delivery_restrictions` sends the smallest generated request accepted by the effective schema: `organizationId`, `isCourierDelivery=False`, `deliverySum=0`, `discountSum=0`, and an empty generated order-item list.

- [ ] **Step 4: Implement target-dependent reads**

```text
get_deliveries_by_id: choose search_delivery_id, then status_delivery_id; otherwise delivery_unavailable.
get_deliveries_by_delivery_date_and_phone: choose search_delivery_phone, then status_delivery_phone.
get_delivery_history_by_delivery_date_and_phone: choose the same fixed phone priority, rowsCount=1, bounded dates.
get_deliveries_by_revision: choose search_delivery_revision, then status_delivery_revision; require non-negative value.
get_delivery_draft_by_id: require response-derived draft_id.
```

All missing codes occur in `build_values` before the generated adapter call.

- [ ] **Step 5: Verify and commit**

```bash
PYTHONDONTWRITEBYTECODE=1 uv run --frozen --offline pytest -q \
  tests/live_support/read_cases/test_deliveries.py
PYTHONDONTWRITEBYTECODE=1 uv run --frozen --offline ruff check \
  tests/integration/read/cases/deliveries.py \
  tests/live_support/read_cases/test_deliveries.py
```

Expected: ten cases pass offline.

```bash
git add tests/integration/read/cases/deliveries.py \
  tests/live_support/read_cases/test_deliveries.py
git commit -m "test: cover iiko delivery reads"
```

### Task 13: Implement reserve, restaurant-section, and table-order cases

**Files:**
- Create: `tests/integration/read/cases/reserves_orders.py`
- Create: `tests/live_support/read_cases/test_reserves_orders.py`

**Interfaces:**
- Consumes: `organization_id`, validated terminal group, bounded windows, Appendix B bindings.
- Produces: seven cases and keys `reserve_terminal_group_id`, `restaurant_section_id`, `table_id`, `reserve_id`, `table_order_id`, and optional hidden `table_order_customer_id`.

- [ ] **Step 1: Write the exact case-set test**

```python
RESERVE_ORDER_IDS = {
    "get_reserve_available_organizations",
    "get_reserve_restaurant_sections",
    "get_reserve_statuses_by_id",
    "get_reserve_terminal_groups",
    "get_restaurant_sections_workload",
    "get_table_orders_by_id",
    "get_table_orders_by_table",
}
```

Test empty terminal/section/table/workload/order results and ensure every missing-target code is emitted before SDK invocation.

- [ ] **Step 2: Run and verify RED**

```bash
PYTHONDONTWRITEBYTECODE=1 uv run --frozen --offline pytest -q \
  tests/live_support/read_cases/test_reserves_orders.py
```

Expected: module does not exist.

- [ ] **Step 3: Implement the read-only dependency chain**

```text
get_reserve_available_organizations -> validate selected organization
get_reserve_terminal_groups -> first terminal group for selected organization
get_reserve_restaurant_sections -> first section and first table for that terminal group
get_restaurant_sections_workload -> bounded window for exactly one section; provide reserve_id if present
get_reserve_statuses_by_id -> exactly one response-derived reserve ID or reserve_unavailable
get_table_orders_by_table -> exactly one response-derived table ID and bounded window; provide table_order_id and only a present customer UUID
get_table_orders_by_id -> exactly one response-derived table order ID or table_order_unavailable
```

Prefer the validated profile terminal only when the reserve terminal response confirms it; otherwise use the first returned terminal. Do not create a reserve or table order.

- [ ] **Step 4: Verify and commit**

```bash
PYTHONDONTWRITEBYTECODE=1 uv run --frozen --offline pytest -q \
  tests/live_support/read_cases/test_reserves_orders.py
PYTHONDONTWRITEBYTECODE=1 uv run --frozen --offline ruff check \
  tests/integration/read/cases/reserves_orders.py \
  tests/live_support/read_cases/test_reserves_orders.py
```

Expected: seven cases pass offline.

```bash
git add tests/integration/read/cases/reserves_orders.py \
  tests/live_support/read_cases/test_reserves_orders.py
git commit -m "test: cover iiko reserve and table reads"
```

### Task 14: Implement employee and courier cases without leaking PII

**Files:**
- Create: `tests/integration/read/cases/employees.py`
- Create: `tests/live_support/read_cases/test_employees.py`

**Interfaces:**
- Consumes: `organization_id`, validated terminal group, Appendix B bindings.
- Produces: eight cases, hidden `courier_employee_id`, and an optional hidden
  `employee_role_code` only if a separately reviewed provider is added later.
  The current generated courier response contains no role code.

- [ ] **Step 1: Write the exact case-set test**

```python
EMPLOYEE_IDS = {
    "get_active_courier_locations",
    "get_active_courier_locations_by_terminal",
    "get_courier_location_history",
    "get_couriers",
    "get_couriers_by_role",
    "get_employee_info",
    "get_personal_session_info",
    "get_terminal_groups_of_employee",
}
```

Use synthetic identifiers/names/coordinates and assert none appear in repr, outcomes, reports, or exception messages. Test empty couriers, missing terminal, and missing role.

- [ ] **Step 2: Run and verify RED**

```bash
PYTHONDONTWRITEBYTECODE=1 uv run --frozen --offline pytest -q \
  tests/live_support/read_cases/test_employees.py
```

Expected: employee case module does not exist.

- [ ] **Step 3: Implement bounded employee requests**

`get_couriers`, `get_active_courier_locations`, and `get_courier_location_history` use exactly `[organization_id]`; location history uses `offsetInSeconds=0`. `get_active_courier_locations_by_terminal` requires the validated terminal group. Extract one courier employee ID from `get_couriers` without retaining names, phones, or coordinates.

`get_employee_info`, `get_personal_session_info`, and `get_terminal_groups_of_employee` use only that response-derived employee as their employee target. The generated employee-info request also requires the selected organization, while personal-session info requires both the selected organization and validated terminal; terminal-groups-of-employee takes only the employee ID. `get_couriers_by_role` requires a non-empty short role code because generated `rolesToCheck` is `List[str]`, not a role UUID. The current generated `get_couriers` response has no role field, and `EmployeeDirectoryEntry.code` is an employee code rather than a role code, so do not infer or publish a role target from it. Until a separate reviewed role-code provider exists, return `employee_role_unavailable` before rate acquisition. Validators check generated response shape and request linkage, not PII values.

- [ ] **Step 4: Verify and commit**

```bash
PYTHONDONTWRITEBYTECODE=1 uv run --frozen --offline pytest -q \
  tests/live_support/read_cases/test_employees.py
PYTHONDONTWRITEBYTECODE=1 uv run --frozen --offline ruff check \
  tests/integration/read/cases/employees.py \
  tests/live_support/read_cases/test_employees.py
```

Expected: eight cases pass offline and the synthetic leakage scan passes.

```bash
git add tests/integration/read/cases/employees.py \
  tests/live_support/read_cases/test_employees.py
git commit -m "test: cover iiko employee reads safely"
```

### Task 15: Implement loyalty, customer, coupon, SMS, and report cases

**Files:**
- Create: `tests/integration/read/cases/loyalty.py`
- Create: `tests/live_support/read_cases/test_loyalty.py`

**Interfaces:**
- Consumes: `organization_id`, product data, response-derived customer/phone IDs, Appendix B bindings.
- Produces: 13 cases and hidden keys `coupon_series`, `coupon_number`, `customer_id`.

- [ ] **Step 1: Write the exact case-set test**

```python
LOYALTY_IDS = {
    "calculate_loyalty_checkin",
    "check_sms_sending_possibility",
    "check_sms_status",
    "get_coupon_info",
    "get_coupon_series",
    "get_customer_categories",
    "get_customer_info",
    "get_customer_transactions_by_date",
    "get_customer_transactions_by_revision",
    "get_loyalty_counters",
    "get_loyalty_manual_conditions",
    "get_loyalty_programs",
    "get_non_activated_coupons_by_series",
}
```

Test discriminator construction for `GetCustomerInfoByIdRequest`, coupon series
with/without a non-empty series number, non-activated responses with/without a
coupon number, SMS ID absence, customer absence, generated report aliases, and
scans for synthetic phone/email/card/coupon/customer values.

- [ ] **Step 2: Run and verify RED**

```bash
PYTHONDONTWRITEBYTECODE=1 uv run --frozen --offline pytest -q \
  tests/live_support/read_cases/test_loyalty.py
```

Expected: loyalty case module does not exist.

- [ ] **Step 3: Implement direct organization reads and coupon chain**

`get_customer_categories`, `get_loyalty_manual_conditions`, `get_loyalty_programs`, `get_coupon_series`, and `check_sms_sending_possibility` use only `organization_id`. Extract a series and coupon number only from explicit generated coupon response fields. Then:

```text
get_non_activated_coupons_by_series -> one response-derived series, page=0, pageSize=1
get_coupon_info -> one response-derived coupon number and optional series
check_sms_status -> sms_unavailable because no read-only provider exists in this stage
```

- [ ] **Step 4: Implement customer-dependent reads and pure calculation**

Choose a response-derived customer UUID in the fixed order `search_delivery_customer_id`, `status_delivery_customer_id`, then a table-order customer key when present. Bind `get_customer_info` to `iikocloud_client.models.get_customer_info_by_id_request.GetCustomerInfoByIdRequest`, which is a generated subclass accepted by the API's base request annotation; values are `type="id"`, `id=str(<hidden customer UUID>)`, and `organizationId` because the concrete generated `id` field is `StrictStr`.

After a successful customer response, provide only `customer_id`. Use it for
counters and both bounded transaction reports. The date report uses the seeded
period with `pageNumber=0` and `pageSize=1`, and may publish the first
non-negative transaction revision. The revision report has no date or page
number fields; use `pageSize=1` and that response-derived revision when present,
otherwise `revision=0`, which its generated optional `StrictInt` field permits.

`calculate_loyalty_checkin` is a calculation-only call. Build its generated
order from `product_id`, `product_price`, and the exact matching entry in
`nomenclature_prices`, plus the first available
`search_delivery_phone`/`status_delivery_phone`. Use one concrete generated
`DeliveryOrderCreateProductItem` with `type="Product"`, `amount=1`, its price,
and the matching `productSizeId` when non-null; use `payments=[]`, omit customer
mutation fields, set top-level campaign IDs to `[]`, and disable loyalty
tracing. If a complete product tuple or phone is absent, return
`product_unavailable` or `delivery_phone_unavailable` before HTTP.

- [ ] **Step 5: Verify and commit**

```bash
PYTHONDONTWRITEBYTECODE=1 uv run --frozen --offline pytest -q \
  tests/live_support/read_cases/test_loyalty.py
PYTHONDONTWRITEBYTECODE=1 uv run --frozen --offline ruff check \
  tests/integration/read/cases/loyalty.py \
  tests/live_support/read_cases/test_loyalty.py
```

Expected: 13 cases pass offline and no synthetic sensitive value appears in safe artifacts.

```bash
git add tests/integration/read/cases/loyalty.py \
  tests/live_support/read_cases/test_loyalty.py
git commit -m "test: cover iiko loyalty reads safely"
```

### Task 16: Implement finance document and transaction read cases

**Files:**
- Create: `tests/integration/read/cases/finance.py`
- Create: `tests/live_support/read_cases/test_finance.py`

**Interfaces:**
- Consumes: `organization_id`, seeded `YYYY-MM-DD` period, document/store/account keys from finance or inventory providers, Appendix B bindings.
- Produces: six cases and unique `finance_*_document_id`/`finance_*_account_id` keys.

- [ ] **Step 1: Write the exact case-set test**

```python
FINANCE_IDS = {
    "get_finance_incoming_service",
    "get_finance_outgoing_service",
    "list_finance_account_transactions",
    "list_finance_document_transactions",
    "list_finance_incoming_services",
    "list_finance_outgoing_services",
}
```

Test `ListRequest.var_from` serializes as `from`, list-to-get ID linkage, empty lists, document choice across all declared family keys, and account absence before SDK invocation.

- [ ] **Step 2: Run and verify RED**

```bash
PYTHONDONTWRITEBYTECODE=1 uv run --frozen --offline pytest -q \
  tests/live_support/read_cases/test_finance.py
```

Expected: finance case module does not exist.

- [ ] **Step 3: Implement period-list and document-get factories**

Implement `make_period_list_case(operation_id, binding, document_key, account_keys, store_keys)` with `ListRequest(var_from, organization_id=str(organization_id), to)` and `make_document_get_case(operation_id, binding, provider_operation_id, document_key)` with `GetByIDRequest(document_id, organization_id=str(organization_id))`. The shared context stores the organization as `UUID`, while every generated finance request declares its GUID fields as `StrictStr`. Keep generated API class/method/keyword explicit per Appendix B; do not infer the class from the URL or operation prefix.

Incoming/outgoing list responses are bare generated-model lists. Each list case chooses a non-deleted item with a non-empty GUID-shaped document string, then provides its own document and revenue-account keys from that same item; these schemas expose no expense-account or store field. Corresponding gets require exactly their family document ID and validate that the exact generated response model contains the requested string identifier.

- [ ] **Step 4: Implement transaction target selection**

`list_finance_document_transactions` may read the declared document keys from all 12 finance/inventory list providers and chooses the first valid value in a fixed tuple order. Its generated request exposes only `documentId` and `organizationId`, so it must not receive date fields. `list_finance_account_transactions` similarly chooses a response-derived revenue/expense/from/to account ID and is the only transaction request that consumes the seeded bounded date period. If a target is absent, return `document_unavailable` or `account_unavailable` before SDK/rate access. Validate the document-transactions response as a bare list of exact `DocumentTransactionItem` models and the account response as the exact `AccountTransactionsResponse` model.

- [ ] **Step 5: Verify and commit**

```bash
PYTHONDONTWRITEBYTECODE=1 uv run --frozen --offline pytest -q \
  tests/live_support/read_cases/test_finance.py
PYTHONDONTWRITEBYTECODE=1 uv run --frozen --offline ruff check \
  tests/integration/read/cases/finance.py \
  tests/live_support/read_cases/test_finance.py
```

Expected: six cases pass offline.

```bash
git add tests/integration/read/cases/finance.py \
  tests/live_support/read_cases/test_finance.py
git commit -m "test: cover iiko finance reads"
```

### Task 17: Implement inventory document, counteragent, and cost-price read cases

**Files:**
- Create: `tests/integration/read/cases/inventory.py`
- Create: `tests/live_support/read_cases/test_inventory.py`

**Interfaces:**
- Consumes: organization/date period, nomenclature product, finance factory behavior, Appendix B bindings.
- Produces: 22 cases plus family-specific document/store/account keys.

- [ ] **Step 1: Write the exact case-set test**

```python
INVENTORY_IDS = {
    "calculate_inventory_cost_prices",
    "get_inventory_counteragents",
    "get_inventory_disassemble_document",
    "get_inventory_incoming_invoice",
    "get_inventory_incoming_returned_invoice",
    "get_inventory_internal_transfer",
    "get_inventory_outgoing_invoice",
    "get_inventory_production_document",
    "get_inventory_returned_invoice",
    "get_inventory_sales_document",
    "get_inventory_transformation_document",
    "get_inventory_writeoff_document",
    "list_inventory_disassemble_documents",
    "list_inventory_incoming_invoices",
    "list_inventory_incoming_returned_invoices",
    "list_inventory_internal_transfers",
    "list_inventory_outgoing_invoices",
    "list_inventory_production_documents",
    "list_inventory_returned_invoices",
    "list_inventory_sales_documents",
    "list_inventory_transformation_documents",
    "list_inventory_writeoff_documents",
}
```

For each of the ten list/get pairs, parameterize exact operation ID, API class, request keyword, exact bare-list item and get-response model, activity field, response document field, and family context key. Test empty lists, same-item extraction, and ID linkage. Separately test counteragent pagination, cost-price product/store absence, the fixed store priority, and exact wrapper response models.

- [ ] **Step 2: Run and verify RED**

```bash
PYTHONDONTWRITEBYTECODE=1 uv run --frozen --offline pytest -q \
  tests/live_support/read_cases/test_inventory.py
```

Expected: inventory case module does not exist.

- [ ] **Step 3: Implement all ten explicit list/get pairs**

Use keyword-only `ListRequest(var_from, organization_id=str(organization_id), to)` for each list and `GetByIDRequest(document_id, organization_id=str(organization_id))` for each get because all generated inventory GUID request fields are `StrictStr`. The ten families are:

```text
disassemble_document
incoming_invoice
incoming_returned_invoice
internal_transfer
outgoing_invoice
production_document
returned_invoice
sales_document
transformation_document
writeoff_document
```

Factories may share value and validation logic, but every `GeneratedReadBinding` remains explicit. All list responses are bare lists; incoming/outgoing invoice list and get operations both use the same `IncomingInvoice`/`OutgoingInvoice` model, while the other eight families have distinct list-item/get-response models. Select the other eight families only when `deleted is False`; select incoming/outgoing invoices only when `status` is exactly `NEW` or `PROCESSED`. Extract only canonical document/store/account GUID strings from the same selected list item; discard products, counteragent names, comments, amounts, and all other document content.

- [ ] **Step 4: Implement counteragent and cost-price cases**

`get_inventory_counteragents` uses `organizationId=str(organization_id)`, `offset=0`, `limit=1`, with no unbounded type expansion, and validates the exact `GetCounteragentsResponse` wrapper. `calculate_inventory_cost_prices` is bound to `PublicApiInvoiceProcessingOutgoingInvoicesApi` exactly as generated, not inferred from its costings path, and validates the exact `GetCostPricesResponse` wrapper. It requires one nomenclature product and one store ID derived from explicit `storeFrom`, `storeTo`, `defaultStore`, or `assignedStores` fields in prior list responses; request one generated `PriceItem(amountFactor=1, productId=str(product_id), storeId=<canonical string>)`. Convert the UTC-derived `date_yyyy_mm_dd` seed to the full timestamp `YYYY-MM-DDT00:00:00.000+00:00` required by the documented API shape. Missing values return `product_unavailable`/`store_unavailable` before HTTP.

Choose cost-price stores in this fixed family/field order:

```text
inventory_disassemble_document_store_from_id
inventory_disassemble_document_store_to_id
inventory_incoming_invoice_default_store_id
inventory_incoming_returned_invoice_assigned_store_id
inventory_internal_transfer_store_from_id
inventory_internal_transfer_store_to_id
inventory_outgoing_invoice_default_store_id
inventory_production_document_store_from_id
inventory_production_document_store_to_id
inventory_returned_invoice_assigned_store_id
inventory_sales_document_assigned_store_id
inventory_transformation_document_store_from_id
inventory_transformation_document_store_to_id
inventory_writeoff_document_store_from_id
```

- [ ] **Step 5: Verify and commit**

```bash
PYTHONDONTWRITEBYTECODE=1 uv run --frozen --offline pytest -q \
  tests/live_support/read_cases/test_inventory.py
PYTHONDONTWRITEBYTECODE=1 uv run --frozen --offline ruff check \
  tests/integration/read/cases/inventory.py \
  tests/live_support/read_cases/test_inventory.py
```

Expected: 22 cases pass offline.

```bash
git add tests/integration/read/cases/inventory.py \
  tests/live_support/read_cases/test_inventory.py
git commit -m "test: cover iiko inventory reads"
```

### Task 18: Assemble the exact 91-case registry and enforce four-way parity

**Files:**
- Create: `tests/integration/read/cases/__init__.py`
- Modify: `tests/live_support/test_read_planner.py`
- Modify: `tests/live_support/test_pytest_gates.py`
- Modify: `tests/integration/read/test_all_reads.py`
- Modify: `tests/integration/read/test_selected_read.py`
- Modify: `tests/conftest.py`

**Interfaces:**
- Consumes: all nine domain tuples.
- Produces: `ALL_READ_CASES: tuple[ReadCase, ...]`, `FULL_READ_PLAN = ReadPlan.build(ALL_READ_CASES)`, and executable preflight parity.

- [ ] **Step 1: Assemble registry in a fixed import order**

```python
ALL_READ_CASES = (
    *FOUNDATION_CASES,
    *ADDRESS_CASES,
    *MENU_CASES,
    *DELIVERY_CASES,
    *RESERVE_ORDER_CASES,
    *EMPLOYEE_CASES,
    *LOYALTY_CASES,
    *FINANCE_CASES,
    *INVENTORY_CASES,
)
FULL_READ_PLAN = ReadPlan.build(ALL_READ_CASES)
```

The planner, not tuple order, determines execution order.

- [ ] **Step 2: Add exact real-repository parity tests**

```python
assert len(FULL_READ_PLAN.cases) == 91
assert set(FULL_READ_PLAN.ordered_operation_ids) == set(safety.automatic_read_ids)
assert set(safety.automatic_read_ids) == live_contract_read_ids
assert all(rate_catalog.operation_budget(op) for op in safety.automatic_read_ids)
assert set(rate_catalog.operation_ids) <= set(live_operation_ids)
assert safety.operations["authenticate"].live_policy is LivePolicy.AUTOMATIC
assert safety.operations["authenticate_v2"].live_policy is LivePolicy.BLOCKED
assert "authenticate_v2" not in live_operation_ids
```

Resolve every Appendix B binding against the committed generated package and assert all body/no-body triples and exact method names.

- [ ] **Step 3: Verify expected no-target coverage**

Assert every context-dependent case declares one or more allowed codes and each declared code is exercised by an offline test. At minimum, the registry has explicit no-target coverage for command, SMS, role, city/street, terminal, product/combo, delivery/phone/revision/draft, reserve/section/table/table-order, customer/coupon, document/account/store.

- [ ] **Step 4: Run the registry and preflight suites in fresh processes**

```bash
PYTHONDONTWRITEBYTECODE=1 uv run --frozen --offline pytest -q \
  tests/live_support/test_read_planner.py \
  tests/live_support/test_pytest_gates.py
PYTHONDONTWRITEBYTECODE=1 uv run --frozen --offline pytest -q \
  tests/live_support/read_cases/test_foundation.py \
  tests/live_support/read_cases/test_menu.py \
  tests/live_support/read_cases/test_deliveries.py \
  tests/live_support/read_cases/test_reserves_orders.py
PYTHONDONTWRITEBYTECODE=1 uv run --frozen --offline pytest -q \
  tests/live_support/read_cases/test_employees.py \
  tests/live_support/read_cases/test_loyalty.py \
  tests/live_support/read_cases/test_finance.py \
  tests/live_support/read_cases/test_inventory.py
```

Expected: all pass; public diagnostics contain only counts/operation IDs.

- [ ] **Step 5: Commit the executable registry**

```bash
git add tests/integration/read/cases/__init__.py \
  tests/live_support/test_read_planner.py \
  tests/live_support/test_pytest_gates.py \
  tests/integration/read/test_all_reads.py \
  tests/integration/read/test_selected_read.py tests/conftest.py
git commit -m "feat: register every guarded iiko read"
```

### Task 19: Document operation, run the complete offline gate, and review the branch

**Files:**
- Modify: `docs/generation.md`
- Modify: `private/README.md`
- Modify only if a verified recurring workaround was needed: `docs/troubleshooting.md`

**Interfaces:**
- Consumes: final commands/statuses and existing generation/correction documentation.
- Produces: operator runbook for full reads, selected capture, safe triage, and future upstream changes.

- [ ] **Step 1: Add the operator instructions**

Document the exact full command:

```bash
PYTHONDONTWRITEBYTECODE=1 uv run --frozen --offline pytest \
  -m live_read_full -n0 \
  --live-profile amato --env-file .env \
  tests/integration/read/test_all_reads.py
```

Explain every flag, especially that uv's `--offline` does not disable iiko HTTP. State that 92 potential requests (one auth plus 91 reads) impose a 45 minute 30 second cadence floor when every case reaches HTTP; persisted stricter per-operation state can make it longer, especially `get_external_menus` at a 9000-second effective interval. Missing targets shorten the run because they consume no rate budget and send no HTTP.

Document the selected capture command:

```bash
PYTHONDONTWRITEBYTECODE=1 uv run --frozen --offline pytest \
  -m live_read_selected -n0 \
  --live-profile amato --env-file .env \
  --capture-http --capture-operation get_nomenclature \
  tests/integration/read/test_selected_read.py
```

State that it runs the canary/dependency closure but captures only `get_nomenclature`, writes sanitized ignored files below `private/captures/`, never captures auth, and cannot be combined with the full runner.

- [ ] **Step 2: Document result interpretation and schema correction**

Define `passed`, `no_live_target`, `failed`, and `aborted`; explain continuation versus global abort. For a confirmed upstream schema issue, instruct the operator to save no private payload in Git, add the smallest public synthetic fixture, change the appropriate overlay/operation-ID/model-name registry, regenerate, rerun all offline gates, and only then schedule another guarded call. State the `429` rule verbatim: stop the entire run; no retry; no second key; investigate and manually reset later.

- [ ] **Step 3: Run formatting, type, security, and focused tests**

```bash
git diff --check
PYTHONDONTWRITEBYTECODE=1 uv run --frozen --offline ruff check tools tests
PYTHONDONTWRITEBYTECODE=1 uv run --frozen --offline mypy tools/openapi_pipeline
PYTHONDONTWRITEBYTECODE=1 uv run --frozen --offline python -m tools.openapi_pipeline verify-no-secrets
PYTHONDONTWRITEBYTECODE=1 uv run --frozen --offline pytest -q tests/live_support
```

Expected: every command exits 0. If the live-support command reproduces the documented long-pytest process crash, run its files in the already listed fresh-process groups; do not change assertions or omit a file.

- [ ] **Step 4: Run the remaining offline suite and generator verification**

```bash
PYTHONDONTWRITEBYTECODE=1 uv run --frozen --offline pytest -q tests \
  --ignore=tests/live_support \
  --ignore=tests/capture
PYTHONDONTWRITEBYTECODE=1 uv run --frozen --offline pytest -q tests/capture
PYTHONDONTWRITEBYTECODE=1 uv run --frozen --offline python -m tools.openapi_pipeline verify
```

Expected: all commands exit 0; no live marker is selected. `verify` may use the already pinned generator container but performs no iiko live API call.

- [ ] **Step 5: Review tracked and ignored boundaries**

Run only metadata-safe checks:

```bash
git status --short
git diff --stat
git diff --name-status
```

Do not display `.env`, `private/`, `.state/`, captures, reports, receipts, or journals. Confirm no generated API/model file was hand-edited and no unexpected file is tracked.

- [ ] **Step 6: Commit the runbook and any verified workaround**

```bash
git add docs/generation.md private/README.md
git add docs/troubleshooting.md  # only when this task added a verified sanitized entry
git commit -m "docs: explain exhaustive guarded live reads"
```

### Task 20: Execute one controlled full read run on Amato and triage without retry

**Files:**
- No tracked file is changed merely because a live run occurred.
- Modify correction-layer files and synthetic tests only if the run provides confirmed evidence of an upstream contract defect.

**Interfaces:**
- Consumes: completed Tasks 1–19, private `amato` profile metadata, `IIKO_API_KEY` from the explicitly selected root `.env`, persistent lock/rate/circuit state.
- Produces: one private ignored report/receipt, optional one-operation sanitized capture only in a separately announced diagnostic run, and an evidence-backed pass/failure summary.

- [ ] **Step 1: Re-run the no-live preflight immediately before credentials are used**

```bash
git status --short --branch
PYTHONDONTWRITEBYTECODE=1 uv run --frozen --offline pytest -q \
  tests/live_support/test_operation_safety.py \
  tests/live_support/test_rates.py \
  tests/live_support/test_read_planner.py \
  tests/live_support/test_pytest_gates.py \
  tests/live_support/test_read_runner.py
```

Expected: the branch is correct and focused offline gates pass. Do not inspect the profile or `.env` contents.

- [ ] **Step 2: Announce the consequential run and start exactly once**

Tell the user that the next command can make up to 92 serial live requests, has a 45:30 cadence floor, may wait longer for persisted stricter budgets, and will stop on the first unsafe condition. Then run exactly:

```bash
PYTHONDONTWRITEBYTECODE=1 uv run --frozen --offline pytest \
  -m live_read_full -n0 \
  --live-profile amato --env-file .env \
  tests/integration/read/test_all_reads.py
```

Do not add `-s`, verbose HTTP logging, shell tracing, retries, xdist, capture flags, or a second test path. Poll the running process often enough to keep the user informed, but never print request/response/profile data.

- [ ] **Step 3: Apply the terminal result policy**

```text
Exit 0:
  accept the run only after fixture teardown verifies closed clients, closed circuit,
  absent mutation journals, completed safe report, and completed receipt.

429 or open circuit:
  stop the entire task immediately; do not retry, reset state, run cleanup, or use IIKO_API_KEY_2;
  report only that 429 occurred and manual investigation/reset is required.

Other HTTP/transport/deserialization/safety abort:
  do not rerun; inspect only public code/schema and normalized safe outcome codes;
  add an offline regression before any correction.

Assertion/extractor failure after 2xx:
  identify the exact operation from the safe outcome, reproduce with a synthetic fixture,
  correct the case or schema offline, and schedule a later run rather than looping now.
```

- [ ] **Step 4: Use selected capture only for a justified schema diagnosis**

If public schema and synthetic evidence are insufficient and the failed operation is a reviewed read, announce one additional diagnostic call. Use the selected command from Task 19 with that exact operation ID. The persistent guard enforces all elapsed limits. Never capture auth or a write, never capture the full run, and never copy private capture content into tracked files or tool output.

- [ ] **Step 5: Correct confirmed defects through the existing layers**

Choose exactly one correction mechanism based on evidence:

```text
wrong public operation name       -> openapi/operation-ids.yaml
wrong request/response schema     -> guarded file in openapi/overlays/
confirmed generated model name    -> openapi/model-name-overrides.yaml
oneOf/polymorphism regression      -> minimal public synthetic fixture plus guarded overlay
test-only dependency/validator bug -> tests/integration/read/cases/<domain>.py and offline test
```

Regenerate the entire SDK and repeat Tasks 18–19 offline. A new live run is a separately announced later action, not an automatic retry in this task.

- [ ] **Step 6: Report completion without exposing private values**

Provide only: command exit result; counts of `passed`, `no_live_target`, `failed`, `aborted`; safe operation IDs for non-passed outcomes; whether `429` occurred; whether both clients closed; whether the receipt completed; and tracked commit IDs. Never quote report/capture/profile/env contents.

## Acceptance checklist

- [ ] `contracts/operation-safety.yaml` is a strict exact bijection with 225 effective operations.
- [ ] The catalog contains exactly 91 `read/automatic`, one `auth/automatic`, one `auth/blocked`, and the 132 reviewed non-read classifications in Appendix A.
- [ ] The executable read allowlist, verified read test budgets, and `ReadCase` registry each contain exactly the same 91 operation IDs.
- [ ] All 91 bindings resolve to the exact generated API method and request type/keyword in Appendix B.
- [ ] Global auth/read spacing is at least 30 seconds; known stricter persistent intervals win; each operation is called at most once.
- [ ] Missing safe targets yield only declared `no_live_target` before rate acquisition and HTTP.
- [ ] Assertion/extractor failures may continue only independent branches; deserialization/HTTP/transport/rate/state/receipt/report/cancellation failures abort all later HTTP.
- [ ] Any 429 opens the persistent circuit and causes zero retry/key fallback/cleanup.
- [ ] Full and selected runs require exact marker/path/`-n0` gates and remain excluded from ordinary pytest/CI.
- [ ] Reports and captures are private, sanitized, atomic, non-symlink, owner-only, and absent from tracked diff.
- [ ] No write operation runs in this stage.
- [ ] All offline tests, Ruff, mypy, secret verification, package tests, and generator verification pass.
- [ ] One controlled Amato full run succeeds without 429; every available read is `passed`, every unavailable read has a reviewed `no_live_target`, and no case is `failed`/`aborted`.

## Appendix A: Exact 225-operation safety classification ledger

The catalog implementation must match these partitions exactly. Counts are part of the contract and sum to 225.

### Auth

- `auth/automatic` (1): `authenticate`.
- `auth/blocked` (1): `authenticate_v2`.

### Reads

- `read/automatic` (91): every operation in Appendix B.

Deprecated `list_organizations`, sensitive-response reads, calculations, and reads that commonly lack a target remain automatic because they are non-mutating and explicitly requested for exhaustive verification. Their safety comes from typed requests, default no capture, sanitized private output, and `no_live_target` before HTTP—not from silently dropping them.

### Creates

- `create/lifecycle_only` (17):
  - Core: `create_delivery_order`, `create_delivery_draft`, `create_or_update_customer`, `create_table_order`, `create_reserve`.
  - Finance: `create_finance_incoming_service`, `create_finance_outgoing_service`.
  - Inventory: `create_inventory_disassemble_document`, `create_inventory_incoming_invoice`, `create_inventory_incoming_returned_invoice`, `create_inventory_internal_transfer`, `create_inventory_outgoing_invoice`, `create_inventory_production_document`, `create_inventory_returned_invoice`, `create_inventory_sales_document`, `create_inventory_transformation_document`, `create_inventory_writeoff_document`.

### Updates

- `update/lifecycle_only` (43):
  - Delivery: `add_delivery_order_items`, `add_delivery_order_payments`, `change_delivery_comment`, `change_delivery_complete_before`, `change_delivery_point`, `change_delivery_driver_info`, `change_delivery_external_data`, `change_delivery_operator`, `change_delivery_payments`, `change_delivery_service_type`, `update_delivery_order_courier`, `update_delivery_order_problem`, `update_delivery_tracking_link`.
  - Draft: `save_delivery_draft`.
  - Customer/category: `add_customer_magnet_card`, `add_customer_to_program`, `add_customer_category`.
  - Table order: `add_customer_to_table_order`, `add_items_to_table_order`, `add_table_order_payments`, `change_table_order_external_data`, `change_table_order_payments`.
  - Reserve: `add_banquet_order_items`, `add_banquet_order_payments`, `change_reserve_estimated_start_time`, `change_banquet_order_items`, `change_reserve_tables`.
  - Menu: `add_products_to_stop_list`.
  - Finance: `update_finance_incoming_service`, `update_finance_outgoing_service`.
  - Inventory documents: `update_inventory_disassemble_document`, `update_inventory_incoming_invoice`, `update_inventory_incoming_returned_invoice`, `update_inventory_internal_transfer`, `update_inventory_outgoing_invoice`, `update_inventory_production_document`, `update_inventory_returned_invoice`, `update_inventory_sales_document`, `update_inventory_transformation_document`, `update_inventory_writeoff_document`.
  - Inventory patches: `set_inventory_incoming_invoice_payment_date`, `set_inventory_outgoing_invoice_payment_date`, `update_inventory_product_barcodes`.
- `update/manual_only` (1): `update_delivery_order_status`.
- `update/blocked` (2): `update_delivery_order_payments`, `update_webhook_settings`.

### Deletes/cancellations

- `delete/lifecycle_only` (20):
  - Core: `cancel_delivery_order`, `delete_delivery_draft`, `remove_customer_magnet_card`, `delete_customers`, `remove_customer_category`, `cancel_table_order`, `cancel_reserve`, `remove_products_from_stop_list`.
  - Finance: `cancel_finance_incoming_service`, `cancel_finance_outgoing_service`.
  - Inventory: `cancel_inventory_disassemble_document`, `cancel_inventory_incoming_invoice`, `cancel_inventory_incoming_returned_invoice`, `cancel_inventory_internal_transfer`, `cancel_inventory_outgoing_invoice`, `cancel_inventory_production_document`, `cancel_inventory_returned_invoice`, `cancel_inventory_sales_document`, `cancel_inventory_transformation_document`, `cancel_inventory_writeoff_document`.

### Business actions

- `action/lifecycle_only` (32):
  - Core: `cancel_delivery_confirmation`, `confirm_delivery`, `commit_delivery_draft`, `lock_delivery_draft`, `unlock_delivery_draft`, `cancel_customer_balance_hold`, `hold_customer_balance`, `restore_customers`.
  - Finance: `post_finance_incoming_service`, `unpost_finance_incoming_service`, `post_finance_outgoing_service`, `unpost_finance_outgoing_service`.
  - Inventory post/unpost: `post_inventory_disassemble_document`, `unpost_inventory_disassemble_document`, `post_inventory_incoming_invoice`, `unpost_inventory_incoming_invoice`, `post_inventory_incoming_returned_invoice`, `unpost_inventory_incoming_returned_invoice`, `post_inventory_internal_transfer`, `unpost_inventory_internal_transfer`, `post_inventory_outgoing_invoice`, `unpost_inventory_outgoing_invoice`, `post_inventory_production_document`, `unpost_inventory_production_document`, `post_inventory_returned_invoice`, `unpost_inventory_returned_invoice`, `post_inventory_sales_document`, `unpost_inventory_sales_document`, `post_inventory_transformation_document`, `unpost_inventory_transformation_document`, `post_inventory_writeoff_document`, `unpost_inventory_writeoff_document`.
- `action/manual_only` (3): `initialize_table_orders_by_pos_orders`, `initialize_table_orders_by_tables`, `awake_terminal_groups`.

### Irreversible or externally/audit-visible effects

- `irreversible/manual_only` (13): `close_delivery_order`, `print_delivery_bill`, `print_table_order_bill`, `withdraw_customer_balance`, `top_up_customer_balance`, `send_loyalty_email`, `send_loyalty_sms`, `send_notification`, `open_personal_session`, `close_personal_session`, `close_table_order`, `add_inventory_incoming_invoice_payment`, `add_inventory_outgoing_invoice_payment`.
- `irreversible/blocked` (1): `clear_stop_list`.

Each YAML entry has a concise operation-specific reason. Use these reviewed reason rules: automatic read = non-mutating query/calculation; lifecycle create/update/delete/action = requires an owned entity and reviewed compensation; manual = external, financial, POS, status, printing, messaging, session, or finalization effect without safe automatic compensation; blocked = deprecated secret-bearing mutation, bulk destructive action, or auth contract not yet migrated.

## Appendix B: Exact 91 read method/path/generated binding ledger

API classes below are relative to `iikocloud_client.api.`. Request model modules are relative to `iikocloud_client.models.`. The generated method is always `<operation_id>_with_http_info`. `NO_REQUEST` means request module/class/keyword are all `None`.

```text
calculate_combo_price | POST /api/1/combo/calculate | menu_api.MenuApi | calculate_combo_price_request:calculate_combo_price_request.CalculateComboPriceRequest
calculate_inventory_cost_prices | POST /api/inventory/v1/costings/calculate | public_api_invoice_processing_outgoing_invoices_api.PublicApiInvoiceProcessingOutgoingInvoicesApi | get_cost_prices_request:get_cost_prices_request.GetCostPricesRequest
calculate_loyalty_checkin | POST /api/1/loyalty/iiko/calculate | discounts_and_promotions_api.DiscountsAndPromotionsApi | calculate_checkin_request:calculate_checkin_request.CalculateCheckinRequest
check_products_in_stop_list | POST /api/1/stop_lists/check | menu_api.MenuApi | check_stop_list_request:check_stop_list_request.CheckStopListRequest
check_sms_sending_possibility | POST /api/1/loyalty/iiko/check_sms_sending_possibility | messages_api.MessagesApi | sms_sending_possibility_request:sms_sending_possibility_request.SmsSendingPossibilityRequest
check_sms_status | POST /api/1/loyalty/iiko/check_sms_status | messages_api.MessagesApi | check_sms_status_request:check_sms_status_request.CheckSmsStatusRequest
check_terminal_groups_availability | POST /api/1/terminal_groups/is_alive | terminal_groups_api.TerminalGroupsApi | terminal_groups_is_alive_request:terminal_groups_is_alive_request.TerminalGroupsIsAliveRequest
get_active_courier_locations | POST /api/1/employees/couriers/active_location | employees_api.EmployeesApi | couriers_request:couriers_request.CouriersRequest
get_active_courier_locations_by_terminal | POST /api/1/employees/couriers/active_location/by_terminal | employees_api.EmployeesApi | active_courier_locations_by_terminal_group_request:active_courier_locations_by_terminal_group_request.ActiveCourierLocationsByTerminalGroupRequest
get_allowed_delivery_restrictions | POST /api/1/delivery_restrictions/allowed | delivery_restrictions_api.DeliveryRestrictionsApi | get_allowed_restrictions_request:get_allowed_restrictions_request.GetAllowedRestrictionsRequest
get_cancel_causes | POST /api/1/cancel_causes | dictionaries_api.DictionariesApi | cancel_causes_request:cancel_causes_request.CancelCausesRequest
get_cities | POST /api/1/cities | addresses_api.AddressesApi | cities_request:cities_request.CitiesRequest
get_combos_info | POST /api/1/combo | menu_api.MenuApi | get_combos_info_request:get_combos_info_request.GetCombosInfoRequest
get_command_status | POST /api/1/commands/status | operations_api.OperationsApi | get_command_status_request:get_command_status_request.GetCommandStatusRequest
get_coupon_info | POST /api/1/loyalty/iiko/coupons/info | discounts_and_promotions_api.DiscountsAndPromotionsApi | coupon_info_request:coupon_info_request.CouponInfoRequest
get_coupon_series | POST /api/1/loyalty/iiko/coupons/series | discounts_and_promotions_api.DiscountsAndPromotionsApi | series_with_not_activated_coupons_request:series_with_not_activated_coupons_request.SeriesWithNotActivatedCouponsRequest
get_courier_location_history | POST /api/1/employees/couriers/locations/by_time_offset | employees_api.EmployeesApi | courier_locations_by_time_offset_request:courier_locations_by_time_offset_request.CourierLocationsByTimeOffsetRequest
get_couriers | POST /api/1/employees/couriers | employees_api.EmployeesApi | couriers_request:couriers_request.CouriersRequest
get_couriers_by_role | POST /api/1/employees/couriers/by_role | employees_api.EmployeesApi | couriers_and_check_role_request:couriers_and_check_role_request.CouriersAndCheckRoleRequest
get_customer_categories | POST /api/1/loyalty/iiko/customer_category | customer_categories_api.CustomerCategoriesApi | get_categories_request:get_categories_request.GetCategoriesRequest
get_customer_info | POST /api/1/loyalty/iiko/customer/info | customers_api.CustomersApi | get_customer_info_request:get_customer_info_by_id_request.GetCustomerInfoByIdRequest
get_customer_transactions_by_date | POST /api/1/loyalty/iiko/customer/transactions/by_date | report_api.ReportApi | get_transactions_report_by_period_request:get_transactions_report_by_period_request.GetTransactionsReportByPeriodRequest
get_customer_transactions_by_revision | POST /api/1/loyalty/iiko/customer/transactions/by_revision | report_api.ReportApi | get_transactions_report_by_revision_request:get_transactions_report_by_revision_request.GetTransactionsReportByRevisionRequest
get_deliveries_by_delivery_date_and_phone | POST /api/1/deliveries/by_delivery_date_and_phone | deliveries_retrieve_api.DeliveriesRetrieveApi | orders_by_delivery_date_and_phone_request:orders_by_delivery_date_and_phone_request.OrdersByDeliveryDateAndPhoneRequest
get_deliveries_by_delivery_date_and_status | POST /api/1/deliveries/by_delivery_date_and_status | deliveries_retrieve_api.DeliveriesRetrieveApi | orders_by_delivery_date_and_status_request:orders_by_delivery_date_and_status_request.OrdersByDeliveryDateAndStatusRequest
get_deliveries_by_id | POST /api/1/deliveries/by_id | deliveries_retrieve_api.DeliveriesRetrieveApi | orders_by_id_request:orders_by_id_request.OrdersByIdRequest
get_deliveries_by_revision | POST /api/1/deliveries/by_revision | deliveries_retrieve_api.DeliveriesRetrieveApi | orders_by_revision_request:orders_by_revision_request.OrdersByRevisionRequest
get_delivery_draft_by_id | POST /api/1/deliveries/drafts/by_id | drafts_api.DraftsApi | get_draft_request:get_draft_request.GetDraftRequest
get_delivery_drafts_by_filter | POST /api/1/deliveries/drafts/by_filter | drafts_api.DraftsApi | filter_drafts_request:filter_drafts_request.FilterDraftsRequest
get_delivery_history_by_delivery_date_and_phone | POST /api/1/deliveries/history/by_delivery_date_and_phone | deliveries_retrieve_api.DeliveriesRetrieveApi | orders_history_by_delivery_date_and_phone_request:orders_history_by_delivery_date_and_phone_request.OrdersHistoryByDeliveryDateAndPhoneRequest
get_delivery_order_types | POST /api/1/deliveries/order_types | dictionaries_api.DictionariesApi | order_types_request:order_types_request.OrderTypesRequest
get_delivery_restrictions | POST /api/1/delivery_restrictions | delivery_restrictions_api.DeliveryRestrictionsApi | get_delivery_restrictions_request:get_delivery_restrictions_request.GetDeliveryRestrictionsRequest
get_discounts | POST /api/1/discounts | dictionaries_api.DictionariesApi | discounts_request:discounts_request.DiscountsRequest
get_employee_info | POST /api/1/employees/info | employees_api.EmployeesApi | employee_info_request:employee_info_request.EmployeeInfoRequest
get_external_menu_by_id | POST /api/2/menu/by_id | menu_api.MenuApi | menu_request:menu_request.MenuRequest
get_external_menus | POST /api/2/menu | menu_api.MenuApi | NO_REQUEST
get_finance_incoming_service | POST /api/finance/v1/incoming_service/get | public_api_invoice_processing_incoming_service_api.PublicApiInvoiceProcessingIncomingServiceApi | get_by_id_request:get_by_id_request.GetByIDRequest
get_finance_outgoing_service | POST /api/finance/v1/outgoing_service/get | public_api_invoice_processing_outgoing_service_api.PublicApiInvoiceProcessingOutgoingServiceApi | get_by_id_request:get_by_id_request.GetByIDRequest
get_inventory_counteragents | POST /api/inventory/v1/counteragents | public_api_invoice_processing_counteragents_api.PublicApiInvoiceProcessingCounteragentsApi | get_counteragents_request:get_counteragents_request.GetCounteragentsRequest
get_inventory_disassemble_document | POST /api/inventory/v1/disassemble_document/get | public_api_invoice_processing_disassemble_document_api.PublicApiInvoiceProcessingDisassembleDocumentApi | get_by_id_request:get_by_id_request.GetByIDRequest
get_inventory_incoming_invoice | POST /api/inventory/v1/incoming_invoice/get | public_api_invoice_processing_incoming_invoices_api.PublicApiInvoiceProcessingIncomingInvoicesApi | get_by_id_request:get_by_id_request.GetByIDRequest
get_inventory_incoming_returned_invoice | POST /api/inventory/v1/incoming_returned_invoice/get | public_api_invoice_processing_incoming_returned_invoice_api.PublicApiInvoiceProcessingIncomingReturnedInvoiceApi | get_by_id_request:get_by_id_request.GetByIDRequest
get_inventory_internal_transfer | POST /api/inventory/v1/internal_transfer/get | public_api_invoice_processing_internal_transfer_api.PublicApiInvoiceProcessingInternalTransferApi | get_by_id_request:get_by_id_request.GetByIDRequest
get_inventory_outgoing_invoice | POST /api/inventory/v1/outgoing_invoice/get | public_api_invoice_processing_outgoing_invoices_api.PublicApiInvoiceProcessingOutgoingInvoicesApi | get_by_id_request:get_by_id_request.GetByIDRequest
get_inventory_production_document | POST /api/inventory/v1/production_document/get | public_api_invoice_processing_production_document_api.PublicApiInvoiceProcessingProductionDocumentApi | get_by_id_request:get_by_id_request.GetByIDRequest
get_inventory_returned_invoice | POST /api/inventory/v1/returned_invoice/get | public_api_invoice_processing_returned_invoice_api.PublicApiInvoiceProcessingReturnedInvoiceApi | get_by_id_request:get_by_id_request.GetByIDRequest
get_inventory_sales_document | POST /api/inventory/v1/sales_document/get | public_api_invoice_processing_sales_document_api.PublicApiInvoiceProcessingSalesDocumentApi | get_by_id_request:get_by_id_request.GetByIDRequest
get_inventory_transformation_document | POST /api/inventory/v1/transformation_document/get | public_api_invoice_processing_transformation_document_api.PublicApiInvoiceProcessingTransformationDocumentApi | get_by_id_request:get_by_id_request.GetByIDRequest
get_inventory_writeoff_document | POST /api/inventory/v1/writeoff_document/get | public_api_invoice_processing_writeoff_document_api.PublicApiInvoiceProcessingWriteoffDocumentApi | get_by_id_request:get_by_id_request.GetByIDRequest
get_loyalty_counters | POST /api/1/loyalty/iiko/get_counters | customers_api.CustomersApi | get_counters_request:get_counters_request.GetCountersRequest
get_loyalty_manual_conditions | POST /api/1/loyalty/iiko/manual_condition | discounts_and_promotions_api.DiscountsAndPromotionsApi | get_by_organization_id_request:get_by_organization_id_request.GetByOrganizationIdRequest
get_loyalty_programs | POST /api/1/loyalty/iiko/program | discounts_and_promotions_api.DiscountsAndPromotionsApi | get_programs_request:get_programs_request.GetProgramsRequest
get_marketing_sources | POST /api/1/marketing_sources | marketing_sources_api.MarketingSourcesApi | marketing_sources_request:marketing_sources_request.MarketingSourcesRequest
get_nomenclature | POST /api/1/nomenclature | menu_api.MenuApi | nomenclature_request:nomenclature_request.NomenclatureRequest
get_non_activated_coupons_by_series | POST /api/1/loyalty/iiko/coupons/by_series | discounts_and_promotions_api.DiscountsAndPromotionsApi | not_activated_coupon_request:not_activated_coupon_request.NotActivatedCouponRequest
get_organization_settings | POST /api/1/organizations/settings | organizations_api.OrganizationsApi | organizations_settings_request:organizations_settings_request.OrganizationsSettingsRequest
get_organizations | POST /api/1/organizations | organizations_api.OrganizationsApi | get_organizations_request:get_organizations_request.GetOrganizationsRequest
get_payment_types | POST /api/1/payment_types | dictionaries_api.DictionariesApi | payment_types_request:payment_types_request.PaymentTypesRequest
get_personal_session_info | POST /api/1/employees/shift/is_open | employees_api.EmployeesApi | get_personal_session_info_request:get_personal_session_info_request.GetPersonalSessionInfoRequest
get_regions | POST /api/1/regions | addresses_api.AddressesApi | regions_request:regions_request.RegionsRequest
get_removal_types | POST /api/1/removal_types | dictionaries_api.DictionariesApi | removal_types_request:removal_types_request.RemovalTypesRequest
get_reserve_available_organizations | POST /api/1/reserve/available_organizations | banquets_reserves_api.BanquetsReservesApi | get_organizations_request:get_organizations_request.GetOrganizationsRequest
get_reserve_restaurant_sections | POST /api/1/reserve/available_restaurant_sections | banquets_reserves_api.BanquetsReservesApi | get_restaurant_sections_request:get_restaurant_sections_request.GetRestaurantSectionsRequest
get_reserve_statuses_by_id | POST /api/1/reserve/status_by_id | banquets_reserves_api.BanquetsReservesApi | reserves_by_id_request:reserves_by_id_request.ReservesByIdRequest
get_reserve_terminal_groups | POST /api/1/reserve/available_terminal_groups | banquets_reserves_api.BanquetsReservesApi | get_terminal_groups_by_organizations_request:get_terminal_groups_by_organizations_request.GetTerminalGroupsByOrganizationsRequest
get_restaurant_sections_workload | POST /api/1/reserve/restaurant_sections_workload | banquets_reserves_api.BanquetsReservesApi | get_restaurant_sections_workload_request:get_restaurant_sections_workload_request.GetRestaurantSectionsWorkloadRequest
get_stop_lists | POST /api/1/stop_lists | menu_api.MenuApi | stop_lists_request:stop_lists_request.StopListsRequest
get_streets_by_city | POST /api/1/streets/by_city | addresses_api.AddressesApi | streets_by_city_request:streets_by_city_request.StreetsByCityRequest
get_streets_by_id | POST /api/1/streets/by_id | addresses_api.AddressesApi | streets_by_id_request:streets_by_id_request.StreetsByIdRequest
get_table_orders_by_id | POST /api/1/order/by_id | orders_api.OrdersApi | get_table_orders_by_id_request:get_table_orders_by_id_request.GetTableOrdersByIdRequest
get_table_orders_by_table | POST /api/1/order/by_table | orders_api.OrdersApi | get_table_orders_by_table_request:get_table_orders_by_table_request.GetTableOrdersByTableRequest
get_terminal_groups | POST /api/1/terminal_groups | terminal_groups_api.TerminalGroupsApi | terminal_groups_request:terminal_groups_request.TerminalGroupsRequest
get_terminal_groups_of_employee | POST /api/1/employees/shifts/by_courier | employees_api.EmployeesApi | get_terminal_groups_of_employee_request:get_terminal_groups_of_employee_request.GetTerminalGroupsOfEmployeeRequest
get_tips_types | POST /api/1/tips_types | dictionaries_api.DictionariesApi | NO_REQUEST
get_webhook_settings | POST /api/1/webhooks/settings | webhooks_api.WebhooksApi | get_web_hook_settings_request:get_web_hook_settings_request.GetWebHookSettingsRequest
list_finance_account_transactions | POST /api/finance/v1/account_transactions/list | public_api_invoice_processing_account_transactions_api.PublicApiInvoiceProcessingAccountTransactionsApi | account_transactions_list_request:account_transactions_list_request.AccountTransactionsListRequest
list_finance_document_transactions | POST /api/finance/v1/document_transactions/list | public_api_invoice_processing_document_transactions_api.PublicApiInvoiceProcessingDocumentTransactionsApi | document_transactions_list_request:document_transactions_list_request.DocumentTransactionsListRequest
list_finance_incoming_services | POST /api/finance/v1/incoming_service/list | public_api_invoice_processing_incoming_service_api.PublicApiInvoiceProcessingIncomingServiceApi | list_request:list_request.ListRequest
list_finance_outgoing_services | POST /api/finance/v1/outgoing_service/list | public_api_invoice_processing_outgoing_service_api.PublicApiInvoiceProcessingOutgoingServiceApi | list_request:list_request.ListRequest
list_inventory_disassemble_documents | POST /api/inventory/v1/disassemble_document/list | public_api_invoice_processing_disassemble_document_api.PublicApiInvoiceProcessingDisassembleDocumentApi | list_request:list_request.ListRequest
list_inventory_incoming_invoices | POST /api/inventory/v1/incoming_invoice/list | public_api_invoice_processing_incoming_invoices_api.PublicApiInvoiceProcessingIncomingInvoicesApi | list_request:list_request.ListRequest
list_inventory_incoming_returned_invoices | POST /api/inventory/v1/incoming_returned_invoice/list | public_api_invoice_processing_incoming_returned_invoice_api.PublicApiInvoiceProcessingIncomingReturnedInvoiceApi | list_request:list_request.ListRequest
list_inventory_internal_transfers | POST /api/inventory/v1/internal_transfer/list | public_api_invoice_processing_internal_transfer_api.PublicApiInvoiceProcessingInternalTransferApi | list_request:list_request.ListRequest
list_inventory_outgoing_invoices | POST /api/inventory/v1/outgoing_invoice/list | public_api_invoice_processing_outgoing_invoices_api.PublicApiInvoiceProcessingOutgoingInvoicesApi | list_request:list_request.ListRequest
list_inventory_production_documents | POST /api/inventory/v1/production_document/list | public_api_invoice_processing_production_document_api.PublicApiInvoiceProcessingProductionDocumentApi | list_request:list_request.ListRequest
list_inventory_returned_invoices | POST /api/inventory/v1/returned_invoice/list | public_api_invoice_processing_returned_invoice_api.PublicApiInvoiceProcessingReturnedInvoiceApi | list_request:list_request.ListRequest
list_inventory_sales_documents | POST /api/inventory/v1/sales_document/list | public_api_invoice_processing_sales_document_api.PublicApiInvoiceProcessingSalesDocumentApi | list_request:list_request.ListRequest
list_inventory_transformation_documents | POST /api/inventory/v1/transformation_document/list | public_api_invoice_processing_transformation_document_api.PublicApiInvoiceProcessingTransformationDocumentApi | list_request:list_request.ListRequest
list_inventory_writeoff_documents | POST /api/inventory/v1/writeoff_document/list | public_api_invoice_processing_writeoff_document_api.PublicApiInvoiceProcessingWriteoffDocumentApi | list_request:list_request.ListRequest
list_organizations | GET /api/1/organizations | deprecated_api.DeprecatedApi | NO_REQUEST
search_deliveries | POST /api/1/deliveries/by_delivery_date_and_source_key_and_filter | deliveries_retrieve_api.DeliveriesRetrieveApi | orders_by_delivery_date_and_filter_request:orders_by_delivery_date_and_filter_request.OrdersByDeliveryDateAndFilterRequest
```
