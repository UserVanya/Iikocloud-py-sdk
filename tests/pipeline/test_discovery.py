from __future__ import annotations

import json
from collections.abc import Mapping
from pathlib import Path
from typing import Any

import httpx
import pytest

from tools.openapi_pipeline.discovery import (
    DiscoveryDependencies,
    _organizations,
    discover_read_targets,
)
from tools.openapi_pipeline.errors import SafetyError
from tools.openapi_pipeline.live.lock import LiveProcessLock
from tools.openapi_pipeline.live.profile import ResolvedDiscoveryProfile
from tools.openapi_pipeline.live.rates import LiveRateGuard, RateCatalog
from tools.openapi_pipeline.live.session import SafeLiveSession, load_operation_contract
from tools.openapi_pipeline.live.state import LiveStateStore
from tools.openapi_pipeline.paths import RepoPaths

ROOT = Path(__file__).resolve().parents[2]
_CORRELATION_ID = "00000000-0000-0000-0000-000000000001"


def _auth_response(token: str) -> dict[str, str]:
    return {"correlationId": _CORRELATION_ID, "token": token}


def _profile() -> ResolvedDiscoveryProfile:
    return ResolvedDiscoveryProfile(
        name="test-server",
        base_url="https://api.example.invalid",
        api_login="private-login",
        fingerprint="f" * 64,
    )


def _dependencies(
    tmp_path: Path,
    handler: Any,
    clock: list[float],
) -> DiscoveryDependencies:
    transport = httpx.MockTransport(handler)

    async def advance(seconds: float) -> None:
        clock[0] += seconds

    def guard_factory(**kwargs: Any) -> LiveRateGuard:
        return LiveRateGuard(
            **kwargs,
            wall_clock=lambda: clock[0],
            monotonic_clock=lambda: clock[0],
            sleeper=advance,
        )

    def session_factory(**kwargs: Any) -> SafeLiveSession:
        return SafeLiveSession(**kwargs, transport=transport)

    return DiscoveryDependencies(
        paths=RepoPaths(tmp_path),
        rate_catalog_loader=lambda _path: RateCatalog.load(ROOT / "contracts/rate-limits.yaml"),
        operation_contract_loader=lambda _path: load_operation_contract(
            ROOT / "contracts/live-operations.yaml"
        ),
        lock_factory=LiveProcessLock,
        profile_resolver=lambda *_args, **_kwargs: _profile(),
        state_factory=LiveStateStore,
        guard_factory=guard_factory,
        session_factory=session_factory,
    )


def _payload(request: httpx.Request) -> Mapping[str, Any] | None:
    if not request.content:
        return None
    value = json.loads(request.content)
    assert isinstance(value, dict)
    return value


def test_organization_parser_preserves_documented_nullable_name() -> None:
    response = httpx.Response(
        200,
        json={"organizations": [{"id": "org-1", "name": None}]},
    )

    assert _organizations(response)[0].name is None


@pytest.mark.asyncio
async def test_discovery_makes_one_guarded_call_per_operation_and_sanitizes_output(
    tmp_path: Path,
) -> None:
    clock = [0.0]
    observed: list[tuple[float, str, Mapping[str, Any] | None]] = []

    async def handler(request: httpx.Request) -> httpx.Response:
        observed.append((clock[0], request.url.path, _payload(request)))
        responses = {
            "/api/1/access_token": _auth_response("private-token"),
            "/api/1/organizations": {
                "correlationId": "must-not-escape",
                "organizations": [
                    {
                        "id": "org-1",
                        "name": "Организация",
                        "internalMetadata": "discarded",
                    }
                ],
            },
            "/api/1/terminal_groups": {
                "correlationId": "must-not-escape",
                "terminalGroups": [
                    {
                        "organizationId": "org-1",
                        "items": [
                            {
                                "id": "terminal-1",
                                "organizationId": "org-1",
                                "name": "Касса",
                                "address": "drop-me",
                            }
                        ],
                    }
                ],
                "terminalGroupsInSleep": [
                    {
                        "organizationId": "org-1",
                        "items": [
                            {
                                "id": "terminal-2",
                                "organizationId": "org-1",
                                "name": "Резерв",
                            }
                        ],
                    }
                ],
            },
            "/api/2/menu": {
                "correlationId": "must-not-escape",
                "externalMenus": [
                    {
                        "id": "menu-1",
                        "name": "Основное меню",
                        "internalMetadata": "discarded",
                    }
                ],
                "priceCategories": [{"id": "drop-me", "name": "drop-me"}],
            },
        }
        return httpx.Response(200, json=responses[request.url.path])

    result = await discover_read_targets(
        live_profile="test-server",
        env_file=".env",
        dependencies=_dependencies(tmp_path, handler, clock),
    )

    assert observed == [
        (0.0, "/api/1/access_token", {"apiLogin": "private-login"}),
        (30.0, "/api/1/organizations", {}),
        (
            60.0,
            "/api/1/terminal_groups",
            {"organizationIds": ["org-1"], "includeDisabled": True},
        ),
        (90.0, "/api/2/menu", None),
    ]
    assert result.to_dict() == {
        "organizations": [
            {
                "id": "org-1",
                "name": "Организация",
                "terminalGroups": [
                    {"id": "terminal-1", "name": "Касса", "isSleeping": False},
                    {"id": "terminal-2", "name": "Резерв", "isSleeping": True},
                ],
            }
        ],
        "externalMenus": [{"id": "menu-1", "name": "Основное меню"}],
    }
    rendered = json.dumps(result.to_dict(), ensure_ascii=False)
    for forbidden in (
        "private-login",
        "private-token",
        _CORRELATION_ID,
        "must-not-escape",
        "discarded",
    ):
        assert forbidden not in rendered


@pytest.mark.asyncio
async def test_discovery_stops_entire_run_on_429_without_retry(tmp_path: Path) -> None:
    clock = [0.0]
    calls: list[str] = []

    async def handler(request: httpx.Request) -> httpx.Response:
        calls.append(request.url.path)
        if request.url.path == "/api/1/access_token":
            return httpx.Response(200, json=_auth_response("token"))
        return httpx.Response(429, json={"error": "too many"})

    with pytest.raises(SafetyError, match="429"):
        await discover_read_targets(
            live_profile="test-server",
            env_file=".env",
            dependencies=_dependencies(tmp_path, handler, clock),
        )

    assert calls == ["/api/1/access_token", "/api/1/organizations"]


@pytest.mark.asyncio
async def test_discovery_rejects_unsafe_identity_before_followup_calls(tmp_path: Path) -> None:
    clock = [0.0]
    calls: list[str] = []

    async def handler(request: httpx.Request) -> httpx.Response:
        calls.append(request.url.path)
        if request.url.path == "/api/1/access_token":
            return httpx.Response(200, json=_auth_response("token"))
        return httpx.Response(
            200,
            json={"organizations": [{"id": "../unsafe", "name": "Bad\nName"}]},
        )

    with pytest.raises(SafetyError, match="organization"):
        await discover_read_targets(
            live_profile="test-server",
            env_file=".env",
            dependencies=_dependencies(tmp_path, handler, clock),
        )

    assert calls == ["/api/1/access_token", "/api/1/organizations"]
