from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import httpx
import pytest

import tools.openapi_pipeline.live.session as session_module
from tools.openapi_pipeline.capture import CaptureWriter, LiveCapture, RedactionHints
from tools.openapi_pipeline.errors import SafetyError
from tools.openapi_pipeline.live.profile import ResolvedLiveProfile
from tools.openapi_pipeline.live.receipt import LiveReceipt
from tools.openapi_pipeline.live.session import (
    SafeLiveSession,
    load_operation_contract,
)

_API_LOGIN = "synthetic-api-login"
_TOKEN = "synthetic-active-token"
_CORRELATION_ID = "00000000-0000-0000-0000-000000000001"
_RESPONSE_SECRET = "never-leak-response-secret"


def _auth_response() -> dict[str, str]:
    return {"correlationId": _CORRELATION_ID, "token": _TOKEN}


class StubGuard:
    def __init__(self) -> None:
        self.acquired: list[str] = []
        self.statuses: list[tuple[str, int]] = []

    async def acquire(self, operation_id: str) -> None:
        self.acquired.append(operation_id)

    def record_status(self, operation_id: str, status: int) -> None:
        self.statuses.append((operation_id, status))


def _profile() -> ResolvedLiveProfile:
    return ResolvedLiveProfile(
        name="test",
        base_url="https://api.example.invalid",
        api_login=_API_LOGIN,
        organization_id="11111111-1111-4111-8111-111111111111",
        external_menu_id="menu",
        terminal_group_id=None,
        write_product_id=None,
        allow_write=False,
        allowed_organization_ids=(),
        fingerprint="f" * 64,
    )


def _schema() -> dict[str, Any]:
    return {
        "openapi": "3.1.0",
        "paths": {
            "/api/1/organizations": {
                "post": {
                    "operationId": "get_organizations",
                    "requestBody": {
                        "content": {
                            "application/json": {
                                "schema": {
                                    "properties": {
                                        "type": {"enum": ["ORGANIZATION", _API_LOGIN, _TOKEN]}
                                    }
                                }
                            }
                        }
                    },
                    "responses": {
                        "200": {
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "properties": {
                                            "type": {
                                                "enum": [
                                                    "ORGANIZATION",
                                                    _API_LOGIN,
                                                    _TOKEN,
                                                ]
                                            },
                                            "name": {"type": "string"},
                                        }
                                    }
                                }
                            }
                        }
                    },
                }
            }
        },
    }


def _capture(root: Path) -> LiveCapture:
    operations = load_operation_contract(Path("contracts/live-operations.yaml"))
    return LiveCapture(
        writer=CaptureWriter(root),
        run_id="run",
        selected_operation="get_organizations",
        operation_catalog=operations,
        hints=RedactionHints.for_operation(_schema(), "get_organizations"),
    )


@pytest.mark.asyncio
async def test_safe_session_captures_only_complete_parsed_read_and_wires_secrets(
    tmp_path: Path,
) -> None:
    calls: list[str] = []

    async def handler(request: httpx.Request) -> httpx.Response:
        calls.append(request.url.path)
        if request.url.path == "/api/1/access_token":
            return httpx.Response(200, json=_auth_response())
        return httpx.Response(
            200,
            json={"type": _TOKEN, "name": f"venue-{_API_LOGIN}"},
            headers={"x-correlation-id": _TOKEN},
        )

    root = tmp_path / "captures"
    guard = StubGuard()
    async with SafeLiveSession(
        profile=_profile(),
        guard=guard,
        transport=httpx.MockTransport(handler),
        operation_contract=load_operation_contract(Path("contracts/live-operations.yaml")),
        capture=_capture(root),
    ) as session:
        await session.authenticate()
        response = await session.request_json(
            "get_organizations",
            "POST",
            "/api/1/organizations",
            {"type": _API_LOGIN},
        )

    assert response.status_code == 200
    assert calls == ["/api/1/access_token", "/api/1/organizations"]
    assert not (root / "run/authenticate").exists()
    request_path = root / "run/get_organizations/request.json"
    response_path = root / "run/get_organizations/response.json"
    serialized = request_path.read_text() + response_path.read_text()
    assert _API_LOGIN not in serialized
    assert _TOKEN not in serialized
    assert json.loads(request_path.read_text())["body"]["type"] == "<redacted:secret>"
    assert json.loads(response_path.read_text())["body"]["type"] == "<redacted:secret>"
    assert guard.acquired == ["authenticate", "get_organizations"]


@pytest.mark.asyncio
@pytest.mark.parametrize(
    ("failure", "status", "content", "content_type", "expected_message"),
    [
        (
            "non-success",
            503,
            _RESPONSE_SECRET.encode(),
            "application/json",
            "Live capture failed: non-success HTTP 503; no retry",
        ),
        (
            "too-large",
            200,
            f'{{"value":"{_RESPONSE_SECRET}"}}'.encode(),
            "application/json",
            "Live capture failed: response too large; no retry",
        ),
        (
            "non-json",
            200,
            _RESPONSE_SECRET.encode(),
            f"application/{_RESPONSE_SECRET}",
            "Live capture failed: response content type is not JSON; no retry",
        ),
        (
            "invalid-json",
            200,
            _RESPONSE_SECRET.encode(),
            "application/json",
            "Live capture failed: invalid JSON response; no retry",
        ),
        (
            "final-processing",
            200,
            f'{{"{_RESPONSE_SECRET}@example.com":"value"}}'.encode(),
            "application/json",
            "Live capture failed: final capture processing; no retry",
        ),
    ],
)
async def test_capture_reports_only_sanitized_failure_class_without_retry(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    failure: str,
    status: int,
    content: bytes,
    content_type: str,
    expected_message: str,
) -> None:
    calls = 0

    if failure == "too-large":
        monkeypatch.setattr(session_module, "_MAX_CAPTURE_BODY", len(content) - 1)

    async def handler(request: httpx.Request) -> httpx.Response:
        nonlocal calls
        calls += 1
        if request.url.path == "/api/1/access_token":
            return httpx.Response(200, json=_auth_response())
        return httpx.Response(
            status,
            content=content,
            headers={
                "content-type": content_type,
                "x-private": _RESPONSE_SECRET,
            },
        )

    root = tmp_path / "captures"
    session = SafeLiveSession(
        profile=_profile(),
        guard=StubGuard(),
        transport=httpx.MockTransport(handler),
        operation_contract=load_operation_contract(Path("contracts/live-operations.yaml")),
        capture=_capture(root),
    )
    await session.authenticate()
    with pytest.raises(SafetyError) as caught:
        await session.request_json("get_organizations", "POST", "/api/1/organizations", {})
    assert str(caught.value) == expected_message
    assert _RESPONSE_SECRET not in str(caught.value)
    with pytest.raises(SafetyError, match="unusable"):
        await session.request_json("get_organizations", "POST", "/api/1/organizations", {})
    await session.close()

    assert calls == 2
    assert not list(root.rglob("*.json"))


@pytest.mark.asyncio
async def test_capture_selection_mismatch_fails_before_rate_reservation_or_http(
    tmp_path: Path,
) -> None:
    calls: list[str] = []

    async def handler(request: httpx.Request) -> httpx.Response:
        calls.append(request.url.path)
        return httpx.Response(200, json=_auth_response())

    guard = StubGuard()
    async with SafeLiveSession(
        profile=_profile(),
        guard=guard,
        transport=httpx.MockTransport(handler),
        operation_contract=load_operation_contract(Path("contracts/live-operations.yaml")),
        capture=_capture(tmp_path / "captures"),
    ) as session:
        await session.authenticate()
        with pytest.raises(SafetyError, match="selected"):
            await session.request_json("get_external_menus", "POST", "/api/2/menu", {})

    assert calls == ["/api/1/access_token"]
    assert guard.acquired == ["authenticate"]


@pytest.mark.asyncio
async def test_capture_filesystem_failure_fails_receipt_and_never_retries(
    tmp_path: Path,
) -> None:
    calls = 0

    async def handler(request: httpx.Request) -> httpx.Response:
        nonlocal calls
        calls += 1
        if request.url.path == "/api/1/access_token":
            return httpx.Response(200, json=_auth_response())
        return httpx.Response(200, json={"type": "ORGANIZATION"})

    root = tmp_path / "wide-captures"
    root.mkdir(mode=0o700)
    root.chmod(0o755)
    receipt_path = tmp_path / "receipt/run.json"
    receipt = LiveReceipt(
        run_id="20260717T000000Z-a1b2c3d4",
        profile_fingerprint="f" * 64,
        effective_schema_sha256="a" * 64,
        generated_tree_sha256="b" * 64,
        operations=(),
        had_429=False,
        completed=False,
    )
    receipt.write(receipt_path)
    session = SafeLiveSession(
        profile=_profile(),
        guard=StubGuard(),
        transport=httpx.MockTransport(handler),
        operation_contract=load_operation_contract(Path("contracts/live-operations.yaml")),
        capture=_capture(root),
        receipt=receipt,
        receipt_path=receipt_path,
    )
    await session.authenticate()
    with pytest.raises(SafetyError, match="capture"):
        await session.request_json("get_organizations", "POST", "/api/1/organizations", {})
    with pytest.raises(SafetyError, match="unusable"):
        await session.request_json("get_organizations", "POST", "/api/1/organizations", {})
    await session.close()

    persisted = LiveReceipt.load(receipt_path)
    assert persisted.operations == ("authenticate", "get_organizations")
    assert not persisted.completed
    assert calls == 2
