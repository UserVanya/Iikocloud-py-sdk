from __future__ import annotations

import os
import re
import subprocess
import sys
from dataclasses import replace
from pathlib import Path
from types import SimpleNamespace
from typing import Any

import conftest as project_conftest
import pytest

from tools.openapi_pipeline.errors import SafetyError
from tools.openapi_pipeline.live.profile import ResolvedLiveProfile
from tools.openapi_pipeline.live.rates import RateCatalog

_ORGANIZATION_ID = "00000000-0000-0000-0000-000000000001"
_TERMINAL_GROUP_ID = "00000000-0000-0000-0000-000000000002"
_PRODUCT_ID = "00000000-0000-0000-0000-000000000003"
_STOP_LIST_SCENARIO_OPERATION_IDS = tuple(
    sorted(
        (
            "get_organizations",
            "get_stop_lists",
            "add_products_to_stop_list",
            "remove_products_from_stop_list",
        )
    )
)


class _Config:
    def __init__(
        self,
        *,
        options: dict[str, object] | None = None,
        arguments: tuple[str, ...] = ("-n0",),
    ) -> None:
        self._options = {
            "--allow-live-write": True,
            "--allow-audit-residue": True,
            "--target-organization": _ORGANIZATION_ID,
            **(options or {}),
        }
        self.invocation_params = SimpleNamespace(args=arguments)
        self._iiko_write_scenario_ids = ("stop_list_product",)

    def getoption(self, name: str) -> object:
        return self._options[name]


def _profile(**overrides: Any) -> ResolvedLiveProfile:
    profile = ResolvedLiveProfile(
        name="test",
        base_url="https://api.example.invalid",
        api_login="synthetic-login",
        organization_id=_ORGANIZATION_ID,
        external_menu_id="synthetic-menu",
        terminal_group_id=_TERMINAL_GROUP_ID,
        write_product_id=_PRODUCT_ID,
        allow_write=True,
        allowed_organization_ids=(_ORGANIZATION_ID,),
        fingerprint="a" * 64,
    )
    return replace(profile, **overrides)


def _catalog(*, unverified: str | None = None) -> RateCatalog:
    return RateCatalog.from_mapping(
        {
            "version": 2,
            "defaults": {
                "utilization": 0.20,
                "global_min_interval_seconds": 30,
                "max_calls_per_operation_per_run": 1,
            },
            "operations": {
                operation_id: {
                    "test_budget": {
                        "min_interval_seconds": 30,
                        "source": "synthetic",
                        "verified": operation_id != unverified,
                    },
                    "server_limit": {
                        "calls": 1,
                        "per_seconds": 60,
                        "source": "synthetic",
                        "verified": True,
                    },
                }
                for operation_id in _STOP_LIST_SCENARIO_OPERATION_IDS
            },
        }
    )


@pytest.mark.parametrize(
    ("options", "message"),
    [
        ({"--allow-live-write": False}, "--allow-live-write"),
        ({"--target-organization": None}, "--target-organization"),
        ({"--allow-audit-residue": False}, "--allow-audit-residue"),
    ],
)
def test_write_cli_gates_require_every_explicit_opt_in_before_private_setup(
    options: dict[str, object],
    message: str,
) -> None:
    with pytest.raises(pytest.UsageError, match=message):
        project_conftest._assert_live_write_cli_gates(  # noqa: SLF001
            _Config(options=options),  # type: ignore[arg-type]
            audit_residue=True,
        )


def test_write_cli_gate_requires_explicit_single_worker_before_private_setup() -> None:
    with pytest.raises(pytest.UsageError, match="single-process"):
        project_conftest._assert_live_write_cli_gates(  # noqa: SLF001
            _Config(arguments=()),  # type: ignore[arg-type]
            audit_residue=True,
        )


@pytest.mark.parametrize(
    ("profile", "options", "message"),
    [
        (_profile(allow_write=False), {}, "allow_write"),
        (_profile(), {"--allow-live-write": False}, "--allow-live-write"),
        (_profile(), {"--target-organization": "different"}, "does not match"),
        (_profile(allowed_organization_ids=()), {}, "allowlist"),
        (_profile(terminal_group_id=None), {}, "terminal group"),
        (_profile(write_product_id=None), {}, "write product"),
    ],
)
def test_write_setup_checks_every_profile_and_target_boundary_before_budgets(
    profile: ResolvedLiveProfile,
    options: dict[str, object],
    message: str,
) -> None:
    with pytest.raises(SafetyError, match=message):
        project_conftest._prepare_live_write_setup(  # noqa: SLF001
            _Config(options=options),  # type: ignore[arg-type]
            profile,
            _catalog(),
        )


@pytest.mark.parametrize("unverified", _STOP_LIST_SCENARIO_OPERATION_IDS)
def test_write_setup_requires_every_distinct_operation_budget(unverified: str) -> None:
    with pytest.raises(SafetyError, match=unverified):
        project_conftest._prepare_live_write_setup(  # noqa: SLF001
            _Config(),  # type: ignore[arg-type]
            _profile(),
            _catalog(unverified=unverified),
        )


def test_write_setup_returns_only_operation_ids_and_a_redacted_target_fingerprint() -> None:
    preflight = project_conftest._prepare_live_write_setup(  # noqa: SLF001
        _Config(),  # type: ignore[arg-type]
        _profile(),
        _catalog(),
    )

    assert preflight.operation_ids == _STOP_LIST_SCENARIO_OPERATION_IDS
    assert re.fullmatch(r"[0-9a-f]{64}", preflight.target_organization_fingerprint)
    assert _ORGANIZATION_ID not in repr(preflight)


def _journal_fixture_inputs(run_id: str) -> tuple[SimpleNamespace, SimpleNamespace]:
    request = SimpleNamespace(
        node=SimpleNamespace(
            get_closest_marker=lambda marker: object() if marker == "live_write" else None
        )
    )
    environment = SimpleNamespace(
        context=SimpleNamespace(receipt=SimpleNamespace(run_id=run_id)),
        profile=SimpleNamespace(fingerprint="f" * 64),
    )
    return request, environment


@pytest.mark.asyncio(loop_scope="session")
async def test_mutation_journal_fixture_removes_empty_journal_but_retains_pending(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(
        project_conftest.RepoPaths,
        "discover",
        lambda: SimpleNamespace(root=tmp_path),
    )
    fixture_function = project_conftest.mutation_journal.__wrapped__  # type: ignore[attr-defined]

    empty_request, empty_environment = _journal_fixture_inputs("empty-run")
    empty_generator = fixture_function(empty_request, empty_environment)
    empty_journal = await anext(empty_generator)
    empty_path = empty_journal.path
    await empty_generator.aclose()

    assert not empty_path.exists()

    pending_request, pending_environment = _journal_fixture_inputs("pending-run")
    pending_generator = fixture_function(pending_request, pending_environment)
    pending_journal = await anext(pending_generator)
    pending_journal.register("remove_products_from_stop_list", {"synthetic": True})
    pending_path = pending_journal.path
    await pending_generator.aclose()

    assert pending_path.exists()
    assert pending_journal.pending_count == 1


def _collect_write_test(*arguments: str) -> subprocess.CompletedProcess[str]:
    environment = os.environ.copy()
    for name in (
        "IIKO_API_KEY",
        "IIKO_API_KEY_2",
        "IIKO_TEST_ORGANIZATION_ID",
        "IIKO_TEST_EXTERNAL_MENU_ID",
        "IIKO_TEST_TERMINAL_GROUP_ID",
        "IIKO_TEST_WRITE_PRODUCT_ID",
    ):
        environment.pop(name, None)
    return subprocess.run(
        [
            sys.executable,
            "-m",
            "pytest",
            "-m",
            "live_write",
            "-n0",
            "--collect-only",
            "-q",
            "tests/integration/write/test_stop_list.py",
            *arguments,
        ],
        cwd=Path.cwd(),
        env=environment,
        check=False,
        capture_output=True,
        text=True,
    )


def test_write_collect_without_profile_is_safe_and_keeps_the_test_visible() -> None:
    result = _collect_write_test()

    assert result.returncode == 0, result.stderr
    assert "test_stop_list_add_is_accepted_and_removed" in result.stdout


def test_write_collect_with_profile_rejects_missing_opt_in_before_private_access() -> None:
    result = _collect_write_test(
        "--live-profile",
        "test-server",
        "--target-organization",
        _ORGANIZATION_ID,
        "--allow-audit-residue",
    )

    assert result.returncode == int(pytest.ExitCode.USAGE_ERROR)
    assert "--allow-live-write" in result.stderr
    assert "Private" not in result.stderr


def test_write_collect_with_profile_rejects_missing_audit_approval_before_private_access() -> None:
    result = _collect_write_test(
        "--live-profile",
        "test-server",
        "--target-organization",
        _ORGANIZATION_ID,
        "--allow-live-write",
    )

    assert result.returncode == int(pytest.ExitCode.USAGE_ERROR)
    assert "--allow-audit-residue" in result.stderr
    assert "Private" not in result.stderr


def test_write_scenario_marker_rejects_unknown_disabled_and_missing(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    def _item(marker_arg: str) -> Any:
        return SimpleNamespace(
            get_closest_marker=lambda name: (
                SimpleNamespace(args=(marker_arg,)) if name == "write_scenario" else None
            )
        )

    root = Path.cwd()
    with pytest.raises(pytest.UsageError, match="Unknown write lifecycle scenario"):
        project_conftest._write_scenario_ids(root, [_item("nope")])  # noqa: SLF001
    assert project_conftest._write_scenario_ids(root, [_item("customer")]) == (  # noqa: SLF001
        "customer",
    )
    disabled = SimpleNamespace(
        get_closest_marker=lambda name: (
            SimpleNamespace(args=("customer",)) if name == "write_scenario" else None
        )
    )
    monkeypatch.setattr(
        project_conftest,
        "_load_write_lifecycle_registry",
        lambda _root: SimpleNamespace(
            scenarios={
                "customer": SimpleNamespace(
                    enabled=False, disabled_reason="synthetic reason"
                )
            }
        ),
    )
    with pytest.raises(pytest.UsageError, match="disabled"):
        project_conftest._write_scenario_ids(root, [disabled])  # noqa: SLF001
    with pytest.raises(pytest.UsageError, match="write_scenario"):
        project_conftest._write_scenario_ids(  # noqa: SLF001
            root,
            [SimpleNamespace(get_closest_marker=lambda name: None)],
        )
