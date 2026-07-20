from __future__ import annotations

import hashlib
import inspect
import json
import math
import os
import re
import stat
import unicodedata
from collections.abc import Callable, Mapping
from contextlib import suppress
from dataclasses import dataclass
from pathlib import Path
from types import MappingProxyType
from typing import Any, cast

from .capture import EMAIL_KEYS, PHONE_KEYS, SECRET_KEYS
from .errors import SafetyError
from .evidence_validation import MenuEvidenceValidator
from .io import canonical_json_bytes
from .live.lock import LiveProcessLock

_APPROVED_OPERATION = "get_external_menu_by_id"
_APPROVED_VERSIONS = frozenset({2, 3, 4})
_EXPECTED_OPERATION_ENTRIES = ("request.json", "response.json")
_MAX_CAPTURE_BYTES = 32 * 1024 * 1024
_MAX_JSON_DEPTH = 64
_CAPTURE_ID = re.compile(r"[A-Za-z0-9][A-Za-z0-9_.:-]{0,127}\Z")
_SHA256 = re.compile(r"[a-f0-9]{64}\Z")
_JWT = re.compile(
    r"(?<![A-Za-z0-9_-])[A-Za-z0-9_-]{8,}\.[A-Za-z0-9_-]{8,}\."
    r"[A-Za-z0-9_-]{8,}(?![A-Za-z0-9_-])"
)
_BEARER = re.compile(r"\bbearer\s+\S+", re.IGNORECASE)
_EMAIL = re.compile(r"(?<![\w.+-])[\w.+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}(?!\w)")
_PHONE = re.compile(r"(?<!\w)\+?\d(?:[ ().-]*\d){9,14}(?!\w)")
_UUID_ANY = re.compile(
    r"[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-5][0-9a-fA-F]{3}-"
    r"[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}"
)
_UUID_LIKE_KEY = re.compile(
    r"[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-"
    r"[0-9a-fA-F]{4}-[0-9a-fA-F]{12}"
)
_SAFE_REDACTIONS = frozenset(
    {
        "<redacted:email>",
        "<redacted:phone>",
        "<redacted:secret>",
        "<redacted:string>",
    }
)
_ALLOWED_METADATA_FIELDS = frozenset(
    {"method", "operationId", "path", "runId", "status", "duration", "headers"}
)
_REQUIRED_METADATA_FIELDS = frozenset({"method", "operationId", "path", "runId", "status"})
_ALLOWED_HEADERS = frozenset({"accept", "content-type", "x-correlation-id"})
_DIRECTORY_FLAGS = os.O_RDONLY | os.O_CLOEXEC | os.O_DIRECTORY | getattr(os, "O_NOFOLLOW", 0)
_FILE_FLAGS = (
    os.O_RDONLY | os.O_CLOEXEC | getattr(os, "O_NOFOLLOW", 0) | getattr(os, "O_NONBLOCK", 0)
)

FrozenJson = (
    None | bool | int | float | str | tuple["FrozenJson", ...] | Mapping[str, "FrozenJson"]
)


@dataclass(frozen=True)
class EvidencePair:
    """One deeply immutable, provenance-bound sanitized capture pair."""

    version: int
    request: Mapping[str, FrozenJson]
    response: Mapping[str, FrozenJson]
    request_sha256: str
    response_sha256: str

    def __post_init__(self) -> None:
        if type(self.version) is not int or self.version not in _APPROVED_VERSIONS:
            raise SafetyError("Evidence pair version must be exactly 2, 3, or 4")
        if not isinstance(self.request, Mapping) or not isinstance(self.response, Mapping):
            raise SafetyError("Evidence pair envelopes must be immutable mappings")
        object.__setattr__(self, "request", _freeze_mapping(self.request))
        object.__setattr__(self, "response", _freeze_mapping(self.response))
        if (
            type(self.request_sha256) is not str
            or _SHA256.fullmatch(self.request_sha256) is None
            or type(self.response_sha256) is not str
            or _SHA256.fullmatch(self.response_sha256) is None
        ):
            raise SafetyError("Evidence pair hashes are invalid")


class CaptureEvidenceReader:
    """Read sanitized menu captures while the caller holds the canonical live lock.

    Lock creation belongs to the promotion orchestration layer. Keeping it outside this
    reader makes a successful read free of filesystem mutations, while the mandatory
    injected lock prevents promotion code from accidentally omitting live coordination.
    """

    def __init__(
        self,
        repository_root: Path,
        effective_schema: dict[str, Any],
        operation: str = _APPROVED_OPERATION,
        *,
        process_lock: LiveProcessLock | None = None,
    ) -> None:
        self.repository_root = _validate_canonical_repository_root(repository_root)
        self.root = self.repository_root / "private/captures"
        self.operation = operation
        self.process_lock = process_lock
        self._validator = MenuEvidenceValidator(effective_schema)

    def read_menu_pairs(self) -> Mapping[int, EvidencePair]:
        lock = self.process_lock
        _validate_canonical_lock(self.repository_root, lock)
        assert lock is not None
        binding_token = lock.capture_binding_token()
        if self.operation != _APPROVED_OPERATION:
            raise SafetyError("Evidence operation is not explicitly approved")
        _validate_canonical_capture_root(self.repository_root, self.root)

        root_fd: int | None = None
        reopened_root_fd: int | None = None
        try:
            root_fd = _open_absolute_private_root(self.root)
            root_metadata = os.fstat(root_fd)
            root_entries = _directory_entries(root_fd)
            run_snapshots: dict[
                str,
                tuple[os.stat_result, tuple[str, ...], os.stat_result | None],
            ] = {}
            collected: dict[int, EvidencePair] = {}

            for run_id in root_entries:
                if _CAPTURE_ID.fullmatch(run_id) is None:
                    raise SafetyError("Evidence capture run ID is unsafe")
                run_fd = _open_private_child(root_fd, run_id, label="Evidence run")
                try:
                    run_metadata = os.fstat(run_fd)
                    run_entries = _directory_entries(run_fd)
                    selected_metadata: os.stat_result | None = None
                    for entry in run_entries:
                        if _CAPTURE_ID.fullmatch(entry) is None:
                            raise SafetyError("Evidence operation directory name is unsafe")
                        operation_fd = _open_private_child(
                            run_fd,
                            entry,
                            label="Evidence operation",
                        )
                        try:
                            if entry == self.operation:
                                selected_metadata = os.fstat(operation_fd)
                        finally:
                            os.close(operation_fd)

                    if selected_metadata is not None:
                        selected_fd = _open_private_child(
                            run_fd,
                            self.operation,
                            label="Evidence operation",
                        )
                        try:
                            if not _same_stable_metadata(
                                selected_metadata,
                                os.fstat(selected_fd),
                            ):
                                raise SafetyError(
                                    "Evidence operation changed during concurrent read"
                                )
                            pair = self._read_pair(selected_fd, run_id)
                        finally:
                            os.close(selected_fd)
                        if pair.version in collected:
                            raise SafetyError(
                                f"Evidence contains duplicate capture for version {pair.version}"
                            )
                        collected[pair.version] = pair

                    _revalidate_directory_at(
                        root_fd,
                        run_id,
                        run_fd,
                        run_metadata,
                        run_entries,
                        label="Evidence run",
                    )
                    run_snapshots[run_id] = (run_metadata, run_entries, selected_metadata)
                finally:
                    os.close(run_fd)

            reopened_root_fd = _open_absolute_private_root(self.root)
            if not _same_stable_metadata(root_metadata, os.fstat(reopened_root_fd)):
                raise SafetyError("Evidence capture root changed during concurrent read")
            if _directory_entries(reopened_root_fd) != root_entries:
                raise SafetyError("Evidence capture root entries changed during concurrent read")
            for run_id, (run_metadata, run_entries, operation_metadata) in run_snapshots.items():
                run_fd = _open_private_child(reopened_root_fd, run_id, label="Evidence run")
                try:
                    if not _same_stable_metadata(run_metadata, os.fstat(run_fd)):
                        raise SafetyError("Evidence run changed during concurrent read")
                    if _directory_entries(run_fd) != run_entries:
                        raise SafetyError("Evidence run entries changed during concurrent read")
                    if operation_metadata is not None:
                        operation_fd = _open_private_child(
                            run_fd,
                            self.operation,
                            label="Evidence operation",
                        )
                        try:
                            if not _same_stable_metadata(
                                operation_metadata,
                                os.fstat(operation_fd),
                            ):
                                raise SafetyError(
                                    "Evidence operation changed during concurrent read"
                                )
                        finally:
                            os.close(operation_fd)
                finally:
                    os.close(run_fd)

            if set(collected) != _APPROVED_VERSIONS or len(collected) != 3:
                raise SafetyError("Evidence requires exactly one capture for versions 2, 3, and 4")
            for version in sorted(collected):
                pair = collected[version]
                try:
                    validate = cast(
                        Callable[[int, Mapping[str, Any], Mapping[str, Any]], object],
                        self._validator.validate,
                    )
                    result = validate(
                        version,
                        pair.request,
                        pair.response,
                    )
                except SafetyError:
                    raise
                except Exception:
                    raise SafetyError(
                        "Evidence schema validator rejected a capture pair"
                    ) from None
                _require_synchronous_none(result)
            lock.assert_binding_token(binding_token)
            return MappingProxyType(dict(sorted(collected.items())))
        finally:
            _close_fd(reopened_root_fd)
            _close_fd(root_fd)

    def _read_pair(self, operation_fd: int, run_id: str) -> EvidencePair:
        operation_metadata = os.fstat(operation_fd)
        entries = _directory_entries(operation_fd)
        if entries != _EXPECTED_OPERATION_ENTRIES:
            raise SafetyError(
                "Evidence operation directory must contain exactly request.json and response.json"
            )

        request_bytes = _read_private_file(operation_fd, "request.json")
        response_bytes = _read_private_file(operation_fd, "response.json")
        if _directory_entries(operation_fd) != entries:
            raise SafetyError("Evidence operation entries changed during concurrent read")
        if not _same_stable_metadata(operation_metadata, os.fstat(operation_fd)):
            raise SafetyError("Evidence operation changed during concurrent read")

        request = _load_strict_canonical_json(request_bytes, label="Evidence request")
        response = _load_strict_canonical_json(response_bytes, label="Evidence response")
        version = revalidate_evidence_pair_contract(
            request,
            response,
            expected_run_id=run_id,
        )

        pair = EvidencePair(
            version=version,
            request=request,
            response=response,
            request_sha256=hashlib.sha256(request_bytes).hexdigest(),
            response_sha256=hashlib.sha256(response_bytes).hexdigest(),
        )
        return pair


def _close_fd(fd: int | None) -> None:
    if fd is not None:
        with suppress(OSError):
            os.close(fd)


def _reject_symlink_components(path: Path, *, label: str) -> None:
    current = Path(path.anchor)
    for part in path.parts[1:]:
        current /= part
        try:
            metadata = current.lstat()
        except FileNotFoundError:
            return
        except OSError as error:
            raise SafetyError(f"Cannot inspect {label} safely") from error
        if stat.S_ISLNK(metadata.st_mode):
            raise SafetyError(f"{label} contains a symlink component")


def _validate_lexical_canonical_path(path: object, *, label: str) -> Path:
    if not isinstance(path, Path) or not path.is_absolute():
        raise SafetyError(f"{label} must be an absolute canonical path")
    absolute = Path(os.path.abspath(path))
    if path != absolute or any(part in {"", ".", ".."} for part in path.parts[1:]):
        raise SafetyError(f"{label} must not contain lexical aliases")
    _reject_symlink_components(path, label=label)
    try:
        resolved = path.resolve(strict=False)
    except (OSError, RuntimeError) as error:
        raise SafetyError(f"Cannot resolve {label} safely") from error
    if resolved != absolute:
        raise SafetyError(f"{label} must resolve to its canonical absolute path")
    return absolute


def _validate_canonical_repository_root(path: object) -> Path:
    root = _validate_lexical_canonical_path(path, label="Evidence repository root")
    try:
        metadata = root.lstat()
    except OSError as error:
        raise SafetyError("Evidence repository root is missing or inaccessible") from error
    if not stat.S_ISDIR(metadata.st_mode):
        raise SafetyError("Evidence repository root must be a directory")
    marker = root / "pyproject.toml"
    try:
        expected = marker.lstat()
    except OSError as error:
        raise SafetyError("Evidence repository root lacks its canonical project marker") from error
    if not stat.S_ISREG(expected.st_mode):
        raise SafetyError("Evidence repository project marker is unsafe")
    flags = os.O_RDONLY | os.O_CLOEXEC | getattr(os, "O_NOFOLLOW", 0)
    try:
        fd = os.open(marker, flags)
    except OSError as error:
        raise SafetyError("Cannot open evidence repository project marker safely") from error
    try:
        actual = os.fstat(fd)
        if not _same_stable_metadata(expected, actual):
            raise SafetyError("Evidence repository project marker changed while opening")
    finally:
        os.close(fd)
    return root


def _validate_canonical_lock(
    repository_root: Path,
    lock: LiveProcessLock | None,
) -> None:
    expected = repository_root / ".state/live.lock"
    if not isinstance(lock, LiveProcessLock):
        raise SafetyError("A held canonical live process lock is required for evidence reads")
    if lock.path != expected:
        raise SafetyError("Evidence reader requires the canonical repository live lock")
    actual = _validate_lexical_canonical_path(lock.path, label="Evidence live lock path")
    if actual != expected or lock.path.resolve(strict=False) != expected:
        raise SafetyError("Evidence reader requires the canonical repository live lock")
    if not lock.held:
        raise SafetyError("A held canonical live process lock is required for evidence reads")
    lock.assert_current_binding()


def _validate_canonical_capture_root(repository_root: Path, capture_root: Path) -> None:
    expected = repository_root / "private/captures"
    if capture_root != expected:
        raise SafetyError("Evidence capture root is not repository-derived")
    actual = _validate_lexical_canonical_path(capture_root, label="Evidence capture root")
    if actual != expected:
        raise SafetyError("Evidence capture root is not canonical")


def _require_synchronous_none(result: object) -> None:
    if inspect.isawaitable(result):
        close = getattr(result, "close", None)
        if callable(close):
            with suppress(Exception):
                close()
        raise SafetyError("Evidence schema validator must be synchronous")
    if result is not None:
        raise SafetyError("Evidence schema validator must return exactly None")


def _same_identity(left: os.stat_result, right: os.stat_result) -> bool:
    return (left.st_dev, left.st_ino) == (right.st_dev, right.st_ino)


def _stable_metadata(value: os.stat_result) -> tuple[int, ...]:
    return (
        value.st_dev,
        value.st_ino,
        value.st_mode,
        value.st_uid,
        value.st_nlink,
        value.st_size,
        value.st_mtime_ns,
        value.st_ctime_ns,
    )


def _same_stable_metadata(left: os.stat_result, right: os.stat_result) -> bool:
    return _stable_metadata(left) == _stable_metadata(right)


def _validate_private_directory(metadata: os.stat_result, *, label: str) -> None:
    if not stat.S_ISDIR(metadata.st_mode):
        raise SafetyError(f"{label} must be a private directory")
    if stat.S_IMODE(metadata.st_mode) != 0o700:
        raise SafetyError(f"{label} directory must have mode 0700")
    if metadata.st_uid != os.getuid():
        raise SafetyError(f"{label} directory must be owned by the current user")


def _validate_private_file(metadata: os.stat_result, *, label: str) -> None:
    if not stat.S_ISREG(metadata.st_mode):
        raise SafetyError(
            f"{label} must be a private regular file, not a symlink or special entry"
        )
    if stat.S_IMODE(metadata.st_mode) != 0o600:
        raise SafetyError(f"{label} private regular file must have mode 0600")
    if metadata.st_uid != os.getuid():
        raise SafetyError(f"{label} private regular file must be owned by the current user")
    if metadata.st_nlink != 1:
        raise SafetyError(f"{label} private regular file must not have a hard link")
    if metadata.st_size > _MAX_CAPTURE_BYTES:
        raise SafetyError(f"{label} is larger than the 32 MiB evidence limit")


def _open_absolute_private_root(root: Path) -> int:
    if getattr(os, "O_NOFOLLOW", 0) == 0 or not root.is_absolute():
        raise SafetyError("Secure evidence directory traversal is unavailable")
    components = root.parts[1:]
    if not components or any(component in {"", ".", ".."} for component in components):
        raise SafetyError("Evidence capture root path is invalid")
    try:
        current_fd = os.open("/", _DIRECTORY_FLAGS)
    except OSError as error:
        raise SafetyError("Cannot open evidence filesystem root safely") from error
    try:
        for index, component in enumerate(components):
            try:
                expected = os.stat(component, dir_fd=current_fd, follow_symlinks=False)
            except OSError as error:
                raise SafetyError("Evidence capture root ancestry is missing or unsafe") from error
            if not stat.S_ISDIR(expected.st_mode) or stat.S_ISLNK(expected.st_mode):
                raise SafetyError(
                    "Evidence capture root ancestry contains a symlink or non-directory"
                )
            try:
                next_fd = os.open(component, _DIRECTORY_FLAGS, dir_fd=current_fd)
            except OSError as error:
                raise SafetyError(
                    "Evidence capture root ancestry is not safely traversable"
                ) from error
            try:
                actual = os.fstat(next_fd)
                if not _same_identity(expected, actual):
                    raise SafetyError("Evidence capture root ancestry changed during traversal")
                if index == len(components) - 1:
                    _validate_private_directory(actual, label="Evidence capture root")
            except BaseException:
                os.close(next_fd)
                raise
            os.close(current_fd)
            current_fd = next_fd
        return current_fd
    except BaseException:
        _close_fd(current_fd)
        raise


def _open_private_child(parent_fd: int, name: str, *, label: str) -> int:
    try:
        expected = os.stat(name, dir_fd=parent_fd, follow_symlinks=False)
    except OSError as error:
        raise SafetyError(f"{label} directory is missing or unsafe") from error
    _validate_private_directory(expected, label=label)
    try:
        fd = os.open(name, _DIRECTORY_FLAGS, dir_fd=parent_fd)
    except OSError as error:
        raise SafetyError(
            f"{label} directory is a symlink or is not safely traversable"
        ) from error
    try:
        actual = os.fstat(fd)
        _validate_private_directory(actual, label=label)
        if not _same_identity(expected, actual):
            raise SafetyError(f"{label} directory changed while it was opened")
        current = os.stat(name, dir_fd=parent_fd, follow_symlinks=False)
        if not _same_identity(actual, current):
            raise SafetyError(f"{label} directory changed while it was opened")
        return fd
    except BaseException:
        os.close(fd)
        raise


def _directory_entries(directory_fd: int) -> tuple[str, ...]:
    try:
        entries = os.listdir(directory_fd)
    except OSError as error:
        raise SafetyError("Cannot list evidence directory safely") from error
    if any(type(entry) is not str or not entry for entry in entries):
        raise SafetyError("Evidence directory contains an invalid entry name")
    return tuple(sorted(entries))


def _revalidate_directory_at(
    parent_fd: int,
    name: str,
    directory_fd: int,
    expected: os.stat_result,
    expected_entries: tuple[str, ...],
    *,
    label: str,
) -> None:
    current = os.fstat(directory_fd)
    if not _same_stable_metadata(expected, current):
        raise SafetyError(f"{label} changed during concurrent read")
    try:
        entry = os.stat(name, dir_fd=parent_fd, follow_symlinks=False)
    except OSError as error:
        raise SafetyError(f"{label} path changed during concurrent read") from error
    if not _same_stable_metadata(expected, entry):
        raise SafetyError(f"{label} path changed during concurrent read")
    if _directory_entries(directory_fd) != expected_entries:
        raise SafetyError(f"{label} entries changed during concurrent read")


def _read_bounded(fd: int, *, label: str) -> bytes:
    chunks: list[bytes] = []
    remaining = _MAX_CAPTURE_BYTES + 1
    while remaining > 0:
        try:
            chunk = os.read(fd, min(65536, remaining))
        except OSError as error:
            raise SafetyError(f"Cannot read {label} safely") from error
        if not chunk:
            break
        chunks.append(chunk)
        remaining -= len(chunk)
    body = b"".join(chunks)
    if len(body) > _MAX_CAPTURE_BYTES:
        raise SafetyError(f"{label} is larger than the 32 MiB evidence limit")
    return body


def _read_private_file_once(
    directory_fd: int,
    name: str,
    expected: os.stat_result,
) -> bytes:
    label = f"Evidence {name}"
    try:
        fd = os.open(name, _FILE_FLAGS, dir_fd=directory_fd)
    except OSError as error:
        raise SafetyError(f"{label} is a symlink or cannot be opened safely") from error
    try:
        opened = os.fstat(fd)
        _validate_private_file(opened, label=label)
        if not _same_stable_metadata(expected, opened):
            raise SafetyError(f"{label} changed while it was opened")
        body = _read_bounded(fd, label=label)
        after = os.fstat(fd)
        if not _same_stable_metadata(opened, after):
            raise SafetyError(f"{label} changed during concurrent read")
        current = os.stat(name, dir_fd=directory_fd, follow_symlinks=False)
        if not _same_stable_metadata(opened, current):
            raise SafetyError(f"{label} path changed during concurrent read")
        return body
    finally:
        os.close(fd)


def _read_private_file(directory_fd: int, name: str) -> bytes:
    label = f"Evidence {name}"
    try:
        expected = os.stat(name, dir_fd=directory_fd, follow_symlinks=False)
    except OSError as error:
        raise SafetyError(f"{label} is missing or unsafe") from error
    _validate_private_file(expected, label=label)
    first = _read_private_file_once(directory_fd, name, expected)
    second = _read_private_file_once(directory_fd, name, expected)
    if first != second:
        raise SafetyError(f"{label} changed during concurrent double-read")
    return first


def _unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("duplicate JSON key")
        result[key] = value
    return result


def _reject_constant(value: str) -> None:
    raise ValueError(f"non-finite JSON number {value}")


def _validate_json_value(value: Any, *, depth: int = 0) -> None:
    if depth > _MAX_JSON_DEPTH:
        raise SafetyError("Evidence JSON exceeds the maximum nesting depth")
    if value is None or type(value) in {bool, int, str}:
        return
    if type(value) is float:
        if not math.isfinite(value):
            raise SafetyError("Evidence JSON contains a non-finite number")
        return
    if type(value) is list:
        for item in value:
            _validate_json_value(item, depth=depth + 1)
        return
    if type(value) is dict:
        if any(type(key) is not str for key in value):
            raise SafetyError("Evidence JSON object keys must be strings")
        for item in value.values():
            _validate_json_value(item, depth=depth + 1)
        return
    raise SafetyError("Evidence accepts only strict JSON values")


def _load_strict_canonical_json(body: bytes, *, label: str) -> dict[str, Any]:
    try:
        value = json.loads(
            body.decode("utf-8"),
            object_pairs_hook=_unique_object,
            parse_constant=_reject_constant,
        )
    except (UnicodeDecodeError, json.JSONDecodeError, ValueError, RecursionError) as error:
        raise SafetyError(f"{label} is not valid strict UTF-8 JSON") from error
    _validate_json_value(value)
    if type(value) is not dict:
        raise SafetyError(f"{label} envelope must be a JSON object")
    if body != canonical_json_bytes(value):
        raise SafetyError(f"{label} must use canonical JSON encoding")
    return value


def _validate_metadata(value: object, *, run_id: str) -> dict[str, Any]:
    if type(value) is not dict:
        raise SafetyError("Evidence metadata must be a strict object")
    fields = set(value)
    if not _REQUIRED_METADATA_FIELDS.issubset(fields) or not fields.issubset(
        _ALLOWED_METADATA_FIELDS
    ):
        raise SafetyError("Evidence metadata fields are invalid")
    expected = {
        "method": "POST",
        "operationId": _APPROVED_OPERATION,
        "path": "/api/2/menu/by_id",
        "runId": run_id,
        "status": 200,
    }
    if any(value.get(name) != expected_value for name, expected_value in expected.items()):
        raise SafetyError("Evidence metadata does not match the approved operation")
    if type(value["status"]) is not int:
        raise SafetyError("Evidence metadata status must be exactly integer 200")
    if "duration" in value:
        duration = value["duration"]
        if type(duration) not in {int, float} or not math.isfinite(duration) or duration < 0:
            raise SafetyError("Evidence metadata duration is invalid")
    if "headers" in value:
        headers = value["headers"]
        if type(headers) is not dict or any(
            type(name) is not str or name not in _ALLOWED_HEADERS or type(header_value) is not str
            for name, header_value in headers.items()
        ):
            raise SafetyError("Evidence metadata headers are invalid")
    return value


def _validate_pair_contract(
    request: dict[str, Any],
    response: dict[str, Any],
    *,
    run_id: str,
) -> int:
    if set(request) != {"body", "metadata"} or set(response) != {"body", "metadata"}:
        raise SafetyError("Evidence envelopes must contain exactly body and metadata")
    request_metadata = _validate_metadata(request["metadata"], run_id=run_id)
    response_metadata = _validate_metadata(response["metadata"], run_id=run_id)
    if canonical_json_bytes(request_metadata) != canonical_json_bytes(response_metadata):
        raise SafetyError("Evidence request and response metadata must be identical")

    request_body = request["body"]
    if type(request_body) is not dict or set(request_body) != {
        "externalMenuId",
        "organizationIds",
        "version",
    }:
        raise SafetyError("Evidence request payload has an invalid shape")
    version = request_body["version"]
    if type(version) is not int or version not in _APPROVED_VERSIONS:
        raise SafetyError("Evidence request version must be exactly 2, 3, or 4")
    external_menu_id = request_body["externalMenuId"]
    organization_ids = request_body["organizationIds"]
    if (
        type(external_menu_id) is not str
        or not external_menu_id
        or len(external_menu_id) > 256
        or type(organization_ids) is not list
        or len(organization_ids) != 1
        or type(organization_ids[0]) is not str
        or not organization_ids[0]
        or len(organization_ids[0]) > 256
    ):
        raise SafetyError("Evidence request payload identifiers are invalid")

    response_body = response["body"]
    if type(response_body) is not dict:
        raise SafetyError("Evidence response body must be an object")
    format_version = response_body.get("formatVersion")
    if type(format_version) is not int or format_version != version:
        raise SafetyError("Evidence response formatVersion must exactly match request version")
    return version


def revalidate_evidence_pair_contract(
    request: Mapping[str, FrozenJson],
    response: Mapping[str, FrozenJson],
    *,
    expected_run_id: str | None = None,
) -> int:
    """Reapply the pure reader envelope, metadata, payload, and PII contract."""

    try:
        request_value = _thaw_evidence_json(request)
        response_value = _thaw_evidence_json(response)
    except SafetyError:
        raise
    except Exception:
        raise SafetyError("Evidence pair cannot be safely copied for revalidation") from None
    if type(request_value) is not dict or type(response_value) is not dict:
        raise SafetyError("Evidence pair envelopes must be strict objects")
    request_metadata = request_value.get("metadata")
    response_metadata = response_value.get("metadata")
    if type(request_metadata) is not dict or type(response_metadata) is not dict:
        raise SafetyError("Evidence pair runId metadata is missing or invalid")
    request_run_id = request_metadata.get("runId")
    response_run_id = response_metadata.get("runId")
    if (
        type(request_run_id) is not str
        or _CAPTURE_ID.fullmatch(request_run_id) is None
        or type(response_run_id) is not str
        or response_run_id != request_run_id
    ):
        raise SafetyError("Evidence pair runId metadata is missing or inconsistent")
    if expected_run_id is not None and (
        type(expected_run_id) is not str
        or _CAPTURE_ID.fullmatch(expected_run_id) is None
        or request_run_id != expected_run_id
    ):
        raise SafetyError("Evidence pair runId does not match its capture directory")
    version = _validate_pair_contract(
        request_value,
        response_value,
        run_id=request_run_id,
    )
    _scan_for_secret_or_pii(request_value)
    _scan_for_secret_or_pii(response_value)
    return version


def _thaw_evidence_json(
    value: object,
    *,
    depth: int = 0,
    active: set[int] | None = None,
) -> Any:
    if depth > _MAX_JSON_DEPTH:
        raise SafetyError("Evidence pair exceeds the maximum nesting depth")
    if value is None or type(value) in {bool, int, str}:
        return value
    if type(value) is float:
        if not math.isfinite(value):
            raise SafetyError("Evidence pair contains a non-finite number")
        return value
    if not isinstance(value, (Mapping, tuple, list)):
        raise SafetyError("Evidence pair accepts only strict JSON values")
    seen = active if active is not None else set()
    identity = id(value)
    if identity in seen:
        raise SafetyError("Evidence pair contains a container cycle")
    seen.add(identity)
    try:
        if isinstance(value, Mapping):
            if any(type(key) is not str for key in value):
                raise SafetyError("Evidence pair object keys must be strings")
            return {
                key: _thaw_evidence_json(child, depth=depth + 1, active=seen)
                for key, child in value.items()
            }
        return [_thaw_evidence_json(child, depth=depth + 1, active=seen) for child in value]
    finally:
        seen.remove(identity)


def _scan_for_secret_or_pii(value: Any, *, key: str | None = None) -> None:
    normalized_key = key.casefold() if key is not None else None
    if normalized_key in SECRET_KEYS and value != "<redacted:secret>":
        raise SafetyError("Evidence capture failed the generic secret/PII scan")
    if normalized_key in EMAIL_KEYS and value != "<redacted:email>":
        raise SafetyError("Evidence capture failed the generic secret/PII scan")
    if normalized_key in PHONE_KEYS and value != "<redacted:phone>":
        raise SafetyError("Evidence capture failed the generic secret/PII scan")
    if type(value) is dict:
        for child_key, child in value.items():
            _scan_text(child_key, object_key=True)
            _scan_for_secret_or_pii(child, key=child_key)
        return
    if type(value) is list:
        for child in value:
            _scan_for_secret_or_pii(child, key=key)
        return
    if type(value) is str:
        _scan_text(value)


def _scan_text(value: str, *, object_key: bool = False) -> None:
    if value in _SAFE_REDACTIONS:
        return
    normalized = unicodedata.normalize("NFKC", value)
    without_uuids = _UUID_ANY.sub("", normalized)
    if (
        (object_key and _UUID_LIKE_KEY.search(normalized))
        or _JWT.search(normalized)
        or _BEARER.search(normalized)
        or _EMAIL.search(normalized)
        or _PHONE.search(without_uuids)
    ):
        raise SafetyError("Evidence capture failed the generic secret/PII scan")


def _freeze_json(value: Any) -> FrozenJson:
    if isinstance(value, Mapping):
        if any(type(key) is not str for key in value):
            raise SafetyError("Evidence pair JSON object keys must be strings")
        return MappingProxyType({key: _freeze_json(item) for key, item in value.items()})
    if type(value) in {list, tuple}:
        return tuple(_freeze_json(item) for item in value)
    if value is None or type(value) in {bool, int, str}:
        return value
    if type(value) is float and math.isfinite(value):
        return value
    raise SafetyError("Evidence pair accepts only strict immutable JSON values")


def _freeze_mapping(value: Mapping[str, Any]) -> Mapping[str, FrozenJson]:
    frozen = _freeze_json(value)
    assert isinstance(frozen, Mapping)
    return frozen
