from __future__ import annotations

import json
import os
import re
import stat
from collections.abc import Mapping
from contextlib import suppress
from dataclasses import dataclass, replace
from datetime import datetime, timezone
from enum import Enum
from pathlib import Path
from types import MappingProxyType
from typing import Any
from urllib.parse import unquote, urlsplit

from ..errors import SafetyError
from ..io import canonical_json_bytes, write_json_atomic
from .read_case import NoLiveTargetCode, ReadFailureCode

_OPERATION_ID = re.compile(r"[A-Za-z0-9][A-Za-z0-9_.:-]{0,127}\Z")
_RUN_ID = re.compile(r"[0-9]{8}T[0-9]{6}Z-[a-f0-9]{8,32}\Z")
_SHA256 = re.compile(r"[a-f0-9]{64}\Z")
_TIMESTAMP = re.compile(r"[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z\Z")
_METHODS = frozenset({"GET", "POST"})
_REPORT_FIELDS = {
    "version",
    "run_id",
    "profile_fingerprint",
    "effective_schema_sha256",
    "generated_tree_sha256",
    "live_contracts_sha256",
    "registry_sha256",
    "started_at",
    "finished_at",
    "completed",
    "outcomes",
    "counts",
}
_OUTCOME_FIELDS = {
    "operation_id",
    "method",
    "path",
    "status",
    "reason",
    "http_status",
    "duration_ms",
}
_MAX_REPORT_BYTES = 1024 * 1024
_DIRECTORY_FLAGS = (
    os.O_RDONLY | os.O_CLOEXEC | os.O_DIRECTORY | getattr(os, "O_NOFOLLOW", 0)
)
_READ_FLAGS = (
    os.O_RDONLY
    | os.O_CLOEXEC
    | getattr(os, "O_NOFOLLOW", 0)
    | getattr(os, "O_NONBLOCK", 0)
)


class ReadStatus(str, Enum):
    PASSED = "passed"
    NO_LIVE_TARGET = "no_live_target"
    FAILED = "failed"
    ABORTED = "aborted"


_COUNT_FIELDS = tuple(status.value for status in ReadStatus)


@dataclass(frozen=True, slots=True)
class ReadOutcome:
    operation_id: str
    method: str
    path: str
    status: ReadStatus
    reason: str | None
    http_status: int | None
    duration_ms: int | None

    def __post_init__(self) -> None:
        if (
            type(self.operation_id) is not str
            or _OPERATION_ID.fullmatch(self.operation_id) is None
        ):
            raise SafetyError("Read outcome operation ID is invalid")
        if type(self.method) is not str or self.method not in _METHODS:
            raise SafetyError("Read outcome method must be uppercase GET or POST")
        _validate_path(self.path)
        if type(self.status) is not ReadStatus:
            raise SafetyError("Read outcome status is invalid")
        _validate_reason(self.status, self.reason)
        if self.http_status is not None and (
            type(self.http_status) is not int or not 100 <= self.http_status <= 599
        ):
            raise SafetyError("Read outcome HTTP status must be an integer from 100 to 599")
        if self.duration_ms is not None and (
            type(self.duration_ms) is not int or self.duration_ms < 0
        ):
            raise SafetyError("Read outcome duration must be a non-negative integer")

    def to_json(self) -> dict[str, Any]:
        return {
            "operation_id": self.operation_id,
            "method": self.method,
            "path": self.path,
            "status": self.status.value,
            "reason": self.reason,
            "http_status": self.http_status,
            "duration_ms": self.duration_ms,
        }


def _validate_path(value: object) -> None:
    if (
        type(value) is not str
        or not value.startswith("/")
        or value.startswith("//")
        or len(value) > 2048
        or "\\" in value
        or "{" in value
        or "}" in value
        or any(ord(character) < 32 or ord(character) == 127 for character in value)
    ):
        raise SafetyError("Read outcome path is unsafe")
    parsed = urlsplit(value)
    decoded = unquote(value)
    if (
        parsed.scheme
        or parsed.netloc
        or parsed.query
        or parsed.fragment
        or parsed.path != value
        or any(character in decoded for character in ("?", "#", "\\"))
        or any(segment in {"", ".", ".."} for segment in decoded.split("/")[1:])
    ):
        raise SafetyError("Read outcome path must be a query-free relative path")


def _validate_reason(status: ReadStatus, reason: object) -> None:
    allowed: set[str | None]
    if status is ReadStatus.PASSED:
        allowed = {None}
    elif status is ReadStatus.NO_LIVE_TARGET:
        allowed = {code.value for code in NoLiveTargetCode}
    elif status is ReadStatus.FAILED:
        allowed = {
            ReadFailureCode.ASSERTION_FAILED.value,
            ReadFailureCode.EXTRACTOR_FAILED.value,
        }
    else:
        allowed = {
            code.value
            for code in ReadFailureCode
            if code
            not in {
                ReadFailureCode.ASSERTION_FAILED,
                ReadFailureCode.EXTRACTOR_FAILED,
            }
        }
    if reason not in allowed or (reason is not None and type(reason) is not str):
        raise SafetyError("Read outcome reason is incompatible with its status")


def _unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    value: dict[str, Any] = {}
    for key, item in pairs:
        if key in value:
            raise ValueError("duplicate JSON key")
        value[key] = item
    return value


def _reject_constant(value: str) -> None:
    raise ValueError(f"non-finite JSON number {value}")


def _validated_timestamp(value: object, *, label: str) -> str:
    if type(value) is not str or _TIMESTAMP.fullmatch(value) is None:
        raise SafetyError(f"Read report {label} is invalid")
    try:
        datetime.strptime(value, "%Y-%m-%dT%H:%M:%SZ")
    except ValueError as error:
        raise SafetyError(f"Read report {label} is invalid") from error
    return value


def _outcome_from_json(value: object) -> ReadOutcome:
    if not isinstance(value, dict) or set(value) != _OUTCOME_FIELDS:
        raise SafetyError("Read report outcome fields are invalid")
    raw_status = value["status"]
    if type(raw_status) is not str:
        raise SafetyError("Read outcome status is invalid")
    try:
        status = ReadStatus(raw_status)
    except ValueError as error:
        raise SafetyError("Read outcome status is invalid") from error
    return ReadOutcome(
        operation_id=value["operation_id"],
        method=value["method"],
        path=value["path"],
        status=status,
        reason=value["reason"],
        http_status=value["http_status"],
        duration_ms=value["duration_ms"],
    )


@dataclass(frozen=True, slots=True)
class ReadReport:
    version: int
    run_id: str
    profile_fingerprint: str
    effective_schema_sha256: str
    generated_tree_sha256: str
    live_contracts_sha256: str
    registry_sha256: str
    started_at: str
    finished_at: str | None
    completed: bool
    outcomes: tuple[ReadOutcome, ...]
    counts: Mapping[str, int]

    def __post_init__(self) -> None:
        if type(self.version) is not int or self.version != 1:
            raise SafetyError("Read report version must be the integer 1")
        if type(self.run_id) is not str or _RUN_ID.fullmatch(self.run_id) is None:
            raise SafetyError("Read report run_id is invalid")
        for label, digest in (
            ("profile fingerprint", self.profile_fingerprint),
            ("effective schema hash", self.effective_schema_sha256),
            ("generated tree hash", self.generated_tree_sha256),
            ("live contracts hash", self.live_contracts_sha256),
            ("registry hash", self.registry_sha256),
        ):
            if type(digest) is not str or _SHA256.fullmatch(digest) is None:
                raise SafetyError(f"Read report {label} is invalid")
        started = _validated_timestamp(self.started_at, label="started_at")
        if self.finished_at is not None:
            finished = _validated_timestamp(self.finished_at, label="finished_at")
            if finished < started:
                raise SafetyError("Read report finished_at precedes started_at")
        if type(self.completed) is not bool:
            raise SafetyError("Read report completed flag must be a boolean")
        if not isinstance(self.outcomes, tuple) or any(
            type(outcome) is not ReadOutcome for outcome in self.outcomes
        ):
            raise SafetyError("Read report outcomes must be a tuple of ReadOutcome values")
        operation_ids = tuple(outcome.operation_id for outcome in self.outcomes)
        if len(set(operation_ids)) != len(operation_ids):
            raise SafetyError("Read report contains a duplicate operation outcome")
        if not isinstance(self.counts, Mapping) or set(self.counts) != set(_COUNT_FIELDS):
            raise SafetyError("Read report counts fields are invalid")
        normalized_counts: dict[str, int] = {}
        for status in _COUNT_FIELDS:
            count = self.counts[status]
            if type(count) is not int or count < 0:
                raise SafetyError("Read report counts must be non-negative integers")
            normalized_counts[status] = count
        expected_counts = {
            status.value: sum(outcome.status is status for outcome in self.outcomes)
            for status in ReadStatus
        }
        if normalized_counts != expected_counts:
            raise SafetyError("Read report counts do not match outcomes")
        object.__setattr__(self, "counts", MappingProxyType(normalized_counts))
        if self.completed:
            if self.finished_at is None:
                raise SafetyError("A completed read report requires finished_at")
            if (
                normalized_counts[ReadStatus.PASSED.value] < 1
                or normalized_counts[ReadStatus.FAILED.value] != 0
                or normalized_counts[ReadStatus.ABORTED.value] != 0
            ):
                raise SafetyError("A completed read report must be successful")

    def to_json(self) -> dict[str, Any]:
        return {
            "version": self.version,
            "run_id": self.run_id,
            "profile_fingerprint": self.profile_fingerprint,
            "effective_schema_sha256": self.effective_schema_sha256,
            "generated_tree_sha256": self.generated_tree_sha256,
            "live_contracts_sha256": self.live_contracts_sha256,
            "registry_sha256": self.registry_sha256,
            "started_at": self.started_at,
            "finished_at": self.finished_at,
            "completed": self.completed,
            "outcomes": [outcome.to_json() for outcome in self.outcomes],
            "counts": dict(self.counts),
        }

    def matches(
        self,
        run_id: str,
        profile_fingerprint: str,
        effective_schema_sha256: str,
        generated_tree_sha256: str,
        live_contracts_sha256: str,
        registry_sha256: str,
    ) -> bool:
        return (
            self.completed
            and self.run_id == run_id
            and self.profile_fingerprint == profile_fingerprint
            and self.effective_schema_sha256 == effective_schema_sha256
            and self.generated_tree_sha256 == generated_tree_sha256
            and self.live_contracts_sha256 == live_contracts_sha256
            and self.registry_sha256 == registry_sha256
        )

    @classmethod
    def from_bytes(cls, body: bytes) -> ReadReport:
        if type(body) is not bytes:
            raise SafetyError("Read report body must be bytes")
        if len(body) > _MAX_REPORT_BYTES:
            raise SafetyError("Read report is too large")
        try:
            value = json.loads(
                body.decode("utf-8"),
                object_pairs_hook=_unique_object,
                parse_constant=_reject_constant,
            )
        except (UnicodeError, ValueError) as error:
            raise SafetyError("Read report is not valid strict JSON") from error
        if not isinstance(value, dict) or set(value) != _REPORT_FIELDS:
            raise SafetyError("Read report fields are invalid")
        if body != canonical_json_bytes(value):
            raise SafetyError("Read report must use canonical JSON encoding")
        raw_outcomes = value["outcomes"]
        if not isinstance(raw_outcomes, list):
            raise SafetyError("Read report outcomes must be an array")
        raw_counts = value["counts"]
        if not isinstance(raw_counts, dict):
            raise SafetyError("Read report counts must be an object")
        return cls(
            version=value["version"],
            run_id=value["run_id"],
            profile_fingerprint=value["profile_fingerprint"],
            effective_schema_sha256=value["effective_schema_sha256"],
            generated_tree_sha256=value["generated_tree_sha256"],
            live_contracts_sha256=value["live_contracts_sha256"],
            registry_sha256=value["registry_sha256"],
            started_at=value["started_at"],
            finished_at=value["finished_at"],
            completed=value["completed"],
            outcomes=tuple(_outcome_from_json(item) for item in raw_outcomes),
            counts=raw_counts,
        )


def _same_identity(left: os.stat_result, right: os.stat_result) -> bool:
    return (left.st_dev, left.st_ino) == (right.st_dev, right.st_ino)


def _directory_metadata(value: os.stat_result) -> tuple[int, ...]:
    return (
        value.st_dev,
        value.st_ino,
        value.st_mode,
        value.st_uid,
        value.st_gid,
        value.st_nlink,
    )


def _file_metadata(value: os.stat_result) -> tuple[int, ...]:
    return (
        value.st_dev,
        value.st_ino,
        value.st_mode,
        value.st_uid,
        value.st_gid,
        value.st_nlink,
        value.st_size,
    )


def _close_fd(fd: int | None) -> None:
    if fd is not None:
        with suppress(OSError):
            os.close(fd)


def _validate_private_directory_fd(fd: int, *, label: str) -> os.stat_result:
    metadata = os.fstat(fd)
    if not stat.S_ISDIR(metadata.st_mode):
        raise SafetyError(f"{label} is not a directory")
    if stat.S_IMODE(metadata.st_mode) != 0o700:
        raise SafetyError(f"{label} must have mode 0700")
    if metadata.st_uid != os.getuid():
        raise SafetyError(f"{label} must be owned by the current user")
    return metadata


def _validate_private_file_metadata(
    metadata: os.stat_result, *, label: str
) -> None:
    if not stat.S_ISREG(metadata.st_mode):
        raise SafetyError(f"{label} must be a regular non-symlink file")
    if stat.S_IMODE(metadata.st_mode) != 0o600:
        raise SafetyError(f"{label} must have mode 0600")
    if metadata.st_uid != os.getuid():
        raise SafetyError(f"{label} must be owned by the current user")
    if metadata.st_nlink != 1:
        raise SafetyError(f"{label} must not have multiple hard links")
    if metadata.st_size > _MAX_REPORT_BYTES:
        raise SafetyError("Read report is too large")


def _absolute_private_root(path: Path) -> Path:
    if not isinstance(path, Path):
        raise SafetyError("Read report private root must be a filesystem path")
    if any(part in {"", ".", ".."} for part in path.parts):
        raise SafetyError("Read report private root must be canonical")
    absolute = Path(os.path.abspath(path))
    if absolute.name != "private" or not absolute.is_absolute():
        raise SafetyError("Read report private root must be the canonical private directory")
    return absolute


def _open_private_root(path: Path) -> int:
    if getattr(os, "O_NOFOLLOW", 0) == 0:
        raise SafetyError("Secure read report directory traversal is unavailable")
    components = path.parts[1:]
    if not components:
        raise SafetyError("Read report private root must be canonical")
    try:
        current_fd = os.open("/", _DIRECTORY_FLAGS)
    except OSError as error:
        raise SafetyError("Cannot open read report filesystem root safely") from error
    try:
        for index, component in enumerate(components):
            try:
                expected = os.stat(component, dir_fd=current_fd, follow_symlinks=False)
                if stat.S_ISLNK(expected.st_mode) or not stat.S_ISDIR(expected.st_mode):
                    raise SafetyError("Read report ancestry contains an unsafe component")
                next_fd = os.open(component, _DIRECTORY_FLAGS, dir_fd=current_fd)
                actual = os.fstat(next_fd)
                if not _same_identity(expected, actual):
                    raise SafetyError("Read report ancestry changed during traversal")
                if index == len(components) - 1:
                    _validate_private_directory_fd(
                        next_fd,
                        label="Read report private root",
                    )
            except OSError as error:
                raise SafetyError("Read report ancestry contains an unsafe component") from error
            _close_fd(current_fd)
            current_fd = next_fd
        return current_fd
    except BaseException:
        _close_fd(current_fd)
        raise


def _open_private_child(parent_fd: int, name: str, *, create: bool) -> int:
    if create:
        try:
            os.mkdir(name, 0o700, dir_fd=parent_fd)
        except FileExistsError:
            pass
        except OSError as error:
            raise SafetyError("Cannot create private read report directory") from error
        else:
            os.fsync(parent_fd)
    try:
        expected = os.stat(name, dir_fd=parent_fd, follow_symlinks=False)
        if stat.S_ISLNK(expected.st_mode):
            raise SafetyError("Read report ancestry contains a symlink")
        child_fd = os.open(name, _DIRECTORY_FLAGS, dir_fd=parent_fd)
        actual = _validate_private_directory_fd(
            child_fd,
            label="Private read report directory",
        )
        if not _same_identity(expected, actual):
            raise SafetyError("Read report ancestry changed during traversal")
        return child_fd
    except SafetyError:
        raise
    except OSError as error:
        raise SafetyError("Read report ancestry is not a safe private directory") from error


def _open_report_directory(private_root: Path, *, create: bool) -> int:
    private_fd: int | None = None
    reports_fd: int | None = None
    try:
        private_fd = _open_private_root(private_root)
        reports_fd = _open_private_child(private_fd, "reports", create=create)
        live_read_fd = _open_private_child(reports_fd, "live-read", create=create)
        return live_read_fd
    finally:
        _close_fd(reports_fd)
        _close_fd(private_fd)


def _read_report_at(directory_fd: int, name: str) -> tuple[bytes, tuple[int, ...]]:
    try:
        expected = os.stat(name, dir_fd=directory_fd, follow_symlinks=False)
        if stat.S_ISLNK(expected.st_mode):
            raise SafetyError("Read report leaf is a symlink")
        _validate_private_file_metadata(expected, label="Read report file")
        fd = os.open(name, _READ_FLAGS, dir_fd=directory_fd)
    except SafetyError:
        raise
    except OSError as error:
        raise SafetyError("Cannot open read report safely") from error
    try:
        opened = os.fstat(fd)
        _validate_private_file_metadata(opened, label="Read report file")
        if _file_metadata(expected) != _file_metadata(opened):
            raise SafetyError("Read report file changed while it was opened")
        chunks: list[bytes] = []
        remaining = _MAX_REPORT_BYTES + 1
        while remaining > 0:
            chunk = os.read(fd, min(65536, remaining))
            if not chunk:
                break
            chunks.append(chunk)
            remaining -= len(chunk)
        body = b"".join(chunks)
        if len(body) > _MAX_REPORT_BYTES:
            raise SafetyError("Read report is too large")
        after = os.fstat(fd)
        current = os.stat(name, dir_fd=directory_fd, follow_symlinks=False)
        if not (
            _file_metadata(opened) == _file_metadata(after)
            and _file_metadata(after) == _file_metadata(current)
        ):
            raise SafetyError("Read report file changed while it was read")
        return body, _file_metadata(current)
    except OSError as error:
        raise SafetyError("Cannot read report safely") from error
    finally:
        os.close(fd)


def _create_report_at(directory_fd: int, name: str, body: bytes) -> tuple[int, ...]:
    flags = (
        os.O_WRONLY
        | os.O_CREAT
        | os.O_EXCL
        | os.O_CLOEXEC
        | getattr(os, "O_NOFOLLOW", 0)
    )
    try:
        fd = os.open(name, flags, 0o600, dir_fd=directory_fd)
    except FileExistsError as error:
        raise SafetyError("Read report file already exists") from error
    except OSError as error:
        raise SafetyError("Cannot create read report safely") from error
    try:
        os.fchmod(fd, 0o600)
        offset = 0
        while offset < len(body):
            written = os.write(fd, body[offset:])
            if written <= 0:
                raise OSError("short read report write")
            offset += written
        os.fsync(fd)
        metadata = os.fstat(fd)
        _validate_private_file_metadata(metadata, label="Read report file")
    except OSError as error:
        raise SafetyError("Cannot create read report safely") from error
    finally:
        os.close(fd)
    os.fsync(directory_fd)
    return _file_metadata(metadata)


def _counts(outcomes: tuple[ReadOutcome, ...]) -> dict[str, int]:
    return {
        status.value: sum(outcome.status is status for outcome in outcomes)
        for status in ReadStatus
    }


def _utc_timestamp() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


class ReadReportWriter:
    """Create and update one credential-free report in bound private storage."""

    def __init__(
        self,
        *,
        private_root: Path,
        path: Path,
        report: ReadReport,
        body: bytes,
        directory_metadata: tuple[int, ...],
        file_metadata: tuple[int, ...],
    ) -> None:
        self.private_root = private_root
        self.path = path
        self._report = report
        self._last_body = body
        self._directory_metadata = directory_metadata
        self._file_metadata = file_metadata

    @classmethod
    def create(
        cls,
        private_root: Path,
        *,
        run_id: str,
        profile_fingerprint: str,
        effective_schema_sha256: str,
        generated_tree_sha256: str,
        live_contracts_sha256: str,
        registry_sha256: str,
        started_at: str | None = None,
    ) -> ReadReportWriter:
        root = _absolute_private_root(private_root)
        report = ReadReport(
            version=1,
            run_id=run_id,
            profile_fingerprint=profile_fingerprint,
            effective_schema_sha256=effective_schema_sha256,
            generated_tree_sha256=generated_tree_sha256,
            live_contracts_sha256=live_contracts_sha256,
            registry_sha256=registry_sha256,
            started_at=_utc_timestamp() if started_at is None else started_at,
            finished_at=None,
            completed=False,
            outcomes=(),
            counts=_counts(()),
        )
        body = canonical_json_bytes(report.to_json())
        name = f"{report.run_id}.json"
        directory_fd: int | None = None
        try:
            directory_fd = _open_report_directory(root, create=True)
            directory_metadata = _directory_metadata(
                _validate_private_directory_fd(
                    directory_fd,
                    label="Private read report directory",
                )
            )
            _create_report_at(directory_fd, name, body)
        finally:
            _close_fd(directory_fd)

        reopened_fd: int | None = None
        try:
            reopened_fd = _open_report_directory(root, create=False)
            reopened_directory = _directory_metadata(
                _validate_private_directory_fd(
                    reopened_fd,
                    label="Private read report directory",
                )
            )
            if reopened_directory != directory_metadata:
                raise SafetyError("Read report ancestry changed during creation")
            reopened_body, file_metadata = _read_report_at(reopened_fd, name)
            if reopened_body != body or ReadReport.from_bytes(reopened_body) != report:
                raise SafetyError("Created read report does not match canonical content")
        finally:
            _close_fd(reopened_fd)
        return cls(
            private_root=root,
            path=root / "reports" / "live-read" / name,
            report=report,
            body=body,
            directory_metadata=directory_metadata,
            file_metadata=file_metadata,
        )

    def _open_bound_directory(self) -> int:
        directory_fd = _open_report_directory(self.private_root, create=False)
        try:
            metadata = _directory_metadata(
                _validate_private_directory_fd(
                    directory_fd,
                    label="Private read report directory",
                )
            )
            if metadata != self._directory_metadata:
                raise SafetyError("Read report ancestry changed after creation")
            return directory_fd
        except BaseException:
            _close_fd(directory_fd)
            raise

    def load_and_verify(self) -> ReadReport:
        directory_fd: int | None = None
        try:
            directory_fd = self._open_bound_directory()
            body, metadata = _read_report_at(directory_fd, self.path.name)
        finally:
            _close_fd(directory_fd)
        if metadata != self._file_metadata or body != self._last_body:
            raise SafetyError("Read report changed since its last verified update")
        loaded = ReadReport.from_bytes(body)
        if loaded != self._report:
            raise SafetyError("Read report does not match writer state")
        return loaded

    def _publish(self, report: ReadReport) -> ReadReport:
        body = canonical_json_bytes(report.to_json())
        directory_fd: int | None = None
        try:
            directory_fd = self._open_bound_directory()
            current_body, current_metadata = _read_report_at(
                directory_fd,
                self.path.name,
            )
            if current_metadata != self._file_metadata or current_body != self._last_body:
                raise SafetyError("Read report changed before update")
            if ReadReport.from_bytes(current_body) != self._report:
                raise SafetyError("Read report does not match writer state")
            bound_path = Path(f"/proc/self/fd/{directory_fd}") / self.path.name
            write_json_atomic(bound_path, report.to_json(), mode=0o600)
            updated_body, updated_metadata = _read_report_at(
                directory_fd,
                self.path.name,
            )
            if updated_body != body or ReadReport.from_bytes(updated_body) != report:
                raise SafetyError("Atomic read report update did not publish canonical content")
        finally:
            _close_fd(directory_fd)

        reopened_fd: int | None = None
        try:
            reopened_fd = self._open_bound_directory()
            reopened_body, reopened_metadata = _read_report_at(
                reopened_fd,
                self.path.name,
            )
            if reopened_body != body or reopened_metadata != updated_metadata:
                raise SafetyError("Read report changed during reopen verification")
            if ReadReport.from_bytes(reopened_body) != report:
                raise SafetyError("Reopened read report does not match canonical content")
        finally:
            _close_fd(reopened_fd)
        self._report = report
        self._last_body = body
        self._file_metadata = reopened_metadata
        return report

    def append(self, outcome: ReadOutcome) -> ReadReport:
        if type(outcome) is not ReadOutcome:
            raise SafetyError("Read report append requires a ReadOutcome")
        if self._report.finished_at is not None:
            raise SafetyError("Cannot append to a finished read report")
        outcomes = (*self._report.outcomes, outcome)
        return self._publish(
            replace(
                self._report,
                outcomes=outcomes,
                counts=_counts(outcomes),
            )
        )

    def finish(
        self,
        success: bool,
        *,
        finished_at: str | None = None,
    ) -> ReadReport:
        if type(success) is not bool:
            raise SafetyError("Read report finish success flag must be a boolean")
        if self._report.finished_at is not None:
            raise SafetyError("Read report is already finished")
        return self._publish(
            replace(
                self._report,
                finished_at=_utc_timestamp() if finished_at is None else finished_at,
                completed=success,
            )
        )
