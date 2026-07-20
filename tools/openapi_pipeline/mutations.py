from __future__ import annotations

import json
import math
import os
import re
import stat
from collections import Counter
from collections.abc import Awaitable, Callable, Mapping
from contextlib import suppress
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from .errors import SafetyError
from .io import canonical_json_bytes, write_json_atomic
from .live.lock import ensure_private_directory, validate_private_regular_file
from .live.rates import OperationBudget
from .live.session import LiveOperation

_SAFE_ID = re.compile(r"[A-Za-z0-9][A-Za-z0-9_.:-]{0,127}\Z")
_JOURNAL_FIELDS = {"run_id", "profile_fingerprint", "completed", "cleanup"}
_ENTRY_FIELDS = {"operation_id", "payload", "done"}
_MAX_JOURNAL_BYTES = 1024 * 1024
_MAX_ACTIONS = 1024
_MAX_JSON_DEPTH = 64

CleanupExecutor = Callable[[str, dict[str, Any]], Awaitable[object]]
BudgetReservation = Callable[[str], object]
Confirmation = Callable[[str], str]
Emitter = Callable[[str], object]


def _safe_id(value: object, *, label: str) -> str:
    if not isinstance(value, str) or _SAFE_ID.fullmatch(value) is None:
        raise SafetyError(f"Mutation journal {label} must be a safe ASCII identifier")
    return value


def _unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("duplicate JSON key")
        result[key] = value
    return result


def _reject_constant(value: str) -> None:
    raise ValueError(f"non-finite JSON number {value}")


def _validate_json(value: object, *, depth: int = 0) -> None:
    if depth > _MAX_JSON_DEPTH:
        raise SafetyError("Mutation journal payload is nested too deeply")
    if value is None or type(value) in {bool, int, str}:
        return
    if type(value) is float:
        if not math.isfinite(value):
            raise SafetyError("Mutation journal payload contains a non-finite number")
        return
    if type(value) is list:
        for item in value:
            _validate_json(item, depth=depth + 1)
        return
    if type(value) is dict:
        if any(type(key) is not str for key in value):
            raise SafetyError("Mutation journal payload keys must be strings")
        for item in value.values():
            _validate_json(item, depth=depth + 1)
        return
    raise SafetyError("Mutation journal payload must contain only strict JSON values")


def _detached_payload(value: object) -> dict[str, Any]:
    if type(value) is not dict:
        raise SafetyError("Mutation journal payload must be a JSON object")
    try:
        _validate_json(value)
        body = canonical_json_bytes(value)
        if len(body) > _MAX_JOURNAL_BYTES:
            raise SafetyError("Mutation journal payload is too large")
        copied = json.loads(
            body.decode("utf-8"),
            object_pairs_hook=_unique_object,
            parse_constant=_reject_constant,
        )
    except SafetyError:
        raise
    except (UnicodeError, ValueError, TypeError, OverflowError, RecursionError):
        raise SafetyError("Mutation journal payload is not strict JSON") from None
    if type(copied) is not dict:  # pragma: no cover - guarded before serialization
        raise SafetyError("Mutation journal payload must be a JSON object")
    return copied


def _private_directory(path: Path, *, label: str) -> None:
    try:
        metadata = path.lstat()
    except FileNotFoundError as error:
        raise SafetyError(f"{label} is missing") from error
    if stat.S_ISLNK(metadata.st_mode) or not stat.S_ISDIR(metadata.st_mode):
        raise SafetyError(f"{label} must be a non-symlink directory")
    if stat.S_IMODE(metadata.st_mode) != 0o700:
        raise SafetyError(f"{label} must have mode 0700")
    if metadata.st_uid != os.getuid():
        raise SafetyError(f"{label} must be owned by the current user")


def _journal_location(path: Path) -> tuple[Path, str]:
    if not isinstance(path, Path) or path.parent.name != "mutations" or path.suffix != ".json":
        raise SafetyError("Mutation journal path is not canonical")
    run_id = _safe_id(path.stem, label="run ID")
    state_root = path.parent.parent
    if path != state_root / "mutations" / f"{run_id}.json":
        raise SafetyError("Mutation journal path is not canonical")
    return state_root, run_id


def _read_private_journal(path: Path) -> bytes:
    state_root, _run_id = _journal_location(path)
    _private_directory(state_root, label="Mutation state directory")
    _private_directory(path.parent, label="Mutation journal directory")
    try:
        expected = validate_private_regular_file(path, label="Mutation journal")
    except FileNotFoundError as error:
        raise SafetyError("Mutation journal is missing") from error
    flags = os.O_RDONLY | os.O_CLOEXEC | getattr(os, "O_NOFOLLOW", 0)
    try:
        descriptor = os.open(path, flags)
    except OSError:
        raise SafetyError("Cannot open mutation journal safely") from None
    try:
        actual = os.fstat(descriptor)
        if (
            not stat.S_ISREG(actual.st_mode)
            or stat.S_IMODE(actual.st_mode) != 0o600
            or actual.st_uid != os.getuid()
            or actual.st_nlink != 1
            or (actual.st_dev, actual.st_ino) != (expected.st_dev, expected.st_ino)
        ):
            raise SafetyError("Mutation journal changed while it was opened")
        chunks: list[bytes] = []
        remaining = _MAX_JOURNAL_BYTES + 1
        while remaining:
            chunk = os.read(descriptor, min(65536, remaining))
            if not chunk:
                break
            chunks.append(chunk)
            remaining -= len(chunk)
        body = b"".join(chunks)
    finally:
        os.close(descriptor)
    if len(body) > _MAX_JOURNAL_BYTES:
        raise SafetyError("Mutation journal is too large")
    try:
        current = validate_private_regular_file(path, label="Mutation journal")
    except FileNotFoundError:
        raise SafetyError("Mutation journal changed while it was read") from None
    if (current.st_dev, current.st_ino) != (expected.st_dev, expected.st_ino):
        raise SafetyError("Mutation journal changed while it was read")
    return body


def _parse_document(body: bytes, *, expected_run_id: str) -> dict[str, Any]:
    try:
        value = json.loads(
            body.decode("utf-8"),
            object_pairs_hook=_unique_object,
            parse_constant=_reject_constant,
        )
    except (UnicodeError, ValueError, RecursionError):
        raise SafetyError("Mutation journal is not valid strict JSON") from None
    if type(value) is not dict or set(value) != _JOURNAL_FIELDS:
        raise SafetyError("Mutation journal fields are invalid")
    run_id = _safe_id(value["run_id"], label="run ID")
    if run_id != expected_run_id:
        raise SafetyError("Mutation journal run ID does not match its filename")
    profile_fingerprint = _safe_id(
        value["profile_fingerprint"],
        label="profile fingerprint",
    )
    completed = value["completed"]
    cleanup = value["cleanup"]
    if type(completed) is not bool:
        raise SafetyError("Mutation journal completed flag must be a boolean")
    if type(cleanup) is not list or len(cleanup) > _MAX_ACTIONS:
        raise SafetyError("Mutation journal cleanup must be a bounded array")
    parsed_entries: list[dict[str, Any]] = []
    for entry in cleanup:
        if type(entry) is not dict or set(entry) != _ENTRY_FIELDS:
            raise SafetyError("Mutation journal cleanup entry fields are invalid")
        operation_id = _safe_id(entry["operation_id"], label="operation ID")
        done = entry["done"]
        if type(done) is not bool:
            raise SafetyError("Mutation journal cleanup done flag must be a boolean")
        parsed_entries.append(
            {
                "operation_id": operation_id,
                "payload": _detached_payload(entry["payload"]),
                "done": done,
            }
        )
    if completed and any(not entry["done"] for entry in parsed_entries):
        raise SafetyError("Completed mutation journal contains pending cleanup")
    parsed = {
        "run_id": run_id,
        "profile_fingerprint": profile_fingerprint,
        "completed": completed,
        "cleanup": parsed_entries,
    }
    try:
        canonical = canonical_json_bytes(parsed)
    except (TypeError, ValueError, OverflowError, RecursionError):
        raise SafetyError("Mutation journal is not valid strict JSON") from None
    if body != canonical:
        raise SafetyError("Mutation journal must use canonical JSON encoding")
    return parsed


class MutationJournal:
    """One private atomic cleanup stack for a single live write run."""

    def __init__(self, path: Path, document: dict[str, Any]) -> None:
        self.path = path
        self._document = document
        self._closed = False

    def __repr__(self) -> str:
        return f"{type(self).__name__}(pending_count={self.pending_count}, closed={self._closed})"

    @property
    def run_id(self) -> str:
        return self._document["run_id"]

    @property
    def profile_fingerprint(self) -> str:
        return self._document["profile_fingerprint"]

    @property
    def pending_count(self) -> int:
        return sum(not entry["done"] for entry in self._document["cleanup"])

    @property
    def completed(self) -> bool:
        return bool(self._document["completed"])

    @classmethod
    def create(
        cls,
        state_root: Path,
        run_id: str,
        profile_fingerprint: str,
    ) -> MutationJournal:
        if not isinstance(state_root, Path):
            raise SafetyError("Mutation state root must be a filesystem path")
        checked_run_id = _safe_id(run_id, label="run ID")
        checked_profile = _safe_id(profile_fingerprint, label="profile fingerprint")
        ensure_private_directory(state_root)
        directory = state_root / "mutations"
        ensure_private_directory(directory)
        path = directory / f"{checked_run_id}.json"
        if path.exists() or path.is_symlink():
            raise SafetyError("Mutation journal already exists for this run")
        journal = cls(
            path,
            {
                "run_id": checked_run_id,
                "profile_fingerprint": checked_profile,
                "completed": False,
                "cleanup": [],
            },
        )
        journal._persist()
        return journal

    @classmethod
    def load(
        cls,
        path: Path,
        *,
        expected_profile_fingerprint: str | None = None,
    ) -> MutationJournal:
        _state_root, expected_run_id = _journal_location(path)
        document = _parse_document(
            _read_private_journal(path),
            expected_run_id=expected_run_id,
        )
        if expected_profile_fingerprint is not None:
            expected = _safe_id(
                expected_profile_fingerprint,
                label="profile fingerprint",
            )
            if document["profile_fingerprint"] != expected:
                raise SafetyError("Mutation journal does not belong to the selected profile")
        return cls(path, document)

    def _persist(self) -> None:
        if self._closed:
            raise SafetyError("Mutation journal is already closed")
        try:
            body = canonical_json_bytes(self._document)
            if len(body) > _MAX_JOURNAL_BYTES:
                raise SafetyError("Mutation journal is too large")
            with_existing = self.path.exists() or self.path.is_symlink()
            if with_existing:
                validate_private_regular_file(self.path, label="Mutation journal")
            write_json_atomic(self.path, self._document, mode=0o600)
            validate_private_regular_file(self.path, label="Mutation journal")
            if _read_private_journal(self.path) != body:
                raise SafetyError("Mutation journal persistence verification failed")
        except Exception:
            raise SafetyError("Cannot persist mutation journal safely") from None

    def _assert_disk_matches(self) -> None:
        if self._closed:
            raise SafetyError("Mutation journal is already closed")
        body = _read_private_journal(self.path)
        if body != canonical_json_bytes(self._document):
            raise SafetyError("Mutation journal changed after planning")

    def register(self, operation_id: str, payload: dict[str, Any]) -> None:
        if self._closed or self.completed:
            raise SafetyError("Cannot register cleanup on a closed mutation journal")
        entry = {
            "operation_id": _safe_id(operation_id, label="operation ID"),
            "payload": _detached_payload(payload),
            "done": False,
        }
        entries: list[dict[str, Any]] = self._document["cleanup"]
        if len(entries) >= _MAX_ACTIONS:
            raise SafetyError("Mutation journal has too many cleanup actions")
        entries.append(entry)
        try:
            self._persist()
        except BaseException:
            entries.pop()
            raise

    async def cleanup(self, execute: CleanupExecutor) -> None:
        if self._closed:
            raise SafetyError("Mutation journal is already closed")
        if not callable(execute):
            raise SafetyError("Mutation cleanup executor must be callable")
        entries: list[dict[str, Any]] = self._document["cleanup"]
        for index in range(len(entries) - 1, -1, -1):
            entry = entries[index]
            if entry["done"]:
                continue
            try:
                await execute(
                    entry["operation_id"],
                    _detached_payload(entry["payload"]),
                )
            except Exception:
                with suppress(SafetyError):
                    self._persist()
                raise SafetyError("Mutation cleanup failed; journal retained") from None
            entry["done"] = True
            try:
                self._persist()
            except SafetyError:
                raise SafetyError(
                    "Mutation cleanup succeeded but progress could not be persisted; "
                    "journal retained"
                ) from None
        self._delete_completed()

    def _delete_completed(self) -> None:
        if self.pending_count != 0:
            raise SafetyError("Mutation journal still has pending cleanup")
        self._assert_disk_matches()
        try:
            self.path.unlink()
        except OSError:
            raise SafetyError("Completed mutation journal could not be removed") from None
        if self.path.exists() or self.path.is_symlink():
            raise SafetyError("Completed mutation journal still exists after removal")
        self._closed = True

    def _pending_operation_ids_lifo(self) -> tuple[str, ...]:
        return tuple(
            entry["operation_id"]
            for entry in reversed(self._document["cleanup"])
            if not entry["done"]
        )


@dataclass(frozen=True, slots=True)
class OrphanCleanupPlan:
    profile_fingerprint: str = field(repr=False)
    _journals: tuple[MutationJournal, ...] = field(repr=False)
    operation_ids: tuple[str, ...]

    @property
    def count(self) -> int:
        return len(self.operation_ids)

    @property
    def journal_count(self) -> int:
        return len(self._journals)

    def render(self) -> str:
        if self.count == 0:
            return "orphan cleanup plan: 0 actions"
        lines = [f"orphan cleanup plan: {self.count} actions across {self.journal_count} journals"]
        counts = Counter(self.operation_ids)
        lines.extend(
            f"- {operation_id}: {counts[operation_id]} action(s)"
            for operation_id in sorted(counts)
        )
        return "\n".join(lines)


def _journal_paths(state_root: Path) -> tuple[Path, ...]:
    if not isinstance(state_root, Path):
        raise SafetyError("Mutation state root must be a filesystem path")
    directory = state_root / "mutations"
    try:
        directory.lstat()
    except FileNotFoundError:
        return ()
    _private_directory(state_root, label="Mutation state directory")
    _private_directory(directory, label="Mutation journal directory")
    try:
        entries = tuple(sorted(directory.iterdir(), key=lambda path: path.name))
    except OSError:
        raise SafetyError("Cannot inspect mutation journal directory") from None
    for path in entries:
        if (
            path.parent != directory
            or path.suffix != ".json"
            or _SAFE_ID.fullmatch(path.stem) is None
        ):
            raise SafetyError("Mutation journal directory contains an unsafe entry")
    return entries


def plan_orphan_cleanup(
    state_root: Path,
    *,
    profile_fingerprint: str,
    operation_contract: Mapping[str, LiveOperation],
) -> OrphanCleanupPlan:
    selected_profile = _safe_id(profile_fingerprint, label="profile fingerprint")
    if not isinstance(operation_contract, Mapping):
        raise SafetyError("Live operation contract is invalid for orphan cleanup")
    selected: list[MutationJournal] = []
    operation_ids: list[str] = []
    for path in _journal_paths(state_root):
        journal = MutationJournal.load(path)
        if journal.profile_fingerprint != selected_profile:
            continue
        if journal.completed:
            raise SafetyError("Completed mutation journal residue requires manual review")
        pending = journal._pending_operation_ids_lifo()
        for operation_id in pending:
            operation = operation_contract.get(operation_id)
            if not isinstance(operation, LiveOperation) or operation.kind != "cleanup":
                raise SafetyError("Orphan operation is not explicitly classified as cleanup")
        selected.append(journal)
        operation_ids.extend(pending)
    return OrphanCleanupPlan(
        profile_fingerprint=selected_profile,
        _journals=tuple(selected),
        operation_ids=tuple(operation_ids),
    )


async def cleanup_orphans(
    state_root: Path,
    *,
    profile_fingerprint: str,
    operation_contract: Mapping[str, LiveOperation],
    reserve_budget: BudgetReservation,
    execute: CleanupExecutor,
    confirm: Confirmation,
    emit: Emitter,
) -> int:
    plan = plan_orphan_cleanup(
        state_root,
        profile_fingerprint=profile_fingerprint,
        operation_contract=operation_contract,
    )
    try:
        emit(plan.render())
    except Exception:
        raise SafetyError("Cannot render orphan cleanup plan safely") from None
    if plan.journal_count == 0:
        return 0
    if not callable(reserve_budget):
        raise SafetyError("Orphan cleanup budget reservation must be callable")
    try:
        for operation_id in plan.operation_ids:
            budget = reserve_budget(operation_id)
            if (
                type(budget) is not OperationBudget
                or budget.operation_id != operation_id
                or type(budget.safe_interval_seconds) is not float
                or not math.isfinite(budget.safe_interval_seconds)
                or budget.safe_interval_seconds < 30
                or type(budget.max_calls_per_run) is not int
                or budget.max_calls_per_run != 1
            ):
                raise SafetyError("Invalid orphan cleanup budget reservation")
    except Exception:
        raise SafetyError("Cannot reserve every cleanup budget before execution") from None
    if not callable(confirm):
        raise SafetyError("Orphan cleanup confirmation must be callable")
    try:
        answer = confirm(f"cleanup {plan.count} actions [y/N]")
    except Exception:
        raise SafetyError("Orphan cleanup confirmation failed") from None
    if not isinstance(answer, str) or answer.strip().lower() != "y":
        raise SafetyError("Orphan cleanup was not confirmed")
    for journal in plan._journals:
        journal._assert_disk_matches()
    for journal in plan._journals:
        await journal.cleanup(execute)
    return plan.count
