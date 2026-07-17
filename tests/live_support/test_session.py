from __future__ import annotations

from pathlib import Path

import httpx
import pytest
import yaml

from tools.openapi_pipeline.errors import SafetyError
from tools.openapi_pipeline.live.lock import LiveProcessLock
from tools.openapi_pipeline.live.profile import ResolvedLiveProfile
from tools.openapi_pipeline.live.rates import LiveRateGuard, RateCatalog
from tools.openapi_pipeline.live.receipt import LiveReceipt
from tools.openapi_pipeline.live.session import SafeLiveSession, load_operation_contract
from tools.openapi_pipeline.live.state import LiveStateStore


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
        api_login="test-login",
        organization_id="00000000-0000-0000-0000-000000000001",
        external_menu_id="menu-1",
        terminal_group_id=None,
        write_product_id=None,
        allow_write=False,
        allowed_organization_ids=(),
        fingerprint="f" * 64,
    )


def _operation_contract():
    return load_operation_contract(Path("contracts/live-operations.yaml"))


@pytest.mark.asyncio
async def test_session_never_retries_429_and_opens_circuit() -> None:
    calls: list[str] = []

    async def handler(request: httpx.Request) -> httpx.Response:
        calls.append(request.url.path)
        if request.url.path == "/api/1/access_token":
            return httpx.Response(200, json={"token": "test-token"})
        return httpx.Response(429, json={"error": "too many"})

    guard = StubGuard()
    async with SafeLiveSession(
        profile=_profile(),
        guard=guard,
        transport=httpx.MockTransport(handler),
        operation_contract=_operation_contract(),
    ) as session:
        await session.authenticate()
        with pytest.raises(SafetyError, match="429"):
            await session.request_json("get_organizations", "POST", "/api/1/organizations", {})
        with pytest.raises(SafetyError, match="unusable"):
            await session.request_json("get_organizations", "POST", "/api/1/organizations", {})

    assert calls == ["/api/1/access_token", "/api/1/organizations"]
    assert guard.acquired == ["authenticate", "get_organizations"]
    assert guard.statuses == [("authenticate", 200), ("get_organizations", 429)]


@pytest.mark.asyncio
async def test_actual_guard_opens_persistent_circuit_on_429(tmp_path) -> None:
    catalog = RateCatalog.from_mapping(
        {
            "version": 1,
            "defaults": {
                "utilization": 0.2,
                "global_min_interval_seconds": 15,
                "max_calls_per_operation_per_run": 1,
            },
            "operations": {
                operation: {
                    "server_limit": {"calls": 100, "per_seconds": 60},
                    "source": "test",
                    "verified": True,
                }
                for operation in ("authenticate", "get_organizations")
            },
        }
    )
    lock = LiveProcessLock(tmp_path / "live.lock")
    state = LiveStateStore(tmp_path / "live-rate-limits.json")
    clock = [100.0]

    async def advance(seconds: float) -> None:
        clock[0] += seconds

    guard = LiveRateGuard(
        profile_fingerprint="f" * 64,
        catalog=catalog,
        state=state,
        process_lock=lock,
        wall_clock=lambda: clock[0],
        monotonic_clock=lambda: clock[0],
        sleeper=advance,
    )
    calls = 0

    async def handler(request: httpx.Request) -> httpx.Response:
        nonlocal calls
        calls += 1
        if request.url.path == "/api/1/access_token":
            return httpx.Response(200, json={"token": "token"})
        return httpx.Response(429, json={})

    with lock:
        async with SafeLiveSession(
            profile=_profile(),
            guard=guard,
            state=state,
            transport=httpx.MockTransport(handler),
            operation_contract=_operation_contract(),
        ) as session:
            await session.authenticate()
            with pytest.raises(SafetyError, match="429"):
                await session.request_json("get_organizations", "POST", "/api/1/organizations", {})
        assert state.circuit_is_open("f" * 64, now=clock[0], lock=lock)
    assert calls == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    ("content", "content_type"),
    [
        (b'{"token":"one","extra":true}', "application/json"),
        (b'{"token":"one","token":"two"}', "application/json"),
        (b'{"token":1}', "application/json"),
        (b'{"token":""}', "application/json"),
        (b"not-json", "application/json"),
        (b'{"token":"one"}', "text/plain"),
    ],
)
async def test_authentication_requires_one_strict_token_response(
    content: bytes, content_type: str
) -> None:
    calls = 0

    async def handler(_request: httpx.Request) -> httpx.Response:
        nonlocal calls
        calls += 1
        return httpx.Response(200, content=content, headers={"content-type": content_type})

    session = SafeLiveSession(
        profile=_profile(),
        guard=StubGuard(),
        transport=httpx.MockTransport(handler),
        operation_contract=_operation_contract(),
    )
    with pytest.raises(SafetyError, match="authentication response"):
        await session.authenticate()
    with pytest.raises(SafetyError, match="unusable"):
        await session.authenticate()
    await session.close()
    assert calls == 1


@pytest.mark.asyncio
async def test_auth_http_failure_is_single_attempt_and_sanitizes_login() -> None:
    secret = "secret-login-that-must-not-leak"
    requests: list[httpx.Request] = []

    async def handler(request: httpx.Request) -> httpx.Response:
        requests.append(request)
        return httpx.Response(500, json={"echo": secret})

    session = SafeLiveSession(
        profile=ResolvedLiveProfile(**{**_profile().__dict__, "api_login": secret}),
        guard=StubGuard(),
        transport=httpx.MockTransport(handler),
        operation_contract=_operation_contract(),
    )
    with pytest.raises(SafetyError) as caught:
        await session.authenticate()
    assert secret not in str(caught.value)
    assert secret not in repr(session)
    with pytest.raises(SafetyError, match="unusable"):
        await session.authenticate()
    await session.close()
    assert len(requests) == 1


@pytest.mark.asyncio
async def test_redirect_is_not_followed() -> None:
    hosts: list[str] = []

    async def handler(request: httpx.Request) -> httpx.Response:
        hosts.append(request.url.host)
        return httpx.Response(302, headers={"location": "https://evil.invalid/steal"})

    async with SafeLiveSession(
        profile=_profile(),
        guard=StubGuard(),
        transport=httpx.MockTransport(handler),
        operation_contract=_operation_contract(),
    ) as session:
        with pytest.raises(SafetyError, match="HTTP 302"):
            await session.authenticate()
    assert hosts == ["api.example.invalid"]


@pytest.mark.asyncio
async def test_request_rejects_unknown_write_method_path_and_payload_before_acquire() -> None:
    calls = 0

    async def handler(request: httpx.Request) -> httpx.Response:
        nonlocal calls
        calls += 1
        return httpx.Response(200, json={"token": "token"})

    guard = StubGuard()
    async with SafeLiveSession(
        profile=_profile(),
        guard=guard,
        transport=httpx.MockTransport(handler),
        operation_contract=_operation_contract(),
    ) as session:
        await session.authenticate()
        bad_calls = [
            ("missing", "POST", "/api/1/organizations", {}),
            ("add_products_to_stop_list", "POST", "/api/1/stop_lists/add", {}),
            ("get_organizations", "post", "/api/1/organizations", {}),
            ("get_organizations", "DELETE", "/api/1/organizations", {}),
            ("get_organizations", "POST", "https://evil.invalid/steal", {}),
            ("get_organizations", "POST", "//evil.invalid/steal", {}),
            ("get_organizations", "POST", "/api/1/organizations?x=1", {}),
            ("get_organizations", "POST", "/api/%2e%2e/steal", {}),
            ("get_organizations", "POST", "/api/1/organizations", {"x": float("nan")}),
        ]
        for operation, method, path, payload in bad_calls:
            with pytest.raises(SafetyError):
                await session.request_json(operation, method, path, payload)

    assert guard.acquired == ["authenticate"]
    assert calls == 1


@pytest.mark.asyncio
async def test_receipt_persists_reserved_operation_before_http(tmp_path) -> None:
    receipt_path = tmp_path / "runs" / "20260716T180000Z-a1b2c3d4.json"
    receipt = LiveReceipt(
        run_id="20260716T180000Z-a1b2c3d4",
        profile_fingerprint="f" * 64,
        effective_schema_sha256="a" * 64,
        generated_tree_sha256="b" * 64,
        operations=(),
        had_429=False,
        completed=False,
    )
    receipt.write(receipt_path)
    observed: list[tuple[str, ...]] = []

    async def handler(request: httpx.Request) -> httpx.Response:
        observed.append(LiveReceipt.load(receipt_path).operations)
        if request.url.path == "/api/1/access_token":
            return httpx.Response(200, json={"token": "token"})
        return httpx.Response(200, json={})

    async with SafeLiveSession(
        profile=_profile(),
        guard=StubGuard(),
        transport=httpx.MockTransport(handler),
        operation_contract=_operation_contract(),
        receipt=receipt,
        receipt_path=receipt_path,
    ) as session:
        await session.authenticate()
        await session.request_json("get_organizations", "POST", "/api/1/organizations", {})

    assert observed == [("authenticate",), ("authenticate", "get_organizations")]


@pytest.mark.asyncio
async def test_transport_failure_is_sanitized_without_retry_and_close_is_idempotent() -> None:
    secret = "secret-login"
    calls = 0

    async def handler(_request: httpx.Request) -> httpx.Response:
        nonlocal calls
        calls += 1
        raise httpx.ConnectError(secret)

    session = SafeLiveSession(
        profile=ResolvedLiveProfile(**{**_profile().__dict__, "api_login": secret}),
        guard=StubGuard(),
        transport=httpx.MockTransport(handler),
        operation_contract=_operation_contract(),
    )
    with pytest.raises(SafetyError) as caught:
        await session.authenticate()
    assert secret not in str(caught.value)
    assert calls == 1
    await session.close()
    await session.close()
    assert session.is_closed


def test_committed_operation_contract_binds_exact_methods_and_paths() -> None:
    operations = load_operation_contract(Path("contracts/live-operations.yaml"))
    assert operations["authenticate"].method == "POST"
    assert operations["authenticate"].path == "/api/1/access_token"
    assert operations["get_organizations"].method == "POST"
    assert operations["get_organizations"].path == "/api/1/organizations"


@pytest.mark.parametrize(
    ("field", "value", "message"),
    [
        ("method", "post", "uppercase"),
        ("method", True, "uppercase"),
        ("path", "/api/1/organizations?x=1", "unsafe path"),
        ("path", "/api/{version}/organizations", "unsafe path"),
        ("path", "/api/../organizations", "unsafe path"),
        ("kind", True, "kind"),
    ],
)
def test_operation_contract_rejects_wrong_endpoint_types_and_values(
    tmp_path: Path, field: str, value: object, message: str
) -> None:
    contract = yaml.safe_load(Path("contracts/live-operations.yaml").read_text(encoding="utf-8"))
    contract["operations"]["get_organizations"][field] = value
    path = tmp_path / "operations.yaml"
    path.write_text(yaml.safe_dump(contract, sort_keys=False), encoding="utf-8")

    with pytest.raises(SafetyError, match=message):
        load_operation_contract(path)


def test_operation_contract_rejects_missing_extra_and_duplicate_fields(tmp_path: Path) -> None:
    original = Path("contracts/live-operations.yaml").read_text(encoding="utf-8")
    path = tmp_path / "operations.yaml"

    path.write_text(original.replace("    method: POST\n", "", 1), encoding="utf-8")
    with pytest.raises(SafetyError, match="invalid fields"):
        load_operation_contract(path)

    path.write_text(
        original.replace("    method: POST\n", "    method: POST\n    extra: true\n", 1),
        encoding="utf-8",
    )
    with pytest.raises(SafetyError, match="invalid fields"):
        load_operation_contract(path)

    path.write_text(
        original.replace("    method: POST\n", "    method: POST\n    method: POST\n", 1),
        encoding="utf-8",
    )
    with pytest.raises(SafetyError, match="strict live operation contract"):
        load_operation_contract(path)


@pytest.mark.asyncio
async def test_operation_endpoint_mismatch_fails_before_guard_receipt_or_http(
    tmp_path: Path,
) -> None:
    calls: list[str] = []

    async def handler(request: httpx.Request) -> httpx.Response:
        calls.append(request.url.path)
        return httpx.Response(200, json={"token": "token"})

    receipt_path = tmp_path / "runs/20260716T180000Z-a1b2c3d4.json"
    receipt = LiveReceipt(
        run_id="20260716T180000Z-a1b2c3d4",
        profile_fingerprint="f" * 64,
        effective_schema_sha256="a" * 64,
        generated_tree_sha256="b" * 64,
        operations=(),
        had_429=False,
        completed=False,
    )
    receipt.write(receipt_path)
    guard = StubGuard()
    async with SafeLiveSession(
        profile=_profile(),
        guard=guard,
        transport=httpx.MockTransport(handler),
        operation_contract=load_operation_contract(Path("contracts/live-operations.yaml")),
        receipt=receipt,
        receipt_path=receipt_path,
    ) as session:
        await session.authenticate()
        for method, path in (
            ("GET", "/api/1/organizations"),
            ("POST", "/api/1/organizations/other"),
        ):
            with pytest.raises(SafetyError, match="endpoint"):
                await session.request_json("get_organizations", method, path, {})

    assert guard.acquired == ["authenticate"]
    assert LiveReceipt.load(receipt_path).operations == ("authenticate",)
    assert calls == ["/api/1/access_token"]
