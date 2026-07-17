# Iikocloud SDK Generation Pipeline Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Построить воспроизводимый конвейер, который получает OpenAPI iiko Cloud, применяет guarded corrections, генерирует устанавливаемый async Python SDK, безопасно проверяет его offline/live и публикует только после safety gates.

**Architecture:** Точный upstream snapshot остаётся неизменяемым, а effective schema строится из Overlay 1.1.0, operation/model registries и проверяемых evidence fixtures. Pipeline генерирует клиент OpenAPI Generator во staging, валидирует wheel и только затем атомарно продвигает snapshot и generated-область. Live-read, live-write, capture и Git publish используют отдельные opt-in safety-компоненты и никогда не включаются обычным `pytest` или CI.

**Tech Stack:** Python 3.10+ для SDK, Python 3.12 для pipeline/CI, `uv`, pytest, PyYAML, `jsonpath-rfc9535`, OpenAPI Generator 7.22.0 в Docker, async `httpx`, Pydantic 2, `detect-secrets` 1.5.0, GitHub Actions.

## Global Constraints

- Источник схемы: `https://api-ru.iiko.services/api-docs/docs`; ReDoc: `https://api-ru.iiko.services/docs`.
- Upstream snapshot сохраняется byte-for-byte и никогда не редактируется вручную.
- Overlay format: 1.1.0; `target` использует только RFC 9535 JSONPath.
- OpenAPI Generator: ровно 7.22.0 и Docker digest из `generator/toolchain.lock`; snapshot/latest запрещены.
- Генерация выполняется без `--skip-validate-spec`; `useOneOfDiscriminatorLookup` остаётся `false`, чтобы не отключать strict `oneOf` validation.
- Generated API/model files нельзя редактировать вручную; собственные Mustache templates изначально отсутствуют.
- Runtime SDK остаётся async; generator backend — `httpx`, sync-варианты не генерируются.
- Pipeline и live-safety tooling поддерживают Linux/WSL; `fcntl`, POSIX permissions и Docker являются осознанными platform requirements. Сам сгенерированный SDK остаётся переносимым Python-пакетом.
- Все обычные тесты offline; live tests никогда не запускаются CI или обычным `pytest`.
- Live tests строго последовательны: `-n0`, process lock, один API login и один access token на сессию.
- Основной read/auth login берётся только из `IIKO_API_KEY` через явно указанный ignored `.env`; значение никогда не выводится. `IIKO_API_KEY_2` не является автоматическим fallback: после `429` любые ключи блокируются общим profile circuit до ручного расследования/reset.
- Неизвестная live-операция отключена. Начальный global interval — 15 секунд, utilization — не более 20%, одна операция — не более одного раза за run.
- Практическая оценка «раз в 30 секунд» не заменяет verified server limit: фактическая пауза всегда равна более строгому вычисленному budget и может быть существенно больше 30 секунд.
- При любом `429` весь suite прекращается без retry и без смены учётных данных; профиль переходит в circuit-open до ручного reset.
- Live-write требует CLI-флаг, локальный `allow_write`, точный organization allowlist и предварительно зарезервированный cleanup budget.
- HTTP capture сохраняет только sanitized JSON в ignored `private/`; raw capture отсутствует.
- На Linux/WSL каталоги `private/` и `.state/` создаются с mode `0700`, а profile, capture, receipt, rate-state и mutation-journal files — с mode `0600`; существующие более широкие permissions считаются safety error.
- `private/`, `.state/`, `.env`, `.env.local`, live receipts, rate state и mutation journals не попадают в Git.
- Любой повторяемый сбой инструмента или проверенный обход фиксируется без секретов в `docs/troubleshooting.md` в том же change set; будущие исполнители обязаны прочитать журнал до pipeline/live-команд.
- В рамках текущего выполнения automated test commands запускаются только вне sandbox. Это не разрешает live HTTP: live остаётся отдельным gate после подтверждения rate limits.
- `sync` и `verify` не создают commit. `publish` не использует `git add -A`, force push или неявный push в `main`.
- Перестройка `/home/ivan/programming/Iikocloud-manager` и публикация в PyPI не входят в этот план.

## Source References

- [OpenAPI Generator 7.22.0 release](https://github.com/OpenAPITools/openapi-generator/releases/tag/v7.22.0)
- [Python generator options and `oneOf` support](https://openapi-generator.tech/docs/generators/python/)
- [OpenAPI Generator mappings and normalizer options](https://openapi-generator.tech/docs/customization/)
- [OpenAPI Overlay 1.1.0](https://spec.openapis.org/overlay/v1.1.0.html)
- [RFC 9535 JSONPath](https://www.rfc-editor.org/rfc/rfc9535.html)
- [detect-secrets 1.5.0](https://github.com/Yelp/detect-secrets/releases/tag/v1.5.0)

## File Responsibility Map

| Path | Responsibility |
|---|---|
| `openapi/upstream/iikocloud.openapi.json` | Единственный committed raw snapshot |
| `openapi/overlays/*.overlay.yaml` | Механические и семантические corrections |
| `openapi/operation-ids.yaml` | Stable mapping `METHOD path -> operationId` |
| `openapi/model-name-overrides.yaml` | Только явные исключения normalizer |
| `contracts/rate-limits.yaml` | Canonical server limits и safe test budgets |
| `contracts/live-operations.yaml` | Классификация read/write/auth и cleanup operations |
| `generator/config.yaml` | Рукописная конфигурация Python generator |
| `generator/toolchain.lock` | Exact image tag + digest |
| `generator/generated-manifest.json` | Пути, принадлежащие codegen |
| `tools/openapi_pipeline/io.py` | Canonical JSON, hashes и atomic writes |
| `tools/openapi_pipeline/fetch.py` | Загрузка candidate snapshot |
| `tools/openapi_pipeline/inventory.py` | Inventory и upstream diff |
| `tools/openapi_pipeline/overlay.py` | Guarded Overlay 1.1 applier |
| `tools/openapi_pipeline/naming.py` | operationId/model registries |
| `tools/openapi_pipeline/validate.py` | Custom lint + generator validate |
| `tools/openapi_pipeline/generator.py` | Pinned Docker codegen |
| `tools/openapi_pipeline/promotion.py` | Staging compare и transactional promotion |
| `tools/openapi_pipeline/pipeline.py` | `sync`, `verify`, `bootstrap` orchestration |
| `tools/openapi_pipeline/live/` | Profiles, limits, circuit, receipts и live session |
| `tools/openapi_pipeline/capture.py` | Schema-aware redaction и private JSON capture |
| `tools/openapi_pipeline/mutations.py` | Durable mutation journal и cleanup stack |
| `tools/openapi_pipeline/secrets.py` | detect-secrets + exact-known-secret scan |
| `tools/openapi_pipeline/publish.py` | Allowlisted Git commit/tag/push |
| `src/iikocloud_client/` | Generated SDK плюс защищённая `_contracts/` metadata |
| `docs/troubleshooting.md` | Durable sanitized failure pattern / workaround / prevention ledger |
| `AGENTS.md` | Короткие обязательные safety rules и ссылка на troubleshooting ledger |
| `tests/pipeline/` | Unit/contract tests pipeline |
| `tests/integration/read/` | Explicit live read tests |
| `tests/integration/write/` | Explicit live write tests |

---

### Task 1: Establish the hand-owned pipeline shell

**Files:**

- Modify: `pyproject.toml`
- Modify: `.gitignore`
- Create: `AGENTS.md`
- Create: `docs/troubleshooting.md`
- Create: `tools/__init__.py`
- Create: `tools/openapi_pipeline/__init__.py`
- Create: `tools/openapi_pipeline/__main__.py`
- Create: `tools/openapi_pipeline/cli.py`
- Create: `tools/openapi_pipeline/errors.py`
- Create: `tools/openapi_pipeline/paths.py`
- Create: `tests/pipeline/test_cli.py`
- Create: `tests/pipeline/test_paths.py`

**Interfaces:**

- Consumes: repository root containing `pyproject.toml`.
- Produces: `RepoPaths.discover(start: Path) -> RepoPaths`, `build_parser() -> argparse.ArgumentParser`, `main(argv: Sequence[str] | None = None) -> int`.

- [ ] **Step 1: Write failing CLI and path tests**

```python
# tests/pipeline/test_cli.py
from tools.openapi_pipeline.cli import build_parser


def test_cli_exposes_only_explicit_pipeline_commands() -> None:
    parser = build_parser()
    choices = parser._subparsers._group_actions[0].choices  # type: ignore[attr-defined]
    assert set(choices) == {
        "bootstrap",
        "sync",
        "verify",
        "upstream-check",
        "capture-evidence",
        "promote-evidence",
        "cleanup-orphans",
        "reset-circuit",
        "verify-no-secrets",
        "publish",
    }
```

```python
# tests/pipeline/test_paths.py
from pathlib import Path

from tools.openapi_pipeline.paths import RepoPaths


def test_repo_paths_are_anchored_at_pyproject(tmp_path: Path) -> None:
    root = tmp_path / "repo"
    nested = root / "tools" / "openapi_pipeline"
    nested.mkdir(parents=True)
    (root / "pyproject.toml").write_text("[project]\nname='demo'\n")

    paths = RepoPaths.discover(nested)

    assert paths.root == root
    assert paths.candidate == root / "build/upstream/candidate.json"
    assert paths.effective == root / "build/openapi/effective.json"
    assert paths.private == root / "private"
    assert paths.state == root / ".state"
```

- [ ] **Step 2: Run the focused tests and verify RED**

Run: `uv run pytest tests/pipeline/test_cli.py tests/pipeline/test_paths.py -q`

Expected: collection fails because `tools.openapi_pipeline.cli` and `paths` do not exist.

- [ ] **Step 3: Add pipeline dependencies and test configuration**

Set `project.requires-python = ">=3.10"` now so the resolver does not attempt the unsupported Python 3.9 split; keep the current runtime dependencies until the first successful full regeneration in Task 11. Add these exact entries to `pyproject.toml`:

```toml
[dependency-groups]
dev = [
  "build>=1.3,<2",
  "detect-secrets==1.5.0",
  "jsonpath-rfc9535==1.0.0",
  "mypy>=1.18,<2",
  "pytest>=9,<10",
  "pytest-asyncio>=1.3,<2",
  "pytest-cov>=7,<8",
  "python-dotenv>=1.1,<2",
  "pyyaml>=6.0.3,<7",
  "ruff>=0.12,<1",
  "setuptools>=77,<82",
  "tomli>=2.2,<3; python_version < '3.11'",
  "types-pyyaml>=6.0.12,<7",
]

[tool.pytest.ini_options]
testpaths = ["tests"]
asyncio_mode = "auto"
markers = [
  "docker: requires the pinned OpenAPI Generator image",
  "live_read_smoke: minimal live read contract checks",
  "live_read_full: extended live read contract checks",
  "live_write: explicit mutating checks",
]
addopts = "-m 'not docker and not live_read_smoke and not live_read_full and not live_write'"

[tool.ruff]
target-version = "py310"
line-length = 99
exclude = ["src/iikocloud_client/api", "src/iikocloud_client/models"]

[tool.ruff.lint]
select = ["E", "F", "I", "UP", "B", "SIM"]
```

Extend `.gitignore` with:

```gitignore
.state/
.env
.env.local
.worktrees/
private/*
!private/.gitignore
!private/README.md
```

Create `AGENTS.md` with repository-local rules to read `docs/troubleshooting.md`, never print `.env`/credentials, never switch API logins after `429`, run live calls only through the guarded commands, and record newly confirmed repeatable failure patterns. Seed `docs/troubleshooting.md` with a table containing `date`, `sanitized command/context`, `symptom`, `root cause`, `safe workaround`, `prevention`, and `verification`; record no speculative causes and no secret-bearing output.

- [ ] **Step 4: Implement the pipeline shell**

```python
# tools/openapi_pipeline/errors.py
class PipelineError(RuntimeError):
    """Expected pipeline failure with a user-actionable message."""


class SafetyError(PipelineError):
    """A live, secret, mutation, or publish safety invariant failed."""


class ValidationError(PipelineError):
    """The upstream or effective OpenAPI document is invalid."""


class StaleOverlayError(ValidationError):
    """An overlay no longer matches the upstream fragment it was written for."""
```

```python
# tools/openapi_pipeline/paths.py
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from .errors import PipelineError


@dataclass(frozen=True)
class RepoPaths:
    root: Path

    @classmethod
    def discover(cls, start: Path | None = None) -> "RepoPaths":
        current = (start or Path.cwd()).resolve()
        for candidate in (current, *current.parents):
            if (candidate / "pyproject.toml").is_file():
                return cls(candidate)
        raise PipelineError("Cannot find repository root containing pyproject.toml")

    @property
    def build(self) -> Path:
        return self.root / "build"

    @property
    def candidate(self) -> Path:
        return self.build / "upstream/candidate.json"

    @property
    def effective(self) -> Path:
        return self.build / "openapi/effective.json"

    @property
    def upstream(self) -> Path:
        return self.root / "openapi/upstream/iikocloud.openapi.json"

    @property
    def private(self) -> Path:
        return self.root / "private"

    @property
    def state(self) -> Path:
        return self.root / ".state"
```

```python
# tools/openapi_pipeline/cli.py
from __future__ import annotations

import argparse
from collections.abc import Sequence

from .errors import PipelineError


COMMANDS = (
    "bootstrap",
    "sync",
    "verify",
    "upstream-check",
    "capture-evidence",
    "promote-evidence",
    "cleanup-orphans",
    "reset-circuit",
    "verify-no-secrets",
    "publish",
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="python -m tools.openapi_pipeline")
    subparsers = parser.add_subparsers(dest="command", required=True)
    for command in COMMANDS:
        subparsers.add_parser(command)
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    raise PipelineError(f"Command is not implemented yet: {args.command}")
```

```python
# tools/openapi_pipeline/__main__.py
from .cli import main

raise SystemExit(main())
```

`tools/__init__.py` and `tools/openapi_pipeline/__init__.py` remain empty.

- [ ] **Step 5: Sync dependencies and verify GREEN**

Run: `uv sync --group dev`

Expected: `uv.lock` updates successfully.

Run: `uv run pytest tests/pipeline/test_cli.py tests/pipeline/test_paths.py -q`

Expected: `2 passed`.

- [ ] **Step 6: Commit the shell**

```bash
git add pyproject.toml uv.lock .gitignore AGENTS.md docs/troubleshooting.md tools tests/pipeline
git commit -m "build: add OpenAPI pipeline shell"
```

### Task 2: Fetch immutable candidates and produce inventory diffs

**Files:**

- Create: `tools/openapi_pipeline/io.py`
- Create: `tools/openapi_pipeline/fetch.py`
- Create: `tools/openapi_pipeline/inventory.py`
- Create: `tests/fixtures/openapi/minimal-v1.json`
- Create: `tests/fixtures/openapi/minimal-v2.json`
- Create: `tests/pipeline/test_fetch.py`
- Create: `tests/pipeline/test_inventory.py`

**Interfaces:**

- Consumes: bytes returned by a supplied HTTPS opener.
- Produces: `FetchResult(body_sha256, path, changed)`, `Inventory`, `InventoryDiff`, canonical atomic JSON files.

- [ ] **Step 1: Add minimal OpenAPI fixtures**

```json
// tests/fixtures/openapi/minimal-v1.json
{
  "openapi": "3.0.1",
  "info": {"title": "Fixture", "version": "1"},
  "paths": {
    "/api/1/ping": {
      "post": {"responses": {"200": {"description": "ok"}}}
    }
  },
  "components": {"schemas": {"Ping": {"type": "object", "properties": {}}}}
}
```

`minimal-v2.json` is the same document with `info.version` set to `2`, a second path `/api/1/status`, and a second schema `Status`.

- [ ] **Step 2: Write failing fetch and inventory tests**

```python
# tests/pipeline/test_fetch.py
from pathlib import Path

import pytest

from tools.openapi_pipeline.fetch import fetch_candidate
from tools.openapi_pipeline.errors import ValidationError


def test_fetch_candidate_preserves_exact_bytes(tmp_path: Path) -> None:
    body = b'{"openapi":"3.0.1","info":{},"paths":{}}\n'
    result = fetch_candidate(
        "https://example.invalid/schema",
        tmp_path / "candidate.json",
        opener=lambda _url, _timeout: body,
    )
    assert result.path.read_bytes() == body
    assert len(result.body_sha256) == 64


def test_fetch_candidate_rejects_non_openapi_json(tmp_path: Path) -> None:
    with pytest.raises(ValidationError, match="OpenAPI root fields"):
        fetch_candidate(
            "https://example.invalid/schema",
            tmp_path / "candidate.json",
            opener=lambda _url, _timeout: b'{"message":"error"}',
        )
```

```python
# tests/pipeline/test_inventory.py
import json
from pathlib import Path

from tools.openapi_pipeline.inventory import collect_inventory, diff_inventory


def test_inventory_diff_reports_added_paths_and_schemas() -> None:
    fixtures = Path("tests/fixtures/openapi")
    before = json.loads((fixtures / "minimal-v1.json").read_text())
    after = json.loads((fixtures / "minimal-v2.json").read_text())

    diff = diff_inventory(collect_inventory(before), collect_inventory(after))

    assert diff.added_paths == ("/api/1/status",)
    assert diff.added_schemas == ("Status",)
```

- [ ] **Step 3: Run focused tests and verify RED**

Run: `uv run pytest tests/pipeline/test_fetch.py tests/pipeline/test_inventory.py -q`

Expected: import errors for `fetch` and `inventory`.

- [ ] **Step 4: Implement canonical I/O and fetching**

```python
# tools/openapi_pipeline/io.py
from __future__ import annotations

import hashlib
import json
import os
import tempfile
from pathlib import Path
from typing import Any


def canonical_json_bytes(value: Any) -> bytes:
    return (json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n").encode()


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def write_bytes_atomic(path: Path, body: bytes, mode: int = 0o644) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, name = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
    temporary = Path(name)
    try:
        os.fchmod(fd, mode)
        with os.fdopen(fd, "wb") as stream:
            stream.write(body)
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temporary, path)
    finally:
        temporary.unlink(missing_ok=True)


def write_json_atomic(path: Path, value: Any, mode: int = 0o644) -> None:
    write_bytes_atomic(path, canonical_json_bytes(value), mode)
```

```python
# tools/openapi_pipeline/fetch.py
from __future__ import annotations

import json
import urllib.request
from collections.abc import Callable
from dataclasses import dataclass
from pathlib import Path

from .errors import ValidationError
from .io import sha256_bytes, write_bytes_atomic

OpenBytes = Callable[[str, float], bytes]


@dataclass(frozen=True)
class FetchResult:
    body_sha256: str
    path: Path
    changed: bool


def _urlopen(url: str, timeout: float) -> bytes:
    request = urllib.request.Request(url, headers={"Accept": "application/json"})
    with urllib.request.urlopen(request, timeout=timeout) as response:
        return response.read()


def fetch_candidate(
    url: str,
    destination: Path,
    *,
    timeout: float = 30.0,
    opener: OpenBytes = _urlopen,
) -> FetchResult:
    body = opener(url, timeout)
    try:
        document = json.loads(body)
    except json.JSONDecodeError as exc:
        raise ValidationError("Upstream response is not JSON") from exc
    if not isinstance(document, dict) or not {"openapi", "info", "paths"} <= document.keys():
        raise ValidationError("Upstream response does not contain required OpenAPI root fields")
    digest = sha256_bytes(body)
    changed = not destination.exists() or sha256_bytes(destination.read_bytes()) != digest
    write_bytes_atomic(destination, body)
    return FetchResult(digest, destination, changed)
```

- [ ] **Step 5: Implement stable inventory and diff data**

```python
# tools/openapi_pipeline/inventory.py
from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Any


HTTP_METHODS = {"get", "put", "post", "delete", "patch", "head", "options", "trace"}


@dataclass(frozen=True)
class Inventory:
    openapi: str
    paths: tuple[str, ...]
    operations: tuple[str, ...]
    schemas: tuple[str, ...]

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class InventoryDiff:
    added_paths: tuple[str, ...]
    removed_paths: tuple[str, ...]
    added_operations: tuple[str, ...]
    removed_operations: tuple[str, ...]
    added_schemas: tuple[str, ...]
    removed_schemas: tuple[str, ...]

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def collect_inventory(document: dict[str, Any]) -> Inventory:
    paths = document.get("paths", {})
    operations = tuple(
        sorted(
            f"{method.upper()} {path}"
            for path, path_item in paths.items()
            for method in path_item
            if method.lower() in HTTP_METHODS
        )
    )
    schemas = document.get("components", {}).get("schemas", {})
    return Inventory(
        openapi=str(document.get("openapi", "")),
        paths=tuple(sorted(paths)),
        operations=operations,
        schemas=tuple(sorted(schemas)),
    )


def diff_inventory(before: Inventory, after: Inventory) -> InventoryDiff:
    def delta(left: tuple[str, ...], right: tuple[str, ...]) -> tuple[str, ...]:
        return tuple(sorted(set(right) - set(left)))

    return InventoryDiff(
        added_paths=delta(before.paths, after.paths),
        removed_paths=delta(after.paths, before.paths),
        added_operations=delta(before.operations, after.operations),
        removed_operations=delta(after.operations, before.operations),
        added_schemas=delta(before.schemas, after.schemas),
        removed_schemas=delta(after.schemas, before.schemas),
    )
```

- [ ] **Step 6: Verify GREEN and commit**

Run: `uv run pytest tests/pipeline/test_fetch.py tests/pipeline/test_inventory.py -q`

Expected: `3 passed`.

```bash
git add tools/openapi_pipeline tests/fixtures/openapi tests/pipeline
git commit -m "feat: fetch and inventory OpenAPI snapshots"
```

### Task 3: Apply guarded OpenAPI Overlay 1.1 documents

**Files:**

- Create: `tools/openapi_pipeline/overlay.py`
- Create: `tests/fixtures/openapi/types.overlay.yaml`
- Create: `tests/pipeline/test_overlay.py`

**Interfaces:**

- Consumes: JSON-like target document and one or more Overlay 1.1 YAML documents.
- Produces: deep-copied effective document or `StaleOverlayError`; never mutates the caller's source object.

- [ ] **Step 1: Write the overlay fixture and failing tests**

```yaml
# tests/fixtures/openapi/types.overlay.yaml
overlay: 1.1.0
info:
  title: Normalize fixture bool
  version: 1.0.0
actions:
  - target: $.components.schemas.Ping.properties.enabled.type
    description: iiko emits bool instead of boolean
    x-iiko-sdk-guard:
      issue: upstream-invalid-bool
      expected-matches: 1
      expected-sha256: 46dc040029afd3985157d72cc44f2d883e99aabbdf811b3c1ffd527fc6b904c4
    update: boolean
```

The SHA-256 is the canonical JSON hash of the primitive JSON value `"bool"`.

```python
# tests/pipeline/test_overlay.py
from pathlib import Path

import pytest
import yaml

from tools.openapi_pipeline.errors import StaleOverlayError
from tools.openapi_pipeline.overlay import apply_overlay


def source_document() -> dict:
    return {
        "openapi": "3.0.1",
        "components": {
            "schemas": {
                "Ping": {"type": "object", "properties": {"enabled": {"type": "bool"}}}
            }
        },
    }


def test_guarded_primitive_update_does_not_mutate_source() -> None:
    overlay = yaml.safe_load(Path("tests/fixtures/openapi/types.overlay.yaml").read_text())
    source = source_document()
    effective = apply_overlay(source, overlay)
    assert source["components"]["schemas"]["Ping"]["properties"]["enabled"]["type"] == "bool"
    assert effective["components"]["schemas"]["Ping"]["properties"]["enabled"]["type"] == "boolean"


def test_changed_upstream_fragment_makes_overlay_stale() -> None:
    overlay = yaml.safe_load(Path("tests/fixtures/openapi/types.overlay.yaml").read_text())
    source = source_document()
    source["components"]["schemas"]["Ping"]["properties"]["enabled"]["type"] = "boolean"
    with pytest.raises(StaleOverlayError, match="upstream-invalid-bool"):
        apply_overlay(source, overlay)
```

- [ ] **Step 2: Run the test and verify RED**

Run: `uv run pytest tests/pipeline/test_overlay.py -q`

Expected: import error for `tools.openapi_pipeline.overlay`.

- [ ] **Step 3: Implement guarded sequential update/remove/copy**

Implement `tools/openapi_pipeline/overlay.py` with these public functions and invariants:

```python
from __future__ import annotations

import copy
from pathlib import Path
from typing import Any

import jsonpath_rfc9535 as jsonpath
import yaml

from .errors import StaleOverlayError, ValidationError
from .io import canonical_json_bytes, sha256_bytes


def _merge(target: Any, update: Any) -> Any:
    if isinstance(target, dict) and isinstance(update, dict):
        merged = copy.deepcopy(target)
        for key, value in update.items():
            merged[key] = _merge(merged[key], value) if key in merged else copy.deepcopy(value)
        return merged
    if isinstance(target, list) and isinstance(update, list):
        return copy.deepcopy(target) + copy.deepcopy(update)
    if isinstance(target, (str, int, float, bool, type(None))) and isinstance(
        update, (str, int, float, bool, type(None))
    ):
        return copy.deepcopy(update)
    raise ValidationError(
        f"Overlay update types are incompatible: {type(target).__name__} and {type(update).__name__}"
    )


def _guard(action: dict[str, Any], values: list[Any]) -> None:
    guard = action.get("x-iiko-sdk-guard")
    if not isinstance(guard, dict):
        raise ValidationError("Every overlay action requires x-iiko-sdk-guard")
    issue = str(guard.get("issue", "unnamed-overlay-action"))
    expected_matches = guard.get("expected-matches")
    if expected_matches != len(values):
        raise StaleOverlayError(
            f"{issue}: expected {expected_matches} matches, found {len(values)}"
        )
    expected_hash = guard.get("expected-sha256")
    actual_hash = sha256_bytes(canonical_json_bytes(values[0] if len(values) == 1 else values))
    if expected_hash is not None and expected_hash != actual_hash:
        raise StaleOverlayError(f"{issue}: upstream fragment hash changed")


def _remove_node(node: Any) -> None:
    if node.parent is None or not node.location:
        raise ValidationError("Overlay cannot remove the document root")
    key = node.location[-1]
    parent = node.parent.value
    if isinstance(parent, list) and isinstance(key, int):
        parent.pop(key)
    elif isinstance(parent, dict) and isinstance(key, str):
        del parent[key]
    else:
        raise ValidationError("Overlay remove target has an unsupported parent")


def apply_overlay(source: dict[str, Any], overlay: dict[str, Any]) -> dict[str, Any]:
    if overlay.get("overlay") != "1.1.0":
        raise ValidationError("Only Overlay 1.1.0 is supported")
    info = overlay.get("info")
    actions = overlay.get("actions")
    if not isinstance(info, dict) or not {"title", "version"} <= info.keys():
        raise ValidationError("Overlay info.title and info.version are required")
    if not isinstance(actions, list) or not actions:
        raise ValidationError("Overlay actions must be a non-empty list")

    result = copy.deepcopy(source)
    for action in actions:
        if not isinstance(action, dict) or not isinstance(action.get("target"), str):
            raise ValidationError("Overlay action.target must be a JSONPath string")
        nodes = list(jsonpath.find(action["target"], result))
        _guard(action, [node.value for node in nodes])
        if action.get("remove") is True:
            for node in sorted(nodes, key=lambda value: value.location, reverse=True):
                _remove_node(node)
            continue
        if "copy" in action:
            sources = list(jsonpath.find(action["copy"], result))
            if len(sources) != 1:
                raise ValidationError("Overlay copy must select exactly one source node")
            update = sources[0].value
        elif "update" in action:
            update = action["update"]
        else:
            raise ValidationError("Overlay action requires update, copy, or remove")
        for node in nodes:
            node.value = _merge(node.value, update)
    return result


def apply_overlay_files(source: dict[str, Any], paths: list[Path]) -> dict[str, Any]:
    result = copy.deepcopy(source)
    for path in paths:
        overlay = yaml.safe_load(path.read_text(encoding="utf-8"))
        if not isinstance(overlay, dict):
            raise ValidationError(f"Overlay is not an object: {path}")
        result = apply_overlay(result, overlay)
    return result
```

- [ ] **Step 4: Verify hash, RED/GREEN behavior, and type checking**

Run: `uv run pytest tests/pipeline/test_overlay.py -q`

Expected: `2 passed`.

Run: `uv run mypy tools/openapi_pipeline/overlay.py`

Expected: `Success: no issues found`.

- [ ] **Step 5: Commit the applier**

```bash
git add tools/openapi_pipeline/overlay.py tests/fixtures/openapi/types.overlay.yaml tests/pipeline/test_overlay.py
git commit -m "feat: apply guarded OpenAPI overlays"
```

### Task 4: Freeze operation IDs and normalized model names

**Files:**

- Create: `tools/openapi_pipeline/naming.py`
- Create: `openapi/operation-ids.yaml`
- Create: `openapi/model-name-overrides.yaml`
- Create: `tests/pipeline/test_naming.py`

**Interfaces:**

- Consumes: effective OpenAPI before codegen plus YAML registries.
- Produces: injected unique `operationId` values and `dict[raw_schema_name, PythonModelName]`; collisions are fatal.

- [ ] **Step 1: Write failing naming tests**

```python
# tests/pipeline/test_naming.py
import pytest

from tools.openapi_pipeline.errors import ValidationError
from tools.openapi_pipeline.naming import build_model_mappings, inject_operation_ids


def test_operation_registry_is_total_and_stable() -> None:
    document = {
        "paths": {
            "/api/1/access_token": {"post": {"responses": {}}},
            "/api/1/organizations": {"post": {"responses": {}}},
        }
    }
    registry = {
        "POST /api/1/access_token": "authenticate",
        "POST /api/1/organizations": "get_organizations",
    }
    result = inject_operation_ids(document, registry)
    assert result["paths"]["/api/1/access_token"]["post"]["operationId"] == "authenticate"
    assert result["paths"]["/api/1/organizations"]["post"]["operationId"] == "get_organizations"


def test_missing_operation_registry_entry_fails() -> None:
    document = {"paths": {"/api/1/new": {"post": {"responses": {}}}}}
    with pytest.raises(ValidationError, match="POST /api/1/new"):
        inject_operation_ids(document, {})


def test_normalized_model_collision_requires_override() -> None:
    schemas = {
        "Namespace.One.Item": {},
        "Namespace.Two.Item": {},
    }
    with pytest.raises(ValidationError, match="Item"):
        build_model_mappings(schemas, {})
    assert build_model_mappings(schemas, {"Namespace.Two.Item": "SecondItem"}) == {
        "Namespace.One.Item": "Item",
        "Namespace.Two.Item": "SecondItem",
    }
```

- [ ] **Step 2: Run the tests and verify RED**

Run: `uv run pytest tests/pipeline/test_naming.py -q`

Expected: import error for `naming`.

- [ ] **Step 3: Implement exact registry injection and conservative normalization**

```python
# tools/openapi_pipeline/naming.py
from __future__ import annotations

import copy
import re
from collections import defaultdict
from typing import Any

from .errors import ValidationError
from .inventory import HTTP_METHODS


def inject_operation_ids(
    source: dict[str, Any], registry: dict[str, str]
) -> dict[str, Any]:
    result = copy.deepcopy(source)
    seen: dict[str, str] = {}
    actual_keys: set[str] = set()
    for path, path_item in result.get("paths", {}).items():
        for method, operation in path_item.items():
            if method.lower() not in HTTP_METHODS:
                continue
            key = f"{method.upper()} {path}"
            actual_keys.add(key)
            operation_id = registry.get(key)
            if operation_id is None:
                raise ValidationError(f"Missing operationId registry entry: {key}")
            if operation_id in seen:
                raise ValidationError(
                    f"Duplicate operationId {operation_id}: {seen[operation_id]} and {key}"
                )
            seen[operation_id] = key
            operation["operationId"] = operation_id
    stale = sorted(set(registry) - actual_keys)
    if stale:
        raise ValidationError(f"Stale operationId registry entries: {', '.join(stale)}")
    return result


def normalize_model_name(raw: str) -> str:
    leaf = raw.rsplit(".", 1)[-1]
    leaf = re.sub(r"`\d+", "", leaf)
    words = re.findall(r"[A-Za-z0-9]+", leaf)
    if not words:
        raise ValidationError(f"Cannot normalize model name: {raw!r}")
    name = "".join(word[:1].upper() + word[1:] for word in words)
    if name[0].isdigit():
        name = f"Model{name}"
    return name


def build_model_mappings(
    schemas: dict[str, Any], overrides: dict[str, str]
) -> dict[str, str]:
    unknown = sorted(set(overrides) - set(schemas))
    if unknown:
        raise ValidationError(f"Stale model name overrides: {', '.join(unknown)}")
    result = {raw: overrides.get(raw, normalize_model_name(raw)) for raw in schemas}
    reverse: dict[str, list[str]] = defaultdict(list)
    for raw, normalized in result.items():
        reverse[normalized].append(raw)
    collisions = {name: raws for name, raws in reverse.items() if len(raws) > 1}
    if collisions:
        details = "; ".join(f"{name}: {', '.join(raws)}" for name, raws in collisions.items())
        raise ValidationError(f"Normalized model name collisions: {details}")
    return result
```

- [ ] **Step 4: Add registry file formats**

```yaml
# openapi/operation-ids.yaml
operations: {}
```

```yaml
# openapi/model-name-overrides.yaml
models: {}
```

The empty registries are only the pre-bootstrap state. Task 7's `bootstrap --accept-current-upstream` populates all current operations and stops on every unresolved model collision.

- [ ] **Step 5: Verify GREEN and commit**

Run: `uv run pytest tests/pipeline/test_naming.py -q`

Expected: `3 passed`.

```bash
git add tools/openapi_pipeline/naming.py openapi tests/pipeline/test_naming.py
git commit -m "feat: freeze generated public names"
```

### Task 5: Generate mechanical corrections and lint the effective schema

**Files:**

- Create: `tools/openapi_pipeline/normalization.py`
- Create: `tools/openapi_pipeline/validate.py`
- Create: `tests/pipeline/test_normalization.py`
- Create: `tests/pipeline/test_validate.py`

**Interfaces:**

- Consumes: candidate OpenAPI after semantic overlays and naming injection.
- Produces: a reviewable `types.overlay.yaml`, `list[LintIssue]`, and `ValidationError` when effective schema violates a hard invariant.

- [ ] **Step 1: Write failing normalization tests**

```python
# tests/pipeline/test_normalization.py
from tools.openapi_pipeline.normalization import correction_for_type


def test_known_iiko_pseudo_types_have_unambiguous_openapi_replacements() -> None:
    assert correction_for_type("bool") == {"type": "boolean"}
    assert correction_for_type("int") == {"type": "integer"}
    assert correction_for_type("float") == {"type": "number", "format": "float"}
    assert correction_for_type("uuid") == {"type": "string", "format": "uuid"}
    assert correction_for_type("integer <int64>") == {"type": "integer", "format": "int64"}
    assert correction_for_type("Array of strings <uuid>") == {
        "type": "array",
        "items": {"type": "string", "format": "uuid"},
    }
    assert correction_for_type("constant string 'OrderUpdate'") == {
        "type": "string",
        "enum": ["OrderUpdate"],
    }


def test_unknown_pseudo_type_is_not_guessed() -> None:
    assert correction_for_type("mystery") is None
```

- [ ] **Step 2: Write failing lint tests**

```python
# tests/pipeline/test_validate.py
import pytest

from tools.openapi_pipeline.errors import ValidationError
from tools.openapi_pipeline.validate import ensure_valid_effective_schema


def valid_document() -> dict:
    return {
        "openapi": "3.0.1",
        "info": {"title": "fixture", "version": "1"},
        "servers": [{"url": "https://api.example.invalid"}],
        "paths": {
            "/ping": {
                "post": {
                    "operationId": "ping",
                    "responses": {"200": {"description": "ok"}},
                }
            }
        },
        "components": {"schemas": {"Ping": {"type": "object", "properties": {}}}},
    }


def test_effective_schema_rejects_invalid_types_and_broken_refs() -> None:
    document = valid_document()
    document["components"]["schemas"]["Broken"] = {
        "type": "bool",
        "allOf": [{"$ref": "#/components/schemas/Missing"}],
    }
    with pytest.raises(ValidationError) as error:
        ensure_valid_effective_schema(document)
    assert "invalid-type" in str(error.value)
    assert "broken-ref" in str(error.value)


def test_required_must_resolve_to_direct_or_allof_properties() -> None:
    document = valid_document()
    document["components"]["schemas"]["Broken"] = {
        "type": "object",
        "required": ["missing"],
        "properties": {"present": {"type": "string"}},
    }
    with pytest.raises(ValidationError, match="required-not-defined"):
        ensure_valid_effective_schema(document)
```

- [ ] **Step 3: Run tests and verify RED**

Run: `uv run pytest tests/pipeline/test_normalization.py tests/pipeline/test_validate.py -q`

Expected: import errors for `normalization` and `validate`.

- [ ] **Step 4: Implement deterministic pseudo-type corrections**

```python
# tools/openapi_pipeline/normalization.py
from __future__ import annotations

import re
from typing import Any

from .io import canonical_json_bytes, sha256_bytes


DIRECT_TYPES: dict[str, dict[str, Any]] = {
    "bool": {"type": "boolean"},
    "int": {"type": "integer"},
    "float": {"type": "number", "format": "float"},
    "uuid": {"type": "string", "format": "uuid"},
    "enum": {"type": "string"},
    "strings": {"type": "string"},
    "string <uuid>": {"type": "string", "format": "uuid"},
    "integer <int32>": {"type": "integer", "format": "int32"},
    "integer <int64>": {"type": "integer", "format": "int64"},
    "Array of strings <uuid>": {
        "type": "array",
        "items": {"type": "string", "format": "uuid"},
    },
}


def correction_for_type(value: str) -> dict[str, Any] | None:
    direct = DIRECT_TYPES.get(value)
    if direct is not None:
        return direct.copy()
    constant = re.fullmatch(r"constant string '([^']+)'", value)
    if constant:
        literal = constant.group(1)
        return {"type": "string", "enum": [literal]}
    return None


def _jsonpath(parts: tuple[str | int, ...]) -> str:
    result = "$"
    for part in parts:
        result += f"[{part}]" if isinstance(part, int) else f"[{part!r}]"
    return result


def build_types_overlay(document: dict[str, Any]) -> dict[str, Any]:
    actions: list[dict[str, Any]] = []

    def visit(value: Any, path: tuple[str | int, ...]) -> None:
        if isinstance(value, dict):
            raw_type = value.get("type")
            if isinstance(raw_type, str):
                correction = correction_for_type(raw_type)
                if correction is not None:
                    actions.append(
                        {
                            "target": _jsonpath(path),
                            "description": f"Normalize iiko pseudo type {raw_type!r}",
                            "x-iiko-sdk-guard": {
                                "issue": f"invalid-type-{len(actions) + 1}",
                                "expected-matches": 1,
                                "expected-sha256": sha256_bytes(canonical_json_bytes(value)),
                            },
                            "update": correction,
                        }
                    )
            for key, child in value.items():
                visit(child, (*path, key))
        elif isinstance(value, list):
            for index, child in enumerate(value):
                visit(child, (*path, index))

    visit(document, ())
    return {
        "overlay": "1.1.0",
        "info": {"title": "Normalize iiko pseudo types", "version": "1.0.0"},
        "actions": actions,
    }
```

- [ ] **Step 5: Implement structural lint**

`tools/openapi_pipeline/validate.py` must expose the following exact types and entry point:

```python
from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from .errors import ValidationError
from .inventory import HTTP_METHODS


VALID_TYPES = {"array", "boolean", "integer", "number", "object", "string"}


@dataclass(frozen=True, order=True)
class LintIssue:
    code: str
    path: str
    message: str


def _resolve_ref(document: dict[str, Any], ref: str) -> Any:
    if not ref.startswith("#/"):
        raise KeyError(ref)
    value: Any = document
    for token in ref[2:].split("/"):
        value = value[token.replace("~1", "/").replace("~0", "~")]
    return value


def _properties(document: dict[str, Any], schema: dict[str, Any], seen: set[str]) -> set[str]:
    result = set(schema.get("properties", {}))
    for branch in schema.get("allOf", []):
        if not isinstance(branch, dict):
            continue
        ref = branch.get("$ref")
        if isinstance(ref, str) and ref not in seen:
            seen.add(ref)
            try:
                resolved = _resolve_ref(document, ref)
            except (KeyError, TypeError):
                continue
            if isinstance(resolved, dict):
                result |= _properties(document, resolved, seen)
        else:
            result |= _properties(document, branch, seen)
    return result


def lint_effective_schema(document: dict[str, Any]) -> list[LintIssue]:
    issues: list[LintIssue] = []
    operation_ids: dict[str, str] = {}

    def visit(value: Any, path: str) -> None:
        if isinstance(value, dict):
            raw_type = value.get("type")
            if isinstance(raw_type, str) and raw_type not in VALID_TYPES:
                issues.append(LintIssue("invalid-type", path, raw_type))
            ref = value.get("$ref")
            if isinstance(ref, str):
                try:
                    _resolve_ref(document, ref)
                except (KeyError, TypeError):
                    issues.append(LintIssue("broken-ref", path, ref))
            required = value.get("required")
            if isinstance(required, list):
                missing = sorted(set(required) - _properties(document, value, set()))
                if missing:
                    issues.append(LintIssue("required-not-defined", path, ", ".join(missing)))
            if raw_type == "array" and "items" not in value:
                issues.append(LintIssue("array-without-items", path, "items is required"))
            for key, child in value.items():
                visit(child, f"{path}/{key}")
        elif isinstance(value, list):
            for index, child in enumerate(value):
                visit(child, f"{path}/{index}")

    visit(document, "#")
    for route, path_item in document.get("paths", {}).items():
        for method, operation in path_item.items():
            if method.lower() not in HTTP_METHODS:
                continue
            operation_id = operation.get("operationId")
            location = f"{method.upper()} {route}"
            if not isinstance(operation_id, str) or not operation_id:
                issues.append(LintIssue("missing-operation-id", location, "operationId is required"))
            elif operation_id in operation_ids:
                issues.append(
                    LintIssue("duplicate-operation-id", location, operation_ids[operation_id])
                )
            else:
                operation_ids[operation_id] = location
    if not document.get("servers"):
        issues.append(LintIssue("missing-servers", "#", "at least one server is required"))
    return sorted(issues)


def ensure_valid_effective_schema(document: dict[str, Any]) -> None:
    issues = lint_effective_schema(document)
    if issues:
        summary = "; ".join(f"{issue.code}@{issue.path}: {issue.message}" for issue in issues)
        raise ValidationError(summary)
```

- [ ] **Step 6: Verify GREEN and commit**

Run: `uv run pytest tests/pipeline/test_normalization.py tests/pipeline/test_validate.py -q`

Expected: `4 passed`.

Run: `uv run ruff check tools/openapi_pipeline/normalization.py tools/openapi_pipeline/validate.py tests/pipeline`

Expected: exit 0.

```bash
git add tools/openapi_pipeline tests/pipeline
git commit -m "feat: normalize and lint effective OpenAPI"
```

### Task 6: Pin OpenAPI Generator and generate only source code into staging

**Files:**

- Create: `generator/config.yaml`
- Create: `generator/toolchain.lock`
- Create: `generator/manual-files.txt`
- Create: `tools/openapi_pipeline/generator.py`
- Create: `tests/pipeline/test_generator.py`

**Interfaces:**

- Consumes: effective schema, model mappings, exact generator lock.
- Produces: validated staged package in `build/generated/iikocloud_client`; Docker commands are lists and never invoke a shell.

- [ ] **Step 1: Write failing command-construction tests**

```python
# tests/pipeline/test_generator.py
from pathlib import Path

import yaml

from tools.openapi_pipeline.generator import (
    Toolchain,
    build_generate_command,
    write_effective_generator_config,
)


def test_generate_command_uses_digest_and_never_skips_validation(tmp_path: Path) -> None:
    base = tmp_path / "generator/config.yaml"
    base.parent.mkdir(parents=True)
    base.write_text("additionalProperties:\n  packageName: iikocloud_client\n")
    effective = tmp_path / "build/generator-config.yaml"
    write_effective_generator_config(
        base,
        effective,
        model_mappings={"Raw.Generic`1[System.String]": "StringGeneric"},
        package_version="0.1.0",
    )
    toolchain = Toolchain(
        image="openapitools/openapi-generator-cli",
        version="v7.22.0",
        digest="sha256:" + "a" * 64,
    )
    command = build_generate_command(root=tmp_path, toolchain=toolchain)
    rendered = " ".join(command)
    assert "openapitools/openapi-generator-cli@sha256:" in rendered
    assert "--skip-validate-spec" not in command
    assert "--network none" in rendered
    assert "/workspace/build/generator-config.yaml" in command
    config = yaml.safe_load(effective.read_text())
    assert config["modelNameMappings"] == {
        "Raw.Generic`1[System.String]": "StringGeneric"
    }
    assert config["additionalProperties"]["packageVersion"] == "0.1.0"
```

- [ ] **Step 2: Run the test and verify RED**

Run: `uv run pytest tests/pipeline/test_generator.py -q`

Expected: import error for `generator`.

- [ ] **Step 3: Add exact generator configuration**

```yaml
# generator/config.yaml
additionalProperties:
  packageName: iikocloud_client
  projectName: iikocloud-client
  packageVersion: 0.1.0
  library: httpx
  generateSourceCodeOnly: true
  supportHttpxSync: false
  hideGenerationTimestamp: true
  lazyImports: false
  disallowAdditionalPropertiesIfNotPresent: false
  useOneOfDiscriminatorLookup: false
  setEnsureAsciiToFalse: true
```

```text
# generator/manual-files.txt
iikocloud_client/_contracts/__init__.py
iikocloud_client/_contracts/rate-limits.yaml
```

`generator/toolchain.lock` is JSON with exact fields `image`, `version`, and `digest`. Create it only through the `pin_toolchain()` function below so the digest cannot be copied incorrectly.

- [ ] **Step 4: Implement strict toolchain parsing and Docker commands**

```python
# tools/openapi_pipeline/generator.py
from __future__ import annotations

import json
import os
import re
import subprocess
from dataclasses import dataclass
from pathlib import Path

import yaml

from .errors import PipelineError
from .io import write_json_atomic


@dataclass(frozen=True)
class Toolchain:
    image: str
    version: str
    digest: str

    @property
    def pinned_image(self) -> str:
        return f"{self.image}@{self.digest}"

    @classmethod
    def load(cls, path: Path) -> "Toolchain":
        data = json.loads(path.read_text(encoding="utf-8"))
        value = cls(data["image"], data["version"], data["digest"])
        if value.version != "v7.22.0" or not re.fullmatch(r"sha256:[0-9a-f]{64}", value.digest):
            raise PipelineError("generator/toolchain.lock is not pinned to v7.22.0 and a digest")
        return value


def pin_toolchain(path: Path) -> Toolchain:
    tagged = "openapitools/openapi-generator-cli:v7.22.0"
    subprocess.run(["docker", "pull", tagged], check=True)
    completed = subprocess.run(
        ["docker", "image", "inspect", tagged, "--format", "{{index .RepoDigests 0}}"],
        check=True,
        capture_output=True,
        text=True,
    )
    repo_digest = completed.stdout.strip()
    image, digest = repo_digest.rsplit("@", 1)
    toolchain = Toolchain(image=image, version="v7.22.0", digest=digest)
    write_json_atomic(path, toolchain.__dict__)
    return toolchain


def build_validate_command(root: Path, toolchain: Toolchain) -> list[str]:
    return [
        "docker", "run", "--rm", "--network", "none",
        "--user", f"{os.getuid()}:{os.getgid()}",
        "-v", f"{root}:/workspace",
        toolchain.pinned_image,
        "validate", "-i", "/workspace/build/openapi/effective.json",
    ]


def write_effective_generator_config(
    base_path: Path,
    destination: Path,
    *,
    model_mappings: dict[str, str],
    package_version: str,
) -> None:
    config = yaml.safe_load(base_path.read_text(encoding="utf-8"))
    config["modelNameMappings"] = dict(sorted(model_mappings.items()))
    config["additionalProperties"]["packageVersion"] = package_version
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(yaml.safe_dump(config, sort_keys=False), encoding="utf-8")


def build_generate_command(root: Path, toolchain: Toolchain) -> list[str]:
    return [
        "docker", "run", "--rm", "--network", "none",
        "--user", f"{os.getuid()}:{os.getgid()}",
        "-v", f"{root}:/workspace",
        toolchain.pinned_image,
        "generate",
        "-i", "/workspace/build/openapi/effective.json",
        "-g", "python",
        "-c", "/workspace/build/generator-config.yaml",
        "-o", "/workspace/build/generated",
    ]


def run_generator(
    root: Path,
    toolchain: Toolchain,
    mappings: dict[str, str],
    package_version: str,
) -> None:
    write_effective_generator_config(
        root / "generator/config.yaml",
        root / "build/generator-config.yaml",
        model_mappings=mappings,
        package_version=package_version,
    )
    subprocess.run(build_validate_command(root, toolchain), check=True)
    subprocess.run(build_generate_command(root, toolchain), check=True)
```

- [ ] **Step 5: Generate the real digest and verify command tests**

Run: `uv run python -c "from pathlib import Path; from tools.openapi_pipeline.generator import pin_toolchain; print(pin_toolchain(Path('generator/toolchain.lock')).pinned_image)"`

Expected: output starts with `openapitools/openapi-generator-cli@sha256:` and contains 64 hex digest characters.

Run: `uv run pytest tests/pipeline/test_generator.py -q`

Expected: `1 passed`.

- [ ] **Step 6: Add a Docker smoke test against the minimal fixture**

Add these imports and test to `tests/pipeline/test_generator.py`:

```python
import json
import subprocess

import pytest

from tools.openapi_pipeline.generator import build_validate_command


@pytest.mark.docker
def test_pinned_generator_validates_minimal_fixture(tmp_path: Path) -> None:
    document = json.loads(Path("tests/fixtures/openapi/minimal-v1.json").read_text())
    document["servers"] = [{"url": "https://api.example.invalid"}]
    document["paths"]["/api/1/ping"]["post"]["operationId"] = "ping"
    effective = tmp_path / "build/openapi/effective.json"
    effective.parent.mkdir(parents=True)
    effective.write_text(json.dumps(document))
    toolchain = Toolchain.load(Path("generator/toolchain.lock"))
    completed = subprocess.run(build_validate_command(tmp_path, toolchain), check=False)
    assert completed.returncode == 0
```

Run: `uv run pytest -m docker tests/pipeline/test_generator.py -q`

Expected: Docker validation exits 0.

- [ ] **Step 7: Commit the pinned generator**

```bash
git add generator tools/openapi_pipeline/generator.py tests/pipeline/test_generator.py
git commit -m "build: pin OpenAPI Generator 7.22.0"
```

### Task 7: Build bootstrap, sync, verify, reports, and transactional promotion

**Files:**

- Create: `tools/openapi_pipeline/reports.py`
- Create: `tools/openapi_pipeline/promotion.py`
- Create: `tools/openapi_pipeline/package_checks.py`
- Create: `tools/openapi_pipeline/pipeline.py`
- Create/populate transactionally: `generator/generated-manifest.json`
- Modify: `tools/openapi_pipeline/cli.py`
- Create: `tests/pipeline/test_promotion.py`
- Create: `tests/pipeline/test_pipeline.py`
- Create: `tests/pipeline/test_package_checks.py`

**Interfaces:**

- Consumes: `RepoPaths`, candidate/raw snapshot, overlays, registries, generator.
- Produces: `bootstrap`, `sync`, `verify`, `upstream-check`; promotion is all-or-rollback for upstream snapshot, generated tree, and generated manifest.

- [ ] **Step 1: Write failing transactional-promotion tests**

```python
# tests/pipeline/test_promotion.py
from pathlib import Path

import pytest

from tools.openapi_pipeline.promotion import PromotionItem, promote_transaction


def test_promotion_rolls_back_all_items_when_second_replace_fails(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    first = tmp_path / "first.txt"
    second = tmp_path / "second.txt"
    first.write_text("old-first")
    second.write_text("old-second")
    new_first = tmp_path / "new-first.txt"
    new_second = tmp_path / "new-second.txt"
    new_first.write_text("new-first")
    new_second.write_text("new-second")

    real_replace = __import__("os").replace
    calls = 0

    def fail_second(source: str | Path, target: str | Path) -> None:
        nonlocal calls
        calls += 1
        if calls == 4:
            raise OSError("simulated promotion failure")
        real_replace(source, target)

    monkeypatch.setattr("tools.openapi_pipeline.promotion.os.replace", fail_second)
    with pytest.raises(OSError, match="simulated"):
        promote_transaction(
            [PromotionItem(new_first, first), PromotionItem(new_second, second)]
        )
    assert first.read_text() == "old-first"
    assert second.read_text() == "old-second"
```

- [ ] **Step 2: Write failing pipeline orchestration tests**

```python
# tests/pipeline/test_pipeline.py
from pathlib import Path
from unittest.mock import Mock

import pytest

from tools.openapi_pipeline.errors import StaleOverlayError
from tools.openapi_pipeline.fetch import FetchResult
from tools.openapi_pipeline.paths import RepoPaths
from tools.openapi_pipeline.pipeline import PipelineDependencies, sync


@pytest.fixture
def fake_dependencies(tmp_path: Path) -> PipelineDependencies:
    paths = RepoPaths(tmp_path)
    paths.candidate.parent.mkdir(parents=True)
    paths.candidate.write_text('{"openapi":"3.0.1","info":{},"paths":{}}')
    generated = tmp_path / "build/generated/iikocloud_client"
    generated.mkdir(parents=True)
    return PipelineDependencies(
        paths=paths,
        fetch=Mock(return_value=FetchResult("a" * 64, paths.candidate, True)),
        apply_corrections=Mock(return_value=({}, {})),
        validate=Mock(),
        generate=Mock(return_value=generated),
        verify_package=Mock(),
        promote=Mock(),
    )


def test_sync_does_not_promote_candidate_when_overlay_is_stale(
    tmp_path: Path, fake_dependencies: PipelineDependencies
) -> None:
    committed = tmp_path / "openapi/upstream/iikocloud.openapi.json"
    committed.parent.mkdir(parents=True)
    committed.write_text('{"openapi":"3.0.1","info":{},"paths":{}}')
    fake_dependencies.apply_corrections.side_effect = StaleOverlayError("stale")

    with pytest.raises(StaleOverlayError):
        sync(fake_dependencies)

    assert committed.read_text() == '{"openapi":"3.0.1","info":{},"paths":{}}'
    assert not (tmp_path / "src/iikocloud_client").exists()
```

- [ ] **Step 3: Run tests and verify RED**

Run: `uv run pytest tests/pipeline/test_promotion.py tests/pipeline/test_pipeline.py tests/pipeline/test_package_checks.py -q`

Expected: import errors for `promotion` and `pipeline`.

- [ ] **Step 4: Implement rollback-safe promotion**

```python
# tools/openapi_pipeline/promotion.py
from __future__ import annotations

import os
import shutil
import uuid
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class PromotionItem:
    staged: Path
    target: Path


def promote_transaction(items: list[PromotionItem]) -> None:
    backups: list[tuple[Path, Path]] = []
    promoted: list[Path] = []
    token = uuid.uuid4().hex
    try:
        for item in items:
            item.target.parent.mkdir(parents=True, exist_ok=True)
            if item.target.exists():
                backup = item.target.with_name(f".{item.target.name}.backup-{token}")
                os.replace(item.target, backup)
                backups.append((backup, item.target))
            os.replace(item.staged, item.target)
            promoted.append(item.target)
    except BaseException:
        for target in reversed(promoted):
            if target.is_dir():
                shutil.rmtree(target)
            else:
                target.unlink(missing_ok=True)
        for backup, target in reversed(backups):
            os.replace(backup, target)
        raise
    else:
        for backup, _target in backups:
            if backup.is_dir():
                shutil.rmtree(backup)
            else:
                backup.unlink(missing_ok=True)
```

- [ ] **Step 5: Implement orchestration as injectable stages**

`tools/openapi_pipeline/pipeline.py` must define:

```python
@dataclass
class PipelineDependencies:
    paths: RepoPaths
    fetch: Callable[[], FetchResult]
    apply_corrections: Callable[[dict[str, Any]], tuple[dict[str, Any], dict[str, str]]]
    validate: Callable[[dict[str, Any]], None]
    generate: Callable[[dict[str, str]], Path]
    verify_package: Callable[[Path], None]
    promote: Callable[[list[PromotionItem]], None] = promote_transaction
```

Implement `sync(dependencies)` in this exact order:

```python
def sync(dependencies: PipelineDependencies) -> None:
    fetched = dependencies.fetch()
    candidate = load_json(fetched.path)
    effective, model_mappings = dependencies.apply_corrections(candidate)
    dependencies.validate(effective)
    write_json_atomic(dependencies.paths.effective, effective)
    generated_package = dependencies.generate(model_mappings)

    staged_snapshot = dependencies.paths.build / "promotion/iikocloud.openapi.json"
    staged_package = dependencies.paths.build / "promotion/iikocloud_client"
    staged_manifest = dependencies.paths.build / "promotion/generated-manifest.json"
    shutil.rmtree(staged_package.parent, ignore_errors=True)
    staged_snapshot.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(fetched.path, staged_snapshot)
    shutil.copytree(generated_package, staged_package, dirs_exist_ok=False)
    write_generated_manifest(
        generated_package,
        staged_manifest,
        effective_schema_sha256=sha256_json(effective),
        toolchain=load_toolchain(dependencies.paths.root / "generator/toolchain.lock"),
    )
    for relative in (dependencies.paths.root / "generator/manual-files.txt").read_text().splitlines():
        relative = relative.strip()
        if not relative or relative.startswith("#"):
            continue
        package_relative = Path(relative).relative_to("iikocloud_client")
        source = dependencies.paths.root / "src/iikocloud_client" / package_relative
        destination = staged_package / package_relative
        if destination.exists():
            raise PipelineError(f"Generated/manual file collision: {relative}")
        if source.exists():
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, destination)
    dependencies.verify_package(staged_package)
    dependencies.promote(
        [
            PromotionItem(staged_snapshot, dependencies.paths.upstream),
            PromotionItem(staged_package, dependencies.paths.root / "src/iikocloud_client"),
            PromotionItem(
                staged_manifest,
                dependencies.paths.root / "generator/generated-manifest.json",
            ),
        ]
    )
```

`write_generated_manifest` records schema hash, generator version/digest, and sorted `relative_path -> sha256` entries from the raw generator output before manual files are copied. `package_checks.verify_package` copies the staged package into a clean `build/package-check/src/`, writes a minimal PEP 621/setuptools project with the exact Task 11 runtime dependencies, builds it via `python -m build --no-isolation --wheel`, installs the wheel in an isolated uv environment, and imports `ApiClient`, `Configuration`, every generated API module, and every generated model module. Subprocesses receive argument lists and an explicit working directory. `tests/pipeline/test_package_checks.py` uses a two-module fixture and asserts a deliberately broken generated import fails before promotion.

`verify` repeats corrections, validation, generation, the same package check, root `uv build`, isolated wheel import, then compares schema/toolchain metadata and every generated file hash against `generator/generated-manifest.json`; it separately verifies the two manual files. It never downloads upstream. `upstream-check` downloads and writes reports but never promotes. Reports go to `build/reports/upstream-diff.json` and `.md`.

- [ ] **Step 6: Implement two-step bootstrap**

`bootstrap` without `--accept-current-upstream` downloads candidate and writes only:

```text
build/bootstrap/types.overlay.yaml
build/bootstrap/operation-ids.yaml
build/bootstrap/model-collisions.yaml
build/reports/upstream-diff.md
```

Operation candidates follow this deterministic order: request schema verb phrase when it ends in `Request`, otherwise normalized path segments after `/api/{version}`, finally the HTTP method to resolve a collision. The command exits non-zero while `model-collisions.yaml` is non-empty.

`bootstrap --accept-current-upstream` requires the destination operation registry to be absent or empty. It combines the reviewed mechanical candidates under `build/bootstrap/` with any reviewed semantic overlays and fixtures already prepared in the worktree, then builds and validates the effective schema, generates the SDK, and runs staging package checks. Only after all checks pass does one `promote_transaction` replace the raw snapshot, mechanical registry/overlay destinations, and generated package. Failure leaves every destination unchanged and preserves the candidates for diagnosis. It refuses to overwrite an existing non-empty registry; later updates always use `sync`.

- [ ] **Step 7: Wire exact CLI arguments**

Replace the Task 1 temporary dispatch in `cli.py` with lazy imports and these arguments:

```text
bootstrap [--accept-current-upstream]
sync [--offline]
verify
upstream-check
```

`main()` catches only `PipelineError`, writes `error: {message}` to stderr, and returns exit code 2. Unexpected exceptions keep their traceback.

- [ ] **Step 8: Verify pipeline tests and Docker fixture**

Run: `uv run pytest tests/pipeline/test_promotion.py tests/pipeline/test_pipeline.py -q`

Expected: all focused tests pass.

Run: `uv run pytest -m docker tests/pipeline/test_generator.py -q`

Expected: pinned generator validates the fixture.

Run: `uv run ruff check tools tests/pipeline`

Expected: exit 0.

- [ ] **Step 9: Commit offline orchestration**

```bash
git add tools/openapi_pipeline tests/pipeline
git commit -m "feat: orchestrate reproducible SDK generation"
```

**Review Gate A:** At this point all pipeline behavior is testable on fixtures, no iiko request has been sent, and the existing generated SDK remains in place.

### Task 8: Enforce persistent rate limits, process locking, and 429 circuit breaking

**Files:**

- Create: `contracts/rate-limits.yaml`
- Create: `contracts/live-operations.yaml`
- Create: `tools/openapi_pipeline/live/__init__.py`
- Create: `tools/openapi_pipeline/live/lock.py`
- Create: `tools/openapi_pipeline/live/rates.py`
- Create: `tools/openapi_pipeline/live/state.py`
- Create: `tests/live_support/test_rates.py`
- Create: `tests/live_support/test_circuit.py`

**Interfaces:**

- Consumes: verified operation limits, profile fingerprint, injectable monotonic/wall clock and sleeper.
- Produces: `LiveRateGuard.acquire(operation_id)`, `record_status(operation_id, status)`, persistent circuit state, exclusive `LiveProcessLock`.

- [ ] **Step 1: Add disabled-by-default contracts**

```yaml
# contracts/rate-limits.yaml
version: 1
defaults:
  utilization: 0.20
  global_min_interval_seconds: 15
  max_calls_per_operation_per_run: 1
operations:
  authenticate:
    server_limit: {calls: 1, per_seconds: 5}
    source: existing-manager-configuration
    verified: false
  get_organizations:
    server_limit: {calls: 1, per_seconds: 10}
    source: existing-manager-configuration
    verified: false
  get_external_menus:
    server_limit: {calls: 1, per_seconds: 1800}
    source: existing-manager-configuration
    verified: false
  get_external_menu_by_id:
    server_limit: {calls: 5, per_seconds: 60}
    source: existing-manager-configuration
    verified: false
  get_stop_lists:
    server_limit: {calls: 10, per_seconds: 60}
    source: existing-manager-configuration
    verified: false
  add_products_to_stop_list:
    server_limit: {calls: 1, per_seconds: 60}
    source: conservative-unverified
    verified: false
  remove_products_from_stop_list:
    server_limit: {calls: 1, per_seconds: 60}
    source: conservative-unverified
    verified: false
```

No live call is permitted until the user reviews a value and changes its `verified` field to `true` in a dedicated commit.

```yaml
# contracts/live-operations.yaml
version: 1
operations:
  authenticate: {kind: auth, cleanup: null}
  get_organizations: {kind: read, cleanup: null}
  get_external_menus: {kind: read, cleanup: null}
  get_external_menu_by_id: {kind: read, cleanup: null}
  get_stop_lists: {kind: read, cleanup: null}
  add_products_to_stop_list:
    kind: compensating
    cleanup: remove_products_from_stop_list
  remove_products_from_stop_list: {kind: cleanup, cleanup: null}
```

- [ ] **Step 2: Write failing safe-interval and circuit tests**

```python
# tests/live_support/test_rates.py
import pytest

from tools.openapi_pipeline.errors import SafetyError
from tools.openapi_pipeline.live.rates import RateLimit, RatePolicy


def test_safe_interval_uses_twenty_percent_and_global_floor() -> None:
    policy = RatePolicy(utilization=0.20, global_min_interval_seconds=15)
    assert policy.safe_interval(RateLimit(calls=1, per_seconds=60)) == 300
    assert policy.safe_interval(RateLimit(calls=100, per_seconds=60)) == 15


def test_unverified_operation_is_disabled() -> None:
    policy = RatePolicy(utilization=0.20, global_min_interval_seconds=15)
    with pytest.raises(SafetyError, match="not verified"):
        policy.operation_budget(
            "unsafe_operation",
            {"verified": False, "server_limit": {"calls": 1, "per_seconds": 60}}
        )
```

```python
# tests/live_support/test_circuit.py
from pathlib import Path

import pytest

from tools.openapi_pipeline.errors import SafetyError
from tools.openapi_pipeline.live.state import LiveStateStore


def test_429_opens_profile_circuit_until_manual_reset(tmp_path: Path) -> None:
    store = LiveStateStore(tmp_path / "live.json")
    store.record_status("profile-hash", "get_organizations", 429, now=100.0)
    with pytest.raises(SafetyError, match="circuit is open"):
        store.assert_circuit_closed("profile-hash")
    store.reset_circuit("profile-hash")
    store.assert_circuit_closed("profile-hash")
```

- [ ] **Step 3: Run focused tests and verify RED**

Run: `uv run pytest tests/live_support/test_rates.py tests/live_support/test_circuit.py -q`

Expected: import errors for live support modules.

- [ ] **Step 4: Implement exact budget calculation**

```python
# tools/openapi_pipeline/live/rates.py
from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Any

from ..errors import SafetyError


@dataclass(frozen=True)
class RateLimit:
    calls: int
    per_seconds: float


@dataclass(frozen=True)
class OperationBudget:
    operation_id: str
    safe_interval_seconds: float
    max_calls_per_run: int


@dataclass(frozen=True)
class RatePolicy:
    utilization: float
    global_min_interval_seconds: float

    def operation_budget(
        self,
        operation_id: str,
        value: dict[str, Any],
        *,
        max_calls_per_run: int = 1,
    ) -> OperationBudget:
        if value.get("verified") is not True:
            raise SafetyError("Operation rate limit is not verified")
        limit = value["server_limit"]
        return OperationBudget(
            operation_id=operation_id,
            safe_interval_seconds=self.safe_interval(
                RateLimit(int(limit["calls"]), float(limit["per_seconds"]))
            ),
            max_calls_per_run=max_calls_per_run,
        )

    def safe_interval(self, limit: RateLimit) -> float:
        if limit.calls <= 0 or limit.per_seconds <= 0 or not 0 < self.utilization <= 0.20:
            raise SafetyError("Invalid or unsafe rate policy")
        interval = limit.per_seconds / (limit.calls * self.utilization)
        return float(max(self.global_min_interval_seconds, math.ceil(interval)))
```

`RateCatalog.load(path)` requires `version == 1`, rejects defaults with utilization above `0.20` or a per-run count other than `1`, and returns an `OperationBudget` only for an explicitly listed, verified operation. Unknown IDs fail closed. `LiveRateGuard` receives this catalog rather than reconstructing limits ad hoc.

- [ ] **Step 5: Implement atomic state and circuit behavior**

`LiveStateStore` persists this shape without credentials:

```json
{
  "profiles": {
    "profile-hash": {
      "circuit_opened_at": null,
      "last_calls": {"get_organizations": 100.0}
    }
  }
}
```

`record_status(..., 429, ...)` sets `circuit_opened_at`; every acquire first calls `assert_circuit_closed`. `reset_circuit` is the only method that clears it. Writes use `write_json_atomic(..., mode=0o600)`.

`LiveRateGuard.acquire` enforces, in order: process lock held, closed circuit, verified operation, one-call-per-run, global last-call interval, per-operation persistent interval. It sleeps once for the calculated remaining duration; it never retries an HTTP call.

- [ ] **Step 6: Implement Linux/WSL process lock**

`LiveProcessLock` opens `.state/live.lock` with mode `0600` and acquires `fcntl.flock(fd, LOCK_EX | LOCK_NB)`. A second process raises `SafetyError("another live test process is active")`. The context manager always unlocks and closes the file descriptor.

- [ ] **Step 7: Verify GREEN and commit**

Run: `uv run pytest tests/live_support/test_rates.py tests/live_support/test_circuit.py -q`

Expected: all focused tests pass without sleeping in wall-clock time; tests inject fake clocks/sleepers.

```bash
git add contracts tools/openapi_pipeline/live tests/live_support
git commit -m "feat: guard live API rate limits"
```

### Task 9: Add private profiles, a no-retry live session, pytest gates, and receipts

**Files:**

- Create: `config/live-profile.example.toml`
- Create: `private/.gitignore`
- Create: `private/README.md`
- Create: `tools/openapi_pipeline/live/profile.py`
- Create: `tools/openapi_pipeline/live/session.py`
- Create: `tools/openapi_pipeline/live/receipt.py`
- Create: `tests/conftest.py`
- Create: `tests/live_support/test_profile.py`
- Create: `tests/live_support/test_session.py`
- Create: `tests/live_support/test_receipt.py`

**Interfaces:**

- Consumes: ignored TOML profile, explicit ignored `.env` plus process environment, `LiveRateGuard`, `httpx.AsyncBaseTransport`.
- Produces: `ResolvedLiveProfile`, `SafeLiveSession.authenticate()`, guarded `request_json()`, hash-bound live receipt.

- [ ] **Step 1: Define the public example and ignored private location**

```toml
# config/live-profile.example.toml
name = "test-server"
base_url = "https://api-ru.iiko.services"
api_login_env = "IIKO_API_KEY"
organization_id_env = "IIKO_TEST_ORGANIZATION_ID"
external_menu_id_env = "IIKO_TEST_EXTERNAL_MENU_ID"
terminal_group_id_env = "IIKO_TEST_TERMINAL_GROUP_ID"
write_product_id_env = "IIKO_TEST_WRITE_PRODUCT_ID"
allow_write = false
allowed_organization_ids = []
```

```gitignore
# private/.gitignore
*
!.gitignore
!README.md
```

`private/README.md` documents copying the example to `private/profiles/test-server.toml`, exporting the named environment variables, setting mode `0600`, and never sharing the file.

- [ ] **Step 2: Write failing profile and session tests**

```python
# tests/live_support/test_profile.py
from pathlib import Path

import pytest

from tools.openapi_pipeline.errors import SafetyError
from tools.openapi_pipeline.live.profile import load_profile


def test_profile_resolves_secrets_without_storing_them(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    profile = tmp_path / "profile.toml"
    profile.write_text(
        'name="test"\nbase_url="https://api.example.invalid"\n'
        'api_login_env="IIKO_LOGIN"\norganization_id_env="IIKO_ORG"\n'
        'external_menu_id_env="IIKO_MENU"\nallow_write=false\nallowed_organization_ids=[]\n'
    )
    profile.chmod(0o600)
    monkeypatch.setenv("IIKO_LOGIN", "secret-login")
    monkeypatch.setenv("IIKO_ORG", "00000000-0000-0000-0000-000000000001")
    monkeypatch.setenv("IIKO_MENU", "1")
    resolved = load_profile(profile)
    assert resolved.api_login == "secret-login"
    assert "secret-login" not in resolved.fingerprint
    assert len(resolved.fingerprint) == 64


def test_profile_reads_primary_key_from_explicit_env_file_without_fallback(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    profile = tmp_path / "profile.toml"
    profile.write_text(
        'name="test"\nbase_url="https://api.example.invalid"\n'
        'api_login_env="IIKO_API_KEY"\norganization_id_env="IIKO_ORG"\n'
        'external_menu_id_env="IIKO_MENU"\nallow_write=false\nallowed_organization_ids=[]\n'
    )
    profile.chmod(0o600)
    env_file = tmp_path / ".env"
    env_file.write_text("IIKO_API_KEY=primary-login\nIIKO_API_KEY_2=secondary-login\n")
    env_file.chmod(0o600)
    monkeypatch.setenv("IIKO_ORG", "00000000-0000-0000-0000-000000000001")
    monkeypatch.setenv("IIKO_MENU", "menu-1")
    resolved = load_profile(profile, env_file=env_file)
    assert resolved.api_login == "primary-login"

    env_file.write_text("IIKO_API_KEY_2=secondary-login\n")
    with pytest.raises(SafetyError, match="IIKO_API_KEY"):
        load_profile(profile, env_file=env_file)


def test_missing_secret_environment_variable_fails(tmp_path: Path) -> None:
    profile = tmp_path / "profile.toml"
    profile.write_text(
        'name="test"\nbase_url="https://api.example.invalid"\n'
        'api_login_env="MISSING"\norganization_id_env="MISSING_ORG"\n'
        'external_menu_id_env="MISSING_MENU"\nallow_write=false\nallowed_organization_ids=[]\n'
    )
    profile.chmod(0o600)
    with pytest.raises(SafetyError, match="MISSING"):
        load_profile(profile)


def test_write_profile_requires_dedicated_terminal_and_product_env(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    profile = tmp_path / "profile.toml"
    profile.write_text(
        'name="test"\nbase_url="https://api.example.invalid"\n'
        'api_login_env="IIKO_LOGIN"\norganization_id_env="IIKO_ORG"\n'
        'external_menu_id_env="IIKO_MENU"\nterminal_group_id_env="IIKO_TERMINAL"\n'
        'write_product_id_env="IIKO_PRODUCT"\nallow_write=true\nallowed_organization_ids=[]\n'
    )
    profile.chmod(0o600)
    monkeypatch.setenv("IIKO_LOGIN", "secret-login")
    monkeypatch.setenv("IIKO_ORG", "00000000-0000-0000-0000-000000000001")
    monkeypatch.setenv("IIKO_MENU", "menu-1")
    with pytest.raises(SafetyError, match="IIKO_TERMINAL"):
        load_profile(profile)
```

```python
# tests/live_support/test_session.py
from unittest.mock import AsyncMock

import httpx
import pytest

from tools.openapi_pipeline.errors import SafetyError
from tools.openapi_pipeline.live.profile import ResolvedLiveProfile
from tools.openapi_pipeline.live.session import SafeLiveSession
from tools.openapi_pipeline.live.state import LiveStateStore


@pytest.mark.asyncio
async def test_session_never_retries_429_and_opens_circuit(tmp_path) -> None:
    organization_calls = 0

    async def handler(request: httpx.Request) -> httpx.Response:
        nonlocal organization_calls
        if request.url.path == "/api/1/access_token":
            return httpx.Response(200, json={"token": "test-token"})
        organization_calls += 1
        return httpx.Response(429, json={"error": "too many"})

    profile = ResolvedLiveProfile(
        name="test",
        base_url="https://api.example.invalid",
        api_login="test-login",
        organization_id="00000000-0000-0000-0000-000000000001",
        external_menu_id="menu-1",
        terminal_group_id=None,
        write_product_id=None,
        allow_write=False,
        allowed_organization_ids=(),
        fingerprint="f" * 64,
    )
    state = LiveStateStore(tmp_path / "live.json")
    session = SafeLiveSession(
        profile=profile,
        guard=AsyncMock(),
        state=state,
        transport=httpx.MockTransport(handler),
    )
    await session.authenticate()
    with pytest.raises(SafetyError, match="429"):
        await session.request_json("get_organizations", "POST", "/api/1/organizations", {})
    assert organization_calls == 1
    assert state.circuit_is_open(profile.fingerprint)
```

```python
# tests/live_support/test_receipt.py
from pathlib import Path

from tools.openapi_pipeline.live.receipt import LiveReceipt


def test_receipt_matches_only_exact_profile_and_artifact_hashes(tmp_path: Path) -> None:
    receipt = LiveReceipt(
        run_id="run-1",
        profile_fingerprint="p" * 64,
        effective_schema_sha256="s" * 64,
        generated_tree_sha256="g" * 64,
        operations=("authenticate", "get_organizations"),
        had_429=False,
        completed=True,
    )
    path = tmp_path / "receipt.json"
    receipt.write(path)
    loaded = LiveReceipt.load(path)
    assert loaded.matches("p" * 64, "s" * 64, "g" * 64)
    assert not loaded.matches("p" * 64, "x" * 64, "g" * 64)
```

- [ ] **Step 3: Run tests and verify RED**

Run: `uv run pytest tests/live_support/test_profile.py tests/live_support/test_session.py tests/live_support/test_receipt.py -q`

Expected: import errors for `profile` and `session`.

- [ ] **Step 4: Implement strict profile loading**

```python
# tools/openapi_pipeline/live/profile.py
from __future__ import annotations

import hashlib
import os
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import urlsplit

from dotenv import dotenv_values

try:
    import tomllib
except ModuleNotFoundError:  # Python 3.10 SDK compatibility
    import tomli as tomllib

from ..errors import SafetyError


@dataclass(frozen=True)
class ResolvedLiveProfile:
    name: str
    base_url: str
    api_login: str
    organization_id: str
    external_menu_id: str
    terminal_group_id: str | None
    write_product_id: str | None
    allow_write: bool
    allowed_organization_ids: tuple[str, ...]
    fingerprint: str


def _required_env(name: str, file_values: dict[str, str | None]) -> str:
    value = os.environ.get(name) or file_values.get(name)
    if not value:
        raise SafetyError(f"Required environment variable is missing: {name}")
    return value


def load_profile(path: Path, *, env_file: Path | None = None) -> ResolvedLiveProfile:
    if path.stat().st_mode & 0o077:
        raise SafetyError("Live profile must not grant group/world permissions")
    if env_file is not None and env_file.stat().st_mode & 0o077:
        raise SafetyError("Environment file must not grant group/world permissions")
    file_values = dict(dotenv_values(env_file)) if env_file is not None else {}
    data = tomllib.loads(path.read_text(encoding="utf-8"))
    base_url = str(data["base_url"]).rstrip("/")
    parsed = urlsplit(base_url)
    if parsed.scheme != "https" or not parsed.netloc:
        raise SafetyError("Live base_url must be an absolute HTTPS URL")
    api_login = _required_env(str(data["api_login_env"]), file_values)
    organization_id = _required_env(str(data["organization_id_env"]), file_values)
    external_menu_id = _required_env(str(data["external_menu_id_env"]), file_values)
    allow_write = bool(data.get("allow_write", False))
    terminal_group_id = (
        _required_env(str(data["terminal_group_id_env"]), file_values)
        if allow_write
        else None
    )
    write_product_id = (
        _required_env(str(data["write_product_id_env"]), file_values)
        if allow_write
        else None
    )
    fingerprint_source = f"{data['name']}\n{base_url}\n{organization_id}".encode()
    return ResolvedLiveProfile(
        name=str(data["name"]),
        base_url=base_url,
        api_login=api_login,
        organization_id=organization_id,
        external_menu_id=external_menu_id,
        terminal_group_id=terminal_group_id,
        write_product_id=write_product_id,
        allow_write=allow_write,
        allowed_organization_ids=tuple(str(v) for v in data.get("allowed_organization_ids", [])),
        fingerprint=hashlib.sha256(fingerprint_source).hexdigest(),
    )
```

- [ ] **Step 5: Implement a single-attempt HTTP session**

`SafeLiveSession(profile, guard, state, transport=None)` owns one `httpx.AsyncClient` created with `httpx.AsyncHTTPTransport(retries=0)` unless a test transport is injected. `authenticate()`:

1. calls `guard.acquire("authenticate")`;
2. sends exactly one `POST /api/1/access_token` with `{"apiLogin": profile.api_login}`;
3. records status;
4. rejects `429` through `SafetyError` after opening the circuit;
5. stores the token only in memory and exposes it through a read-only `access_token` property for generated `Configuration`; the value is never persisted, logged, included in receipts, or returned from `repr`;
6. refuses a second authentication attempt in the same session.

`request_json(operation_id, method, path, payload)` requires prior authentication except for `authenticate`, acquires the operation budget once, sends one request, records status, returns the `httpx.Response`, and never contains a loop or retry transport.

The class exposes async context manager methods and always calls `await client.aclose()`.

- [ ] **Step 6: Implement pytest collection gates**

`tests/conftest.py` adds:

```python
def pytest_addoption(parser: pytest.Parser) -> None:
    parser.addoption("--live-profile", action="store")
    parser.addoption("--env-file", action="store")
    parser.addoption("--allow-live-write", action="store_true", default=False)
    parser.addoption("--allow-audit-residue", action="store_true", default=False)
    parser.addoption("--target-organization", action="store")
    parser.addoption("--capture-http", action="store_true", default=False)
    parser.addoption("--capture-operation", action="store")


def pytest_collection_modifyitems(config: pytest.Config, items: list[pytest.Item]) -> None:
    live_profile = config.getoption("--live-profile")
    for item in items:
        is_live = any(
            item.get_closest_marker(marker) is not None
            for marker in ("live_read_smoke", "live_read_full", "live_write")
        )
        if is_live and not live_profile:
            item.add_marker(pytest.mark.skip(reason="live tests require --live-profile"))
```

The session-scoped live fixture resolves only `private/profiles/{name}.toml`. If `--env-file` is supplied, it must resolve exactly to repository-root `.env`; there is no implicit directory search. The fixture acquires `LiveProcessLock`, loads rate contracts, constructs `LiveRateGuard`, resolves `IIKO_API_KEY` from process environment first and the explicit file second, authenticates once, yields the session, and closes it in `finally`. It never looks for or falls back to `IIKO_API_KEY_2`.

- [ ] **Step 7: Implement hash-bound receipts**

Receipt path: `.state/live-runs/{run_id}.json`. Required fields:

```json
{
  "run_id": "20260716T180000Z-a1b2c3d4",
  "profile_fingerprint": "64-hex",
  "effective_schema_sha256": "64-hex",
  "generated_tree_sha256": "64-hex",
  "operations": ["authenticate", "get_organizations"],
  "had_429": false,
  "completed": true
}
```

`LiveReceipt.matches(profile, schema_hash, generated_hash)` returns true only when all hashes match, `completed` is true, and `had_429` is false. No API login, token, organization UUID, request, or response is stored.

The session fixture creates the receipt with `completed=false` before its first live call, appends each acquired operation ID, and persists after every state change with mode `0600`. In fixture teardown it sets `completed=true` only when pytest reports no failed live test, the circuit stayed closed, both clients closed cleanly, and no mutation journal remains. The schema hash comes from `build/openapi/effective.json` recomputed from committed inputs; the generated-tree hash comes from canonical `generator/generated-manifest.json`. Thus Task 11's successful generated read-smoke creates the exact receipt required by `publish`, while interrupted or failed runs cannot authorize a release.

- [ ] **Step 8: Verify GREEN and commit**

Run: `uv run pytest tests/live_support -q`

Expected: all live-support tests pass using only mock transports and fake clocks.

```bash
git add config private tools/openapi_pipeline/live tests/conftest.py tests/live_support
git commit -m "feat: add opt-in live test session"
```

**Review Gate B:** The rate/session subsystem is fully mock-tested. Before any real request, review `contracts/rate-limits.yaml` and commit `verified: true` only for operations whose limits have been independently confirmed.

### Task 10: Sanitize and persist private HTTP captures

**Files:**

- Create: `tools/openapi_pipeline/capture.py`
- Create: `tests/capture/test_sanitizer.py`
- Create: `tests/capture/test_writer.py`
- Modify: `tools/openapi_pipeline/live/session.py`

**Interfaces:**

- Consumes: operation metadata, in-memory request/response JSON, known active secrets.
- Produces: sanitized `request.json`/`response.json` with mode `0600`, plus a run-bound `LiveCapture.write_model_pair(...)`; auth bodies and raw data are never accepted by the writer.

- [ ] **Step 1: Write failing redaction tests**

```python
# tests/capture/test_sanitizer.py
from tools.openapi_pipeline.capture import Sanitizer


def test_sanitizer_removes_secrets_pii_and_stabilizes_uuid_links() -> None:
    sanitizer = Sanitizer(known_secrets=("exact-api-login", "exact-token"))
    value = {
        "authToken": "exact-token",
        "email": "person@example.com",
        "phone": "+79991234567",
        "organizationId": "11111111-1111-4111-8111-111111111111",
        "items": [{"id": "11111111-1111-4111-8111-111111111111", "type": "DISH"}],
        "comment": "customer free text",
    }
    sanitized = sanitizer.sanitize(value, enum_keys={"type"})
    assert sanitized["authToken"] == "<redacted:secret>"
    assert sanitized["email"] == "<redacted:email>"
    assert sanitized["phone"] == "<redacted:phone>"
    assert sanitized["organizationId"] == sanitized["items"][0]["id"]
    assert sanitized["items"][0]["type"] == "DISH"
    assert sanitized["comment"] == "<redacted:string>"
```

```python
# tests/capture/test_writer.py
from pathlib import Path

import pytest

from tools.openapi_pipeline.capture import CaptureWriter
from tools.openapi_pipeline.errors import SafetyError


def test_capture_writer_forbids_auth_body_and_writes_only_after_scan(tmp_path: Path) -> None:
    writer = CaptureWriter(tmp_path, known_secrets=("secret-token",))
    with pytest.raises(SafetyError, match="auth body"):
        writer.write(
            run_id="run",
            operation_id="authenticate",
            kind="auth",
            request_json={"apiLogin": "secret-token"},
            response_json={"token": "secret-token"},
            metadata={"method": "POST", "path": "/api/1/access_token", "status": 200},
        )
    assert list(tmp_path.rglob("*.json")) == []


def test_capture_writer_sanitizes_before_writing_mode_0600(tmp_path: Path) -> None:
    writer = CaptureWriter(tmp_path, known_secrets=("secret-token",))
    writer.write(
        run_id="run",
        operation_id="get_organizations",
        kind="read",
        request_json={"organizationId": "11111111-1111-4111-8111-111111111111"},
        response_json={"name": "Private venue", "token": "secret-token"},
        metadata={
            "method": "POST",
            "path": "/api/1/organizations",
            "status": 200,
        },
    )
    response_path = tmp_path / "run/get_organizations/response.json"
    contents = response_path.read_text(encoding="utf-8")
    assert response_path.exists()
    assert response_path.stat().st_mode & 0o777 == 0o600
    assert "secret-token" not in contents
    assert "Private venue" not in contents
```

- [ ] **Step 2: Run tests and verify RED**

Run: `uv run pytest tests/capture -q`

Expected: import error for `capture`.

- [ ] **Step 3: Implement schema-aware recursive sanitization**

`Sanitizer` uses these case-insensitive key groups:

```python
SECRET_KEYS = {
    "authorization", "cookie", "set-cookie", "apikey", "api_key", "apilogin",
    "api_login", "token", "accesstoken", "access_token", "authtoken", "auth_token",
    "password", "secret",
}
EMAIL_KEYS = {"email", "emailaddress"}
PHONE_KEYS = {"phone", "phone_number", "phonenumber"}
FREE_TEXT_KEYS = {"comment", "description", "name", "address", "message"}
```

Values matching JWT/Bearer/email/phone patterns or an exact `known_secrets` value are always redacted regardless of key. UUIDs map deterministically per `Sanitizer` instance to `00000000-0000-4000-8000-{sequence:012d}`. Keys listed in `enum_keys` preserve string values after secret-pattern scanning. Non-enum free strings become `<redacted:string>`.

`RedactionHints.for_operation(effective_schema, operation_id)` resolves local `$ref`, `allOf`, `oneOf`, and `anyOf` branches for that operation's JSON request and success response, then returns the union of property names whose schema declares `enum`, `const`, or the operation's discriminator property. Cycles are cut by visited `$ref`. Capture refuses an unknown operation or a broken hint traversal; it never infers safe strings from observed values. Add a fixture test proving a menu discriminator is retained while adjacent names/comments are redacted.

- [ ] **Step 4: Implement scan-before-write capture storage**

`CaptureWriter.write`:

1. rejects `kind == "auth"` before sanitization;
2. accepts only JSON-like request/response values;
3. strips all headers except `content-type`, `accept`, `x-correlation-id`;
4. sanitizes request, response, path segments, and metadata;
5. serializes to bytes in memory;
6. scans serialized bytes again for JWT, Bearer, email, phone and each known secret;
7. writes `private/captures/{run_id}/{operation_id}/request.json` and `response.json` with `write_json_atomic(..., mode=0o600)` only if both scans pass.

Every newly created parent directory is chmod `0700`; a pre-existing group/world-readable private directory raises before writing. Binary content, non-JSON content and full query-bearing URLs raise `SafetyError`.

- [ ] **Step 5: Connect capture through live adapters, never generated files**

`LiveCapture` binds a `CaptureWriter`, run ID, selected operation, immutable `live-operations.yaml` catalog, and `RedactionHints` derived from the current effective schema. Its `write_model_pair(operation_id, request_model, response_model, metadata)` converts Pydantic models with `model_dump(mode="json", by_alias=True)` and delegates to `CaptureWriter.write` with the catalog's operation kind and allowed enum/discriminator keys. It rejects an operation other than the one explicitly selected on the command line.

Both `SafeLiveSession` and Task 11's `GeneratedLiveSdk` may receive `LiveCapture | None`. They pass the caller-supplied request JSON/model and parsed response JSON/model only after the response is complete. Neither component mutates generated SDK files, and `LiveCapture` refuses `authenticate` even if misconfigured.

- [ ] **Step 6: Verify GREEN and file permissions**

Run: `uv run pytest tests/capture -q`

Expected: all capture tests pass; the successful non-auth capture is sanitized before either file is written and both files have mode `0600`.

```bash
git add tools/openapi_pipeline/capture.py tools/openapi_pipeline/live/session.py tests/capture
git commit -m "feat: capture sanitized private API examples"
```

### Task 11: Bootstrap the real upstream, collect menu evidence, and replace the legacy generated SDK

**Files:**

- Populate: `openapi/upstream/iikocloud.openapi.json`
- Populate: `openapi/operation-ids.yaml`
- Populate: `openapi/model-name-overrides.yaml`
- Create/populate: `openapi/overlays/types.overlay.yaml`
- Create: `openapi/overlays/operations.overlay.yaml`
- Create: `openapi/overlays/polymorphism.overlay.yaml`
- Create: `openapi/overlays/contracts.overlay.yaml`
- Create: `tests/fixtures/contracts/external-menu-v2.json`
- Create: `tests/fixtures/contracts/external-menu-v3.json`
- Create: `tests/fixtures/contracts/external-menu-v4.json`
- Create: `tests/generated/test_external_menu_response.py`
- Create: `tools/openapi_pipeline/live/generated.py`
- Modify: `tests/conftest.py`
- Create: `tests/live_support/test_generated_adapter.py`
- Create: `tests/integration/read/test_organizations.py`
- Create: `src/iikocloud_client/_contracts/__init__.py`
- Create: `src/iikocloud_client/_contracts/rate-limits.yaml`
- Modify: `pyproject.toml`
- Modify: `README.md`
- Remove after successful replacement: legacy generated package/tests/docs/scripts listed below.

**Interfaces:**

- Consumes: reviewed bootstrap candidates and three separately rate-limited sanitized menu captures for requested response versions 2, 3, and 4.
- Produces: strict effective schema, evidence-backed menu union, reproducible `src/iikocloud_client`, wheel import smoke, zero regeneration diff.

- [ ] **Step 1: Seed the hand-owned files that generation must preserve**

Create `src/iikocloud_client/_contracts/__init__.py` containing only a module docstring and copy `contracts/rate-limits.yaml` byte-for-byte to `src/iikocloud_client/_contracts/rate-limits.yaml`. Task 7's `generator/manual-files.txt` then preserves both files in staging and rejects a generator collision with either path.

- [ ] **Step 2: Download and review bootstrap candidates without promotion**

Run: `uv run python -m tools.openapi_pipeline bootstrap`

Expected at the inspected 2026-07-16 upstream: report exactly 224 paths, 225 operations, and 721 schemas; committed files remain unchanged. A later count change is drift to review, not an instruction to hard-code these counts forever.

Review these generated files:

```text
build/bootstrap/types.overlay.yaml
build/bootstrap/operation-ids.yaml
build/bootstrap/model-collisions.yaml
build/reports/upstream-diff.md
```

Resolve every collision by adding a domain-specific name to the bootstrap `model-name-overrides.yaml`. Numeric suffixes such as `Item2` are rejected unless `2` is genuinely part of the upstream domain name.

- [ ] **Step 3: Normalize bearer authentication as a generated-SDK contract**

The upstream repeats an `Authorization` header parameter and does not define a reusable security scheme. Add guarded actions to `openapi/overlays/contracts.overlay.yaml` that:

1. add `components.securitySchemes.BearerAuth = {type: http, scheme: bearer}`;
2. remove each exact upstream `Authorization` header parameter after checking its fragment hash;
3. add `security: [{BearerAuth: []}]` to every iiko API operation except `/api/1/access_token`;
4. set `security: []` on `/api/1/access_token` explicitly;
5. add root `servers: [{url: https://api-ru.iiko.services}]`, while live fixtures still override `Configuration.host` from the selected profile.

Extend custom lint so generation fails if a non-auth operation lacks `BearerAuth`, the auth endpoint requires it, or an operation still contains a raw `Authorization` header parameter. Add a fixture test proving `Configuration.access_token` produces exactly one `Authorization: Bearer ...` header and that the token is absent from model dumps and `repr` output.

- [ ] **Step 4: Verify live limits before evidence calls**

For `authenticate` and `get_external_menu_by_id`, compare `contracts/rate-limits.yaml` with the authoritative account/server restriction. Commit only the verified flag changes:

```bash
git add contracts/rate-limits.yaml
git commit -m "test: verify menu live-test budgets"
```

Do not proceed while either operation remains `verified: false`.

- [ ] **Step 5: Capture one menu version per command/run**

With `private/profiles/test-server.toml` and the three required environment variables configured, run these as separate invocations. Persistent state enforces the safe interval between them:

```bash
uv run python -m tools.openapi_pipeline capture-evidence --live-profile test-server --env-file .env --operation get_external_menu_by_id --menu-version 2
uv run python -m tools.openapi_pipeline capture-evidence --live-profile test-server --env-file .env --operation get_external_menu_by_id --menu-version 3
uv run python -m tools.openapi_pipeline capture-evidence --live-profile test-server --env-file .env --operation get_external_menu_by_id --menu-version 4
```

Each invocation performs one auth call and one menu call at most. Any `429` stops the evidence process and invalidates all promotion until manual circuit reset.

- [ ] **Step 6: Build reviewed semantic candidates from sanitized evidence**

Run: `uv run python -m tools.openapi_pipeline promote-evidence --operation get_external_menu_by_id`

The command refuses promotion unless:

- captures exist for response `formatVersion` values 2, 3, and 4;
- each capture matches exactly one response branch;
- dish/combo discriminator values are internally consistent;
- at least one combo item exists when deriving `ExternalMenuComboItem` properties;
- no secret/PII scanner finding exists.

The raw evidence reader deliberately does not infer a mapping between the
`DISH`/`COMBO` literal and either structurally reviewed `oneOf` branch. It only
requires a raw literal and at least one matching branch. The next evidence
promotion analyzer must establish branch-to-literal consistency before it may
write a semantic candidate or allow `--accept`; until then the capture is raw
evidence, not a promotable contract.

It writes candidates to `build/evidence-candidates/`, including minimized synthetic fixtures and overlay actions guarded by the original schema fragment hash. After human inspection, rerun with `--accept` to copy them to `tests/fixtures/contracts/` and `openapi/overlays/`.

- [ ] **Step 7: Add the generated union contract test**

```python
# tests/generated/test_external_menu_response.py
from pathlib import Path

import pytest

from iikocloud_client.models.external_menu_response import ExternalMenuResponse


@pytest.mark.parametrize("version", [2, 3, 4])
def test_external_menu_union_selects_exactly_one_version(version: int) -> None:
    body = Path(f"tests/fixtures/contracts/external-menu-v{version}.json").read_text()
    response = ExternalMenuResponse.from_json(body)
    assert response.actual_instance.format_version == version
```

The operations overlay gives `/api/2/menu/by_id` response schema the stable title `ExternalMenuResponse`; the polymorphism overlay makes version branches disjoint. `useOneOfDiscriminatorLookup` remains false so this test exercises exact one-branch matching.

- [ ] **Step 8: Atomically accept the reviewed initial baseline**

Run: `uv run python -m tools.openapi_pipeline bootstrap --accept-current-upstream`

Expected: the command combines the reviewed bootstrap candidates, bearer corrections, semantic menu overlays, and evidence fixtures; then strict lint, generator validation, codegen, contract tests, and staging wheel checks pass. Only then are the raw snapshot, mechanical correction inputs, and generated tree promoted together. If any check fails, candidates remain under `build/`, the committed snapshot and generated SDK remain unchanged, and the legacy SDK is not removed.

- [ ] **Step 9: Exercise a guarded read through the generated SDK**

`tools/openapi_pipeline/live/generated.py` defines `GeneratedLiveSdk(api_client, profile, guard, state, capture=None)`. Its only request entry point is:

```python
async def call_generated(
    self,
    operation_id: str,
    request_model: object,
    invoke: Callable[[], Awaitable[ApiResponse[T]]],
) -> T:
    await self.guard.acquire(operation_id)
    try:
        response = await invoke()
    except ApiException as error:
        self.state.record_status(
            self.profile.fingerprint,
            operation_id,
            int(error.status or 0),
        )
        if error.status == 429:
            raise SafetyError("iiko returned 429; live circuit opened") from error
        raise
    self.state.record_status(
        self.profile.fingerprint,
        operation_id,
        response.status_code,
    )
    if self.capture is not None:
        self.capture.write_model_pair(
            operation_id,
            request_model,
            response.data,
            metadata={"status": response.status_code},
        )
    return response.data
```

Imports for `ApiResponse`, `ApiException` and `T` use the concrete generated package paths established by the pinned generator; a mock adapter test supplies a fake `ApiResponse`, asserts one guard acquire, and proves a `429` exception opens the circuit without invoking the callable twice.

The `live_sdk` fixture first authenticates once with `SafeLiveSession`, then creates `Configuration(host=profile.base_url, access_token=session.access_token)`, one generated async `ApiClient`, and the adapter. Both clients close in `finally`.

```python
# tests/integration/read/test_organizations.py
from typing import Any

import pytest

from iikocloud_client import OrganizationsApi, OrganizationsGetOrganizationsRequest


def contains_value(value: Any, expected: str) -> bool:
    if isinstance(value, dict):
        return expected in value.values() or any(
            contains_value(child, expected) for child in value.values()
        )
    if isinstance(value, list):
        return any(contains_value(child, expected) for child in value)
    return False


@pytest.mark.live_read_smoke
async def test_generated_sdk_lists_target_organization(live_sdk, live_profile) -> None:
    api = OrganizationsApi(live_sdk.api_client)
    request = OrganizationsGetOrganizationsRequest(
        organization_ids=[live_profile.organization_id],
        return_additional_info=False,
        include_disabled=False,
    )
    response = await live_sdk.call_generated(
        "get_organizations",
        request,
        lambda: api.get_organizations_with_http_info(
            organizations_get_organizations_request=request
        ),
    )
    assert contains_value(
        response.model_dump(mode="json", by_alias=True),
        live_profile.organization_id,
    )
```

During naming review, lock these exact public symbols and method names in registries before accepting the test. Run only after the `authenticate` and `get_organizations` limits are verified:

```bash
uv run pytest -m live_read_smoke -n0 --live-profile test-server --env-file .env tests/integration/read/test_organizations.py
```

The command sends at most one auth request and one organizations request. It is never part of ordinary pytest or CI.

- [ ] **Step 10: Run strict real sync and package checks**

Run: `uv run python -m tools.openapi_pipeline sync --offline`

Expected: strict lint, generator validation, codegen, generated imports, union tests and staging wheel checks all pass before promotion.

- [ ] **Step 11: Switch packaging to hand-owned src layout**

Replace the runtime portion of `pyproject.toml` with:

```toml
[project]
name = "iikocloud-client"
version = "0.1.0"
description = "Generated async Python SDK for iiko Cloud API"
readme = "README.md"
requires-python = ">=3.10"
dependencies = [
  "httpx>=0.28,<1",
  "pydantic>=2.11,<3",
  "python-dateutil>=2.9,<3",
  "typing-extensions>=4.12,<5",
]

[project.urls]
Repository = "https://github.com/UserVanya/Iikocloud-py-sdk"

[build-system]
requires = ["setuptools>=77,<82"]
build-backend = "setuptools.build_meta"

[tool.setuptools.packages.find]
where = ["src"]

[tool.setuptools.package-data]
iikocloud_client = ["py.typed", "_contracts/*.yaml"]
```

Copy `contracts/rate-limits.yaml` byte-for-byte to `src/iikocloud_client/_contracts/rate-limits.yaml`; `verify` asserts equality on every run.

- [ ] **Step 12: Remove only confirmed legacy generated artifacts**

After `src/iikocloud_client` passes the real wheel test, remove these tracked legacy outputs:

```bash
git rm -r iikocloud_client test .openapi-generator
git rm codegen.sh config.yaml git_push.sh iikocloud_openapi.json setup.py setup.cfg requirements.txt test-requirements.txt tox.ini .openapi-generator-ignore
```

Remove only tracked Markdown files directly below `docs/` with `git rm -- ':(glob)docs/*.md'`. Git's glob magic does not cross `/`, so `docs/superpowers/` remains intact. Review `git diff --name-status` immediately afterward; never delete the whole `docs` directory.

Rewrite `README.md` as a hand-owned quick start containing installation from tag, async authentication/configuration, the four pipeline commands, and links to `docs/generation.md` and `docs/known-upstream-issues.md`.

- [ ] **Step 13: Verify complete regeneration and wheel installation**

Run: `uv sync --group dev`

Run: `uv run python -m tools.openapi_pipeline verify`

Run: `uv build`

Run: `uv run --isolated --with ./dist/iikocloud_client-0.1.0-py3-none-any.whl python -c "import iikocloud_client; print(iikocloud_client.__name__)"`

Expected: `iikocloud_client` and exit 0.

Run: `git status --short`

Expected: only reviewed upstream/correction/generated/package changes are present; `private/`, `.state/`, `build/`, tokens and captures are absent.

- [ ] **Step 14: Commit the first clean generated baseline**

Stage explicit roots only:

```bash
git add openapi contracts generator src tests pyproject.toml uv.lock README.md docs
git commit -m "feat: regenerate iiko Cloud SDK from guarded OpenAPI"
```

**Review Gate C:** The old hand-edited generated tree is gone, the new SDK is reproducible from committed inputs, and all menu composition changes have evidence fixtures.

### Task 12: Add durable mutation journals and an explicit write round-trip

**Files:**

- Create: `tools/openapi_pipeline/mutations.py`
- Modify: `tools/openapi_pipeline/live/generated.py`
- Modify: `tests/conftest.py`
- Create: `tests/live_support/test_mutations.py`
- Create: `tests/integration/write/test_stop_list.py`

**Interfaces:**

- Consumes: live profile, operation classification, reserved cleanup budget.
- Produces: atomic `.state/mutations/{run_id}.json`, LIFO cleanup, `cleanup-orphans`; cleanup failure blocks publish.

- [ ] **Step 1: Write failing mutation-journal tests**

```python
# tests/live_support/test_mutations.py
from pathlib import Path

import pytest

from tools.openapi_pipeline.mutations import MutationJournal


@pytest.mark.asyncio
async def test_cleanup_is_registered_before_assertions_and_runs_lifo(tmp_path: Path) -> None:
    calls: list[str] = []
    journal = MutationJournal.create(tmp_path, "run-1", "profile-hash")
    journal.register("delete-child", {"id": "child"})
    journal.register("delete-parent", {"id": "parent"})
    assert journal.path.exists()

    async def execute(operation_id: str, _payload: dict) -> None:
        calls.append(operation_id)

    await journal.cleanup(execute)
    assert calls == ["delete-parent", "delete-child"]
    assert not journal.path.exists()
```

- [ ] **Step 2: Run the test and verify RED**

Run: `uv run pytest tests/live_support/test_mutations.py -q`

Expected: import error for `mutations`.

- [ ] **Step 3: Implement durable register/arm-before-assertion semantics**

The journal JSON is:

```json
{
  "run_id": "run-1",
  "profile_fingerprint": "profile-hash",
  "completed": false,
  "cleanup": [
    {"operation_id": "delete-child", "payload": {"id": "child"}, "done": false}
  ]
}
```

`register()` atomically rewrites mode `0600` before returning. When a deterministic cleanup payload is known before a write, it is registered immediately before dispatch; when cleanup depends on a server-created ID, it is registered immediately after the successful response and before the first assertion. `cleanup()` executes pending entries in reverse list order, marks each entry done immediately after success, and deletes the file only when all entries are done. On any failure it persists the remaining entries and raises `SafetyError`.

`cleanup-orphans --live-profile NAME` loads all incomplete journals for that profile, reserves budgets for every pending operation before the first call, prints the plan, and requires interactive confirmation `cleanup {count} actions [y/N]`. It never executes an operation not classified as a cleanup in `contracts/live-operations.yaml`.

Add `GeneratedLiveSdk.execute_cleanup(operation_id, payload)`. It accepts only `remove_products_from_stop_list`, rebuilds `RemoveProductsFromStopListRequest.model_validate(payload)`, and dispatches once to `MenuApi.remove_products_from_stop_list_with_http_info` through `call_generated`. An unknown or non-cleanup operation raises before acquiring a rate budget or making HTTP. This explicit dispatcher is the only durable-journal-to-generated-code bridge; no dynamic `getattr` is used.

- [ ] **Step 4: Strengthen write collection gates**

For every `live_write` item, `tests/conftest.py` must require all of:

```python
assert config.getoption("--allow-live-write") is True
assert profile.allow_write is True
assert config.getoption("--target-organization") == profile.organization_id
assert profile.organization_id in profile.allowed_organization_ids
assert profile.terminal_group_id is not None
assert profile.write_product_id is not None
assert worker_count_is_one(config)
```

Tests marked `audit_residue` additionally require `--allow-audit-residue`. Before yielding the write fixture, reserve cleanup operation budgets and print operation IDs plus target organization fingerprint, never the raw UUID.

- [ ] **Step 5: Add a compensating stop-list test with distinct operation budgets**

```python
# tests/integration/write/test_stop_list.py
from typing import Any

import pytest

from iikocloud_client import (
    AddProductsToStopListItem,
    AddProductsToStopListRequest,
    MenuApi,
    RemoveProductsFromStopListItem,
    RemoveProductsFromStopListRequest,
    StopListsRequest,
)


def contains_product(value: Any, product_id: str) -> bool:
    if isinstance(value, dict):
        return any(
            (key == "productId" and child == product_id)
            or contains_product(child, product_id)
            for key, child in value.items()
        )
    if isinstance(value, list):
        return any(contains_product(child, product_id) for child in value)
    return False


@pytest.mark.live_write
@pytest.mark.audit_residue
async def test_stop_list_add_is_accepted_and_removed(
    live_sdk, mutation_journal, live_profile
) -> None:
    assert live_profile.terminal_group_id is not None
    assert live_profile.write_product_id is not None
    api = MenuApi(live_sdk.api_client)
    add = AddProductsToStopListRequest(
        organization_id=live_profile.organization_id,
        terminal_group_id=live_profile.terminal_group_id,
        items=[
            AddProductsToStopListItem(
                product_id=live_profile.write_product_id,
                balance=0,
            )
        ],
    )
    remove = RemoveProductsFromStopListRequest(
        organization_id=live_profile.organization_id,
        terminal_group_id=live_profile.terminal_group_id,
        items=[
            RemoveProductsFromStopListItem(product_id=live_profile.write_product_id)
        ],
    )

    try:
        preflight_request = StopListsRequest(
            organization_ids=[live_profile.organization_id],
            terminal_groups_ids=[live_profile.terminal_group_id],
        )
        before = await live_sdk.call_generated(
            "get_stop_lists",
            preflight_request,
            lambda: api.get_stop_lists_with_http_info(
                stop_lists_request=preflight_request
            ),
        )
        assert not contains_product(
            before.model_dump(mode="json", by_alias=True),
            live_profile.write_product_id,
        ), "dedicated test product is already in the stop list"

        mutation_journal.register(
            "remove_products_from_stop_list",
            remove.model_dump(mode="json", by_alias=True),
        )
        added = await live_sdk.call_generated(
            "add_products_to_stop_list",
            add,
            lambda: api.add_products_to_stop_list_with_http_info(
                add_products_to_stop_list_request=add
            ),
        )
        assert added.model_dump(mode="json", by_alias=True).get("correlationId")
    finally:
        await mutation_journal.cleanup(live_sdk.execute_cleanup)
```

The configured product must be a dedicated disposable test product. A guarded preflight proves it is absent before mutation; if it is already present, the test fails without writing so cleanup cannot remove legitimate state. The run calls each operation at most once: one preflight read, one add, and one distinct remove cleanup. Because the remove payload is known in advance and is safe for the dedicated absent product, the journal is persisted immediately before dispatching the add; even an ambiguous timeout leaves enough information for `finally` or `cleanup-orphans`. The test still requires audit-residue approval because the server can retain an audit trail even after cleanup.

- [ ] **Step 6: Verify gates without sending requests**

Run: `uv run pytest tests/live_support/test_mutations.py -q`

Expected: unit tests pass.

Run: `uv run pytest -m live_write tests/integration/write --collect-only -q`

Expected: test is collected but skipped without `--live-profile`; no HTTP call occurs.

- [ ] **Step 7: Commit write safety**

```bash
git add tools/openapi_pipeline/mutations.py tests/conftest.py tests/live_support tests/integration/write
git commit -m "test: add reversible live-write safety"
```

### Task 13: Block secrets and publish only allowlisted Git changes

**Files:**

- Create: `.secrets.baseline`
- Create: `tools/openapi_pipeline/secrets.py`
- Create: `tools/openapi_pipeline/publish.py`
- Modify: `tools/openapi_pipeline/cli.py`
- Create: `tests/security/test_secrets.py`
- Create: `tests/publish/test_publish.py`

**Interfaces:**

- Consumes: tracked/staged files, active known secrets, live receipt, clean allowlisted worktree.
- Produces: `verify_no_secrets()`, one commit, `v{version}` tag, optional non-force push.

- [ ] **Step 1: Write failing exact-secret tests**

```python
# tests/security/test_secrets.py
from pathlib import Path

import pytest

from tools.openapi_pipeline.errors import SafetyError
from tools.openapi_pipeline.secrets import assert_known_secrets_absent


def test_exact_active_secret_blocks_publish_without_echoing_value(tmp_path: Path) -> None:
    secret = "live-api-login-value"
    file = tmp_path / "tracked.json"
    file.write_text(f'{{"value":"{secret}"}}')
    with pytest.raises(SafetyError) as error:
        assert_known_secrets_absent([file], [secret])
    assert secret not in str(error.value)
```

- [ ] **Step 2: Write failing publish-scope tests**

```python
# tests/publish/test_publish.py
from pathlib import Path

import pytest

from tools.openapi_pipeline.errors import SafetyError
from tools.openapi_pipeline.publish import assert_publishable_paths


def test_private_and_unrelated_paths_are_never_publishable(tmp_path: Path) -> None:
    with pytest.raises(SafetyError, match="private/captures"):
        assert_publishable_paths(["private/captures/run/response.json"])
    with pytest.raises(SafetyError, match="notes.txt"):
        assert_publishable_paths(["notes.txt"])
```

- [ ] **Step 3: Implement layered secret scanning**

`verify_no_secrets(root, known_secrets)` performs:

1. `git ls-files -z` to obtain tracked files;
2. `git diff --cached --name-only -z` to obtain staged files;
3. rejects any tracked/staged path under `private/`, `.state/`, `build/`, or matching `.env.local`;
4. invokes `detect-secrets-hook --baseline .secrets.baseline` with explicit filenames and no shell;
5. reads text/JSON/YAML/TOML files and searches exact non-empty `known_secrets` values;
6. reports only path and category, never the matched value.

`verify-no-secrets --create-baseline` is a separate bootstrap mode. It obtains the tracked filename list itself, invokes `detect-secrets scan --no-verify` with argument arrays and captured stdout, parses the resulting JSON, and writes `.secrets.baseline` atomically only when the scan command and JSON validation succeed. It never silently updates an existing baseline during normal verification.

Bootstrap and audit once with:

```bash
uv run python -m tools.openapi_pipeline verify-no-secrets --create-baseline
uv run detect-secrets audit .secrets.baseline
uv run python -m tools.openapi_pipeline verify-no-secrets
```

Review every initial finding and mark only confirmed false positives in the audit UI. Add a committed non-secret canary fixture and a temporary-secret unit test proving that the audited baseline does not suppress a new finding.

- [ ] **Step 4: Implement allowlisted publish preparation**

The only publishable path prefixes are:

```python
PUBLISH_PREFIXES = (
    "openapi/",
    "contracts/",
    "generator/",
    "src/iikocloud_client/",
    "tests/fixtures/contracts/",
    "tests/generated/",
    "docs/generation.md",
    "docs/known-upstream-issues.md",
    "README.md",
    "pyproject.toml",
    "uv.lock",
)
```

`assert_publishable_paths` rejects every dirty path not equal to a listed file or below a listed directory. `publish` then:

1. refuses `main`/`master` unless ignored `private/publish.toml` contains `allow_protected_branch = true`;
2. runs `verify`;
3. verifies a completed matching live receipt;
4. rejects open circuit and incomplete mutation journals;
5. runs secret scanning;
6. updates the exact PEP 621 version line and reruns wheel smoke;
7. prints `git diff --stat` and dirty path list;
8. executes `git add --` followed only by the approved paths;
9. runs staged secret scanning again;
10. commits `chore(sdk): sync iiko OpenAPI YYYY-MM-DD`;
11. creates annotated tag `v{version}`;
12. with `--push`, runs `git push origin HEAD` and then `git push origin v{version}`.

Every Git subprocess receives a list of arguments and `check=True`; no force option exists.

- [ ] **Step 5: Test publish in an isolated temporary Git repository**

The test initializes a temp repository with local name/email, creates an allowed generated file and an unrelated file, verifies the unrelated file blocks preparation, removes it, creates a fake matching receipt, stubs `verify`/secret scan, and asserts exactly one commit and one annotated tag are created. A separate test sets branch `main` and asserts it is rejected without the private opt-in.

Run: `uv run pytest tests/security tests/publish -q`

Expected: all tests pass without contacting a remote.

- [ ] **Step 6: Wire commands and commit**

`verify-no-secrets` runs the scanner only. `publish` accepts required `--version`, optional `--push`, and no force/protected-branch flags.

```bash
git add .secrets.baseline tools/openapi_pipeline tests/security tests/publish
git commit -m "feat: gate SDK publication"
```

### Task 14: Add offline CI, operator documentation, and final end-to-end verification

**Files:**

- Replace: `.github/workflows/python.yml`
- Create: `.github/workflows/upstream-check.yml`
- Create: `docs/generation.md`
- Create: `docs/known-upstream-issues.md`
- Modify: `docs/troubleshooting.md`
- Modify: `README.md`

**Interfaces:**

- Consumes: committed snapshot/corrections/generated package.
- Produces: offline PR gate, scheduled public-schema drift signal, operator runbook.

- [ ] **Step 1: Replace generated CI with an offline matrix**

```yaml
# .github/workflows/python.yml
name: offline

on:
  push:
  pull_request:

permissions:
  contents: read

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      fail-fast: false
      matrix:
        python-version: ["3.10", "3.12"]
    steps:
      - uses: actions/checkout@v4
      - uses: astral-sh/setup-uv@v6
        with:
          enable-cache: true
      - uses: actions/setup-python@v5
        with:
          python-version: ${{ matrix.python-version }}
      - run: uv sync --frozen --group dev
      - run: uv run ruff check tools tests
      - run: uv run pytest -q
      - run: uv run python -m tools.openapi_pipeline verify-no-secrets
      - run: uv build
      - if: matrix.python-version == '3.12'
        run: uv run mypy tools/openapi_pipeline
      - if: matrix.python-version == '3.12'
        run: uv run python -m tools.openapi_pipeline verify
```

`verify-no-secrets` already rejects tracked/staged paths under `private/`, `.state/`, and `build/`, with only `private/.gitignore` and `private/README.md` allowlisted. Therefore the workflow uses the same tested Python path-policy implementation instead of duplicating it in shell. No job defines a live credential, `--live-profile`, or a live marker.

- [ ] **Step 2: Add non-mutating scheduled upstream detection**

```yaml
# .github/workflows/upstream-check.yml
name: upstream-check

on:
  schedule:
    - cron: "17 4 * * 1"
  workflow_dispatch:

permissions:
  contents: read

jobs:
  drift:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: astral-sh/setup-uv@v6
        with:
          enable-cache: true
      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
      - run: uv sync --frozen --group dev
      - run: uv run python -m tools.openapi_pipeline upstream-check
      - if: always()
        uses: actions/upload-artifact@v4
        with:
          name: upstream-diff
          path: build/reports/upstream-diff.*
          if-no-files-found: error
```

The command only fetches a public candidate and writes reports. The workflow never calls `sync`, commits, opens a PR, runs live tests, or pushes.

- [ ] **Step 3: Write the operator runbook**

`docs/generation.md` includes exact sections:

1. prerequisites (`uv`, Docker, Python 3.12);
2. offline `verify`;
3. `upstream-check` versus `sync`;
4. stale overlay repair workflow;
5. operation/model naming review;
6. `.env` permission check, explicit `--env-file .env`, and primary `IIKO_API_KEY` lookup;
7. confirming a rate limit before changing `verified`;
8. live-read commands and 429 response procedure, including the prohibition on automatic `IIKO_API_KEY_2` fallback;
9. capture/evidence promotion;
10. explicit write test and `cleanup-orphans`;
11. `verify-no-secrets` and secret rotation procedure;
12. `publish --version ... --push`;
13. installation from Git tag in `Iikocloud-manager`;
14. how to add a sanitized, verified entry to `docs/troubleshooting.md` after a repeated failure pattern.

`docs/known-upstream-issues.md` records each overlay issue ID, upstream fragment, correction, evidence fixture, date observed, and removal condition. It explicitly documents menu V2/V3/V4 ambiguity and `ExternalMenuComboItem`.

- [ ] **Step 4: Run complete fresh verification**

Run: `uv sync --frozen --group dev`

Run: `uv run ruff check tools tests`

Run: `uv run mypy tools/openapi_pipeline`

Run: `uv run pytest -q`

Run: `uv run python -m tools.openapi_pipeline verify`

Run: `uv run python -m tools.openapi_pipeline verify-no-secrets`

Run: `uv build`

Expected: every command exits 0; ordinary pytest reports no live tests executed; regeneration diff is empty; wheel exists in `dist/`.

- [ ] **Step 5: Verify downstream installation without modifying the manager repository**

Create an isolated temporary uv environment and install the local wheel, then run:

```bash
uv run --isolated --with ./dist/iikocloud_client-0.1.0-py3-none-any.whl python -c "from iikocloud_client import ApiClient, Configuration; print(ApiClient.__name__, Configuration.__name__)"
```

Expected: `ApiClient Configuration`.

Do not edit `/home/ivan/programming/Iikocloud-manager` in this plan. After release, that repository will pin `v0.1.0` in a separate migration project.

- [ ] **Step 6: Commit CI and operations documentation**

```bash
git add .github README.md docs/generation.md docs/known-upstream-issues.md docs/troubleshooting.md
git commit -m "docs: add SDK generation runbook"
```

**Review Gate D:** All design acceptance criteria have an automated check or an explicitly documented live checkpoint. The SDK is ready for the separate release command; no push is performed by implementation tasks.

## Spec Coverage

| Design acceptance criterion | Plan coverage |
|---|---|
| Snapshot + corrections build effective schema; repeated sync is stable | Tasks 2, 3, 7, 11 |
| Stale upstream fragments fail closed | Task 3 guarded fragment hashes and Task 7 rollback tests |
| Strict OpenAPI validation without skip | Tasks 5 and 6 |
| Stable unique operation IDs and model names | Task 4 plus Task 11 naming review |
| Menu `oneOf` branches and combo contract remain intact | Tasks 10 and 11 evidence/contract tests |
| Generated code is fully reproducible and wheel-installable | Tasks 6, 7, 11, and 14 |
| Ordinary pytest is offline | Tasks 1, 9, and 14 |
| Unknown/parallel live calls and synthetic 429 fail closed without retry | Tasks 8, 9, and 11 adapter tests |
| Write requires all gates and leaves recoverable cleanup state | Task 12 |
| Capture never persists auth or known secrets | Task 10 |
| Private/staged secret paths block publish | Task 13 |
| Release is consumable by Git tag | Tasks 13 and 14 |
| Primary `.env` key, no post-429 key rotation | Tasks 1, 8, 9, and 14 runbook |
| Repeated failures become durable sanitized knowledge | Task 1 `AGENTS.md`/troubleshooting ledger and Task 14 review |

## Execution Order and External Checkpoints

1. Tasks 1-8 are fully offline except the explicit Docker image pull in Task 6.
2. Task 9 remains mock-only until rate entries are reviewed.
3. Task 11 pauses before the first real iiko call so the user can configure `private/profiles/test-server.toml` and confirm limits.
4. Task 12 implements write tests but does not run them live during normal execution.
5. Task 13 tests Git publication locally but does not push.
6. Task 14 completes offline verification; an actual `publish --push` remains a separate explicit user-controlled action.
7. During this implementation, every automated test command is executed outside sandbox; live HTTP still waits for Review Gate B and explicit rate verification.

## Execution Handoff

Plan implementation should use one of:

1. **Subagent-Driven (recommended):** fresh implementer per task with specification and quality review between commits.
2. **Inline Execution:** execute tasks in this session via `superpowers:executing-plans`, in reviewed batches with checkpoints A-D.
