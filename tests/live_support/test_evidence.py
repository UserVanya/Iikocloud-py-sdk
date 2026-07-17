from __future__ import annotations

import inspect
from collections.abc import Mapping
from dataclasses import replace
from pathlib import Path
from typing import Any, cast

import pytest

from tools.openapi_pipeline import evidence as evidence_module
from tools.openapi_pipeline.capture import CaptureWriter, LiveCapture, RedactionHints
from tools.openapi_pipeline.errors import SafetyError
from tools.openapi_pipeline.evidence import (
    CaptureEvidenceDependencies,
    capture_evidence,
    default_capture_evidence_dependencies,
)
from tools.openapi_pipeline.live.lock import LiveProcessLock
from tools.openapi_pipeline.live.profile import ResolvedLiveProfile
from tools.openapi_pipeline.live.pytest_support import resolve_locked_live_profile
from tools.openapi_pipeline.live.rates import LiveRateGuard, OperationBudget, RateCatalog
from tools.openapi_pipeline.live.session import (
    LiveOperation,
    SafeLiveSession,
    load_operation_contract,
)
from tools.openapi_pipeline.live.state import LiveStateStore
from tools.openapi_pipeline.paths import RepoPaths


class StubCatalog:
    def __init__(self, events: list[str], *, fail_on: str | None = None) -> None:
        self.events = events
        self.fail_on = fail_on

    def operation_budget(self, operation_id: str) -> OperationBudget:
        self.events.append(f"budget:{operation_id}")
        if operation_id == self.fail_on:
            raise SafetyError(f"{operation_id} is not verified")
        return OperationBudget(operation_id, 30.0, 1)


class StubLock:
    def __init__(self, path: Path, events: list[str]) -> None:
        self.path = path
        self.held = False
        self.events = events

    def __enter__(self) -> StubLock:
        self.held = True
        self.events.append("lock:enter")
        return self

    def __exit__(self, *exc_info: object) -> None:
        self.events.append("lock:exit")
        self.held = False


class StubSession:
    def __init__(self, events: list[str], *, fail_at: str | None = None) -> None:
        self.events = events
        self.fail_at = fail_at
        self.requests: list[tuple[str, str, str, Mapping[str, Any]]] = []

    async def authenticate(self) -> None:
        self.events.append("session:authenticate")
        if self.fail_at == "authenticate":
            raise SafetyError("authentication failed")

    async def request_json(
        self,
        operation_id: str,
        method: str,
        path: str,
        payload: Mapping[str, Any],
    ) -> object:
        self.events.append("session:menu")
        self.requests.append((operation_id, method, path, payload))
        if self.fail_at == "menu":
            raise SafetyError("menu failed")
        return object()

    async def close(self) -> None:
        self.events.append("session:close")


def _profile() -> ResolvedLiveProfile:
    return ResolvedLiveProfile(
        name="test-server",
        base_url="https://api.example.invalid",
        api_login="synthetic-primary-login",
        organization_id="target-organization",
        external_menu_id="target-menu",
        terminal_group_id=None,
        write_product_id=None,
        allow_write=False,
        allowed_organization_ids=(),
        fingerprint="a" * 64,
    )


def _schema() -> dict[str, Any]:
    return {
        "openapi": "3.0.3",
        "paths": {
            "/api/2/menu/by_id": {
                "post": {
                    "operationId": "get_external_menu_by_id",
                    "requestBody": {
                        "content": {"application/json": {"schema": {"type": "object"}}}
                    },
                    "responses": {
                        "200": {"content": {"application/json": {"schema": {"type": "object"}}}}
                    },
                }
            }
        },
    }


def _operations() -> Mapping[str, LiveOperation]:
    return {
        "authenticate": LiveOperation("auth", None, "POST", "/api/1/access_token"),
        "get_external_menu_by_id": LiveOperation("read", None, "POST", "/api/2/menu/by_id"),
    }


def _dependencies(
    tmp_path: Path,
    events: list[str],
    *,
    fail_budget: str | None = None,
    fail_session: str | None = None,
) -> tuple[CaptureEvidenceDependencies, StubSession]:
    session = StubSession(events, fail_at=fail_session)
    base = default_capture_evidence_dependencies(RepoPaths(tmp_path))
    dependencies = replace(
        base,
        rate_catalog_loader=lambda path: (
            events.append("catalog:load")
            or cast(RateCatalog, StubCatalog(events, fail_on=fail_budget))
        ),
        candidate_composer=lambda paths: events.append("candidate:compose") or (_schema(), {}),
        operation_contract_loader=lambda path: events.append("operations:load") or _operations(),
        hints_builder=lambda schema, operation: (
            events.append("hints:build") or RedactionHints.for_operation(schema, operation)
        ),
        lock_factory=lambda path: cast(LiveProcessLock, StubLock(path, events)),
        profile_resolver=lambda *args, **kwargs: events.append("profile:resolve") or _profile(),
        state_factory=lambda *args, **kwargs: events.append("state:create") or object(),
        guard_factory=lambda *args, **kwargs: events.append("guard:create") or object(),
        writer_factory=lambda path: (
            events.append("writer:create") or cast(CaptureWriter, object())
        ),
        capture_factory=lambda **kwargs: (
            events.append("capture:create") or cast(LiveCapture, object())
        ),
        session_factory=lambda **kwargs: (
            events.append("session:create") or cast(SafeLiveSession, session)
        ),
        run_id_factory=lambda: "20260717T120000Z-a1b2c3d4",
    )
    return dependencies, session


@pytest.mark.asyncio
@pytest.mark.parametrize("fail_budget", ["authenticate", "get_external_menu_by_id"])
async def test_capture_evidence_fails_disabled_before_secret_or_socket_access(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    fail_budget: str,
) -> None:
    events: list[str] = []
    dependencies, _session = _dependencies(tmp_path, events, fail_budget=fail_budget)
    monkeypatch.setattr(
        "httpx.AsyncHTTPTransport",
        lambda *args, **kwargs: (_ for _ in ()).throw(AssertionError("socket transport created")),
    )

    with pytest.raises(SafetyError, match="not verified"):
        await capture_evidence(
            live_profile="test-server",
            env_file=".env",
            operation="get_external_menu_by_id",
            menu_version=2,
            dependencies=dependencies,
        )

    assert "profile:resolve" not in events
    assert "session:create" not in events
    assert events[:2] == ["catalog:load", "budget:authenticate"]
    if fail_budget == "get_external_menu_by_id":
        assert events[:3] == [
            "catalog:load",
            "budget:authenticate",
            "budget:get_external_menu_by_id",
        ]


@pytest.mark.asyncio
async def test_capture_evidence_calls_auth_and_menu_once_with_exact_payload_in_order(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    events: list[str] = []
    dependencies, session = _dependencies(tmp_path, events)
    monkeypatch.setattr(
        "httpx.AsyncHTTPTransport",
        lambda *args, **kwargs: (_ for _ in ()).throw(AssertionError("socket transport created")),
    )

    await capture_evidence(
        live_profile="test-server",
        env_file=".env",
        operation="get_external_menu_by_id",
        menu_version=4,
        dependencies=dependencies,
    )

    assert events == [
        "catalog:load",
        "budget:authenticate",
        "budget:get_external_menu_by_id",
        "candidate:compose",
        "operations:load",
        "hints:build",
        "lock:enter",
        "profile:resolve",
        "state:create",
        "guard:create",
        "writer:create",
        "capture:create",
        "session:create",
        "session:authenticate",
        "session:menu",
        "session:close",
        "lock:exit",
    ]
    assert session.requests == [
        (
            "get_external_menu_by_id",
            "POST",
            "/api/2/menu/by_id",
            {
                "externalMenuId": "target-menu",
                "organizationIds": ["target-organization"],
                "version": 4,
            },
        )
    ]


@pytest.mark.asyncio
@pytest.mark.parametrize("fail_session", ["authenticate", "menu"])
async def test_capture_evidence_closes_once_after_any_live_failure(
    tmp_path: Path, fail_session: str
) -> None:
    events: list[str] = []
    dependencies, _session = _dependencies(tmp_path, events, fail_session=fail_session)

    with pytest.raises(SafetyError, match="failed"):
        await capture_evidence(
            live_profile="test-server",
            env_file=".env",
            operation="get_external_menu_by_id",
            menu_version=3,
            dependencies=dependencies,
        )

    assert events.count("session:authenticate") == 1
    assert events.count("session:menu") == (0 if fail_session == "authenticate" else 1)
    assert events.count("session:close") == 1
    assert events[-2:] == ["session:close", "lock:exit"]


@pytest.mark.asyncio
@pytest.mark.parametrize(
    ("operation", "version"),
    [("get_organizations", 2), ("get_external_menu_by_id", 1), ("get_external_menu_by_id", True)],
)
async def test_capture_evidence_runtime_rejects_unapproved_selection_before_loading(
    tmp_path: Path, operation: str, version: object
) -> None:
    events: list[str] = []
    dependencies, _session = _dependencies(tmp_path, events)

    with pytest.raises(SafetyError, match="operation|version"):
        await capture_evidence(
            live_profile="test-server",
            env_file=".env",
            operation=operation,
            menu_version=cast(int, version),
            dependencies=dependencies,
        )

    assert events == []


def test_default_capture_dependencies_use_canonical_guarded_primitives(tmp_path: Path) -> None:
    dependencies = default_capture_evidence_dependencies(RepoPaths(tmp_path))

    assert dependencies.rate_catalog_loader == RateCatalog.load
    assert dependencies.operation_contract_loader is load_operation_contract
    assert dependencies.lock_factory is LiveProcessLock
    assert dependencies.profile_resolver is resolve_locked_live_profile
    assert dependencies.state_factory is LiveStateStore
    assert dependencies.guard_factory is LiveRateGuard
    assert dependencies.writer_factory is CaptureWriter
    assert dependencies.capture_factory is LiveCapture
    assert dependencies.session_factory is SafeLiveSession
    assert dependencies.hints_builder == RedactionHints.for_operation
    source = inspect.getsource(evidence_module)
    assert "IIKO_API_KEY_2" not in source
    assert '".state/live.lock"' in source
