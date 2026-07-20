from __future__ import annotations

import os
import socket
from collections.abc import Callable
from dataclasses import dataclass
from pathlib import Path
from types import SimpleNamespace
from typing import Any, cast

import pytest

from tools.openapi_pipeline.errors import SafetyError
from tools.openapi_pipeline.live.generated import validate_generated_cleanup_request
from tools.openapi_pipeline.live.profile import ResolvedLiveProfile
from tools.openapi_pipeline.live.rates import OperationBudget
from tools.openapi_pipeline.live.session import LiveOperation
from tools.openapi_pipeline.mutations import MutationJournal, cleanup_orphans
from tools.openapi_pipeline.orphan_cleanup import (
    CleanupOrphansDependencies,
    cleanup_orphans_command,
)
from tools.openapi_pipeline.paths import RepoPaths

_CLEANUP_OPERATION = "remove_products_from_stop_list"
_ORGANIZATION_ID = "11111111-1111-4111-8111-111111111111"
_TERMINAL_GROUP_ID = "22222222-2222-4222-8222-222222222222"
_PRODUCT_ID = "33333333-3333-4333-8333-333333333333"
_OTHER_ID = "99999999-9999-4999-8999-999999999999"
_PRIVATE_PAYLOAD = "private-payload-marker"


class _Catalog:
    def __init__(self, events: list[str], *, fail_operation: str | None = None) -> None:
        self.events = events
        self.fail_operation = fail_operation

    def operation_budget(self, operation_id: str) -> OperationBudget:
        self.events.append(f"budget:{operation_id}")
        if operation_id == self.fail_operation:
            raise RuntimeError("private-budget-marker")
        return OperationBudget(
            operation_id=operation_id,
            safe_interval_seconds=30.0,
            max_calls_per_run=1,
        )


class _Lock:
    def __init__(self, path: Path, events: list[str]) -> None:
        self.path = path
        self.events = events
        self.held = False

    def __enter__(self) -> _Lock:
        self.events.append("lock:enter")
        self.held = True
        return self

    def __exit__(self, *_args: object) -> None:
        self.events.append("lock:exit")
        self.held = False


@dataclass
class _Harness:
    dependencies: CleanupOrphansDependencies
    output: list[str]
    cleanup_calls: list[tuple[str, object]]


@pytest.fixture(autouse=True)
def _forbid_network(monkeypatch: pytest.MonkeyPatch) -> None:
    real_socket = socket.socket

    def guarded_socket(*args: Any, **kwargs: Any) -> socket.SocketType:
        family = kwargs.get("family", args[0] if args else socket.AF_INET)
        if family in {socket.AF_INET, socket.AF_INET6}:
            raise AssertionError("orphan cleanup tests must not create a network socket")
        return real_socket(*args, **kwargs)

    monkeypatch.setattr(socket, "socket", guarded_socket)


def _profile() -> ResolvedLiveProfile:
    return ResolvedLiveProfile(
        name="test-server",
        base_url="https://api.example.invalid",
        api_login="private-api-login",
        organization_id=_ORGANIZATION_ID,
        external_menu_id="menu-id",
        terminal_group_id=_TERMINAL_GROUP_ID,
        write_product_id=_PRODUCT_ID,
        allow_write=True,
        allowed_organization_ids=(_ORGANIZATION_ID,),
        fingerprint="f" * 64,
    )


def _operation_contract() -> dict[str, LiveOperation]:
    return {
        "authenticate": LiveOperation("auth", None, "POST", "/api/1/access_token"),
        _CLEANUP_OPERATION: LiveOperation(
            "cleanup",
            None,
            "POST",
            "/api/1/stop_lists/remove",
        ),
        "get_organizations": LiveOperation(
            "read",
            None,
            "POST",
            "/api/1/organizations",
        ),
    }


def _harness(
    tmp_path: Path,
    events: list[str],
    *,
    answer: str = "y",
    catalog: _Catalog | None = None,
    operation_contract: dict[str, LiveOperation] | None = None,
    fail_execute: bool = False,
    fail_env: bool = False,
    cleanup_validator: Callable[[str, object, ResolvedLiveProfile], object] | None = None,
) -> _Harness:
    output: list[str] = []
    cleanup_calls: list[tuple[str, object]] = []
    selected_catalog = catalog or _Catalog(events)
    selected_contract = operation_contract or _operation_contract()

    def load_catalog(path: Path) -> _Catalog:
        assert path == tmp_path / "contracts/rate-limits.yaml"
        events.append("catalog:load")
        return selected_catalog

    def load_contract(path: Path) -> dict[str, LiveOperation]:
        assert path == tmp_path / "contracts/live-operations.yaml"
        events.append("contract:load")
        return selected_contract

    def validate_env(root: Path, value: object) -> Path | None:
        assert root == tmp_path
        events.append(f"env:{value}")
        if fail_env:
            raise SafetyError("--env-file must resolve exactly to the repository root .env")
        return None if value is None else root / ".env"

    def make_lock(path: Path) -> _Lock:
        assert path == tmp_path / ".state/live.lock"
        events.append("lock:create")
        return _Lock(path, events)

    def resolve_profile(
        root: Path,
        *,
        process_lock: _Lock,
        profile_name: object,
        env_file_option: object,
    ) -> ResolvedLiveProfile:
        assert root == tmp_path
        assert process_lock.held
        assert profile_name == "test-server"
        assert env_file_option in {None, str(tmp_path / ".env")}
        events.append("profile:resolve")
        return _profile()

    def make_state(path: Path, *, process_lock: _Lock) -> object:
        assert path == tmp_path / ".state/live-rate-limits.json"
        assert process_lock.held
        events.append("state:create")
        return object()

    def make_guard(**kwargs: object) -> SimpleNamespace:
        assert kwargs["profile_fingerprint"] == "f" * 64
        assert kwargs["catalog"] is selected_catalog
        assert isinstance(kwargs["process_lock"], _Lock)
        events.append("guard:create")
        return SimpleNamespace(state=kwargs["state"])

    class FakeSession:
        def __init__(self, **kwargs: object) -> None:
            assert kwargs["profile"] == _profile()
            assert kwargs["operation_contract"] is selected_contract
            self.authenticated = False
            events.append("session:create")

        @property
        def access_token(self) -> str:
            assert self.authenticated
            return "private-access-token"

        async def authenticate(self) -> None:
            assert not self.authenticated
            self.authenticated = True
            events.append("session:authenticate")

        async def close(self) -> None:
            events.append("session:close")

    class FakeConfiguration:
        def __init__(self, *, host: str, access_token: str) -> None:
            assert host == _profile().base_url
            assert access_token == "private-access-token"
            events.append("configuration:create")

    class FakeApiClient:
        def __init__(self, _configuration: FakeConfiguration) -> None:
            events.append("api-client:create")

        async def close(self) -> None:
            events.append("api-client:close")

    class FakeGeneratedSdk:
        def __init__(self, **kwargs: object) -> None:
            assert kwargs["profile"] == _profile()
            guard = kwargs["guard"]
            assert isinstance(guard, SimpleNamespace)
            assert guard.state is kwargs["state"]
            events.append("generated-sdk:create")

        async def execute_cleanup(
            self,
            operation_id: str,
            payload: dict[str, Any],
        ) -> None:
            events.append(f"cleanup:{operation_id}")
            cleanup_calls.append((operation_id, payload))
            if fail_execute:
                raise RuntimeError("private-execute-marker")

    def load_runtime() -> SimpleNamespace:
        events.append("runtime:load")
        return SimpleNamespace(
            configuration=FakeConfiguration,
            api_client=FakeApiClient,
            adapter=FakeGeneratedSdk,
        )

    def validate_cleanup(
        operation_id: str,
        payload: object,
        profile: ResolvedLiveProfile,
    ) -> object:
        assert profile == _profile()
        events.append(f"validate:{operation_id}")
        return payload

    def confirm(prompt: str) -> str:
        events.append(f"confirm:{prompt}")
        return answer

    def emit(line: str) -> None:
        events.append(f"emit:{line}")
        output.append(line)

    return _Harness(
        dependencies=CleanupOrphansDependencies(
            paths=RepoPaths(tmp_path),
            rate_catalog_loader=cast(Any, load_catalog),
            operation_contract_loader=load_contract,
            env_file_validator=validate_env,
            lock_factory=cast(Any, make_lock),
            profile_resolver=resolve_profile,
            state_factory=cast(Any, make_state),
            guard_factory=cast(Any, make_guard),
            session_factory=cast(Any, FakeSession),
            runtime_loader=load_runtime,
            cleanup_validator=cleanup_validator or validate_cleanup,
            cleanup_runner=cleanup_orphans,
            confirm=confirm,
            emit=emit,
        ),
        output=output,
        cleanup_calls=cleanup_calls,
    )


def _assert_in_order(events: list[str], *expected: str) -> None:
    position = -1
    for event in expected:
        position = events.index(event, position + 1)


@pytest.mark.asyncio
async def test_cleanup_command_preflights_then_lazily_authenticates_and_closes_clients(
    tmp_path: Path,
) -> None:
    state_root = tmp_path / ".state"
    journal = MutationJournal.create(state_root, "run-1", "f" * 64)
    journal.register(_CLEANUP_OPERATION, {"id": _PRIVATE_PAYLOAD})
    events: list[str] = []
    harness = _harness(tmp_path, events)

    count = await cleanup_orphans_command(
        live_profile="test-server",
        env_file=".env",
        dependencies=harness.dependencies,
    )

    assert count == 1
    assert not journal.path.exists()
    assert harness.cleanup_calls == [(_CLEANUP_OPERATION, {"id": _PRIVATE_PAYLOAD})]
    _assert_in_order(
        events,
        "catalog:load",
        "contract:load",
        "budget:authenticate",
        "env:.env",
        "lock:enter",
        "profile:resolve",
        f"budget:{_CLEANUP_OPERATION}",
        "confirm:cleanup 1 actions [y/N]",
        f"validate:{_CLEANUP_OPERATION}",
        "state:create",
        "guard:create",
        "session:create",
        "session:authenticate",
        "runtime:load",
        "configuration:create",
        "api-client:create",
        "generated-sdk:create",
        f"cleanup:{_CLEANUP_OPERATION}",
        "api-client:close",
        "session:close",
        "lock:exit",
    )
    rendered = "\n".join(harness.output)
    assert "f" * 64 in rendered
    assert _CLEANUP_OPERATION in rendered
    assert _PRIVATE_PAYLOAD not in rendered
    assert _ORGANIZATION_ID not in rendered
    assert "private-api-login" not in rendered
    assert "private-access-token" not in rendered


@pytest.mark.asyncio
async def test_schema_valid_orphan_outside_profile_fails_before_state_session_or_auth(
    tmp_path: Path,
) -> None:
    state_root = tmp_path / ".state"
    journal = MutationJournal.create(state_root, "run-1", "f" * 64)
    journal.register(
        _CLEANUP_OPERATION,
        {
            "items": [{"productId": _PRODUCT_ID}],
            "organizationId": _OTHER_ID,
            "terminalGroupId": _TERMINAL_GROUP_ID,
        },
    )
    events: list[str] = []

    def validate_cleanup(
        operation_id: str,
        payload: object,
        profile: ResolvedLiveProfile,
    ) -> object:
        events.append(f"validate:{operation_id}")
        return validate_generated_cleanup_request(operation_id, payload, profile)

    harness = _harness(tmp_path, events, cleanup_validator=validate_cleanup)

    with pytest.raises(SafetyError, match="journal retained") as caught:
        await cleanup_orphans_command(
            live_profile="test-server",
            env_file=None,
            dependencies=harness.dependencies,
        )

    assert _OTHER_ID not in str(caught.value)
    assert events.count(f"validate:{_CLEANUP_OPERATION}") == 1
    assert "state:create" not in events
    assert "guard:create" not in events
    assert "session:create" not in events
    assert "session:authenticate" not in events
    assert "runtime:load" not in events
    assert "configuration:create" not in events
    assert "api-client:create" not in events
    assert "generated-sdk:create" not in events
    assert harness.cleanup_calls == []
    assert journal.path.exists()
    assert MutationJournal.load(journal.path).pending_count == 1


@pytest.mark.asyncio
async def test_duplicate_operation_budget_fails_before_auth_or_cleanup(
    tmp_path: Path,
) -> None:
    state_root = tmp_path / ".state"
    journal = MutationJournal.create(state_root, "run-1", "f" * 64)
    journal.register(_CLEANUP_OPERATION, {"id": "first"})
    journal.register(_CLEANUP_OPERATION, {"id": "second"})
    events: list[str] = []
    harness = _harness(tmp_path, events)

    with pytest.raises(SafetyError, match="reserve every cleanup budget"):
        await cleanup_orphans_command(
            live_profile="test-server",
            env_file=None,
            dependencies=harness.dependencies,
        )

    assert events.count(f"budget:{_CLEANUP_OPERATION}") == 2
    assert not any(event.startswith("confirm:") for event in events)
    assert "state:create" not in events
    assert "session:create" not in events
    assert harness.cleanup_calls == []
    assert journal.path.exists()
    assert MutationJournal.load(journal.path).pending_count == 2


@pytest.mark.asyncio
async def test_decline_and_no_actions_never_create_live_clients(tmp_path: Path) -> None:
    state_root = tmp_path / ".state"
    journal = MutationJournal.create(state_root, "run-1", "f" * 64)
    journal.register(_CLEANUP_OPERATION, {"id": "retained"})
    decline_events: list[str] = []
    declined = _harness(tmp_path, decline_events, answer="n")

    with pytest.raises(SafetyError, match="not confirmed"):
        await cleanup_orphans_command(
            live_profile="test-server",
            env_file=None,
            dependencies=declined.dependencies,
        )

    assert journal.path.exists()
    assert "state:create" not in decline_events
    assert "session:create" not in decline_events
    assert decline_events.count(f"budget:{_CLEANUP_OPERATION}") == 1

    await journal.cleanup(lambda _operation, _payload: _completed())
    empty_events: list[str] = []
    empty = _harness(tmp_path, empty_events)
    result = await cleanup_orphans_command(
        live_profile="test-server",
        env_file=None,
        dependencies=empty.dependencies,
    )

    assert result == 0
    assert "state:create" not in empty_events
    assert "session:create" not in empty_events
    assert not any(event.startswith("confirm:") for event in empty_events)


async def _completed() -> None:
    return None


@pytest.mark.asyncio
@pytest.mark.parametrize("malformation", ["unknown-operation", "invalid-json"])
async def test_invalid_journal_fails_before_prompt_or_live_clients_and_is_retained(
    tmp_path: Path,
    malformation: str,
) -> None:
    state_root = tmp_path / ".state"
    if malformation == "unknown-operation":
        journal = MutationJournal.create(state_root, "run-1", "f" * 64)
        journal.register("unknown_cleanup", {"id": _PRIVATE_PAYLOAD})
        path = journal.path
    else:
        mutation_root = state_root / "mutations"
        mutation_root.mkdir(mode=0o700, parents=True)
        os.chmod(state_root, 0o700)
        path = mutation_root / "run-1.json"
        path.write_bytes(b"{invalid-json}\n")
        os.chmod(path, 0o600)
    events: list[str] = []
    harness = _harness(tmp_path, events)

    with pytest.raises(SafetyError):
        await cleanup_orphans_command(
            live_profile="test-server",
            env_file=None,
            dependencies=harness.dependencies,
        )

    assert path.exists()
    assert not any(event.startswith("confirm:") for event in events)
    assert "state:create" not in events
    assert "session:create" not in events
    assert harness.cleanup_calls == []


@pytest.mark.asyncio
async def test_cleanup_failure_retains_journal_and_closes_both_clients(
    tmp_path: Path,
) -> None:
    state_root = tmp_path / ".state"
    journal = MutationJournal.create(state_root, "run-1", "f" * 64)
    journal.register(_CLEANUP_OPERATION, {"id": _PRIVATE_PAYLOAD})
    events: list[str] = []
    harness = _harness(tmp_path, events, fail_execute=True)

    with pytest.raises(SafetyError, match="journal retained") as caught:
        await cleanup_orphans_command(
            live_profile="test-server",
            env_file=None,
            dependencies=harness.dependencies,
        )

    assert "private-execute-marker" not in str(caught.value)
    assert journal.path.exists()
    _assert_in_order(events, "api-client:create", "api-client:close", "session:close")


@pytest.mark.asyncio
@pytest.mark.parametrize("failure", ["contract", "auth-budget", "env"])
async def test_public_preflight_and_env_validation_fail_before_private_access(
    tmp_path: Path,
    failure: str,
) -> None:
    events: list[str] = []
    contract = _operation_contract()
    if failure == "contract":
        contract["authenticate"] = LiveOperation(
            "auth",
            None,
            "POST",
            "/wrong-auth-path",
        )
    catalog = _Catalog(
        events,
        fail_operation="authenticate" if failure == "auth-budget" else None,
    )
    harness = _harness(
        tmp_path,
        events,
        catalog=catalog,
        operation_contract=contract,
        fail_env=failure == "env",
    )

    with pytest.raises(SafetyError):
        await cleanup_orphans_command(
            live_profile="test-server",
            env_file=".env",
            dependencies=harness.dependencies,
        )

    assert "profile:resolve" not in events
    assert "state:create" not in events
    assert "session:create" not in events
