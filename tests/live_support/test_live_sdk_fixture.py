from __future__ import annotations

import asyncio
import sys
from collections.abc import AsyncIterator
from pathlib import Path
from types import ModuleType, SimpleNamespace
from typing import Any

import pytest
import pytest_asyncio

from tools.openapi_pipeline.errors import SafetyError
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


class _LoopBoundClient:
    def __init__(self) -> None:
        self.setup_loop = asyncio.get_running_loop()
        self.bound_loop: asyncio.AbstractEventLoop | None = None

    async def call(self) -> None:
        self.bound_loop = asyncio.get_running_loop()

    async def close(self) -> None:
        if self.bound_loop is None:
            raise AssertionError("synthetic client was not used")
        self.bound_loop.call_soon(lambda: None)
        await asyncio.sleep(0)
        assert asyncio.get_running_loop() is self.setup_loop is self.bound_loop


@pytest_asyncio.fixture(scope="session", loop_scope="session")
async def loop_bound_live_client() -> AsyncIterator[_LoopBoundClient]:
    client = _LoopBoundClient()
    yield client
    await client.close()


@pytest.mark.asyncio(loop_scope="session")
async def test_session_scoped_async_resource_lifecycle_stays_on_one_loop(
    loop_bound_live_client: _LoopBoundClient,
) -> None:
    await loop_bound_live_client.call()


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

    monkeypatch.setattr(
        fixtures,
        "_load_generated_runtime",
        lambda: SimpleNamespace(
            configuration=FakeConfiguration,
            api_client=FakeApiClient,
            adapter=FakeGeneratedLiveSdk,
        ),
    )

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

    monkeypatch.setattr(
        fixtures,
        "_load_generated_runtime",
        lambda: SimpleNamespace(
            configuration=FakeConfiguration,
            api_client=FailingApiClient,
            adapter=FakeGeneratedLiveSdk,
        ),
    )

    generator = fixtures.live_sdk.__wrapped__(environment, session)
    await anext(generator)
    with pytest.raises(RuntimeError, match="synthetic close failure"):
        await generator.aclose()

    assert not context.generated_client_closed
    context.session_client_closed = True
    assert not context.clients_closed
    assert context.receipt.operations == ("authenticate", "get_organizations")


def test_generated_package_origin_accepts_only_exact_regular_src_file(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    fixtures = _fixture_module()
    expected = tmp_path / "src/iikocloud_client/__init__.py"
    expected.parent.mkdir(parents=True)
    expected.write_text("# generated\n", encoding="utf-8")
    calls: list[str] = []

    def find_spec(name: str) -> SimpleNamespace:
        calls.append(name)
        return SimpleNamespace(origin=str(expected))

    monkeypatch.setattr(fixtures.importlib.util, "find_spec", find_spec)

    fixtures._assert_generated_package_origin(tmp_path)

    assert calls == ["iikocloud_client"]


@pytest.mark.parametrize("failure", ["missing", "wrong", "symlink"])
def test_generated_package_origin_fails_closed_before_runtime_import(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    failure: str,
) -> None:
    fixtures = _fixture_module()
    expected = tmp_path / "src/iikocloud_client/__init__.py"
    expected.parent.mkdir(parents=True)
    if failure == "symlink":
        target = tmp_path / "outside.py"
        target.write_text("# wrong\n", encoding="utf-8")
        expected.symlink_to(target)
        origin: str | None = str(expected)
    else:
        expected.write_text("# generated\n", encoding="utf-8")
        if failure == "wrong":
            wrong = tmp_path / "iikocloud_client/__init__.py"
            wrong.parent.mkdir(parents=True)
            wrong.write_text("# legacy\n", encoding="utf-8")
            origin = str(wrong)
        else:
            origin = None

    monkeypatch.setattr(
        fixtures.importlib.util,
        "find_spec",
        lambda _name: None if origin is None else SimpleNamespace(origin=origin),
    )

    with pytest.raises(SafetyError, match="package origin"):
        fixtures._assert_generated_package_origin(tmp_path)


def test_live_environment_rejects_package_origin_before_private_profile_access(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    fixtures = _fixture_module()
    events: list[str] = []
    request = SimpleNamespace(
        config=SimpleNamespace(invocation_params=SimpleNamespace(args=("-n0",)))
    )

    monkeypatch.setattr(
        fixtures.RepoPaths,
        "discover",
        lambda: SimpleNamespace(root=tmp_path),
    )

    def prepare_preflight(_root: Path, *, invocation_args: object) -> object:
        events.append("preflight")
        return object()

    monkeypatch.setattr(fixtures, "prepare_live_preflight", prepare_preflight)

    def reject_origin(_root: Path) -> None:
        events.append("origin")
        raise SafetyError("Generated package origin is not the exact src package")

    monkeypatch.setattr(fixtures, "_assert_generated_package_origin", reject_origin)

    def resolve_private(*_args: object, **_kwargs: object) -> ResolvedLiveProfile:
        events.append("private")
        return _profile()

    monkeypatch.setattr(fixtures, "resolve_locked_live_profile", resolve_private)

    environment = fixtures._live_environment.__wrapped__(request)
    with pytest.raises(SafetyError, match="package origin"):
        next(environment)

    assert events == ["preflight", "origin"]
    assert not (tmp_path / ".state").exists()
