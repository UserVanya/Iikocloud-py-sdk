from __future__ import annotations

import sys
from pathlib import Path
from types import ModuleType, SimpleNamespace
from typing import Any

import pytest

from tools.openapi_pipeline.live.profile import ResolvedLiveProfile
from tools.openapi_pipeline.live.receipt import LiveReceipt


def _fixture_module() -> ModuleType:
    expected = (Path(__file__).parents[1] / "conftest.py").resolve()
    for module in tuple(sys.modules.values()):
        module_path = getattr(module, "__file__", None)
        if module_path is not None and Path(module_path).resolve() == expected:
            return module
    raise AssertionError("root pytest fixture module is not loaded")


def _profile() -> ResolvedLiveProfile:
    return ResolvedLiveProfile(
        name="test-server",
        base_url="https://api.example.invalid",
        api_login="synthetic-login",
        organization_id="organization-id",
        external_menu_id="menu-id",
        terminal_group_id=None,
        write_product_id=None,
        allow_write=False,
        allowed_organization_ids=("organization-id",),
        fingerprint="f" * 64,
    )


def _auth_receipt(path: Path) -> LiveReceipt:
    receipt = LiveReceipt(
        run_id="20260720T120000Z-a1b2c3d4",
        profile_fingerprint="f" * 64,
        effective_schema_sha256="a" * 64,
        generated_tree_sha256="b" * 64,
        operations=("authenticate",),
        had_429=False,
        completed=False,
    )
    receipt.write(path)
    return receipt


@pytest.mark.asyncio
async def test_live_sdk_uses_authenticated_session_guard_state_and_closes_client(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    fixtures = _fixture_module()
    profile = _profile()
    receipt_path = tmp_path / "live-runs/receipt.json"
    receipt = _auth_receipt(receipt_path)
    context = fixtures._LiveRunContext(receipt=receipt, receipt_path=receipt_path)
    state = object()
    guard = SimpleNamespace(state=state)
    session = SimpleNamespace(
        profile=profile,
        access_token="synthetic-access-token",
        guard=guard,
        state=state,
        receipt=receipt,
    )
    environment = SimpleNamespace(profile=profile, state=state, context=context)
    constructed: dict[str, Any] = {}

    class FakeConfiguration:
        def __init__(self, *, host: str, access_token: str) -> None:
            constructed["host"] = host
            constructed["access_token"] = access_token

    class FakeApiClient:
        def __init__(self, configuration: FakeConfiguration) -> None:
            constructed["client"] = self
            constructed["configuration"] = configuration
            self.closed = False

        async def close(self) -> None:
            self.closed = True

    class FakeGeneratedLiveSdk:
        def __init__(self, **kwargs: Any) -> None:
            constructed["adapter_kwargs"] = kwargs
            self.api_client = kwargs["api_client"]
            self.receipt = kwargs["receipt"]

    monkeypatch.setattr(fixtures, "Configuration", FakeConfiguration)
    monkeypatch.setattr(fixtures, "ApiClient", FakeApiClient)
    monkeypatch.setattr(fixtures, "GeneratedLiveSdk", FakeGeneratedLiveSdk)

    fixture_function = fixtures.live_sdk.__wrapped__
    generator = fixture_function(environment, session)
    adapter = await anext(generator)

    assert adapter.api_client is constructed["client"]
    assert constructed["host"] == profile.base_url
    assert constructed["access_token"] == session.access_token
    assert constructed["adapter_kwargs"] == {
        "api_client": constructed["client"],
        "profile": profile,
        "guard": guard,
        "state": state,
        "receipt": receipt,
        "receipt_path": receipt_path,
    }
    assert context.generated_client_required
    assert not context.clients_closed

    adapter.receipt = receipt.with_operation("get_organizations")
    await generator.aclose()

    assert constructed["client"].closed
    assert context.generated_client_closed
    assert context.receipt == adapter.receipt
    context.session_client_closed = True
    assert context.clients_closed


@pytest.mark.asyncio
async def test_live_sdk_close_failure_keeps_client_gate_closed(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    fixtures = _fixture_module()
    profile = _profile()
    receipt_path = tmp_path / "live-runs/receipt.json"
    receipt = _auth_receipt(receipt_path)
    context = fixtures._LiveRunContext(receipt=receipt, receipt_path=receipt_path)
    state = object()
    guard = SimpleNamespace(state=state)
    session = SimpleNamespace(
        profile=profile,
        access_token="synthetic-access-token",
        guard=guard,
        state=state,
        receipt=receipt,
    )
    environment = SimpleNamespace(profile=profile, state=state, context=context)

    class FakeConfiguration:
        def __init__(self, *, host: str, access_token: str) -> None:
            pass

    class FailingApiClient:
        def __init__(self, configuration: FakeConfiguration) -> None:
            pass

        async def close(self) -> None:
            raise RuntimeError("synthetic close failure")

    class FakeGeneratedLiveSdk:
        def __init__(self, **kwargs: Any) -> None:
            self.api_client = kwargs["api_client"]
            self.receipt = kwargs["receipt"].with_operation("get_organizations")

    monkeypatch.setattr(fixtures, "Configuration", FakeConfiguration)
    monkeypatch.setattr(fixtures, "ApiClient", FailingApiClient)
    monkeypatch.setattr(fixtures, "GeneratedLiveSdk", FakeGeneratedLiveSdk)

    generator = fixtures.live_sdk.__wrapped__(environment, session)
    await anext(generator)
    with pytest.raises(RuntimeError, match="synthetic close failure"):
        await generator.aclose()

    assert not context.generated_client_closed
    context.session_client_closed = True
    assert not context.clients_closed
    assert context.receipt.operations == ("authenticate", "get_organizations")
