from __future__ import annotations

import copy
import inspect
import json
from collections.abc import Callable, Mapping
from dataclasses import replace
from pathlib import Path
from typing import Any, TypeVar, cast

import pytest

from tools.openapi_pipeline import evidence as evidence_module
from tools.openapi_pipeline.capture import ARRAY_ITEM, CaptureWriter, LiveCapture, RedactionHints
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

_T = TypeVar("_T")


def _event_result(events: list[str], event: str, factory: Callable[[], _T]) -> _T:
    events.append(event)
    return factory()


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
                        "200": {
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "oneOf": [
                                            {"$ref": "#/components/schemas/ExternalMenuV2"},
                                            {"$ref": "#/components/schemas/ExternalMenuV3"},
                                            {"$ref": "#/components/schemas/ExternalMenuV4"},
                                        ]
                                    }
                                }
                            }
                        }
                    },
                }
            }
        },
        "components": {
            "schemas": {
                "ExternalMenuV2": {
                    "type": "object",
                    "properties": {
                        "mode": {"type": "string", "enum": ["V2"]},
                    },
                },
                "ExternalMenuV3": {
                    "type": "object",
                    "properties": {
                        "mode": {"type": "string", "enum": ["V3"]},
                    },
                },
                "ExternalMenuV4": {
                    "type": "object",
                    "properties": {
                        "mode": {"type": "string", "enum": ["V4"]},
                        "itemGroups": {
                            "type": "array",
                            "items": {"$ref": "#/components/schemas/ExternalMenuCategory3"},
                        },
                    },
                },
                "ExternalMenuCategory3": {
                    "type": "object",
                    "properties": {
                        "items": {
                            "type": "array",
                            "items": {
                                "oneOf": [
                                    {"$ref": "#/components/schemas/ExternalMenuItem3"},
                                    {"$ref": "#/components/schemas/ExternalMenuComboItem"},
                                ]
                            },
                        }
                    },
                },
                "ExternalMenuItem3": {
                    "type": "object",
                    "properties": {
                        "orderItemType": {
                            "description": "Product or compound",
                            "enum": ["Product", "Compound"],
                            "format": "enum",
                            "type": "string",
                        },
                        "type": {
                            "enum": ["DISH", "COMBO"],
                            "type": "string",
                            "description": "Item type",
                            "default": "DISH",
                        },
                        "name": {"type": "string"},
                    },
                },
                "ExternalMenuComboItem": {
                    "required": ["type"],
                    "type": "object",
                    "properties": {
                        "priceStrategy": {
                            "default": "BY_COMPONENT",
                            "description": "Price strategy",
                            "enum": ["BY_COMPONENT"],
                            "type": "string",
                        },
                        "type": {"type": "string"},
                        "comment": {"type": "string"},
                    },
                },
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
        rate_catalog_loader=lambda path: _event_result(
            events,
            "catalog:load",
            lambda: cast(RateCatalog, StubCatalog(events, fail_on=fail_budget)),
        ),
        candidate_composer=lambda paths: _event_result(
            events,
            "candidate:compose",
            lambda: (_schema(), {}),
        ),
        operation_contract_loader=lambda path: _event_result(
            events,
            "operations:load",
            _operations,
        ),
        hints_builder=lambda schema, operation, version: _event_result(
            events,
            f"hints:build:{version}",
            lambda: evidence_module.build_versioned_evidence_redaction_hints(
                schema, operation, version
            ),
        ),
        lock_factory=lambda path: cast(LiveProcessLock, StubLock(path, events)),
        profile_resolver=lambda *args, **kwargs: _event_result(
            events, "profile:resolve", _profile
        ),
        state_factory=lambda *args, **kwargs: _event_result(
            events, "state:create", lambda: cast(LiveStateStore, object())
        ),
        guard_factory=lambda *args, **kwargs: _event_result(
            events, "guard:create", lambda: cast(LiveRateGuard, object())
        ),
        writer_factory=lambda path: _event_result(
            events, "writer:create", lambda: cast(CaptureWriter, object())
        ),
        capture_factory=lambda **kwargs: _event_result(
            events, "capture:create", lambda: cast(LiveCapture, object())
        ),
        session_factory=lambda **kwargs: _event_result(
            events, "session:create", lambda: cast(SafeLiveSession, session)
        ),
        run_id_factory=lambda: "20260717T120000Z-a1b2c3d4",
    )
    return dependencies, session


_ITEM_TYPE_PATH = (
    "itemGroups",
    ARRAY_ITEM,
    "items",
    ARRAY_ITEM,
    "type",
)
_ITEM_ORDER_TYPE_PATH = (*_ITEM_TYPE_PATH[:-1], "orderItemType")
_ITEM_PRICE_STRATEGY_PATH = (*_ITEM_TYPE_PATH[:-1], "priceStrategy")


def test_generic_hints_keep_one_of_with_unconstrained_branch_redacted() -> None:
    hints = RedactionHints.for_operation(_schema(), "get_external_menu_by_id")

    assert hints.response_values_for_status(200)[_ITEM_TYPE_PATH] == frozenset()


def test_evidence_hints_preserve_only_declared_item_types_at_exact_capture_path(
    tmp_path: Path,
) -> None:
    hints = evidence_module.build_evidence_redaction_hints(_schema(), "get_external_menu_by_id")
    capture = LiveCapture(
        writer=CaptureWriter(tmp_path),
        run_id="run",
        selected_operation="get_external_menu_by_id",
        operation_catalog=_operations(),
        hints=hints,
    )

    _request_path, response_path = capture.write_model_pair(
        "get_external_menu_by_id",
        {},
        {
            "type": "DISH",
            "itemGroups": [
                {
                    "type": "COMBO",
                    "items": [
                        {"type": "DISH", "name": "private dish"},
                        {"type": "COMBO", "comment": "private combo"},
                        {"type": "ARBITRARY"},
                        {"nested": {"type": "DISH"}},
                    ],
                }
            ],
        },
        metadata={"status": 200},
    )

    response = json.loads(response_path.read_text(encoding="utf-8"))["body"]
    assert response["type"] == "<redacted:string>"
    assert response["itemGroups"][0]["type"] == "<redacted:string>"
    assert response["itemGroups"][0]["items"] == [
        {"name": "<redacted:string>", "type": "DISH"},
        {"comment": "<redacted:string>", "type": "COMBO"},
        {"type": "<redacted:string>"},
        {"nested": {"type": "<redacted:string>"}},
    ]


def test_evidence_hints_derive_exact_values_from_upstream_enum() -> None:
    schema = _schema()
    item_type = schema["components"]["schemas"]["ExternalMenuItem3"]["properties"]["type"]
    item_type["enum"] = ["MEAL", "SET"]
    item_type["default"] = "MEAL"

    hints = evidence_module.build_evidence_redaction_hints(schema, "get_external_menu_by_id")

    assert hints.response_values_for_status(200)[_ITEM_TYPE_PATH] == frozenset({"MEAL", "SET"})


@pytest.mark.parametrize(
    ("menu_version", "expected"),
    [(2, "V2"), (3, "V3"), (4, "V4")],
)
def test_versioned_evidence_hints_select_only_requested_response_root(
    menu_version: int,
    expected: str,
) -> None:
    hints = evidence_module.build_versioned_evidence_redaction_hints(
        _schema(),
        "get_external_menu_by_id",
        menu_version,
    )

    values = hints.response_values_for_status(200)
    assert values[("mode",)] == frozenset({expected})
    assert all(version not in values[("mode",)] for version in {"V2", "V3", "V4"} - {expected})
    if menu_version == 4:
        assert values[_ITEM_ORDER_TYPE_PATH] == frozenset({"Product", "Compound"})
        assert values[_ITEM_PRICE_STRATEGY_PATH] == frozenset({"BY_COMPONENT"})


@pytest.mark.parametrize("menu_version", [1, True])
def test_versioned_evidence_hints_reject_unapproved_version(menu_version: object) -> None:
    with pytest.raises(SafetyError, match="version"):
        evidence_module.build_versioned_evidence_redaction_hints(
            _schema(),
            "get_external_menu_by_id",
            cast(int, menu_version),
        )


@pytest.mark.parametrize(
    "mutation",
    [
        "combo-defines-order-item-type",
        "missing-item-order-item-type-enum",
        "item-order-item-type-redaction-sentinel",
        "missing-combo-price-strategy-enum",
        "combo-price-strategy-redaction-sentinel",
    ],
)
def test_versioned_v4_hints_fail_closed_on_ambiguous_enum_schema(
    mutation: str,
) -> None:
    schema = _schema()
    item_properties = schema["components"]["schemas"]["ExternalMenuItem3"]["properties"]
    combo_properties = schema["components"]["schemas"]["ExternalMenuComboItem"]["properties"]
    if mutation == "combo-defines-order-item-type":
        combo_properties["orderItemType"] = copy.deepcopy(item_properties["orderItemType"])
    elif mutation == "missing-item-order-item-type-enum":
        del item_properties["orderItemType"]["enum"]
    elif mutation == "item-order-item-type-redaction-sentinel":
        item_properties["orderItemType"]["enum"] = ["<redacted:string>"]
    elif mutation == "missing-combo-price-strategy-enum":
        del combo_properties["priceStrategy"]["enum"]
    elif mutation == "combo-price-strategy-redaction-sentinel":
        combo_properties["priceStrategy"]["enum"] = ["<redacted:string>"]

    with pytest.raises(SafetyError, match="orderItemType|priceStrategy"):
        evidence_module.build_versioned_evidence_redaction_hints(
            schema,
            "get_external_menu_by_id",
            4,
        )


@pytest.mark.parametrize(
    "mutation",
    [
        "unexpected-operation",
        "unexpected-success-status",
        "missing-v4-ref",
        "drifted-category-ref",
        "drifted-item-one-of",
        "drifted-combo-type",
        "empty-enum",
        "empty-enum-value",
        "non-string-enum",
        "duplicate-enum",
    ],
)
def test_evidence_hints_fail_closed_on_schema_chain_drift(mutation: str) -> None:
    schema = _schema()
    operation_id = "get_external_menu_by_id"
    operation = schema["paths"]["/api/2/menu/by_id"]["post"]
    if mutation == "unexpected-operation":
        operation_id = "get_organizations"
    elif mutation == "unexpected-success-status":
        operation["responses"]["202"] = copy.deepcopy(operation["responses"]["200"])
    elif mutation == "missing-v4-ref":
        operation["responses"]["200"]["content"]["application/json"]["schema"]["oneOf"] = [
            {"$ref": "#/components/schemas/ExternalMenuV2"},
            {"$ref": "#/components/schemas/ExternalMenuV3"},
        ]
    elif mutation == "drifted-category-ref":
        schema["components"]["schemas"]["ExternalMenuV4"]["properties"]["itemGroups"]["items"] = {
            "$ref": "#/components/schemas/ExternalMenuCategory2"
        }
    elif mutation == "drifted-item-one-of":
        schema["components"]["schemas"]["ExternalMenuCategory3"]["properties"]["items"]["items"][
            "oneOf"
        ].append({"type": "string"})
    elif mutation == "drifted-combo-type":
        schema["components"]["schemas"]["ExternalMenuComboItem"]["properties"]["type"] = {
            "enum": ["COMBO"],
            "type": "string",
        }
    else:
        enum = schema["components"]["schemas"]["ExternalMenuItem3"]["properties"]["type"]["enum"]
        if mutation == "empty-enum":
            enum.clear()
        elif mutation == "empty-enum-value":
            enum[0] = ""
        elif mutation == "non-string-enum":
            enum[0] = 1
        elif mutation == "duplicate-enum":
            enum[1] = enum[0]

    with pytest.raises(SafetyError):
        evidence_module.build_evidence_redaction_hints(schema, operation_id)


@pytest.mark.asyncio
async def test_capture_evidence_rejects_hint_schema_drift_before_private_setup(
    tmp_path: Path,
) -> None:
    events: list[str] = []
    dependencies, _session = _dependencies(tmp_path, events)
    drifted = _schema()
    drifted["components"]["schemas"]["ExternalMenuComboItem"]["properties"]["type"] = {
        "enum": ["COMBO"],
        "type": "string",
    }
    dependencies = replace(
        dependencies,
        candidate_composer=lambda paths: _event_result(
            events,
            "candidate:compose",
            lambda: (drifted, {}),
        ),
    )

    with pytest.raises(SafetyError, match="combo type shape"):
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
        "hints:build:4",
    ]


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
        "hints:build:4",
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


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "authenticate",
    [
        LiveOperation("read", None, "POST", "/api/1/access_token"),
        LiveOperation("auth", "cleanup", "POST", "/api/1/access_token"),
        LiveOperation("auth", None, "GET", "/api/1/access_token"),
        LiveOperation("auth", None, "POST", "/api/1/organizations"),
    ],
)
async def test_capture_evidence_rejects_drifted_auth_contract_before_private_setup(
    tmp_path: Path,
    authenticate: LiveOperation,
) -> None:
    events: list[str] = []
    dependencies, _session = _dependencies(tmp_path, events)
    drifted = {**_operations(), "authenticate": authenticate}
    dependencies = replace(
        dependencies,
        operation_contract_loader=lambda path: _event_result(
            events,
            "operations:load",
            lambda: drifted,
        ),
    )

    with pytest.raises(SafetyError, match="authentication.*contract|auth.*contract"):
        await capture_evidence(
            live_profile="test-server",
            env_file=".env",
            operation="get_external_menu_by_id",
            menu_version=2,
            dependencies=dependencies,
        )

    assert events == [
        "catalog:load",
        "budget:authenticate",
        "budget:get_external_menu_by_id",
        "candidate:compose",
        "operations:load",
    ]


@pytest.mark.asyncio
async def test_capture_evidence_rejects_menu_cleanup_contract_before_private_setup(
    tmp_path: Path,
) -> None:
    events: list[str] = []
    dependencies, _session = _dependencies(tmp_path, events)
    drifted = {
        **_operations(),
        "get_external_menu_by_id": LiveOperation(
            "read",
            "cleanup",
            "POST",
            "/api/2/menu/by_id",
        ),
    }
    dependencies = replace(
        dependencies,
        operation_contract_loader=lambda path: _event_result(
            events,
            "operations:load",
            lambda: drifted,
        ),
    )

    with pytest.raises(SafetyError, match="read endpoint"):
        await capture_evidence(
            live_profile="test-server",
            env_file=".env",
            operation="get_external_menu_by_id",
            menu_version=2,
            dependencies=dependencies,
        )

    assert events == [
        "catalog:load",
        "budget:authenticate",
        "budget:get_external_menu_by_id",
        "candidate:compose",
        "operations:load",
    ]


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
    assert dependencies.hints_builder is evidence_module.build_versioned_evidence_redaction_hints
    source = inspect.getsource(evidence_module)
    assert "IIKO_API_KEY_2" not in source
    assert '".state/live.lock"' in source
