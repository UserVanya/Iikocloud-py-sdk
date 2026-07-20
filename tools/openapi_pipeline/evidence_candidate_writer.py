"""Fail-safe persistence for detached evidence-candidate trees.

All official evidence-candidate writers, including the D3 persistence step, must
cooperate on the fixed build-root lock before inspecting or changing publication
state. A non-cooperating same-UID process is out of scope: it can already mutate
the checkout directly, so this API serializes supported writers without claiming
to defend against a malicious peer with the repository owner's authority.
"""

from __future__ import annotations

import ctypes
import errno
import fcntl
import json
import math
import os
import re
import secrets
import stat
from collections.abc import Mapping
from contextlib import suppress
from dataclasses import dataclass
from pathlib import Path
from types import MappingProxyType
from typing import Any, cast

import yaml

from .errors import SafetyError
from .evidence_candidate_contract import (
    EVIDENCE_CANDIDATE_PAYLOAD_PATHS,
    EVIDENCE_FIXTURE_PATHS,
    EVIDENCE_OPERATION_ID,
    EVIDENCE_VERSIONS,
    MANIFEST_SCHEMA_VERSION,
    MANIFEST_TOOL_NAME,
    MANIFEST_TOOL_VERSION,
    OPERATIONS_OVERLAY_PATH,
    POLYMORPHISM_OVERLAY_PATH,
    assert_evidence_candidate_bytes_safe,
    assert_evidence_candidate_values_safe,
    canonical_evidence_candidate_payloads,
)
from .evidence_candidate_store import EvidenceCandidateManifestResult
from .io import canonical_json_bytes, sha256_bytes
from .paths import RepoPaths

_CANDIDATE_DIRECTORY = "evidence-candidates"
_LOCK_FILE = ".evidence-candidates.lock"
_STAGING_PREFIX = ".evidence-candidates.tmp-"
_MANIFEST_PATH = "candidate-manifest.json"
_RENAME_NOREPLACE = 1
_SHA256 = re.compile(r"[a-f0-9]{64}\Z")
_MAPPING_PROXY_TYPE: type[Any] = type(MappingProxyType({}))
_MAX_JSON_DEPTH = 128

_DIRECTORY_PATHS = (
    "",
    "openapi",
    "openapi/overlays",
    "tests",
    "tests/fixtures",
    "tests/fixtures/contracts",
)
_FILE_PATHS = (_MANIFEST_PATH, *EVIDENCE_CANDIDATE_PAYLOAD_PATHS)
_EXPECTED_ENTRIES = {
    "": (_MANIFEST_PATH, "openapi", "tests"),
    "openapi": ("overlays",),
    "openapi/overlays": (
        "operations.overlay.yaml",
        "polymorphism.overlay.yaml",
    ),
    "tests": ("fixtures",),
    "tests/fixtures": ("contracts",),
    "tests/fixtures/contracts": (
        "external-menu-v2.json",
        "external-menu-v3.json",
        "external-menu-v4.json",
    ),
}
_MANIFEST_FIELDS = (
    "schema_version",
    "tool",
    "operation_id",
    "effective_schema_sha256",
    "evidence_analysis_sha256",
    "evidence_provenance",
    "files",
)


@dataclass(frozen=True)
class EvidenceCandidateWriteResult:
    root: Path
    manifest_path: Path
    manifest_sha256: str
    changed: bool


@dataclass(frozen=True)
class _CandidateTree:
    files: Mapping[str, bytes]
    manifest_sha256: str


class _DestinationExists(Exception):
    pass


def write_evidence_candidate_tree(
    result: EvidenceCandidateManifestResult,
    paths: RepoPaths,
) -> EvidenceCandidateWriteResult:
    """Persist a detached candidate snapshot without overwriting a reviewed tree.

    The canonical mode-0755 ``build/`` directory must already exist. Publication into
    that ignored directory is a consistency operation only and does not authorize
    acceptance into tracked overlays or fixtures. All official writers cooperate on
    the persistent lock; the lock is held from residue inventory through descriptor
    closure. Any staging residue blocks publication until an operator resolves it.
    Any failure after staging allocation deliberately leaves the hidden staging or
    complete published tree untouched; the writer only closes file descriptors and
    never attempts name-based cleanup. A non-cooperating same-UID process is out of
    scope because it can already mutate the checkout directly.
    """

    tree = _snapshot_candidate_tree(result)
    repository_root = _validated_repository_path(paths)
    renameat2 = _require_secure_publication_primitives()
    candidate_root = repository_root / "build" / _CANDIDATE_DIRECTORY
    output = EvidenceCandidateWriteResult(
        root=candidate_root,
        manifest_path=candidate_root / _MANIFEST_PATH,
        manifest_sha256=tree.manifest_sha256,
        changed=True,
    )

    repository_fd: int | None = None
    build_fd: int | None = None
    lock_fd: int | None = None
    candidate_fd: int | None = None
    directory_fds: dict[str, int] = {}
    try:
        repository_fd = _open_repository_root(repository_root)
        build_fd = _open_build(repository_fd)
        lock_fd = _open_and_lock_writer(build_fd)
        _reject_staging_residue(build_fd)
        candidate_fd = _open_optional_public_directory(
            build_fd,
            _CANDIDATE_DIRECTORY,
            label="Evidence candidate root",
        )
        if candidate_fd is not None:
            _validate_exact_tree(candidate_fd, tree.files)
            _revalidate_published_candidate(
                repository_root,
                repository_fd=repository_fd,
                build_fd=build_fd,
                candidate_fd=candidate_fd,
                files=tree.files,
            )
            return _write_result_with_changed(output, changed=False)

        staging_name, staging_fd = _create_staging_directory(build_fd)
        try:
            _register_directory_fd(directory_fds, "", staging_fd)
        except BaseException:
            _close_fd(staging_fd)
            raise
        _create_staging_tree(directory_fds, tree.files)
        _validate_exact_tree(staging_fd, tree.files)
        _revalidate_directory_binding(
            build_fd,
            staging_name,
            staging_fd,
            label="Evidence candidate staging root",
        )
        try:
            _rename_directory_noreplace(
                build_fd,
                staging_name,
                _CANDIDATE_DIRECTORY,
                renameat2,
            )
        except _DestinationExists:
            candidate_fd = _open_required_public_directory(
                build_fd,
                _CANDIDATE_DIRECTORY,
                label="Concurrent evidence candidate root",
            )
            _validate_exact_tree(candidate_fd, tree.files)
            _revalidate_published_candidate(
                repository_root,
                repository_fd=repository_fd,
                build_fd=build_fd,
                candidate_fd=candidate_fd,
                files=tree.files,
            )
            raise SafetyError(
                "Concurrent evidence candidate publication preserved staging residue"
            ) from None

        _fsync_fd(build_fd)
        _revalidate_published_candidate(
            repository_root,
            repository_fd=repository_fd,
            build_fd=build_fd,
            candidate_fd=staging_fd,
            files=tree.files,
        )
        return output
    finally:
        _close_directory_fds(directory_fds)
        _close_fd(candidate_fd)
        _close_fd(build_fd)
        _close_fd(repository_fd)
        _close_fd(lock_fd)


def _write_result_with_changed(
    value: EvidenceCandidateWriteResult,
    *,
    changed: bool,
) -> EvidenceCandidateWriteResult:
    return EvidenceCandidateWriteResult(
        root=value.root,
        manifest_path=value.manifest_path,
        manifest_sha256=value.manifest_sha256,
        changed=changed,
    )


def _snapshot_candidate_tree(result: object) -> _CandidateTree:
    if type(result) is not EvidenceCandidateManifestResult:
        raise SafetyError("Evidence candidate writer requires an exact manifest result")
    manifest_source, payload_source, manifest_body, manifest_sha256 = (
        result.manifest,
        result.canonical_payloads,
        result.canonical_json_bytes,
        result.sha256,
    )
    if type(manifest_body) is not bytes or not manifest_body:
        raise SafetyError("Evidence candidate manifest bytes are invalid")
    digest = _require_sha256(
        manifest_sha256,
        "Evidence candidate detached manifest digest is invalid",
    )
    manifest = _materialize_immutable_json(
        manifest_source,
        message="Evidence candidate manifest snapshot is invalid",
    )
    if type(manifest) is not dict:
        raise SafetyError("Evidence candidate manifest snapshot is invalid")
    payloads = _snapshot_payloads(payload_source)

    decoded_manifest = _load_canonical_json(manifest_body, label="Evidence candidate manifest")
    if decoded_manifest != manifest or canonical_json_bytes(manifest) != manifest_body:
        raise SafetyError("Evidence candidate manifest bytes are inconsistent")
    if sha256_bytes(manifest_body) != digest:
        raise SafetyError("Evidence candidate detached manifest digest is invalid")
    _validate_manifest_shape(manifest, payloads)
    _validate_canonical_payloads(payloads)
    assert_evidence_candidate_values_safe(manifest)
    assert_evidence_candidate_bytes_safe((manifest_body, *payloads.values()))

    files = MappingProxyType(
        {
            _MANIFEST_PATH: manifest_body,
            **{path: payloads[path] for path in EVIDENCE_CANDIDATE_PAYLOAD_PATHS},
        }
    )
    return _CandidateTree(files=files, manifest_sha256=digest)


def _snapshot_payloads(value: object) -> dict[str, bytes]:
    entries = _immutable_mapping_entries(
        value,
        message="Evidence candidate payload snapshot is invalid",
    )
    if tuple(path for path, _body in entries) != EVIDENCE_CANDIDATE_PAYLOAD_PATHS:
        raise SafetyError("Evidence candidate payload paths or order are invalid")
    payloads: dict[str, bytes] = {}
    for path, body in entries:
        if type(path) is not str or type(body) is not bytes or not body:
            raise SafetyError("Evidence candidate payload body is invalid")
        payloads[path] = body
    return payloads


def _validate_manifest_shape(
    manifest: dict[str, Any],
    payloads: Mapping[str, bytes],
) -> None:
    if tuple(manifest) != _MANIFEST_FIELDS:
        raise SafetyError("Evidence candidate manifest shape is invalid")
    if type(manifest["schema_version"]) is not int or (
        manifest["schema_version"] != MANIFEST_SCHEMA_VERSION
    ):
        raise SafetyError("Evidence candidate manifest schema version is invalid")
    tool = manifest["tool"]
    if (
        type(tool) is not dict
        or tuple(tool) != ("name", "version")
        or tool["name"] != MANIFEST_TOOL_NAME
        or type(tool["name"]) is not str
        or tool["version"] != MANIFEST_TOOL_VERSION
        or type(tool["version"]) is not int
    ):
        raise SafetyError("Evidence candidate manifest tool binding is invalid")
    if (
        type(manifest["operation_id"]) is not str
        or manifest["operation_id"] != EVIDENCE_OPERATION_ID
    ):
        raise SafetyError("Evidence candidate manifest operation binding is invalid")
    _require_sha256(
        manifest["effective_schema_sha256"],
        "Evidence candidate manifest schema binding is invalid",
    )
    _require_sha256(
        manifest["evidence_analysis_sha256"],
        "Evidence candidate manifest analysis binding is invalid",
    )
    provenance = manifest["evidence_provenance"]
    expected_versions = tuple(str(version) for version in EVIDENCE_VERSIONS)
    if type(provenance) is not dict or tuple(provenance) != expected_versions:
        raise SafetyError("Evidence candidate manifest provenance is invalid")
    for version in expected_versions:
        entry = provenance[version]
        if type(entry) is not dict or tuple(entry) != (
            "request_sha256",
            "response_sha256",
        ):
            raise SafetyError("Evidence candidate manifest provenance is invalid")
        _require_sha256(
            entry["request_sha256"],
            "Evidence candidate manifest provenance is invalid",
        )
        _require_sha256(
            entry["response_sha256"],
            "Evidence candidate manifest provenance is invalid",
        )
    files = manifest["files"]
    if type(files) is not dict or tuple(files) != EVIDENCE_CANDIDATE_PAYLOAD_PATHS:
        raise SafetyError("Evidence candidate manifest file scope is invalid")
    for path in EVIDENCE_CANDIDATE_PAYLOAD_PATHS:
        recorded = _require_sha256(
            files[path],
            "Evidence candidate manifest file digest is invalid",
        )
        if recorded != sha256_bytes(payloads[path]):
            raise SafetyError("Evidence candidate manifest file digest is inconsistent")


def _validate_canonical_payloads(payloads: Mapping[str, bytes]) -> None:
    operations = _load_canonical_overlay(
        payloads[OPERATIONS_OVERLAY_PATH],
        label="Evidence operations overlay",
    )
    polymorphism = _load_canonical_overlay(
        payloads[POLYMORPHISM_OVERLAY_PATH],
        label="Evidence polymorphism overlay",
    )
    fixtures = {
        version: _load_canonical_fixture(
            payloads[EVIDENCE_FIXTURE_PATHS[version]],
            label=f"Evidence V{version} fixture",
        )
        for version in EVIDENCE_VERSIONS
    }
    expected = canonical_evidence_candidate_payloads(
        operations_overlay=operations,
        polymorphism_overlay=polymorphism,
        fixtures=fixtures,
    )
    if any(payloads[path] != expected[path] for path in EVIDENCE_CANDIDATE_PAYLOAD_PATHS):
        raise SafetyError("Evidence candidate payload must use canonical encoding")


def _load_canonical_overlay(body: bytes, *, label: str) -> dict[str, Any]:
    failed = False
    try:
        value = yaml.safe_load(body.decode("utf-8"))
    except (UnicodeError, yaml.YAMLError, RecursionError):
        failed = True
        value = None
    if failed:
        raise SafetyError(f"{label} is not valid canonical UTF-8 YAML") from None
    _validate_plain_json(value, label=label)
    if type(value) is not dict:
        raise SafetyError(f"{label} root must be an object")
    return value


def _load_canonical_fixture(body: bytes, *, label: str) -> dict[str, Any]:
    value = _load_canonical_json(body, label=label)
    if type(value) is not dict:
        raise SafetyError(f"{label} root must be an object")
    return value


def _load_canonical_json(body: bytes, *, label: str) -> Any:
    failed = False
    try:
        value = json.loads(
            body.decode("utf-8"),
            object_pairs_hook=_unique_json_object,
            parse_constant=_reject_json_constant,
        )
    except (UnicodeError, json.JSONDecodeError, ValueError, RecursionError):
        failed = True
        value = None
    if failed:
        raise SafetyError(f"{label} is not valid strict UTF-8 JSON") from None
    _validate_plain_json(value, label=label)
    if body != canonical_json_bytes(value):
        raise SafetyError(f"{label} must use canonical JSON encoding")
    return value


def _unique_json_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("duplicate JSON key")
        result[key] = value
    return result


def _reject_json_constant(_value: str) -> None:
    raise ValueError("non-finite JSON number")


def _validate_plain_json(
    value: Any,
    *,
    label: str,
    depth: int = 0,
    active: set[int] | None = None,
) -> None:
    if depth > _MAX_JSON_DEPTH:
        raise SafetyError(f"{label} exceeds the maximum nesting depth")
    if value is None or type(value) in {bool, int, str}:
        return
    if type(value) is float:
        if not math.isfinite(value):
            raise SafetyError(f"{label} contains a non-finite number")
        return
    if type(value) not in {dict, list}:
        raise SafetyError(f"{label} contains a non-JSON value")
    seen = active if active is not None else set()
    identity = id(value)
    if identity in seen:
        raise SafetyError(f"{label} contains a recursive value")
    seen.add(identity)
    try:
        if type(value) is dict:
            if any(type(key) is not str for key in value):
                raise SafetyError(f"{label} contains a non-string object key")
            children = value.values()
        else:
            children = value
        for child in children:
            _validate_plain_json(
                child,
                label=label,
                depth=depth + 1,
                active=seen,
            )
    finally:
        seen.remove(identity)


def _immutable_mapping_entries(
    value: object,
    *,
    message: str,
) -> tuple[tuple[Any, Any], ...]:
    if type(value) is not _MAPPING_PROXY_TYPE:
        raise SafetyError(message)
    mapping = cast(Mapping[Any, Any], value)
    traversal_failed = False
    try:
        keys = tuple(mapping)
    except MemoryError:
        raise
    except Exception:
        traversal_failed = True
        keys = ()
    if traversal_failed:
        raise SafetyError(message) from None
    entries: list[tuple[Any, Any]] = []
    for key in keys:
        lookup_failed = False
        try:
            child = mapping[key]
        except MemoryError:
            raise
        except Exception:
            lookup_failed = True
            child = None
        if lookup_failed:
            raise SafetyError(message) from None
        entries.append((key, child))
    return tuple(entries)


def _materialize_immutable_json(
    value: object,
    *,
    message: str,
    depth: int = 0,
    active: set[int] | None = None,
) -> Any:
    if depth > _MAX_JSON_DEPTH:
        raise SafetyError(message)
    if value is None or type(value) in {bool, int, str}:
        return value
    if type(value) is float:
        if not math.isfinite(value):
            raise SafetyError(message)
        return value
    if type(value) not in {_MAPPING_PROXY_TYPE, tuple}:
        raise SafetyError(message)
    seen = active if active is not None else set()
    identity = id(value)
    if identity in seen:
        raise SafetyError(message)
    seen.add(identity)
    try:
        if type(value) is _MAPPING_PROXY_TYPE:
            entries = _immutable_mapping_entries(value, message=message)
            if any(type(key) is not str for key, _child in entries):
                raise SafetyError(message)
            return {
                key: _materialize_immutable_json(
                    child,
                    message=message,
                    depth=depth + 1,
                    active=seen,
                )
                for key, child in entries
            }
        sequence = cast(tuple[Any, ...], value)
        return [
            _materialize_immutable_json(
                child,
                message=message,
                depth=depth + 1,
                active=seen,
            )
            for child in sequence
        ]
    finally:
        seen.remove(identity)


def _require_sha256(value: object, message: str) -> str:
    if type(value) is not str or _SHA256.fullmatch(value) is None:
        raise SafetyError(message)
    return value


def _validated_repository_path(paths: object) -> Path:
    if type(paths) is not RepoPaths:
        raise SafetyError("Evidence candidate writer requires exact repository paths")
    root = paths.root
    if type(root) is not type(Path()):
        raise SafetyError("Evidence repository root must be an exact filesystem path")
    if not root.is_absolute():
        raise SafetyError("Evidence repository root must be an absolute canonical path")
    absolute = Path(os.path.abspath(root))
    if root != absolute or any(component in {"", ".", ".."} for component in root.parts[1:]):
        raise SafetyError("Evidence repository root must not contain lexical aliases")
    return root


def _directory_flags() -> int:
    return os.O_RDONLY | os.O_CLOEXEC | os.O_DIRECTORY | os.O_NOFOLLOW


def _load_renameat2() -> Any | None:
    try:
        libc = ctypes.CDLL(None, use_errno=True)
    except OSError:
        return None
    renameat2 = getattr(libc, "renameat2", None)
    if renameat2 is None:
        return None
    renameat2.argtypes = [
        ctypes.c_int,
        ctypes.c_char_p,
        ctypes.c_int,
        ctypes.c_char_p,
        ctypes.c_uint,
    ]
    renameat2.restype = ctypes.c_int
    return renameat2


def _require_secure_publication_primitives() -> Any:
    if (
        getattr(os, "O_NOFOLLOW", 0) == 0
        or getattr(os, "O_DIRECTORY", 0) == 0
        or getattr(os, "O_NONBLOCK", 0) == 0
    ):
        raise SafetyError("Secure evidence candidate publication is unavailable")
    renameat2 = _load_renameat2()
    if renameat2 is None or not callable(renameat2) or not _probe_renameat2(renameat2):
        raise SafetyError("Atomic no-replace evidence candidate publication is unavailable")
    return renameat2


def _probe_renameat2(renameat2: Any) -> bool:
    ctypes.set_errno(0)
    result = renameat2(
        -1,
        b".",
        -1,
        b".",
        _RENAME_NOREPLACE,
    )
    error_number = ctypes.get_errno()
    return result == -1 and error_number == errno.EBADF


def _open_repository_root(root: Path) -> int:
    components = root.parts[1:]
    if not components:
        raise SafetyError("Evidence repository root is invalid")
    current_fd = _safe_open(
        "/",
        _directory_flags(),
        message="Cannot open evidence filesystem root safely",
    )
    try:
        for component in components:
            expected = _safe_stat_at(
                current_fd,
                component,
                message="Evidence repository ancestry is missing or unsafe",
            )
            if not stat.S_ISDIR(expected.st_mode) or stat.S_ISLNK(expected.st_mode):
                raise SafetyError(
                    "Evidence repository ancestry contains a symlink or non-directory"
                )
            next_fd = _safe_open(
                component,
                _directory_flags(),
                dir_fd=current_fd,
                message="Evidence repository ancestry is not safely traversable",
            )
            try:
                actual = _safe_fstat(
                    next_fd,
                    message="Cannot inspect evidence repository ancestry safely",
                )
                if not _same_identity(expected, actual):
                    raise SafetyError("Evidence repository ancestry changed during traversal")
            except BaseException:
                _close_fd(next_fd)
                raise
            _close_fd(current_fd)
            current_fd = next_fd
        _validate_repository_marker(current_fd)
        return current_fd
    except BaseException:
        _close_fd(current_fd)
        raise


def _validate_repository_marker(repository_fd: int) -> None:
    expected = _safe_stat_at(
        repository_fd,
        "pyproject.toml",
        message="Evidence repository root lacks its canonical pyproject marker",
    )
    if not stat.S_ISREG(expected.st_mode) or stat.S_ISLNK(expected.st_mode):
        raise SafetyError("Evidence repository pyproject marker is unsafe")
    fd = _safe_open(
        "pyproject.toml",
        os.O_RDONLY | os.O_CLOEXEC | os.O_NOFOLLOW | os.O_NONBLOCK,
        dir_fd=repository_fd,
        message="Cannot open evidence repository pyproject marker safely",
    )
    try:
        actual = _safe_fstat(
            fd,
            message="Cannot inspect evidence repository pyproject marker safely",
        )
        if not _same_stable_metadata(expected, actual):
            raise SafetyError("Evidence repository pyproject marker changed while opening")
    finally:
        _close_fd(fd)


def _open_build(repository_fd: int) -> int:
    return _open_required_public_directory(
        repository_fd,
        "build",
        label="Evidence build root",
    )


def _open_and_lock_writer(build_fd: int) -> int:
    lock_fd = _open_or_create_writer_lock(build_fd)
    try:
        _acquire_writer_lock(lock_fd)
        _revalidate_writer_lock_binding(build_fd, lock_fd)
        return lock_fd
    except BaseException:
        _close_fd(lock_fd)
        raise


def _open_or_create_writer_lock(build_fd: int) -> int:
    flags = os.O_RDWR | os.O_CLOEXEC | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW | os.O_NONBLOCK
    exists = False
    failed = False
    lock_fd = -1
    try:
        lock_fd = os.open(_LOCK_FILE, flags, 0o644, dir_fd=build_fd)
    except FileExistsError:
        exists = True
    except OSError:
        failed = True
    if exists:
        return _open_existing_writer_lock(build_fd)
    if failed:
        raise SafetyError("Cannot create evidence candidate writer lock safely") from None

    try:
        _fchmod_fd(lock_fd, 0o644)
        _revalidate_writer_lock_binding(build_fd, lock_fd)
        _fsync_fd(lock_fd)
        _fsync_fd(build_fd)
        return lock_fd
    except BaseException:
        _close_fd(lock_fd)
        raise


def _open_existing_writer_lock(build_fd: int) -> int:
    expected = _safe_stat_at(
        build_fd,
        _LOCK_FILE,
        message="Cannot inspect evidence candidate writer lock safely",
    )
    _validate_public_file(expected, label="Evidence candidate writer lock")
    lock_fd = _safe_open(
        _LOCK_FILE,
        os.O_RDWR | os.O_CLOEXEC | os.O_NOFOLLOW | os.O_NONBLOCK,
        dir_fd=build_fd,
        message="Cannot open evidence candidate writer lock safely",
    )
    try:
        actual = _safe_fstat(
            lock_fd,
            message="Cannot inspect evidence candidate writer lock safely",
        )
        _validate_public_file(actual, label="Evidence candidate writer lock")
        if not _same_stable_metadata(expected, actual):
            raise SafetyError("Evidence candidate writer lock changed while opening")
        _revalidate_writer_lock_binding(build_fd, lock_fd)
        return lock_fd
    except BaseException:
        _close_fd(lock_fd)
        raise


def _acquire_writer_lock(lock_fd: int) -> None:
    contended = False
    failed = False
    try:
        fcntl.flock(lock_fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
    except BlockingIOError:
        contended = True
    except OSError as error:
        if error.errno in {errno.EACCES, errno.EAGAIN, errno.EWOULDBLOCK}:
            contended = True
        else:
            failed = True
    if contended:
        raise SafetyError("Evidence candidate writer lock is already held") from None
    if failed:
        raise SafetyError("Cannot acquire evidence candidate writer lock safely") from None


def _revalidate_writer_lock_binding(build_fd: int, lock_fd: int) -> None:
    held = _safe_fstat(
        lock_fd,
        message="Cannot inspect evidence candidate writer lock safely",
    )
    current = _safe_stat_at(
        build_fd,
        _LOCK_FILE,
        message="Cannot revalidate evidence candidate writer lock safely",
    )
    _validate_public_file(held, label="Evidence candidate writer lock")
    _validate_public_file(current, label="Evidence candidate writer lock")
    if not _same_stable_metadata(held, current):
        raise SafetyError("Evidence candidate writer lock binding changed")


def _reject_staging_residue(build_fd: int) -> None:
    if any(name.startswith(_STAGING_PREFIX) for name in _safe_listdir(build_fd)):
        raise SafetyError("Evidence candidate staging residue requires operator resolution")


def _open_optional_public_directory(
    parent_fd: int,
    name: str,
    *,
    label: str,
) -> int | None:
    missing = False
    failed = False
    expected: os.stat_result | None = None
    try:
        expected = os.stat(name, dir_fd=parent_fd, follow_symlinks=False)
    except FileNotFoundError:
        missing = True
    except OSError:
        failed = True
    if failed:
        raise SafetyError(f"Cannot inspect {label} safely") from None
    if missing:
        return None
    assert expected is not None
    return _open_public_directory_from_metadata(parent_fd, name, expected, label=label)


def _open_required_public_directory(
    parent_fd: int,
    name: str,
    *,
    label: str,
    validate_mode: bool = True,
) -> int:
    expected = _safe_stat_at(parent_fd, name, message=f"{label} is missing or unsafe")
    if validate_mode:
        _validate_public_directory(expected, label=label)
    elif not stat.S_ISDIR(expected.st_mode) or stat.S_ISLNK(expected.st_mode):
        raise SafetyError(f"{label} is a symlink or non-directory")
    return _open_public_directory_from_metadata(
        parent_fd,
        name,
        expected,
        label=label,
        validate_mode=validate_mode,
    )


def _open_public_directory_from_metadata(
    parent_fd: int,
    name: str,
    expected: os.stat_result,
    *,
    label: str,
    validate_mode: bool = True,
) -> int:
    if validate_mode:
        _validate_public_directory(expected, label=label)
    fd = _safe_open(
        name,
        _directory_flags(),
        dir_fd=parent_fd,
        message=f"{label} is a symlink or is not safely traversable",
    )
    try:
        actual = _safe_fstat(fd, message=f"Cannot inspect {label} safely")
        if validate_mode:
            _validate_public_directory(actual, label=label)
        if not _same_identity(expected, actual):
            raise SafetyError(f"{label} changed while opening")
        current = _safe_stat_at(parent_fd, name, message=f"Cannot revalidate {label} safely")
        if validate_mode:
            _validate_public_directory(current, label=label)
        if not _same_identity(actual, current):
            raise SafetyError(f"{label} changed while opening")
        return fd
    except BaseException:
        _close_fd(fd)
        raise


def _create_staging_directory(build_fd: int) -> tuple[str, int]:
    for _attempt in range(32):
        name = f".{_CANDIDATE_DIRECTORY}.tmp-{secrets.token_hex(12)}"
        if not _safe_mkdir_at(build_fd, name, 0o755):
            continue
        staging_fd: int | None = None
        try:
            staging_fd = _open_required_public_directory(
                build_fd,
                name,
                label="Evidence candidate staging root",
            )
            _fsync_fd(staging_fd)
            _fsync_fd(build_fd)
            return name, staging_fd
        except BaseException:
            _close_fd(staging_fd)
            raise
    raise SafetyError("Cannot allocate a unique evidence candidate staging directory")


def _create_staging_tree(
    directory_fds: dict[str, int],
    files: Mapping[str, bytes],
) -> None:
    for relative in _DIRECTORY_PATHS[1:]:
        parent, name = _split_relative(relative)
        parent_fd = directory_fds[parent]
        if not _safe_mkdir_at(parent_fd, name, 0o755):
            raise SafetyError("Evidence candidate staging directory unexpectedly exists")
        child_fd: int | None = None
        try:
            child_fd = _open_required_public_directory(
                parent_fd,
                name,
                label="Evidence candidate staging directory",
            )
            registered_fd = child_fd
            _register_directory_fd(directory_fds, relative, registered_fd)
            child_fd = None
        finally:
            _close_fd(child_fd)
    for relative in _FILE_PATHS:
        parent, name = _split_relative(relative)
        _write_file_at(directory_fds[parent], name, files[relative])
    for relative in reversed(_DIRECTORY_PATHS):
        _fsync_fd(directory_fds[relative])


def _write_file_at(directory_fd: int, name: str, body: bytes) -> None:
    fd = _safe_open(
        name,
        os.O_WRONLY | os.O_CLOEXEC | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW,
        mode=0o644,
        dir_fd=directory_fd,
        message="Cannot create evidence candidate file safely",
    )
    try:
        _fchmod_fd(fd, 0o644)
        offset = 0
        while offset < len(body):
            failed = False
            written = 0
            try:
                written = os.write(fd, body[offset:])
            except OSError:
                failed = True
            if failed or written <= 0:
                raise SafetyError("Cannot write evidence candidate file safely") from None
            offset += written
        _fsync_fd(fd)
        metadata = _safe_fstat(fd, message="Cannot inspect evidence candidate file safely")
        _validate_public_file(metadata, label="Evidence candidate file")
        if metadata.st_size != len(body):
            raise SafetyError("Evidence candidate file write was incomplete")
        current = _safe_stat_at(
            directory_fd,
            name,
            message="Cannot revalidate evidence candidate file safely",
        )
        if not _same_identity(metadata, current):
            raise SafetyError("Evidence candidate file changed while writing")
    finally:
        _close_fd(fd)


def _validate_exact_tree(root_fd: int, files: Mapping[str, bytes]) -> None:
    _validate_tree_directory(root_fd, "", files)


def _validate_tree_directory(
    directory_fd: int,
    relative: str,
    files: Mapping[str, bytes],
) -> None:
    before = _safe_fstat(
        directory_fd,
        message="Cannot inspect evidence candidate directory safely",
    )
    _validate_public_directory(before, label="Evidence candidate directory")
    entries = _safe_listdir(directory_fd)
    if tuple(sorted(entries)) != tuple(sorted(_EXPECTED_ENTRIES[relative])):
        raise SafetyError("Evidence candidate tree has missing, partial, or extra entries")
    for name in _EXPECTED_ENTRIES[relative]:
        child_relative = f"{relative}/{name}" if relative else name
        if child_relative in _DIRECTORY_PATHS:
            child_fd = _open_required_public_directory(
                directory_fd,
                name,
                label="Evidence candidate directory",
            )
            try:
                _validate_tree_directory(child_fd, child_relative, files)
            finally:
                _close_fd(child_fd)
        else:
            _read_expected_public_file(
                directory_fd,
                name,
                files[child_relative],
            )
    after = _safe_fstat(
        directory_fd,
        message="Cannot revalidate evidence candidate directory safely",
    )
    if not _same_stable_metadata(before, after):
        raise SafetyError("Evidence candidate directory changed during validation")
    if _safe_listdir(directory_fd) != entries:
        raise SafetyError("Evidence candidate directory entries changed during validation")


def _read_expected_public_file(directory_fd: int, name: str, expected_body: bytes) -> None:
    expected = _safe_stat_at(
        directory_fd,
        name,
        message="Evidence candidate file is missing or unsafe",
    )
    _validate_public_file(expected, label="Evidence candidate file")
    if expected.st_size != len(expected_body):
        raise SafetyError("Evidence candidate file differs from the reviewed snapshot")
    fd = _safe_open(
        name,
        os.O_RDONLY | os.O_CLOEXEC | os.O_NOFOLLOW | os.O_NONBLOCK,
        dir_fd=directory_fd,
        message="Evidence candidate file cannot be opened safely",
    )
    try:
        opened = _safe_fstat(fd, message="Cannot inspect evidence candidate file safely")
        _validate_public_file(opened, label="Evidence candidate file")
        if not _same_stable_metadata(expected, opened):
            raise SafetyError("Evidence candidate file changed while opening")
        body = _read_bounded(fd, len(expected_body) + 1)
        if body != expected_body:
            raise SafetyError("Evidence candidate file differs from the reviewed snapshot")
        after = _safe_fstat(
            fd,
            message="Cannot revalidate evidence candidate file safely",
        )
        if not _same_stable_metadata(opened, after):
            raise SafetyError("Evidence candidate file changed during validation")
        current = _safe_stat_at(
            directory_fd,
            name,
            message="Evidence candidate file path changed during validation",
        )
        if not _same_stable_metadata(opened, current):
            raise SafetyError("Evidence candidate file path changed during validation")
    finally:
        _close_fd(fd)


def _read_bounded(fd: int, limit: int) -> bytes:
    chunks: list[bytes] = []
    remaining = limit
    while remaining > 0:
        failed = False
        chunk = b""
        try:
            chunk = os.read(fd, min(65536, remaining))
        except OSError:
            failed = True
        if failed:
            raise SafetyError("Cannot read evidence candidate file safely") from None
        if not chunk:
            break
        chunks.append(chunk)
        remaining -= len(chunk)
    return b"".join(chunks)


def _rename_directory_noreplace(
    parent_fd: int,
    source: str,
    destination: str,
    renameat2: Any,
) -> None:
    result = renameat2(
        parent_fd,
        os.fsencode(source),
        parent_fd,
        os.fsencode(destination),
        _RENAME_NOREPLACE,
    )
    if result == 0:
        return
    error_number = ctypes.get_errno()
    if error_number in {errno.EEXIST, errno.ENOTEMPTY}:
        raise _DestinationExists
    raise SafetyError("Atomic no-replace evidence candidate publication failed")


def _revalidate_published_candidate(
    repository_root: Path,
    *,
    repository_fd: int,
    build_fd: int,
    candidate_fd: int,
    files: Mapping[str, bytes],
) -> None:
    reopened_repository_fd: int | None = None
    reopened_build_fd: int | None = None
    reopened_candidate_fd: int | None = None
    try:
        reopened_repository_fd = _open_repository_root(repository_root)
        if not _same_identity_fds(reopened_repository_fd, repository_fd):
            raise SafetyError("Evidence repository binding changed during publication")
        reopened_build_fd = _open_required_public_directory(
            reopened_repository_fd,
            "build",
            label="Evidence build root",
        )
        if not _same_identity_fds(reopened_build_fd, build_fd):
            raise SafetyError("Evidence build binding changed during publication")
        reopened_candidate_fd = _open_required_public_directory(
            reopened_build_fd,
            _CANDIDATE_DIRECTORY,
            label="Evidence candidate root",
        )
        if not _same_identity_fds(reopened_candidate_fd, candidate_fd):
            raise SafetyError("Evidence candidate identity changed during publication")
        _validate_exact_tree(reopened_candidate_fd, files)
    finally:
        _close_fd(reopened_candidate_fd)
        _close_fd(reopened_build_fd)
        _close_fd(reopened_repository_fd)


def _validate_public_directory(metadata: os.stat_result, *, label: str) -> None:
    if not stat.S_ISDIR(metadata.st_mode) or stat.S_ISLNK(metadata.st_mode):
        raise SafetyError(f"{label} must be a non-symlink directory")
    if stat.S_IMODE(metadata.st_mode) != 0o755:
        raise SafetyError(f"{label} must have mode 0755")
    if metadata.st_uid != os.getuid():
        raise SafetyError(f"{label} must be owned by the current user")


def _validate_public_file(metadata: os.stat_result, *, label: str) -> None:
    if not stat.S_ISREG(metadata.st_mode) or stat.S_ISLNK(metadata.st_mode):
        raise SafetyError(f"{label} must be a regular non-symlink file")
    if stat.S_IMODE(metadata.st_mode) != 0o644:
        raise SafetyError(f"{label} must have mode 0644")
    if metadata.st_uid != os.getuid():
        raise SafetyError(f"{label} must be owned by the current user")
    if metadata.st_nlink != 1:
        raise SafetyError(f"{label} must not have a hard link")


def _safe_open(
    path: str,
    flags: int,
    *,
    mode: int | None = None,
    dir_fd: int | None = None,
    message: str,
) -> int:
    failed = False
    fd = -1
    try:
        if mode is None:
            fd = os.open(path, flags, dir_fd=dir_fd)
        else:
            fd = os.open(path, flags, mode, dir_fd=dir_fd)
    except OSError:
        failed = True
    if failed:
        raise SafetyError(message) from None
    return fd


def _safe_stat_at(parent_fd: int, name: str, *, message: str) -> os.stat_result:
    failed = False
    metadata: os.stat_result | None = None
    try:
        metadata = os.stat(name, dir_fd=parent_fd, follow_symlinks=False)
    except OSError:
        failed = True
    if failed or metadata is None:
        raise SafetyError(message) from None
    return metadata


def _safe_fstat(fd: int, *, message: str) -> os.stat_result:
    failed = False
    metadata: os.stat_result | None = None
    try:
        metadata = os.fstat(fd)
    except OSError:
        failed = True
    if failed or metadata is None:
        raise SafetyError(message) from None
    return metadata


def _safe_mkdir_at(parent_fd: int, name: str, mode: int) -> bool:
    exists = False
    failed = False
    try:
        os.mkdir(name, mode, dir_fd=parent_fd)
    except FileExistsError:
        exists = True
    except OSError:
        failed = True
    if failed:
        raise SafetyError("Cannot create evidence candidate directory safely") from None
    return not exists


def _safe_listdir(directory_fd: int) -> tuple[str, ...]:
    failed = False
    entries: list[str] = []
    try:
        entries = os.listdir(directory_fd)
    except OSError:
        failed = True
    if failed or any(type(entry) is not str or not entry for entry in entries):
        raise SafetyError("Cannot list evidence candidate directory safely") from None
    return tuple(sorted(entries))


def _fchmod_fd(fd: int, mode: int) -> None:
    failed = False
    try:
        os.fchmod(fd, mode)
    except OSError:
        failed = True
    if failed:
        raise SafetyError("Cannot set evidence candidate permissions safely") from None


def _fsync_fd(fd: int) -> None:
    failed = False
    try:
        os.fsync(fd)
    except OSError:
        failed = True
    if failed:
        raise SafetyError("Cannot fsync evidence candidate data safely") from None


def _close_fd(fd: int | None) -> None:
    if fd is not None:
        with suppress(OSError):
            os.close(fd)


def _close_directory_fds(directory_fds: Mapping[str, int]) -> None:
    for relative in reversed(_DIRECTORY_PATHS):
        _close_fd(directory_fds.get(relative))


def _register_directory_fd(
    directory_fds: dict[str, int],
    relative: str,
    fd: int,
) -> None:
    directory_fds[relative] = fd


def _revalidate_directory_binding(
    parent_fd: int,
    name: str,
    fd: int,
    *,
    label: str,
) -> None:
    held = _safe_fstat(fd, message=f"Cannot inspect {label} safely")
    current = _safe_stat_at(parent_fd, name, message=f"Cannot revalidate {label} safely")
    _validate_public_directory(held, label=label)
    _validate_public_directory(current, label=label)
    if not _same_identity(held, current):
        raise SafetyError(f"{label} binding changed")


def _same_identity(left: os.stat_result, right: os.stat_result) -> bool:
    return (left.st_dev, left.st_ino) == (right.st_dev, right.st_ino)


def _same_identity_fds(left_fd: int, right_fd: int) -> bool:
    return _same_identity(
        _safe_fstat(left_fd, message="Cannot inspect evidence directory identity safely"),
        _safe_fstat(right_fd, message="Cannot inspect evidence directory identity safely"),
    )


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


def _split_relative(relative: str) -> tuple[str, str]:
    parent, separator, name = relative.rpartition("/")
    if not separator:
        return "", relative
    return parent, name
