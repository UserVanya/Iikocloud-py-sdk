from __future__ import annotations

import json
import os
import stat
from pathlib import Path
from typing import Any

import pytest

import tools.openapi_pipeline.mutations as mutation_module
from tools.openapi_pipeline.errors import SafetyError
from tools.openapi_pipeline.io import canonical_json_bytes
from tools.openapi_pipeline.live.rates import OperationBudget
from tools.openapi_pipeline.live.session import LiveOperation
from tools.openapi_pipeline.mutations import (
    MutationJournal,
    cleanup_orphans,
    plan_orphan_cleanup,
)


def _cleanup_contract() -> dict[str, LiveOperation]:
    return {
        "remove_child": LiveOperation("cleanup", None, "POST", "/cleanup/child"),
        "remove_parent": LiveOperation("cleanup", None, "POST", "/cleanup/parent"),
        "read_only": LiveOperation("read", None, "POST", "/read"),
    }


def _budget(operation_id: str) -> OperationBudget:
    return OperationBudget(
        operation_id=operation_id,
        safe_interval_seconds=30.0,
        max_calls_per_run=1,
    )


def _write_private(path: Path, body: bytes) -> None:
    path.parent.mkdir(mode=0o700, parents=True, exist_ok=True)
    os.chmod(path.parent, 0o700)
    path.write_bytes(body)
    os.chmod(path, 0o600)


@pytest.mark.asyncio
async def test_cleanup_is_registered_durably_and_runs_pending_entries_lifo(
    tmp_path: Path,
) -> None:
    calls: list[str] = []
    journal = MutationJournal.create(tmp_path, "run-1", "profile-hash")

    journal.register("remove_child", {"id": "child"})
    journal.register("remove_parent", {"id": "parent"})

    expected = {
        "run_id": "run-1",
        "profile_fingerprint": "profile-hash",
        "completed": False,
        "cleanup": [
            {"operation_id": "remove_child", "payload": {"id": "child"}, "done": False},
            {
                "operation_id": "remove_parent",
                "payload": {"id": "parent"},
                "done": False,
            },
        ],
    }
    assert journal.path == tmp_path / "mutations/run-1.json"
    assert journal.path.read_bytes() == canonical_json_bytes(expected)
    assert stat.S_IMODE(journal.path.stat().st_mode) == 0o600
    assert stat.S_IMODE(journal.path.parent.stat().st_mode) == 0o700

    async def execute(operation_id: str, _payload: dict[str, Any]) -> None:
        calls.append(operation_id)

    await journal.cleanup(execute)

    assert calls == ["remove_parent", "remove_child"]
    assert not journal.path.exists()


def test_register_detaches_payload_and_rolls_back_memory_when_atomic_write_fails(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    journal = MutationJournal.create(tmp_path, "run-1", "profile-hash")
    payload = {"items": [{"id": "first"}]}
    journal.register("remove_child", payload)
    payload["items"][0]["id"] = "changed-after-register"
    before = journal.path.read_bytes()

    def fail_write(*_args: object, **_kwargs: object) -> None:
        raise OSError("private-payload-marker")

    monkeypatch.setattr(mutation_module, "write_json_atomic", fail_write)
    with pytest.raises(SafetyError, match="persist mutation journal") as caught:
        journal.register("remove_parent", {"id": "second"})

    assert "private-payload-marker" not in str(caught.value)
    assert journal.pending_count == 1
    assert journal.path.read_bytes() == before
    assert b"changed-after-register" not in before


def test_register_rejects_oversized_full_journal_before_atomic_write(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    journal = MutationJournal.create(tmp_path, "run-1", "profile-hash")
    journal.register("remove_child", {"blob": "a" * 600_000})
    before = journal.path.read_bytes()
    writes: list[Path] = []
    real_write = mutation_module.write_json_atomic

    def observe_write(path: Path, value: Any, mode: int = 0o644) -> None:
        writes.append(path)
        real_write(path, value, mode=mode)

    monkeypatch.setattr(mutation_module, "write_json_atomic", observe_write)

    with pytest.raises(SafetyError, match="persist mutation journal"):
        journal.register("remove_parent", {"blob": "b" * 600_000})

    assert writes == []
    assert journal.path.read_bytes() == before
    loaded = MutationJournal.load(
        journal.path,
        expected_profile_fingerprint="profile-hash",
    )
    assert loaded.pending_count == 1


@pytest.mark.asyncio
async def test_cleanup_failure_persists_each_prior_success_and_keeps_pending_journal(
    tmp_path: Path,
) -> None:
    journal = MutationJournal.create(tmp_path, "run-1", "profile-hash")
    journal.register("remove_child", {"id": "child"})
    journal.register("remove_parent", {"id": "parent"})
    calls: list[str] = []

    async def fail_second(operation_id: str, _payload: dict[str, Any]) -> None:
        calls.append(operation_id)
        if operation_id == "remove_child":
            raise RuntimeError("private-payload-marker")

    with pytest.raises(SafetyError, match="journal retained") as caught:
        await journal.cleanup(fail_second)

    assert "private-payload-marker" not in str(caught.value)
    assert calls == ["remove_parent", "remove_child"]
    assert journal.path.exists()
    resumed = MutationJournal.load(
        journal.path,
        expected_profile_fingerprint="profile-hash",
    )
    assert resumed.pending_count == 1

    retried: list[str] = []

    async def succeed(operation_id: str, _payload: dict[str, Any]) -> None:
        retried.append(operation_id)

    await resumed.cleanup(succeed)
    assert retried == ["remove_child"]
    assert not journal.path.exists()


def test_load_requires_matching_profile_without_echoing_fingerprints(tmp_path: Path) -> None:
    journal = MutationJournal.create(tmp_path, "run-1", "profile-private-a")

    with pytest.raises(SafetyError, match="selected profile") as caught:
        MutationJournal.load(
            journal.path,
            expected_profile_fingerprint="profile-private-b",
        )

    message = str(caught.value)
    assert "profile-private-a" not in message
    assert "profile-private-b" not in message


@pytest.mark.parametrize(
    ("body", "message"),
    [
        (b"{not-json}\n", "strict JSON"),
        (
            b'{"cleanup":[],"completed":false,"profile_fingerprint":"profile-hash",'
            b'"run_id":"run-1","run_id":"run-2"}\n',
            "strict JSON",
        ),
        (
            canonical_json_bytes(
                {
                    "run_id": "run-1",
                    "profile_fingerprint": "profile-hash",
                    "completed": False,
                    "cleanup": [],
                    "extra": True,
                }
            ),
            "fields",
        ),
        (
            json.dumps(
                {
                    "run_id": "run-1",
                    "profile_fingerprint": "profile-hash",
                    "completed": False,
                    "cleanup": [],
                }
            ).encode(),
            "canonical JSON",
        ),
        (
            canonical_json_bytes(
                {
                    "run_id": "run-1",
                    "profile_fingerprint": "profile-hash",
                    "completed": False,
                    "cleanup": [{"operation_id": "remove_child", "payload": [], "done": False}],
                }
            ),
            "payload",
        ),
    ],
)
def test_load_rejects_malformed_or_noncanonical_journal(
    tmp_path: Path,
    body: bytes,
    message: str,
) -> None:
    path = tmp_path / "mutations/run-1.json"
    _write_private(path, body)

    with pytest.raises(SafetyError, match=message):
        MutationJournal.load(path)


def test_load_rejects_unsafe_mode_symlink_and_hardlink(tmp_path: Path) -> None:
    journal = MutationJournal.create(tmp_path, "run-1", "profile-hash")
    os.chmod(journal.path, 0o644)
    with pytest.raises(SafetyError, match="0600"):
        MutationJournal.load(journal.path)

    os.chmod(journal.path, 0o600)
    symlink = journal.path.with_name("run-2.json")
    symlink.symlink_to(journal.path)
    with pytest.raises(SafetyError, match="symlink"):
        MutationJournal.load(symlink)

    hardlink = journal.path.with_name("run-3.json")
    os.link(journal.path, hardlink)
    with pytest.raises(SafetyError, match="link"):
        MutationJournal.load(hardlink)


def test_create_and_register_reject_unsafe_inputs_without_payload_echo(tmp_path: Path) -> None:
    with pytest.raises(SafetyError, match="run ID"):
        MutationJournal.create(tmp_path, "../escape", "profile-hash")
    journal = MutationJournal.create(tmp_path, "run-1", "profile-hash")
    with pytest.raises(SafetyError, match="already exists"):
        MutationJournal.create(tmp_path, "run-1", "profile-hash")
    marker = "private-payload-marker"
    with pytest.raises(SafetyError, match="payload") as caught:
        journal.register("remove_child", {"value": object(), "marker": marker})
    assert marker not in str(caught.value)
    assert marker not in repr(journal)


def test_plan_loads_only_selected_profile_and_preserves_each_journal_lifo(
    tmp_path: Path,
) -> None:
    selected = MutationJournal.create(tmp_path, "run-1", "profile-selected")
    selected.register("remove_child", {"id": "private-child-payload"})
    selected.register("remove_parent", {"id": "private-parent-payload"})
    other = MutationJournal.create(tmp_path, "run-2", "profile-other")
    other.register("remove_child", {"id": "other"})

    plan = plan_orphan_cleanup(
        tmp_path,
        profile_fingerprint="profile-selected",
        operation_contract=_cleanup_contract(),
    )

    assert plan.count == 2
    assert plan.journal_count == 1
    assert plan.operation_ids == ("remove_parent", "remove_child")
    assert "profile-selected" not in plan.render()
    assert "private-parent-payload" not in plan.render()
    assert "private-child-payload" not in plan.render()


@pytest.mark.parametrize("operation_id", ["missing", "read_only"])
def test_plan_rejects_unknown_or_noncleanup_operation_before_any_budget(
    tmp_path: Path,
    operation_id: str,
) -> None:
    journal = MutationJournal.create(tmp_path, "run-1", "profile-hash")
    journal.register(operation_id, {"id": "private-payload-marker"})

    with pytest.raises(SafetyError, match="classified as cleanup") as caught:
        plan_orphan_cleanup(
            tmp_path,
            profile_fingerprint="profile-hash",
            operation_contract=_cleanup_contract(),
        )

    assert "private-payload-marker" not in str(caught.value)


@pytest.mark.asyncio
async def test_cleanup_orphans_checks_every_budget_then_confirms_before_first_call(
    tmp_path: Path,
) -> None:
    journal = MutationJournal.create(tmp_path, "run-1", "profile-hash")
    journal.register("remove_child", {"id": "private-payload-marker"})
    journal.register("remove_parent", {"id": "parent"})
    events: list[str] = []
    output: list[str] = []

    def confirm(prompt: str) -> str:
        events.append(f"confirm:{prompt}")
        return "y"

    def reserve_budget(operation_id: str) -> OperationBudget:
        events.append(f"budget:{operation_id}")
        return _budget(operation_id)

    async def execute(operation_id: str, _payload: dict[str, Any]) -> None:
        events.append(f"call:{operation_id}")

    count = await cleanup_orphans(
        tmp_path,
        profile_fingerprint="profile-hash",
        operation_contract=_cleanup_contract(),
        reserve_budget=reserve_budget,
        execute=execute,
        confirm=confirm,
        emit=output.append,
    )

    assert count == 2
    assert events == [
        "budget:remove_parent",
        "budget:remove_child",
        "confirm:cleanup 2 actions [y/N]",
        "call:remove_parent",
        "call:remove_child",
    ]
    rendered = "\n".join(output)
    assert "remove_parent" in rendered
    assert "remove_child" in rendered
    assert "private-payload-marker" not in rendered
    assert not journal.path.exists()


@pytest.mark.asyncio
async def test_cleanup_orphans_decline_or_budget_failure_makes_no_call_and_keeps_journal(
    tmp_path: Path,
) -> None:
    journal = MutationJournal.create(tmp_path, "run-1", "profile-hash")
    journal.register("remove_child", {"id": "child"})
    calls: list[str] = []
    decline_budget_calls: list[str] = []

    def reserve_before_decline(operation_id: str) -> OperationBudget:
        decline_budget_calls.append(operation_id)
        return _budget(operation_id)

    async def execute(operation_id: str, _payload: dict[str, Any]) -> None:
        calls.append(operation_id)

    with pytest.raises(SafetyError, match="not confirmed"):
        await cleanup_orphans(
            tmp_path,
            profile_fingerprint="profile-hash",
            operation_contract=_cleanup_contract(),
            reserve_budget=reserve_before_decline,
            execute=execute,
            confirm=lambda _prompt: "n",
            emit=lambda _line: None,
        )
    assert decline_budget_calls == ["remove_child"]
    assert calls == []
    assert journal.path.exists()

    budget_calls: list[str] = []
    budget_failure_prompts: list[str] = []

    def fail_budget(operation_id: str) -> OperationBudget:
        budget_calls.append(operation_id)
        raise RuntimeError("private-payload-marker")

    def confirm_after_budgets(prompt: str) -> str:
        budget_failure_prompts.append(prompt)
        return "y"

    with pytest.raises(SafetyError, match="reserve every cleanup budget") as caught:
        await cleanup_orphans(
            tmp_path,
            profile_fingerprint="profile-hash",
            operation_contract=_cleanup_contract(),
            reserve_budget=fail_budget,
            execute=execute,
            confirm=confirm_after_budgets,
            emit=lambda _line: None,
        )
    assert "private-payload-marker" not in str(caught.value)
    assert budget_calls == ["remove_child"]
    assert budget_failure_prompts == []
    assert calls == []
    assert journal.path.exists()


@pytest.mark.asyncio
async def test_duplicate_operation_budget_failure_happens_before_first_cleanup_call(
    tmp_path: Path,
) -> None:
    journal = MutationJournal.create(tmp_path, "run-1", "profile-hash")
    journal.register("remove_child", {"id": "first"})
    journal.register("remove_child", {"id": "second"})
    reserved: set[str] = set()
    calls: list[str] = []

    def reserve_once(operation_id: str) -> OperationBudget:
        if operation_id in reserved:
            raise SafetyError("max calls per run exhausted")
        reserved.add(operation_id)
        return _budget(operation_id)

    async def execute(operation_id: str, _payload: dict[str, Any]) -> None:
        calls.append(operation_id)

    with pytest.raises(SafetyError, match="reserve every cleanup budget"):
        await cleanup_orphans(
            tmp_path,
            profile_fingerprint="profile-hash",
            operation_contract=_cleanup_contract(),
            reserve_budget=reserve_once,
            execute=execute,
            confirm=lambda _prompt: "y",
            emit=lambda _line: None,
        )

    assert reserved == {"remove_child"}
    assert calls == []
    assert journal.path.exists()
    assert MutationJournal.load(journal.path).pending_count == 2


@pytest.mark.asyncio
async def test_invalid_budget_result_fails_before_first_cleanup_call(tmp_path: Path) -> None:
    journal = MutationJournal.create(tmp_path, "run-1", "profile-hash")
    journal.register("remove_child", {"id": "child"})
    calls: list[str] = []

    async def execute(operation_id: str, _payload: dict[str, Any]) -> None:
        calls.append(operation_id)

    with pytest.raises(SafetyError, match="reserve every cleanup budget"):
        await cleanup_orphans(
            tmp_path,
            profile_fingerprint="profile-hash",
            operation_contract=_cleanup_contract(),
            reserve_budget=lambda _operation_id: None,
            execute=execute,
            confirm=lambda _prompt: "y",
            emit=lambda _line: None,
        )

    assert calls == []
    assert journal.path.exists()


def test_plan_fails_closed_on_unrelated_malformed_journal(tmp_path: Path) -> None:
    selected = MutationJournal.create(tmp_path, "run-1", "profile-selected")
    selected.register("remove_child", {"id": "child"})
    malformed = tmp_path / "mutations/run-2.json"
    _write_private(malformed, b"not-json\n")

    with pytest.raises(SafetyError, match="strict JSON"):
        plan_orphan_cleanup(
            tmp_path,
            profile_fingerprint="profile-selected",
            operation_contract=_cleanup_contract(),
        )


@pytest.mark.asyncio
async def test_cleanup_orphans_accepts_no_actions_without_confirmation_or_budget(
    tmp_path: Path,
) -> None:
    events: list[str] = []

    def confirm(prompt: str) -> str:
        events.append(f"confirm:{prompt}")
        return "y"

    result = await cleanup_orphans(
        tmp_path,
        profile_fingerprint="profile-hash",
        operation_contract=_cleanup_contract(),
        reserve_budget=lambda operation_id: events.append(f"budget:{operation_id}"),
        execute=lambda operation_id, payload: _async_event(events, operation_id, payload),
        confirm=confirm,
        emit=lambda line: events.append(f"emit:{line}"),
    )

    assert result == 0
    assert events == ["emit:orphan cleanup plan: 0 actions"]


async def _async_event(
    events: list[str],
    operation_id: str,
    _payload: dict[str, Any],
) -> None:
    events.append(f"call:{operation_id}")
