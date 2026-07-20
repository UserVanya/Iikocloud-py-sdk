from __future__ import annotations

import ctypes
import dataclasses
import errno
import json
import os
import socket
import stat
from collections.abc import Callable, Iterator, Mapping
from pathlib import Path, PosixPath
from types import MappingProxyType
from typing import Any, cast, get_type_hints

import pytest
from test_evidence_analysis import _pairs
from test_evidence_candidates import _retained_items, _reviewed_schema

import tools.openapi_pipeline.evidence_candidate_writer as writer_module
from tools.openapi_pipeline.errors import SafetyError
from tools.openapi_pipeline.evidence_analysis import analyze_menu_evidence
from tools.openapi_pipeline.evidence_candidate_contract import (
    EVIDENCE_CANDIDATE_PAYLOAD_PATHS,
    MANIFEST_SCHEMA_VERSION,
    MANIFEST_TOOL_NAME,
    MANIFEST_TOOL_VERSION,
)
from tools.openapi_pipeline.evidence_candidate_store import (
    EvidenceCandidateManifestResult,
    build_evidence_candidate_manifest,
)
from tools.openapi_pipeline.evidence_candidate_writer import (
    EvidenceCandidateWriteResult,
    write_evidence_candidate_tree,
)
from tools.openapi_pipeline.evidence_candidates import build_evidence_candidate_bundle
from tools.openapi_pipeline.io import canonical_json_bytes, sha256_bytes
from tools.openapi_pipeline.paths import RepoPaths

SENSITIVE_MARKER = "caller-private-sensitive-marker"


class _CallbackMapping(Mapping[Any, Any]):
    def __init__(self, values: Mapping[Any, Any], callback: Callable[[], None]) -> None:
        self._values = values
        self._callback = callback

    def __iter__(self) -> Iterator[Any]:
        self._callback()
        return iter(self._values)

    def __getitem__(self, key: Any) -> Any:
        return self._values[key]

    def __len__(self) -> int:
        return len(self._values)


def _result():
    schema = _reviewed_schema()
    pairs = _pairs(schema, _retained_items(), order=(4, 2, 3))
    bundle = build_evidence_candidate_bundle(
        analysis=analyze_menu_evidence(pairs, schema),
        pairs=pairs,
        effective_schema=schema,
    )
    return build_evidence_candidate_manifest(bundle)


def _repository(tmp_path: Path) -> RepoPaths:
    root = tmp_path / "repository"
    root.mkdir(mode=0o755)
    (root / "pyproject.toml").write_text("[project]\nname='test'\n", encoding="utf-8")
    build = root / "build"
    build.mkdir(mode=0o755)
    build.chmod(0o755)
    return RepoPaths(root)


def _expected_files(result) -> dict[str, bytes]:
    return {
        "candidate-manifest.json": result.canonical_json_bytes,
        **dict(result.canonical_payloads),
    }


def _plain(value: Any) -> Any:
    if isinstance(value, Mapping):
        return {key: _plain(child) for key, child in value.items()}
    if type(value) is tuple:
        return [_plain(child) for child in value]
    return value


def _freeze(value: Any) -> Any:
    if type(value) is dict:
        return MappingProxyType({key: _freeze(child) for key, child in value.items()})
    if type(value) is list:
        return tuple(_freeze(child) for child in value)
    return value


def _forged_result(
    result: EvidenceCandidateManifestResult,
    *,
    payload_update: tuple[str, bytes] | None = None,
    manifest_update: Callable[[dict[str, Any]], None] | None = None,
) -> EvidenceCandidateManifestResult:
    payloads = dict(result.canonical_payloads)
    if payload_update is not None:
        payloads[payload_update[0]] = payload_update[1]
    manifest = cast(dict[str, Any], _plain(result.manifest))
    manifest["files"] = {
        path: sha256_bytes(payloads[path]) for path in EVIDENCE_CANDIDATE_PAYLOAD_PATHS
    }
    if manifest_update is not None:
        manifest_update(manifest)
    body = canonical_json_bytes(manifest)
    return EvidenceCandidateManifestResult(
        manifest=_freeze(manifest),
        canonical_payloads=MappingProxyType(payloads),
        canonical_json_bytes=body,
        sha256=sha256_bytes(body),
    )


def _write_tree_directly(
    paths: RepoPaths,
    result: EvidenceCandidateManifestResult,
    *,
    changed_path: str | None = None,
) -> Path:
    root = paths.build / "evidence-candidates"
    for directory in (
        root,
        root / "openapi",
        root / "openapi/overlays",
        root / "tests",
        root / "tests/fixtures",
        root / "tests/fixtures/contracts",
    ):
        directory.mkdir(mode=0o755, parents=True, exist_ok=True)
        directory.chmod(0o755)
    for relative, body in _expected_files(result).items():
        target = root / relative
        if relative == changed_path:
            body += b"\n"
        target.write_bytes(body)
        target.chmod(0o644)
    return root


def _assert_sanitized(error: SafetyError) -> None:
    assert SENSITIVE_MARKER not in str(error)
    assert SENSITIVE_MARKER not in repr(error)
    assert error.__cause__ is None
    assert error.__context__ is None


def _assert_empty_build(paths: RepoPaths) -> None:
    assert paths.build.is_dir()
    assert stat.S_IMODE(os.lstat(paths.build).st_mode) == 0o755
    assert list(paths.build.iterdir()) == []


def _single_staging_residue(paths: RepoPaths) -> Path:
    residues = list(paths.build.glob(".evidence-candidates.tmp-*"))
    assert len(residues) == 1
    return residues[0]


def _assert_public_staging_subset(
    staging: Path,
    result: EvidenceCandidateManifestResult,
) -> None:
    expected_files = _expected_files(result)
    expected_directories = {
        "openapi",
        "openapi/overlays",
        "tests",
        "tests/fixtures",
        "tests/fixtures/contracts",
    }
    root_metadata = os.lstat(staging)
    assert stat.S_ISDIR(root_metadata.st_mode)
    assert stat.S_IMODE(root_metadata.st_mode) == 0o755
    for path in staging.rglob("*"):
        metadata = os.lstat(path)
        relative = path.relative_to(staging).as_posix()
        if stat.S_ISDIR(metadata.st_mode):
            assert relative in expected_directories
            assert stat.S_IMODE(metadata.st_mode) == 0o755
            continue
        assert stat.S_ISREG(metadata.st_mode)
        assert relative in expected_files
        assert stat.S_IMODE(metadata.st_mode) == 0o644
        assert path.read_bytes() == expected_files[relative]


def _assert_complete_staging(
    staging: Path,
    result: EvidenceCandidateManifestResult,
) -> None:
    _assert_public_staging_subset(staging, result)
    assert {
        path.relative_to(staging).as_posix() for path in staging.rglob("*") if path.is_file()
    } == set(_expected_files(result))


def test_writer_atomically_publishes_exact_candidate_tree(tmp_path: Path) -> None:
    result = _result()
    paths = _repository(tmp_path)

    written = write_evidence_candidate_tree(result, paths)

    root = paths.build / "evidence-candidates"
    assert written == EvidenceCandidateWriteResult(
        root=root,
        manifest_path=root / "candidate-manifest.json",
        manifest_sha256=result.sha256,
        changed=True,
    )
    expected = _expected_files(result)
    actual = {
        path.relative_to(root).as_posix(): path.read_bytes()
        for path in root.rglob("*")
        if path.is_file()
    }
    assert actual == expected
    assert sorted(
        path.relative_to(root).as_posix() for path in root.rglob("*") if path.is_dir()
    ) == [
        "openapi",
        "openapi/overlays",
        "tests",
        "tests/fixtures",
        "tests/fixtures/contracts",
    ]
    assert paths.build.stat().st_mode & 0o777 == 0o755
    assert root.stat().st_mode & 0o777 == 0o755
    assert all(path.stat().st_mode & 0o777 == 0o755 for path in root.rglob("*") if path.is_dir())
    assert all(path.stat().st_mode & 0o777 == 0o644 for path in root.rglob("*") if path.is_file())
    assert not list(paths.build.glob(".evidence-candidates.tmp-*"))


def test_writer_identical_existing_tree_is_untouched(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    result = _result()
    paths = _repository(tmp_path)
    first = write_evidence_candidate_tree(result, paths)
    before = {
        path.relative_to(first.root).as_posix(): (
            os.lstat(path).st_ino,
            os.lstat(path).st_mtime_ns,
            os.lstat(path).st_ctime_ns,
        )
        for path in (first.root, *first.root.rglob("*"))
    }

    def forbidden(*_args: Any, **_kwargs: Any) -> Any:
        raise AssertionError("identical no-op must not enter staging or write helpers")

    monkeypatch.setattr(writer_module, "_create_staging_directory", forbidden)
    monkeypatch.setattr(writer_module, "_write_file_at", forbidden)
    monkeypatch.setattr(writer_module, "_rename_directory_noreplace", forbidden)

    second = write_evidence_candidate_tree(result, paths)

    after = {
        path.relative_to(first.root).as_posix(): (
            os.lstat(path).st_ino,
            os.lstat(path).st_mtime_ns,
            os.lstat(path).st_ctime_ns,
        )
        for path in (first.root, *first.root.rglob("*"))
    }
    assert second == EvidenceCandidateWriteResult(
        root=first.root,
        manifest_path=first.manifest_path,
        manifest_sha256=result.sha256,
        changed=False,
    )
    assert after == before
    assert not list(paths.build.glob(".evidence-candidates.tmp-*"))


def test_writer_uses_only_detached_manifest_result(tmp_path: Path) -> None:
    result = _result()
    paths = _repository(tmp_path)

    written = write_evidence_candidate_tree(result, paths)

    assert {
        path.relative_to(written.root).as_posix(): path.read_bytes()
        for path in written.root.rglob("*")
        if path.is_file()
    } == _expected_files(result)
    assert tuple(result.canonical_payloads) == EVIDENCE_CANDIDATE_PAYLOAD_PATHS


def test_writer_runtime_type_hints_are_exact() -> None:
    hints = get_type_hints(write_evidence_candidate_tree)

    assert hints == {
        "result": EvidenceCandidateManifestResult,
        "paths": RepoPaths,
        "return": EvidenceCandidateWriteResult,
    }


@pytest.mark.parametrize(
    "forge",
    [
        lambda result: dataclasses.replace(result, canonical_json_bytes=b"{}\n"),
        lambda result: dataclasses.replace(result, sha256="0" * 64),
        lambda result: _forged_result(
            result,
            manifest_update=lambda value: value.__setitem__("schema_version", 2),
        ),
        lambda result: _forged_result(
            result,
            manifest_update=lambda value: value.__setitem__(
                "tool", {"name": MANIFEST_TOOL_NAME, "version": MANIFEST_TOOL_VERSION + 1}
            ),
        ),
        lambda result: _forged_result(
            result,
            manifest_update=lambda value: value.__setitem__("operation_id", "other"),
        ),
        lambda result: _forged_result(
            result,
            manifest_update=lambda value: value["evidence_provenance"].pop("2"),
        ),
        lambda result: dataclasses.replace(
            result,
            canonical_payloads=MappingProxyType(
                dict(reversed(tuple(result.canonical_payloads.items())))
            ),
        ),
    ],
    ids=[
        "manifest-bytes",
        "detached-digest",
        "schema-version",
        "tool-version",
        "operation",
        "provenance",
        "payload-order",
    ],
)
def test_writer_rejects_forged_result_before_filesystem_mutation(
    tmp_path: Path,
    forge: Callable[[EvidenceCandidateManifestResult], EvidenceCandidateManifestResult],
) -> None:
    paths = _repository(tmp_path)

    with pytest.raises(SafetyError):
        write_evidence_candidate_tree(forge(_result()), paths)

    _assert_empty_build(paths)


def test_writer_requires_exact_result_and_paths_types_before_mutation(tmp_path: Path) -> None:
    paths = _repository(tmp_path)

    class ResultSubclass(EvidenceCandidateManifestResult):
        pass

    class PathsSubclass(RepoPaths):
        pass

    result = _result()
    subclassed = ResultSubclass(
        result.manifest,
        result.canonical_payloads,
        result.canonical_json_bytes,
        result.sha256,
    )
    with pytest.raises(SafetyError, match="exact"):
        write_evidence_candidate_tree(subclassed, paths)
    with pytest.raises(SafetyError, match="exact"):
        write_evidence_candidate_tree(result, PathsSubclass(paths.root))

    _assert_empty_build(paths)


def test_writer_reparses_and_reencodes_every_payload_before_mutation(tmp_path: Path) -> None:
    paths = _repository(tmp_path)
    result = _result()
    overlay_path = EVIDENCE_CANDIDATE_PAYLOAD_PATHS[0]
    fixture_path = EVIDENCE_CANDIDATE_PAYLOAD_PATHS[-1]
    noncanonical_overlay = b"---\n" + result.canonical_payloads[overlay_path]
    fixture_value = json.loads(result.canonical_payloads[fixture_path])
    noncanonical_fixture = json.dumps(fixture_value, sort_keys=True).encode()

    for forged in (
        _forged_result(result, payload_update=(overlay_path, noncanonical_overlay)),
        _forged_result(result, payload_update=(fixture_path, noncanonical_fixture)),
    ):
        with pytest.raises(SafetyError, match="canonical"):
            write_evidence_candidate_tree(forged, paths)

    _assert_empty_build(paths)


def test_writer_rescans_self_consistent_secret_bearing_payload_before_mutation(
    tmp_path: Path,
) -> None:
    paths = _repository(tmp_path)
    result = _result()
    fixture_path = EVIDENCE_CANDIDATE_PAYLOAD_PATHS[2]
    fixture = json.loads(result.canonical_payloads[fixture_path])
    fixture["api_key"] = SENSITIVE_MARKER
    forged = _forged_result(
        result,
        payload_update=(fixture_path, canonical_json_bytes(fixture)),
    )

    with pytest.raises(SafetyError) as caught:
        write_evidence_candidate_tree(forged, paths)

    _assert_sanitized(caught.value)
    _assert_empty_build(paths)


def test_writer_sanitizes_caller_mapping_exception_and_does_not_mutate(
    tmp_path: Path,
) -> None:
    paths = _repository(tmp_path)
    result = _result()

    def fail() -> None:
        raise RuntimeError(SENSITIVE_MARKER)

    forged = dataclasses.replace(
        result,
        canonical_payloads=MappingProxyType(_CallbackMapping(result.canonical_payloads, fail)),
    )

    with pytest.raises(SafetyError) as caught:
        write_evidence_candidate_tree(forged, paths)

    _assert_sanitized(caught.value)
    _assert_empty_build(paths)


def test_writer_snapshots_all_result_fields_before_caller_callback(tmp_path: Path) -> None:
    paths = _repository(tmp_path)
    original = _result()
    expected = dataclasses.replace(original)
    holder: dict[str, EvidenceCandidateManifestResult] = {}

    def mutate_result() -> None:
        target = holder["result"]
        object.__setattr__(target, "manifest", MappingProxyType({}))
        object.__setattr__(target, "canonical_json_bytes", SENSITIVE_MARKER.encode())
        object.__setattr__(target, "sha256", SENSITIVE_MARKER)

    forged = dataclasses.replace(
        original,
        canonical_payloads=MappingProxyType(
            _CallbackMapping(original.canonical_payloads, mutate_result)
        ),
    )
    holder["result"] = forged

    written = write_evidence_candidate_tree(forged, paths)

    assert written.manifest_sha256 == expected.sha256
    assert _expected_files(expected) == {
        path.relative_to(written.root).as_posix(): path.read_bytes()
        for path in written.root.rglob("*")
        if path.is_file()
    }


@pytest.mark.parametrize("exception_type", [MemoryError, KeyboardInterrupt, SystemExit])
def test_writer_does_not_swallow_caller_base_exceptions(
    tmp_path: Path,
    exception_type: type[BaseException],
) -> None:
    paths = _repository(tmp_path)
    result = _result()

    def fail() -> None:
        raise exception_type(SENSITIVE_MARKER)

    forged = dataclasses.replace(
        result,
        canonical_payloads=MappingProxyType(_CallbackMapping(result.canonical_payloads, fail)),
    )

    with pytest.raises(exception_type):
        write_evidence_candidate_tree(forged, paths)

    _assert_empty_build(paths)


def test_writer_does_not_mask_trusted_internal_errors(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    paths = _repository(tmp_path)
    sentinel = RuntimeError("trusted canonical encoder failure")

    def fail(_value: Any) -> bytes:
        raise sentinel

    monkeypatch.setattr(writer_module, "canonical_json_bytes", fail)

    with pytest.raises(RuntimeError) as caught:
        write_evidence_candidate_tree(_result(), paths)

    assert caught.value is sentinel
    _assert_empty_build(paths)


@pytest.mark.parametrize("state", ["different", "partial", "extra"])
def test_writer_refuses_nonidentical_existing_candidate_without_clobber(
    tmp_path: Path,
    state: str,
) -> None:
    paths = _repository(tmp_path)
    result = _result()
    root = paths.build / "evidence-candidates"
    if state == "partial":
        root.mkdir(parents=True, mode=0o755)
        root.chmod(0o755)
    else:
        write_evidence_candidate_tree(result, paths)
        if state == "different":
            target = root / EVIDENCE_CANDIDATE_PAYLOAD_PATHS[0]
            target.write_bytes(target.read_bytes() + b"\n")
            target.chmod(0o644)
        else:
            (root / "unexpected.txt").write_bytes(b"unexpected")
            (root / "unexpected.txt").chmod(0o644)
    before = {
        path.relative_to(root).as_posix(): (
            os.lstat(path).st_mode,
            os.lstat(path).st_ino,
            path.read_bytes() if path.is_file() else None,
        )
        for path in (root, *root.rglob("*"))
    }

    with pytest.raises(SafetyError):
        write_evidence_candidate_tree(result, paths)

    after = {
        path.relative_to(root).as_posix(): (
            os.lstat(path).st_mode,
            os.lstat(path).st_ino,
            path.read_bytes() if path.is_file() else None,
        )
        for path in (root, *root.rglob("*"))
    }
    assert after == before
    assert not list(paths.build.glob(".evidence-candidates.tmp-*"))


@pytest.mark.parametrize(
    "unsafe_kind",
    ["directory-symlink", "file-symlink", "hardlink", "fifo", "socket"],
)
def test_writer_rejects_unsafe_existing_nested_entry_without_reading_it(
    tmp_path: Path,
    unsafe_kind: str,
) -> None:
    paths = _repository(tmp_path)
    result = _result()
    root = _write_tree_directly(paths, result)
    outside = tmp_path / "outside"
    outside.mkdir(mode=0o755)
    socket_handle: socket.socket | None = None
    if unsafe_kind == "directory-symlink":
        target = root / "tests/fixtures/contracts"
        moved = root / "contracts-real"
        target.rename(moved)
        target.symlink_to(outside, target_is_directory=True)
    elif unsafe_kind == "socket":
        target = root / "unsafe.sock"
        socket_handle = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        previous_cwd = Path.cwd()
        try:
            os.chdir(root)
            socket_handle.bind(target.name)
        finally:
            os.chdir(previous_cwd)
    else:
        target = root / "candidate-manifest.json"
        target.unlink()
        external_file = outside / "external.json"
        external_file.write_bytes(result.canonical_json_bytes)
        external_file.chmod(0o644)
        if unsafe_kind == "file-symlink":
            target.symlink_to(external_file)
        elif unsafe_kind == "hardlink":
            target.hardlink_to(external_file)
        elif unsafe_kind == "fifo":
            os.mkfifo(target, mode=0o644)

    try:
        with pytest.raises(SafetyError, match="symlink|hard|regular|entry|tree|directory"):
            write_evidence_candidate_tree(result, paths)
    finally:
        if socket_handle is not None:
            socket_handle.close()

    assert not list(paths.build.glob(".evidence-candidates.tmp-*"))
    assert not list(outside.glob(".evidence-candidates.tmp-*"))


@pytest.mark.parametrize("wrong_kind", ["file-mode", "directory-mode", "owner"])
def test_writer_rejects_wrong_mode_or_owner_without_repairing_existing_tree(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    wrong_kind: str,
) -> None:
    paths = _repository(tmp_path)
    result = _result()
    root = _write_tree_directly(paths, result)
    if wrong_kind == "file-mode":
        target = root / "candidate-manifest.json"
        target.chmod(0o600)
    elif wrong_kind == "directory-mode":
        target = root / "openapi"
        target.chmod(0o700)
    else:
        target = root
        current_uid = os.getuid()
        monkeypatch.setattr(writer_module.os, "getuid", lambda: current_uid + 1)
    before_mode = target.stat().st_mode

    with pytest.raises(SafetyError, match="mode|owned|owner"):
        write_evidence_candidate_tree(result, paths)

    assert target.stat().st_mode == before_mode


def test_writer_rejects_device_metadata_without_opening_special_entry(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    regular = os.stat_result((stat.S_IFCHR | 0o644, 1, 1, 1, os.getuid(), 0, 0, 0, 0, 0))

    with pytest.raises(SafetyError, match="regular"):
        writer_module._validate_public_file(regular, label="candidate")


def test_writer_rejects_symlinked_repository_root_without_external_writes(
    tmp_path: Path,
) -> None:
    real_paths = _repository(tmp_path)
    alias = tmp_path / "repository-link"
    alias.symlink_to(real_paths.root, target_is_directory=True)

    with pytest.raises(SafetyError, match="symlink|canonical|directory"):
        write_evidence_candidate_tree(_result(), RepoPaths(alias))

    _assert_empty_build(real_paths)


@pytest.mark.parametrize("kind", ["build", "candidate"])
def test_writer_rejects_symlinked_build_or_candidate_without_external_writes(
    tmp_path: Path,
    kind: str,
) -> None:
    paths = _repository(tmp_path)
    outside = tmp_path / "outside"
    outside.mkdir(mode=0o755)
    if kind == "build":
        paths.build.rmdir()
        paths.build.symlink_to(outside, target_is_directory=True)
    else:
        (paths.build / "evidence-candidates").symlink_to(
            outside,
            target_is_directory=True,
        )

    with pytest.raises(SafetyError, match="symlink|directory|safe"):
        write_evidence_candidate_tree(_result(), paths)

    assert list(outside.iterdir()) == []


def test_writer_requires_existing_canonical_repository_with_project_marker(
    tmp_path: Path,
) -> None:
    missing = tmp_path / "missing"
    with pytest.raises(SafetyError, match="repository|missing"):
        write_evidence_candidate_tree(_result(), RepoPaths(missing))
    assert not missing.exists()

    root = tmp_path / "without-marker"
    root.mkdir(mode=0o755)
    with pytest.raises(SafetyError, match="marker|pyproject"):
        write_evidence_candidate_tree(_result(), RepoPaths(root))
    assert not (root / "build").exists()


def test_writer_requires_preexisting_build_without_trying_to_create_it(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    paths = _repository(tmp_path)
    paths.build.rmdir()
    real_mkdir = writer_module.os.mkdir
    fixed_build_mkdir_calls = 0

    def observe_mkdir(
        path: str | bytes,
        mode: int = 0o777,
        *,
        dir_fd: int | None = None,
    ) -> None:
        nonlocal fixed_build_mkdir_calls
        if path == "build" and dir_fd is not None:
            fixed_build_mkdir_calls += 1
        real_mkdir(path, mode, dir_fd=dir_fd)

    monkeypatch.setattr(writer_module.os, "mkdir", observe_mkdir)

    with pytest.raises(SafetyError, match="build|missing|safe"):
        write_evidence_candidate_tree(_result(), paths)

    assert fixed_build_mkdir_calls == 0
    assert not paths.build.exists()


def test_writer_rejects_path_subclass_callback_before_mutation(tmp_path: Path) -> None:
    paths = _repository(tmp_path)

    class RaisingPath(PosixPath):
        def is_absolute(self) -> bool:
            raise RuntimeError(SENSITIVE_MARKER)

    forged_root = RaisingPath(str(paths.root))

    with pytest.raises(SafetyError) as caught:
        write_evidence_candidate_tree(_result(), RepoPaths(forged_root))

    _assert_sanitized(caught.value)
    _assert_empty_build(paths)


def test_writer_rejects_existing_build_with_wrong_mode_without_repair(
    tmp_path: Path,
) -> None:
    paths = _repository(tmp_path)
    paths.build.chmod(0o700)

    with pytest.raises(SafetyError, match="0755|mode"):
        write_evidence_candidate_tree(_result(), paths)

    assert paths.build.stat().st_mode & 0o777 == 0o700
    assert list(paths.build.iterdir()) == []


def test_writer_never_calls_mkdir_for_fixed_build_at_syscall_boundary(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    paths = _repository(tmp_path)
    result = _result()
    real_mkdir = writer_module.os.mkdir
    original = os.lstat(paths.build)
    displaced = paths.root / "displaced-build"
    fixed_build_mkdir_calls = 0

    def swap_if_fixed_build_is_created(
        path: str | bytes,
        mode: int = 0o777,
        *,
        dir_fd: int | None = None,
    ) -> None:
        nonlocal fixed_build_mkdir_calls
        if path == "build" and dir_fd is not None:
            fixed_build_mkdir_calls += 1
            paths.build.rename(displaced)
            real_mkdir("build", 0o700, dir_fd=dir_fd)
            return
        real_mkdir(path, mode, dir_fd=dir_fd)

    monkeypatch.setattr(writer_module.os, "mkdir", swap_if_fixed_build_is_created)

    written = write_evidence_candidate_tree(result, paths)

    current = os.lstat(paths.build)
    assert fixed_build_mkdir_calls == 0
    assert (current.st_dev, current.st_ino, stat.S_IMODE(current.st_mode)) == (
        original.st_dev,
        original.st_ino,
        0o755,
    )
    assert written.changed is True
    assert not displaced.exists()


def test_writer_rejects_swapped_preexisting_build_before_staging(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    paths = _repository(tmp_path)
    real_open = writer_module._open_public_directory_from_metadata
    displaced = paths.root / "displaced-build"
    holder: dict[str, os.stat_result] = {}

    def swap_before_open(
        parent_fd: int,
        name: str,
        expected: os.stat_result,
        *,
        label: str,
        validate_mode: bool = True,
    ) -> int:
        if label == "Evidence build root":
            paths.build.rename(displaced)
            paths.build.mkdir(mode=0o755)
            paths.build.chmod(0o755)
            holder["foreign"] = os.lstat(paths.build)
        return real_open(
            parent_fd,
            name,
            expected,
            label=label,
            validate_mode=validate_mode,
        )

    monkeypatch.setattr(
        writer_module,
        "_open_public_directory_from_metadata",
        swap_before_open,
    )

    with pytest.raises(SafetyError, match="changed|binding"):
        write_evidence_candidate_tree(_result(), paths)

    foreign = holder["foreign"]
    current = os.lstat(paths.build)
    assert (current.st_dev, current.st_ino, stat.S_IMODE(current.st_mode)) == (
        foreign.st_dev,
        foreign.st_ino,
        0o755,
    )
    assert displaced.is_dir()
    assert not list(paths.build.iterdir())


def test_existing_file_reads_are_nofollow_nonblocking_and_bounded(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    paths = _repository(tmp_path)
    result = _result()
    write_evidence_candidate_tree(result, paths)
    real_open = writer_module.os.open
    real_read = writer_module.os.read
    file_flags: list[int] = []
    read_sizes: list[tuple[str, int]] = []

    def observe_open(*args: Any, **kwargs: Any) -> int:
        fd = real_open(*args, **kwargs)
        path = args[0]
        if type(path) is str and path.endswith((".json", ".yaml")):
            file_flags.append(args[1])
        return fd

    def observe_read(fd: int, size: int) -> bytes:
        target = os.readlink(f"/proc/self/fd/{fd}")
        if target.endswith((".json", ".yaml")):
            read_sizes.append((target, size))
            expected = next(
                len(body)
                for relative, body in _expected_files(result).items()
                if target.endswith(relative)
            )
            assert size <= expected + 1
        return real_read(fd, size)

    monkeypatch.setattr(writer_module.os, "open", observe_open)
    monkeypatch.setattr(writer_module.os, "read", observe_read)

    unchanged = write_evidence_candidate_tree(result, paths)

    assert unchanged.changed is False
    assert file_flags
    assert all(flags & os.O_NOFOLLOW for flags in file_flags)
    assert all(flags & os.O_NONBLOCK for flags in file_flags)
    assert read_sizes


def test_filesystem_fstat_marker_error_is_sanitized_and_fds_close(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    paths = _repository(tmp_path)
    real_fstat = writer_module.os.fstat
    calls = 0

    def fail_first(fd: int) -> os.stat_result:
        nonlocal calls
        calls += 1
        if calls == 1:
            raise OSError(SENSITIVE_MARKER)
        return real_fstat(fd)

    monkeypatch.setattr(writer_module.os, "fstat", fail_first)

    with pytest.raises(SafetyError) as caught:
        write_evidence_candidate_tree(_result(), paths)

    _assert_sanitized(caught.value)
    _assert_empty_build(paths)


@pytest.mark.parametrize("primitive", ["nofollow", "renameat2"])
def test_writer_requires_secure_publication_primitives_before_mutation(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    primitive: str,
) -> None:
    paths = _repository(tmp_path)
    if primitive == "nofollow":
        monkeypatch.setattr(writer_module.os, "O_NOFOLLOW", 0)
    else:
        monkeypatch.setattr(writer_module, "_load_renameat2", lambda: None)

    with pytest.raises(SafetyError, match="unavailable"):
        write_evidence_candidate_tree(_result(), paths)

    _assert_empty_build(paths)


def test_writer_probes_renameat2_kernel_support_before_mutation(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    paths = _repository(tmp_path)

    def unsupported(*_args: Any) -> int:
        ctypes.set_errno(errno.ENOSYS)
        return -1

    monkeypatch.setattr(writer_module, "_load_renameat2", lambda: unsupported)

    with pytest.raises(SafetyError, match="unavailable"):
        write_evidence_candidate_tree(_result(), paths)

    _assert_empty_build(paths)


@pytest.mark.parametrize("error_number", [errno.EPERM, errno.EACCES, errno.EIO])
def test_writer_rejects_ambiguous_renameat2_probe_before_mutation(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    error_number: int,
) -> None:
    paths = _repository(tmp_path)

    def ambiguous(*_args: Any) -> int:
        ctypes.set_errno(error_number)
        return -1

    monkeypatch.setattr(writer_module, "_load_renameat2", lambda: ambiguous)

    with pytest.raises(SafetyError, match="unavailable"):
        write_evidence_candidate_tree(_result(), paths)

    _assert_empty_build(paths)


@pytest.mark.parametrize(
    ("result", "error_number", "supported"),
    [
        (-1, errno.EBADF, True),
        (-1, errno.EPERM, False),
        (-1, errno.EACCES, False),
        (-1, errno.EIO, False),
        (0, 0, False),
    ],
)
def test_renameat2_probe_accepts_only_precise_ebadf(
    result: int,
    error_number: int,
    supported: bool,
) -> None:
    def probe(*_args: Any) -> int:
        ctypes.set_errno(error_number)
        return result

    assert writer_module._probe_renameat2(probe) is supported


@pytest.mark.parametrize("failure", ["write", "fsync", "rename"])
def test_writer_preserves_safe_staging_and_primary_on_prerename_failure(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    failure: str,
) -> None:
    paths = _repository(tmp_path)
    result = _result()
    sentinel = OSError(f"synthetic {failure} failure")
    real_open = writer_module.os.open
    opened: list[int] = []

    def tracking_open(*args: Any, **kwargs: Any) -> int:
        fd = real_open(*args, **kwargs)
        opened.append(fd)
        return fd

    monkeypatch.setattr(writer_module.os, "open", tracking_open)
    if failure == "write":
        real_write = writer_module._write_file_at
        calls = 0

        def fail_write(directory_fd: int, name: str, body: bytes) -> Any:
            nonlocal calls
            calls += 1
            if calls == 2:
                raise sentinel
            return real_write(directory_fd, name, body)

        monkeypatch.setattr(writer_module, "_write_file_at", fail_write)
    elif failure == "fsync":
        real_fsync = writer_module._fsync_fd

        def fail_staging_fsync(fd: int) -> None:
            target = os.readlink(f"/proc/self/fd/{fd}")
            if ".evidence-candidates.tmp-" in target:
                raise sentinel
            real_fsync(fd)

        monkeypatch.setattr(writer_module, "_fsync_fd", fail_staging_fsync)
    else:

        def fail_rename(*_args: Any, **_kwargs: Any) -> None:
            raise sentinel

        monkeypatch.setattr(writer_module, "_rename_directory_noreplace", fail_rename)

    with pytest.raises(OSError) as caught:
        write_evidence_candidate_tree(result, paths)

    assert caught.value is sentinel
    assert not (paths.build / "evidence-candidates").exists()
    _assert_public_staging_subset(_single_staging_residue(paths), result)
    for fd in opened:
        with pytest.raises(OSError):
            os.fstat(fd)


@pytest.mark.parametrize("exception_type", [KeyboardInterrupt, SystemExit])
def test_writer_preserves_safe_staging_and_injected_base_exception(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    exception_type: type[BaseException],
) -> None:
    paths = _repository(tmp_path)

    def fail(*_args: Any, **_kwargs: Any) -> None:
        raise exception_type(SENSITIVE_MARKER)

    monkeypatch.setattr(writer_module, "_write_file_at", fail)

    result = _result()
    with pytest.raises(exception_type) as caught:
        write_evidence_candidate_tree(result, paths)

    assert caught.value.args == (SENSITIVE_MARKER,)
    assert not (paths.build / "evidence-candidates").exists()
    _assert_public_staging_subset(_single_staging_residue(paths), result)


def test_writer_never_calls_unlink_or_rmdir_on_failure(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    paths = _repository(tmp_path)
    result = _result()
    primary = RuntimeError("synthetic primary failure")
    removal_calls: list[str] = []

    def fail_rename(*_args: Any, **_kwargs: Any) -> None:
        raise primary

    def forbidden_unlink(*_args: Any, **_kwargs: Any) -> None:
        removal_calls.append("unlink")
        raise AssertionError("writer must never unlink a staging entry")

    def forbidden_rmdir(*_args: Any, **_kwargs: Any) -> None:
        removal_calls.append("rmdir")
        raise AssertionError("writer must never remove a staging directory")

    monkeypatch.setattr(writer_module, "_rename_directory_noreplace", fail_rename)
    monkeypatch.setattr(writer_module.os, "unlink", forbidden_unlink)
    monkeypatch.setattr(writer_module.os, "rmdir", forbidden_rmdir)

    with pytest.raises(RuntimeError) as caught:
        write_evidence_candidate_tree(result, paths)

    assert caught.value is primary
    assert removal_calls == []
    assert not (paths.build / "evidence-candidates").exists()
    _assert_complete_staging(_single_staging_residue(paths), result)


def test_writer_never_fchmods_a_created_directory(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    paths = _repository(tmp_path)
    real_fchmod = writer_module.os.fchmod
    directory_calls: list[int] = []

    def reject_directory_fchmod(fd: int, mode: int) -> None:
        if stat.S_ISDIR(os.fstat(fd).st_mode):
            directory_calls.append(fd)
            raise AssertionError("created directories must never be repaired with fchmod")
        real_fchmod(fd, mode)

    monkeypatch.setattr(writer_module.os, "fchmod", reject_directory_fchmod)

    written = write_evidence_candidate_tree(_result(), paths)

    assert written.changed is True
    assert directory_calls == []


def test_writer_rejects_umask_narrowed_staging_mode_without_repair(
    tmp_path: Path,
) -> None:
    paths = _repository(tmp_path)
    previous_umask = os.umask(0o077)
    try:
        with pytest.raises(SafetyError, match="0755|mode"):
            write_evidence_candidate_tree(_result(), paths)
    finally:
        os.umask(previous_umask)

    assert not (paths.build / "evidence-candidates").exists()
    staging = _single_staging_residue(paths)
    assert stat.S_IMODE(os.lstat(staging).st_mode) == 0o700


def test_writer_rejects_current_staging_mode_change_before_first_child(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    paths = _repository(tmp_path)
    real_stat = writer_module._safe_stat_at
    real_mkdir = writer_module.os.mkdir
    child_mkdir_calls = 0

    def narrow_mode_before_current_stat(
        parent_fd: int,
        name: str,
        *,
        message: str,
    ) -> os.stat_result:
        if message == "Cannot revalidate Evidence candidate staging root safely":
            os.chmod(
                name,
                0o700,
                dir_fd=parent_fd,
                follow_symlinks=False,
            )
        return real_stat(parent_fd, name, message=message)

    def observe_mkdir(
        path: str | bytes,
        mode: int = 0o777,
        *,
        dir_fd: int | None = None,
    ) -> None:
        nonlocal child_mkdir_calls
        if path == "openapi":
            child_mkdir_calls += 1
        real_mkdir(path, mode, dir_fd=dir_fd)

    monkeypatch.setattr(writer_module, "_safe_stat_at", narrow_mode_before_current_stat)
    monkeypatch.setattr(writer_module.os, "mkdir", observe_mkdir)

    with pytest.raises(SafetyError, match="0755|mode"):
        write_evidence_candidate_tree(_result(), paths)

    assert child_mkdir_calls == 0
    staging = _single_staging_residue(paths)
    assert stat.S_IMODE(os.lstat(staging).st_mode) == 0o700


@pytest.mark.parametrize("registration", ["root", "child"])
def test_writer_closes_unregistered_directory_fd_on_memory_error(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    registration: str,
) -> None:
    paths = _repository(tmp_path)
    real_open = writer_module.os.open
    opened: list[int] = []

    def tracking_open(*args: Any, **kwargs: Any) -> int:
        fd = real_open(*args, **kwargs)
        opened.append(fd)
        return fd

    def fail_registration(
        directory_fds: dict[str, int],
        relative: str,
        fd: int,
    ) -> None:
        if relative == ("" if registration == "root" else "openapi"):
            raise MemoryError(SENSITIVE_MARKER)
        directory_fds[relative] = fd

    monkeypatch.setattr(writer_module.os, "open", tracking_open)
    monkeypatch.setattr(
        writer_module,
        "_register_directory_fd",
        fail_registration,
        raising=False,
    )

    with pytest.raises(MemoryError) as caught:
        write_evidence_candidate_tree(_result(), paths)

    assert caught.value.args == (SENSITIVE_MARKER,)
    assert not (paths.build / "evidence-candidates").exists()
    staging = _single_staging_residue(paths)
    _assert_public_staging_subset(staging, _result())
    assert not list(staging.rglob("*.json"))
    assert not list(staging.rglob("*.yaml"))
    assert opened
    for fd in opened:
        with pytest.raises(OSError):
            os.fstat(fd)


@pytest.mark.parametrize("winner", ["identical", "different"])
def test_writer_handles_concurrent_no_replace_winner_without_clobber(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    winner: str,
) -> None:
    paths = _repository(tmp_path)
    result = _result()
    real_rename = writer_module._rename_directory_noreplace

    def race_publish(*args: Any, **kwargs: Any) -> None:
        changed = "candidate-manifest.json" if winner == "different" else None
        _write_tree_directly(paths, result, changed_path=changed)
        real_rename(*args, **kwargs)

    monkeypatch.setattr(writer_module, "_rename_directory_noreplace", race_publish)

    expected_error = (
        "Concurrent evidence candidate publication preserved staging residue"
        if winner == "identical"
        else None
    )
    with pytest.raises(SafetyError, match=expected_error):
        write_evidence_candidate_tree(result, paths)

    root = paths.build / "evidence-candidates"
    expected_manifest = result.canonical_json_bytes
    if winner == "different":
        expected_manifest += b"\n"
    assert (root / "candidate-manifest.json").read_bytes() == expected_manifest
    _assert_complete_staging(_single_staging_residue(paths), result)


def test_postrename_revalidation_preserves_complete_final_name_and_fails_closed(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    paths = _repository(tmp_path)
    result = _result()
    displaced = paths.build / "displaced-original"
    real_revalidate = writer_module._revalidate_published_candidate

    def replace_then_revalidate(*args: Any, **kwargs: Any) -> None:
        root = paths.build / "evidence-candidates"
        root.rename(displaced)
        _write_tree_directly(paths, result, changed_path="candidate-manifest.json")
        real_revalidate(*args, **kwargs)

    monkeypatch.setattr(
        writer_module,
        "_revalidate_published_candidate",
        replace_then_revalidate,
    )

    with pytest.raises(SafetyError, match="changed|binding|identity"):
        write_evidence_candidate_tree(result, paths)

    replacement = paths.build / "evidence-candidates"
    assert (replacement / "candidate-manifest.json").read_bytes() == (
        result.canonical_json_bytes + b"\n"
    )
    assert displaced.is_dir()
    with pytest.raises(SafetyError):
        write_evidence_candidate_tree(result, paths)


def test_failure_preserves_primary_and_foreign_staging_replacement(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    paths = _repository(tmp_path)
    primary = RuntimeError("synthetic primary after staging swap")
    moved_holder: dict[str, Path] = {}

    def swap_staging_then_fail(directory_fd: int, _name: str, _body: bytes) -> None:
        staging = Path(os.readlink(f"/proc/self/fd/{directory_fd}"))
        moved = staging.with_name(staging.name + "-moved")
        staging.rename(moved)
        staging.mkdir(mode=0o755)
        sentinel = staging / "foreign-sentinel"
        sentinel.write_bytes(b"foreign")
        sentinel.chmod(0o644)
        moved_holder["path"] = moved
        raise primary

    monkeypatch.setattr(writer_module, "_write_file_at", swap_staging_then_fail)

    with pytest.raises(RuntimeError) as caught:
        write_evidence_candidate_tree(_result(), paths)

    assert caught.value is primary
    foreign = next(
        path
        for path in paths.build.glob(".evidence-candidates.tmp-*")
        if not path.name.endswith("-moved")
    )
    assert (foreign / "foreign-sentinel").read_bytes() == b"foreign"
    assert moved_holder["path"].is_dir()


def test_staging_open_failure_does_not_delete_swapped_foreign_directory(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    paths = _repository(tmp_path)
    real_open = writer_module._open_public_directory_from_metadata
    holder: dict[str, Any] = {}

    def swap_before_open(
        parent_fd: int,
        name: str,
        expected: os.stat_result,
        *,
        label: str,
        validate_mode: bool = True,
    ) -> int:
        if label == "Evidence candidate staging root":
            build = Path(os.readlink(f"/proc/self/fd/{parent_fd}"))
            staging = build / name
            displaced = build / f"{name}-writer-owned"
            staging.rename(displaced)
            staging.mkdir(mode=0o755)
            staging.chmod(0o755)
            holder.update(
                staging=staging,
                foreign=os.lstat(staging),
                displaced=displaced,
                displaced_inode=os.lstat(displaced).st_ino,
            )
        return real_open(
            parent_fd,
            name,
            expected,
            label=label,
            validate_mode=validate_mode,
        )

    monkeypatch.setattr(
        writer_module,
        "_open_public_directory_from_metadata",
        swap_before_open,
    )

    with pytest.raises(SafetyError, match="changed"):
        write_evidence_candidate_tree(_result(), paths)

    staging = cast(Path, holder["staging"])
    foreign = cast(os.stat_result, holder["foreign"])
    displaced = cast(Path, holder["displaced"])
    current = os.lstat(staging)
    assert (current.st_dev, current.st_ino, stat.S_IMODE(current.st_mode)) == (
        foreign.st_dev,
        foreign.st_ino,
        0o755,
    )
    assert displaced.is_dir()
    assert os.lstat(displaced).st_ino == holder["displaced_inode"]
    assert not (paths.build / "evidence-candidates").exists()


def test_writer_revalidates_staging_name_binding_immediately_before_rename(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    paths = _repository(tmp_path)
    result = _result()
    real_create_tree = writer_module._create_staging_tree
    holder: dict[str, Path] = {}

    def swap_after_complete_tree(*args: Any, **kwargs: Any) -> None:
        real_create_tree(*args, **kwargs)
        directory_fds = cast(dict[str, int], args[0])
        staging = Path(os.readlink(f"/proc/self/fd/{directory_fds['']}"))
        displaced = staging.with_name(staging.name + "-writer-owned")
        staging.rename(displaced)
        staging.mkdir(mode=0o755)
        staging.chmod(0o755)
        holder.update(foreign=staging, displaced=displaced)

    monkeypatch.setattr(writer_module, "_create_staging_tree", swap_after_complete_tree)

    with pytest.raises(SafetyError, match="binding|changed|revalidate"):
        write_evidence_candidate_tree(result, paths)

    foreign = holder["foreign"]
    displaced = holder["displaced"]
    assert foreign.is_dir()
    assert list(foreign.iterdir()) == []
    _assert_complete_staging(displaced, result)
    assert not (paths.build / "evidence-candidates").exists()


@pytest.mark.parametrize("swap", ["repository", "build"])
def test_held_directory_fds_prevent_escape_and_preserve_postrename_tree(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    swap: str,
) -> None:
    paths = _repository(tmp_path)
    result = _result()
    outside = tmp_path / "outside"
    outside.mkdir(mode=0o755)
    moved = tmp_path / f"moved-{swap}"
    real_create = writer_module._create_staging_directory

    def swap_then_create(build_fd: int) -> tuple[str, int]:
        if swap == "repository":
            paths.root.rename(moved)
            paths.root.symlink_to(outside, target_is_directory=True)
        else:
            paths.build.rename(moved)
            paths.build.symlink_to(outside, target_is_directory=True)
        return real_create(build_fd)

    monkeypatch.setattr(writer_module, "_create_staging_directory", swap_then_create)

    with pytest.raises(SafetyError, match="changed|ancestry|binding|missing|safe|symlink"):
        write_evidence_candidate_tree(result, paths)

    assert not list(outside.rglob("candidate-manifest.json"))
    assert not list(outside.rglob(".evidence-candidates.tmp-*"))
    moved_build = moved / "build" if swap == "repository" else moved
    published = moved_build / "evidence-candidates"
    _assert_complete_staging(published, result)
    assert not list(moved_build.glob(".evidence-candidates.tmp-*"))


def test_writer_closes_every_opened_fd_after_success_and_failure(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    paths = _repository(tmp_path)
    real_open = writer_module.os.open
    opened: list[int] = []

    def tracking_open(*args: Any, **kwargs: Any) -> int:
        fd = real_open(*args, **kwargs)
        opened.append(fd)
        return fd

    monkeypatch.setattr(writer_module.os, "open", tracking_open)
    write_evidence_candidate_tree(_result(), paths)
    with pytest.raises(SafetyError):
        write_evidence_candidate_tree(
            dataclasses.replace(_result(), sha256="0" * 64),
            paths,
        )

    assert opened
    for fd in opened:
        with pytest.raises(OSError):
            os.fstat(fd)


def test_writer_has_no_caller_controlled_relative_destination(tmp_path: Path) -> None:
    paths = _repository(tmp_path)
    result = _result()
    payloads = dict(result.canonical_payloads)
    first = payloads.pop(EVIDENCE_CANDIDATE_PAYLOAD_PATHS[0])
    payloads[f"../../{SENSITIVE_MARKER}"] = first
    forged = dataclasses.replace(
        result,
        canonical_payloads=MappingProxyType(payloads),
    )

    with pytest.raises(SafetyError) as caught:
        write_evidence_candidate_tree(forged, paths)

    _assert_sanitized(caught.value)
    _assert_empty_build(paths)
    assert not (tmp_path / SENSITIVE_MARKER).exists()


def test_writer_static_contract_constants_remain_pinned() -> None:
    assert MANIFEST_SCHEMA_VERSION == 1
    assert MANIFEST_TOOL_NAME == "iikocloud-evidence-candidates"
    assert MANIFEST_TOOL_VERSION == 1
