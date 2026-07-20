from __future__ import annotations

import ctypes
import dataclasses
import errno
import fcntl
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
LOCK_NAME = ".evidence-candidates.lock"
STAGING_PREFIX = ".evidence-candidates.tmp-"


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


def _metadata_signature(path: Path) -> tuple[int, ...]:
    metadata = os.lstat(path)
    return (
        metadata.st_dev,
        metadata.st_ino,
        metadata.st_mode,
        metadata.st_uid,
        metadata.st_nlink,
        metadata.st_size,
        metadata.st_mtime_ns,
        metadata.st_ctime_ns,
    )


def _assert_lock_only_build(paths: RepoPaths) -> Path:
    lock_path = paths.build / LOCK_NAME
    assert sorted(path.name for path in paths.build.iterdir()) == [LOCK_NAME]
    metadata = os.lstat(lock_path)
    assert stat.S_ISREG(metadata.st_mode)
    assert stat.S_IMODE(metadata.st_mode) == 0o644
    assert metadata.st_uid == os.getuid()
    assert metadata.st_nlink == 1
    return lock_path


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


def test_public_process_lock_context_exposes_canonical_path_and_lifecycle(
    tmp_path: Path,
) -> None:
    paths = _repository(tmp_path)
    process_lock_type = getattr(writer_module, "EvidenceCandidateProcessLock", None)
    assert process_lock_type is not None
    process_lock = process_lock_type(paths)

    assert process_lock.path == paths.build / LOCK_NAME
    assert process_lock.held is False
    with process_lock as entered:
        assert entered is process_lock
        assert process_lock.held is True
        assert process_lock.path == paths.build / LOCK_NAME
        assert _assert_lock_only_build(paths) == process_lock.path
    assert process_lock.held is False


def test_public_process_lock_acquisition_is_nonblocking(tmp_path: Path) -> None:
    paths = _repository(tmp_path)
    first = writer_module.EvidenceCandidateProcessLock(paths)
    second = writer_module.EvidenceCandidateProcessLock(paths)

    with first:
        with pytest.raises(
            SafetyError,
            match="^Evidence candidate writer lock is already held$",
        ):
            second.acquire()
        assert first.held is True
        assert second.held is False
    assert first.held is False


def test_public_process_lock_binding_token_and_residue_gate(tmp_path: Path) -> None:
    paths = _repository(tmp_path)
    process_lock = writer_module.EvidenceCandidateProcessLock(paths)
    capture_binding = getattr(process_lock, "capture_binding", None)
    assert callable(capture_binding)
    assert callable(getattr(process_lock, "assert_binding", None))
    assert callable(getattr(process_lock, "assert_no_staging_residue", None))

    with process_lock:
        token = capture_binding()
        process_lock.assert_binding(token)
        process_lock.assert_no_staging_residue()
        residue = paths.build / f"{STAGING_PREFIX}operator-review"
        residue.mkdir(mode=0o755)
        with pytest.raises(
            SafetyError,
            match="^Evidence candidate staging residue requires operator resolution$",
        ):
            process_lock.assert_no_staging_residue()
        process_lock.assert_binding(token)


def test_public_process_lock_release_and_reacquire_invalidate_old_token(
    tmp_path: Path,
) -> None:
    paths = _repository(tmp_path)
    process_lock = writer_module.EvidenceCandidateProcessLock(paths)
    process_lock.acquire()
    old_token = process_lock.capture_binding()

    process_lock.release()
    with pytest.raises(SafetyError, match="binding|held|acquisition"):
        process_lock.assert_binding(old_token)

    process_lock.acquire()
    try:
        new_token = process_lock.capture_binding()
        assert new_token is not old_token
        with pytest.raises(SafetyError, match="binding|held|acquisition"):
            process_lock.assert_binding(old_token)
        process_lock.assert_binding(new_token)
    finally:
        process_lock.release()


@pytest.mark.parametrize("binding", ["repository", "build", "lock"])
def test_public_process_lock_binding_token_rejects_rebound_canonical_name(
    tmp_path: Path,
    binding: str,
) -> None:
    paths = _repository(tmp_path)
    process_lock = writer_module.EvidenceCandidateProcessLock(paths)
    process_lock.acquire()
    token = process_lock.capture_binding()
    try:
        if binding == "repository":
            displaced = tmp_path / "displaced-repository"
            paths.root.rename(displaced)
            paths.root.mkdir(mode=0o755)
            (paths.root / "pyproject.toml").write_text(
                "[project]\nname='replacement'\n",
                encoding="utf-8",
            )
            paths.build.mkdir(mode=0o755)
        elif binding == "build":
            displaced = paths.root / "displaced-build"
            paths.build.rename(displaced)
            paths.build.mkdir(mode=0o755)
        else:
            displaced = paths.build / "displaced-lock"
            process_lock.path.rename(displaced)
            process_lock.path.write_bytes(b"")
            process_lock.path.chmod(0o644)

        with pytest.raises(SafetyError, match="binding|changed|lock"):
            process_lock.assert_binding(token)
    finally:
        process_lock.release()


@pytest.mark.skipif(not hasattr(os, "fork"), reason="process binding requires POSIX fork")
def test_public_process_lock_binding_is_invalid_in_forked_child(tmp_path: Path) -> None:
    paths = _repository(tmp_path)
    process_lock = writer_module.EvidenceCandidateProcessLock(paths)
    with process_lock:
        token = process_lock.capture_binding()
        child_pid = os.fork()
        if child_pid == 0:
            exit_code = 3
            try:
                if process_lock.held:
                    exit_code = 2
                else:
                    with pytest.raises(SafetyError, match="process|binding|held|acquisition"):
                        process_lock.assert_binding(token)
                    exit_code = 0
            finally:
                os._exit(exit_code)
        waited_pid, status = os.waitpid(child_pid, 0)
        assert waited_pid == child_pid
        assert os.waitstatus_to_exitcode(status) == 0
        process_lock.assert_binding(token)


def test_public_process_lock_memory_error_during_binding_allocation_closes_fds(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    paths = _repository(tmp_path)
    process_lock = writer_module.EvidenceCandidateProcessLock(paths)
    real_open = writer_module.os.open
    opened: list[int] = []

    def track_open(*args: Any, **kwargs: Any) -> int:
        descriptor = real_open(*args, **kwargs)
        opened.append(descriptor)
        return descriptor

    def fail_binding_allocation() -> object:
        raise MemoryError(SENSITIVE_MARKER)

    assert hasattr(writer_module, "_new_process_lock_binding_token")
    monkeypatch.setattr(writer_module.os, "open", track_open)
    monkeypatch.setattr(
        writer_module,
        "_new_process_lock_binding_token",
        fail_binding_allocation,
    )

    with pytest.raises(MemoryError) as caught:
        process_lock.acquire()

    assert caught.value.args == (SENSITIVE_MARKER,)
    assert process_lock.held is False
    assert opened
    for descriptor in opened:
        with pytest.raises(OSError):
            os.fstat(descriptor)


def test_writer_uses_public_process_lock_and_its_residue_gate(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    paths = _repository(tmp_path)
    process_lock_type = writer_module.EvidenceCandidateProcessLock
    real_acquire = process_lock_type.acquire
    real_release = process_lock_type.release
    real_residue_gate = process_lock_type.assert_no_staging_residue
    events: list[str] = []

    def observe_acquire(self: Any) -> Any:
        events.append("acquire")
        return real_acquire(self)

    def observe_residue_gate(self: Any) -> None:
        events.append("residue")
        real_residue_gate(self)

    def observe_release(self: Any) -> None:
        events.append("release")
        real_release(self)

    monkeypatch.setattr(process_lock_type, "acquire", observe_acquire)
    monkeypatch.setattr(
        process_lock_type,
        "assert_no_staging_residue",
        observe_residue_gate,
    )
    monkeypatch.setattr(process_lock_type, "release", observe_release)

    write_evidence_candidate_tree(_result(), paths)

    assert events == ["acquire", "residue", "release"]


def _filesystem_snapshot(root: Path) -> dict[str, tuple[tuple[int, ...], bytes | None]]:
    snapshot: dict[str, tuple[tuple[int, ...], bytes | None]] = {}
    for path in (root, *root.rglob("*")):
        metadata = os.lstat(path)
        relative = path.relative_to(root).as_posix() or "."
        stable = (
            metadata.st_dev,
            metadata.st_ino,
            metadata.st_mode,
            metadata.st_uid,
            metadata.st_nlink,
            metadata.st_size,
            metadata.st_mtime_ns,
            metadata.st_ctime_ns,
        )
        body = path.read_bytes() if stat.S_ISREG(metadata.st_mode) else None
        snapshot[relative] = (stable, body)
    return snapshot


def test_candidate_matcher_is_read_only_and_compares_the_exact_snapshot(
    tmp_path: Path,
) -> None:
    paths = _repository(tmp_path)
    result = _result()
    written = write_evidence_candidate_tree(result, paths)
    matcher = getattr(writer_module, "assert_evidence_candidate_tree_matches", None)
    assert callable(matcher)

    with writer_module.EvidenceCandidateProcessLock(paths) as process_lock:
        before = _filesystem_snapshot(paths.root)
        assert matcher(result, paths, process_lock=process_lock) is None
        after = _filesystem_snapshot(paths.root)

    assert after == before
    assert written.root == paths.build / "evidence-candidates"


@pytest.mark.parametrize("mutation", ["tamper", "extra", "missing"])
def test_candidate_matcher_rejects_inexact_tree_without_repair(
    tmp_path: Path,
    mutation: str,
) -> None:
    paths = _repository(tmp_path)
    result = _result()
    root = _write_tree_directly(paths, result)
    if mutation == "tamper":
        target = root / EVIDENCE_CANDIDATE_PAYLOAD_PATHS[0]
        target.write_bytes(target.read_bytes() + b"\n")
        target.chmod(0o644)
    elif mutation == "extra":
        target = root / "unexpected.txt"
        target.write_bytes(b"untouched")
        target.chmod(0o644)
    else:
        target = root / EVIDENCE_CANDIDATE_PAYLOAD_PATHS[-1]
        target.unlink()
    mutated_tree = _filesystem_snapshot(root)

    with (
        writer_module.EvidenceCandidateProcessLock(paths) as process_lock,
        pytest.raises(SafetyError, match="tree|entry|differs|missing|partial"),
    ):
        writer_module.assert_evidence_candidate_tree_matches(
            result,
            paths,
            process_lock=process_lock,
        )

    assert _filesystem_snapshot(root) == mutated_tree


@pytest.mark.parametrize("unsafe_kind", ["mode", "owner", "hardlink"])
def test_candidate_matcher_rejects_unsafe_candidate_metadata(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    unsafe_kind: str,
) -> None:
    paths = _repository(tmp_path)
    result = _result()
    root = _write_tree_directly(paths, result)
    target = root / "candidate-manifest.json"
    if unsafe_kind == "mode":
        target.chmod(0o600)
    elif unsafe_kind == "hardlink":
        (tmp_path / "manifest-hardlink").hardlink_to(target)
    else:
        real_stat = writer_module._safe_stat_at

        def report_foreign_candidate_owner(
            parent_fd: int,
            name: str,
            *,
            message: str,
        ) -> os.stat_result:
            metadata = real_stat(parent_fd, name, message=message)
            if name != "candidate-manifest.json":
                return metadata
            values = list(metadata)
            values[4] = metadata.st_uid + 1
            return os.stat_result(values)

        monkeypatch.setattr(
            writer_module,
            "_safe_stat_at",
            report_foreign_candidate_owner,
        )

    with (
        writer_module.EvidenceCandidateProcessLock(paths) as process_lock,
        pytest.raises(SafetyError, match="mode|owned|owner|hard link"),
    ):
        writer_module.assert_evidence_candidate_tree_matches(
            result,
            paths,
            process_lock=process_lock,
        )


@pytest.mark.parametrize("unsafe_kind", ["symlink", "fifo", "socket"])
def test_candidate_matcher_rejects_special_candidate_file_without_blocking(
    tmp_path: Path,
    unsafe_kind: str,
) -> None:
    paths = _repository(tmp_path)
    result = _result()
    root = _write_tree_directly(paths, result)
    target = root / "candidate-manifest.json"
    target.unlink()
    socket_handle: socket.socket | None = None
    if unsafe_kind == "symlink":
        outside = tmp_path / "outside-manifest"
        outside.write_bytes(result.canonical_json_bytes)
        target.symlink_to(outside)
    elif unsafe_kind == "fifo":
        os.mkfifo(target, mode=0o644)
    else:
        socket_handle = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        previous_cwd = Path.cwd()
        try:
            os.chdir(root)
            socket_handle.bind(target.name)
        finally:
            os.chdir(previous_cwd)

    try:
        with (
            writer_module.EvidenceCandidateProcessLock(paths) as process_lock,
            pytest.raises(SafetyError, match="regular|symlink|unsafe|file"),
        ):
            writer_module.assert_evidence_candidate_tree_matches(
                result,
                paths,
                process_lock=process_lock,
            )
    finally:
        if socket_handle is not None:
            socket_handle.close()


def test_candidate_matcher_rejects_residue_before_reading_candidate(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    paths = _repository(tmp_path)
    result = _result()
    _write_tree_directly(paths, result)
    residue = paths.build / f"{STAGING_PREFIX}operator-review"
    residue.mkdir(mode=0o755)

    def forbidden(*_args: Any, **_kwargs: Any) -> None:
        raise AssertionError("candidate tree must not be read before the residue gate")

    monkeypatch.setattr(writer_module, "_validate_exact_tree", forbidden)
    with (
        writer_module.EvidenceCandidateProcessLock(paths) as process_lock,
        pytest.raises(
            SafetyError,
            match="^Evidence candidate staging residue requires operator resolution$",
        ),
    ):
        writer_module.assert_evidence_candidate_tree_matches(
            result,
            paths,
            process_lock=process_lock,
        )


def test_candidate_matcher_requires_held_lock_for_the_same_canonical_repository(
    tmp_path: Path,
) -> None:
    expected_parent = tmp_path / "expected"
    other_parent = tmp_path / "other"
    expected_parent.mkdir()
    other_parent.mkdir()
    paths = _repository(expected_parent)
    other_paths = _repository(other_parent)
    result = _result()
    _write_tree_directly(paths, result)
    released = writer_module.EvidenceCandidateProcessLock(paths)

    with pytest.raises(SafetyError, match="held|binding|acquisition"):
        writer_module.assert_evidence_candidate_tree_matches(
            result,
            paths,
            process_lock=released,
        )

    with (
        writer_module.EvidenceCandidateProcessLock(other_paths) as wrong_lock,
        pytest.raises(SafetyError, match="canonical|repository|lock"),
    ):
        writer_module.assert_evidence_candidate_tree_matches(
            result,
            paths,
            process_lock=wrong_lock,
        )


def test_candidate_matcher_requires_exact_process_lock_type(tmp_path: Path) -> None:
    paths = _repository(tmp_path)
    result = _result()
    _write_tree_directly(paths, result)

    class ProcessLockSubclass(writer_module.EvidenceCandidateProcessLock):
        pass

    with (
        ProcessLockSubclass(paths) as process_lock,
        pytest.raises(SafetyError, match="exact.*process lock|process lock.*exact"),
    ):
        writer_module.assert_evidence_candidate_tree_matches(
            result,
            paths,
            process_lock=process_lock,
        )


@pytest.mark.parametrize("forged_kind", ["result", "paths"])
def test_candidate_matcher_requires_exact_result_and_paths_types(
    tmp_path: Path,
    forged_kind: str,
) -> None:
    paths = _repository(tmp_path)
    result = _result()
    _write_tree_directly(paths, result)

    class ResultSubclass(EvidenceCandidateManifestResult):
        pass

    class PathsSubclass(RepoPaths):
        pass

    supplied_result: EvidenceCandidateManifestResult = result
    supplied_paths: RepoPaths = paths
    if forged_kind == "result":
        supplied_result = ResultSubclass(
            manifest=result.manifest,
            canonical_payloads=result.canonical_payloads,
            canonical_json_bytes=result.canonical_json_bytes,
            sha256=result.sha256,
        )
    else:
        supplied_paths = PathsSubclass(paths.root)

    with (
        writer_module.EvidenceCandidateProcessLock(paths) as process_lock,
        pytest.raises(SafetyError, match="exact.*manifest result|exact.*repository paths"),
    ):
        writer_module.assert_evidence_candidate_tree_matches(
            supplied_result,
            supplied_paths,
            process_lock=process_lock,
        )


def test_candidate_matcher_runtime_type_hints_are_exact() -> None:
    hints = get_type_hints(writer_module.assert_evidence_candidate_tree_matches)

    assert hints == {
        "result": EvidenceCandidateManifestResult,
        "paths": RepoPaths,
        "process_lock": writer_module.EvidenceCandidateProcessLock,
        "return": type(None),
    }


def test_candidate_matcher_requires_the_same_current_acquisition_token(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    paths = _repository(tmp_path)
    result = _result()
    _write_tree_directly(paths, result)
    process_lock_type = writer_module.EvidenceCandidateProcessLock
    real_capture = process_lock_type.capture_binding
    calls = 0

    def stale_capture(self: Any) -> object:
        nonlocal calls
        token = real_capture(self)
        calls += 1
        if calls == 1:
            self.release()
            self.acquire()
        return token

    monkeypatch.setattr(process_lock_type, "capture_binding", stale_capture)
    with (
        process_lock_type(paths) as process_lock,
        pytest.raises(SafetyError, match="binding|current|acquisition"),
    ):
        writer_module.assert_evidence_candidate_tree_matches(
            result,
            paths,
            process_lock=process_lock,
        )


def test_candidate_matcher_reads_every_file_nofollow_nonblocking_and_bounded(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    paths = _repository(tmp_path)
    result = _result()
    _write_tree_directly(paths, result)
    real_open = writer_module.os.open
    real_read = writer_module.os.read
    flags: list[int] = []
    read_sizes: list[int] = []
    expected_files = _expected_files(result)

    def observe_open(*args: Any, **kwargs: Any) -> int:
        descriptor = real_open(*args, **kwargs)
        target = os.readlink(f"/proc/self/fd/{descriptor}")
        if "/evidence-candidates/" in target and target.endswith((".json", ".yaml")):
            flags.append(args[1])
        return descriptor

    def observe_read(descriptor: int, size: int) -> bytes:
        target = os.readlink(f"/proc/self/fd/{descriptor}")
        if "/evidence-candidates/" in target:
            relative = target.split("/evidence-candidates/", maxsplit=1)[1]
            assert size <= len(expected_files[relative]) + 1
            read_sizes.append(size)
        return real_read(descriptor, size)

    monkeypatch.setattr(writer_module.os, "open", observe_open)
    monkeypatch.setattr(writer_module.os, "read", observe_read)
    with writer_module.EvidenceCandidateProcessLock(paths) as process_lock:
        writer_module.assert_evidence_candidate_tree_matches(
            result,
            paths,
            process_lock=process_lock,
        )

    assert len(flags) >= len(expected_files)
    assert all(value & os.O_NOFOLLOW for value in flags)
    assert all(value & os.O_NONBLOCK for value in flags)
    assert len(read_sizes) >= len(expected_files)


def test_candidate_matcher_rejects_self_consistent_disk_manifest_tamper(
    tmp_path: Path,
) -> None:
    paths = _repository(tmp_path)
    result = _result()
    root = _write_tree_directly(paths, result)
    relative = EVIDENCE_CANDIDATE_PAYLOAD_PATHS[0]
    payload = root / relative
    tampered_body = payload.read_bytes() + b"\n"
    payload.write_bytes(tampered_body)
    payload.chmod(0o644)
    manifest_path = root / "candidate-manifest.json"
    manifest = json.loads(manifest_path.read_bytes())
    manifest["files"][relative] = sha256_bytes(tampered_body)
    manifest_path.write_bytes(canonical_json_bytes(manifest))
    manifest_path.chmod(0o644)

    with (
        writer_module.EvidenceCandidateProcessLock(paths) as process_lock,
        pytest.raises(SafetyError, match="differs|snapshot"),
    ):
        writer_module.assert_evidence_candidate_tree_matches(
            result,
            paths,
            process_lock=process_lock,
        )


@pytest.mark.parametrize("binding", ["candidate", "lock"])
def test_candidate_matcher_fails_closed_on_binding_race(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    binding: str,
) -> None:
    paths = _repository(tmp_path)
    result = _result()
    root = _write_tree_directly(paths, result)
    real_validate = writer_module._validate_exact_tree
    validations = 0

    def swap_after_first_validation(
        root_fd: int,
        files: Mapping[str, bytes],
    ) -> None:
        nonlocal validations
        real_validate(root_fd, files)
        validations += 1
        if validations != 1:
            return
        if binding == "candidate":
            displaced = paths.build / "displaced-candidate"
            root.rename(displaced)
            root.mkdir(mode=0o755)
        else:
            displaced = paths.build / "displaced-lock"
            lock_path = paths.build / LOCK_NAME
            lock_path.rename(displaced)
            lock_path.write_bytes(b"")
            lock_path.chmod(0o644)

    monkeypatch.setattr(
        writer_module,
        "_validate_exact_tree",
        swap_after_first_validation,
    )
    with (
        writer_module.EvidenceCandidateProcessLock(paths) as process_lock,
        pytest.raises(SafetyError, match="binding|changed|tree|entry|candidate|lock"),
    ):
        writer_module.assert_evidence_candidate_tree_matches(
            result,
            paths,
            process_lock=process_lock,
        )

    assert validations == (1 if binding == "candidate" else 2)


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
    lock_path = paths.build / LOCK_NAME
    lock_metadata = os.lstat(lock_path)
    assert stat.S_ISREG(lock_metadata.st_mode)
    assert stat.S_IMODE(lock_metadata.st_mode) == 0o644
    assert lock_metadata.st_uid == os.getuid()
    assert lock_metadata.st_nlink == 1
    assert lock_metadata.st_size == 0
    assert sorted(path.name for path in paths.build.iterdir()) == [LOCK_NAME, root.name]
    assert not list(paths.build.glob(".evidence-candidates.tmp-*"))


def test_writer_identical_existing_tree_is_untouched(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    result = _result()
    paths = _repository(tmp_path)
    first = write_evidence_candidate_tree(result, paths)
    lock_path = paths.build / LOCK_NAME
    before = {
        path.relative_to(paths.root).as_posix(): (
            os.lstat(path).st_ino,
            os.lstat(path).st_mtime_ns,
            os.lstat(path).st_ctime_ns,
        )
        for path in (paths.build, lock_path, first.root, *first.root.rglob("*"))
    }

    def forbidden(*_args: Any, **_kwargs: Any) -> Any:
        raise AssertionError("identical no-op must not enter staging or write helpers")

    monkeypatch.setattr(writer_module, "_create_staging_directory", forbidden)
    monkeypatch.setattr(writer_module, "_write_file_at", forbidden)
    monkeypatch.setattr(writer_module, "_rename_directory_noreplace", forbidden)

    second = write_evidence_candidate_tree(result, paths)

    after = {
        path.relative_to(paths.root).as_posix(): (
            os.lstat(path).st_ino,
            os.lstat(path).st_mtime_ns,
            os.lstat(path).st_ctime_ns,
        )
        for path in (paths.build, lock_path, first.root, *first.root.rglob("*"))
    }
    assert second == EvidenceCandidateWriteResult(
        root=first.root,
        manifest_path=first.manifest_path,
        manifest_sha256=result.sha256,
        changed=False,
    )
    assert after == before
    assert not list(paths.build.glob(".evidence-candidates.tmp-*"))


def test_writer_documents_cooperative_lock_threat_boundary() -> None:
    documentation = "\n".join(
        (writer_module.__doc__ or "", write_evidence_candidate_tree.__doc__ or "")
    ).lower()

    assert "all official" in documentation
    assert "cooperate" in documentation
    assert "same-uid" in documentation
    assert "out of scope" in documentation


def test_writer_creates_lock_atomically_and_durably_before_staging(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    paths = _repository(tmp_path)
    real_open = writer_module.os.open
    real_fsync = writer_module._fsync_fd
    lock_creations: list[tuple[int, int | None]] = []
    fsync_targets_before_staging: list[str] = []
    staging_started = False

    def observe_open(*args: Any, **kwargs: Any) -> int:
        if args[0] == LOCK_NAME:
            lock_creations.append((args[1], args[2] if len(args) > 2 else None))
        return real_open(*args, **kwargs)

    def observe_fsync(fd: int) -> None:
        if not staging_started:
            fsync_targets_before_staging.append(os.readlink(f"/proc/self/fd/{fd}"))
        real_fsync(fd)

    real_create_staging = writer_module._create_staging_directory

    def observe_staging(build_fd: int) -> tuple[str, int]:
        nonlocal staging_started
        staging_started = True
        return real_create_staging(build_fd)

    monkeypatch.setattr(writer_module.os, "open", observe_open)
    monkeypatch.setattr(writer_module, "_fsync_fd", observe_fsync)
    monkeypatch.setattr(writer_module, "_create_staging_directory", observe_staging)

    write_evidence_candidate_tree(_result(), paths)

    assert len(lock_creations) == 1
    flags, mode = lock_creations[0]
    assert flags & os.O_CREAT
    assert flags & os.O_EXCL
    assert flags & os.O_NOFOLLOW
    assert mode == 0o644
    assert fsync_targets_before_staging == [
        str(paths.build / LOCK_NAME),
        str(paths.build),
    ]


def test_writer_lock_contention_fails_before_staging_without_mutation(
    tmp_path: Path,
) -> None:
    paths = _repository(tmp_path)
    lock_path = paths.build / LOCK_NAME
    lock_path.write_bytes(b"")
    lock_path.chmod(0o644)
    before = _metadata_signature(lock_path)
    held_fd = os.open(lock_path, os.O_RDWR | os.O_CLOEXEC | os.O_NOFOLLOW)
    fcntl.flock(held_fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
    try:
        with pytest.raises(
            SafetyError,
            match="^Evidence candidate writer lock is already held$",
        ):
            write_evidence_candidate_tree(_result(), paths)
    finally:
        os.close(held_fd)

    assert _metadata_signature(lock_path) == before
    assert _assert_lock_only_build(paths) == lock_path
    assert not (paths.build / "evidence-candidates").exists()
    assert not list(paths.build.glob(f"{STAGING_PREFIX}*"))


@pytest.mark.parametrize("boundary", ["root", "child"])
def test_writer_holds_cooperative_lock_at_every_staging_mkdir_boundary(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    boundary: str,
) -> None:
    paths = _repository(tmp_path)
    result = _result()
    real_mkdir = writer_module.os.mkdir
    checked: list[str] = []

    def observe_mkdir(
        path: str | bytes,
        mode: int = 0o777,
        *,
        dir_fd: int | None = None,
    ) -> None:
        is_root = type(path) is str and path.startswith(STAGING_PREFIX)
        if (boundary == "root" and is_root) or (boundary == "child" and not is_root):
            assert type(path) is str
            checked.append(path)
            if boundary == "root":
                with pytest.raises(
                    SafetyError,
                    match="^Evidence candidate writer lock is already held$",
                ):
                    write_evidence_candidate_tree(result, paths)
            else:
                probe_fd = os.open(
                    paths.build / LOCK_NAME,
                    os.O_RDWR | os.O_CLOEXEC | os.O_NOFOLLOW,
                )
                try:
                    with pytest.raises(BlockingIOError):
                        fcntl.flock(probe_fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
                finally:
                    os.close(probe_fd)
        real_mkdir(path, mode, dir_fd=dir_fd)

    monkeypatch.setattr(writer_module.os, "mkdir", observe_mkdir)

    written = write_evidence_candidate_tree(result, paths)

    assert written.changed is True
    assert len(checked) == (1 if boundary == "root" else len(writer_module._DIRECTORY_PATHS) - 1)


def test_writer_holds_lock_until_every_other_writer_fd_is_closed(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    paths = _repository(tmp_path)
    real_open = writer_module.os.open
    real_close = writer_module.os.close
    lock_fds: list[int] = []
    close_order: list[int] = []
    lock_checks = 0

    def track_open(*args: Any, **kwargs: Any) -> int:
        fd = real_open(*args, **kwargs)
        if args[0] == LOCK_NAME:
            lock_fds.append(fd)
        return fd

    def assert_lock_before_close(fd: int) -> None:
        nonlocal lock_checks
        if lock_fds and fd != lock_fds[0]:
            try:
                os.fstat(lock_fds[0])
            except OSError:
                pass
            else:
                probe_fd = real_open(
                    paths.build / LOCK_NAME,
                    os.O_RDWR | os.O_CLOEXEC | os.O_NOFOLLOW,
                )
                try:
                    with pytest.raises(BlockingIOError):
                        fcntl.flock(probe_fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
                    lock_checks += 1
                finally:
                    real_close(probe_fd)
        close_order.append(fd)
        real_close(fd)

    monkeypatch.setattr(writer_module.os, "open", track_open)
    monkeypatch.setattr(writer_module.os, "close", assert_lock_before_close)

    write_evidence_candidate_tree(_result(), paths)

    assert len(lock_fds) == 1
    assert lock_checks > 0
    assert close_order[-1] == lock_fds[0]


@pytest.mark.parametrize(
    "unsafe_kind",
    ["symlink", "hardlink", "wrong-mode", "fifo"],
)
def test_writer_rejects_unsafe_existing_lock_untouched(
    tmp_path: Path,
    unsafe_kind: str,
) -> None:
    paths = _repository(tmp_path)
    lock_path = paths.build / LOCK_NAME
    outside = tmp_path / "outside-lock"
    outside.write_bytes(b"")
    outside.chmod(0o644)
    if unsafe_kind == "symlink":
        lock_path.symlink_to(outside)
    elif unsafe_kind == "hardlink":
        lock_path.hardlink_to(outside)
    elif unsafe_kind == "wrong-mode":
        lock_path.write_bytes(b"")
        lock_path.chmod(0o600)
    else:
        os.mkfifo(lock_path, mode=0o644)
    before = _metadata_signature(lock_path)

    with pytest.raises(SafetyError, match="lock|0644|regular|hard link"):
        write_evidence_candidate_tree(_result(), paths)

    assert _metadata_signature(lock_path) == before
    assert not (paths.build / "evidence-candidates").exists()
    assert not list(paths.build.glob(f"{STAGING_PREFIX}*"))


def test_writer_rejects_wrong_owner_lock_untouched(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    paths = _repository(tmp_path)
    lock_path = paths.build / LOCK_NAME
    lock_path.write_bytes(b"")
    lock_path.chmod(0o644)
    before = _metadata_signature(lock_path)
    real_stat = writer_module._safe_stat_at

    def report_foreign_lock_owner(
        parent_fd: int,
        name: str,
        *,
        message: str,
    ) -> os.stat_result:
        metadata = real_stat(parent_fd, name, message=message)
        if name != LOCK_NAME:
            return metadata
        return os.stat_result(
            (
                metadata.st_mode,
                metadata.st_ino,
                metadata.st_dev,
                metadata.st_nlink,
                metadata.st_uid + 1,
                metadata.st_gid,
                metadata.st_size,
                metadata.st_atime,
                metadata.st_mtime,
                metadata.st_ctime,
            )
        )

    monkeypatch.setattr(writer_module, "_safe_stat_at", report_foreign_lock_owner)

    with pytest.raises(SafetyError, match="owned|lock"):
        write_evidence_candidate_tree(_result(), paths)

    assert _metadata_signature(lock_path) == before
    assert not (paths.build / "evidence-candidates").exists()


@pytest.mark.parametrize("operation", ["open", "flock"])
def test_writer_sanitizes_lock_oserror_without_staging(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    operation: str,
) -> None:
    paths = _repository(tmp_path)
    lock_path = paths.build / LOCK_NAME
    lock_path.write_bytes(b"")
    lock_path.chmod(0o644)
    if operation == "open":
        real_open = writer_module.os.open

        def fail_lock_open(*args: Any, **kwargs: Any) -> int:
            if args[0] == LOCK_NAME:
                raise OSError(SENSITIVE_MARKER)
            return real_open(*args, **kwargs)

        monkeypatch.setattr(writer_module.os, "open", fail_lock_open)
    else:

        def fail_flock(_fd: int, _operation: int) -> None:
            raise OSError(SENSITIVE_MARKER)

        monkeypatch.setattr(fcntl, "flock", fail_flock)

    with pytest.raises(SafetyError) as caught:
        write_evidence_candidate_tree(_result(), paths)

    _assert_sanitized(caught.value)
    assert not (paths.build / "evidence-candidates").exists()
    assert not list(paths.build.glob(f"{STAGING_PREFIX}*"))


@pytest.mark.parametrize("exception_type", [MemoryError, KeyboardInterrupt, SystemExit])
def test_writer_preserves_lock_base_exceptions_and_closes_fd(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    exception_type: type[BaseException],
) -> None:
    paths = _repository(tmp_path)
    lock_path = paths.build / LOCK_NAME
    lock_path.write_bytes(b"")
    lock_path.chmod(0o644)
    real_open = writer_module.os.open
    lock_fds: list[int] = []

    def track_lock_open(*args: Any, **kwargs: Any) -> int:
        fd = real_open(*args, **kwargs)
        if args[0] == LOCK_NAME:
            lock_fds.append(fd)
        return fd

    def fail_flock(_fd: int, _operation: int) -> None:
        raise exception_type(SENSITIVE_MARKER)

    monkeypatch.setattr(writer_module.os, "open", track_lock_open)
    monkeypatch.setattr(fcntl, "flock", fail_flock)

    with pytest.raises(exception_type) as caught:
        write_evidence_candidate_tree(_result(), paths)

    assert caught.value.args == (SENSITIVE_MARKER,)
    assert lock_fds
    for fd in lock_fds:
        with pytest.raises(OSError):
            os.fstat(fd)
    assert not (paths.build / "evidence-candidates").exists()


def test_writer_revalidates_lock_name_binding_after_acquisition(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    paths = _repository(tmp_path)
    lock_path = paths.build / LOCK_NAME
    lock_path.write_bytes(b"")
    lock_path.chmod(0o644)
    displaced = paths.build / "displaced-lock"
    real_flock = fcntl.flock

    def swap_after_lock(fd: int, operation: int) -> None:
        real_flock(fd, operation)
        lock_path.rename(displaced)
        lock_path.write_bytes(b"")
        lock_path.chmod(0o644)

    monkeypatch.setattr(fcntl, "flock", swap_after_lock)

    with pytest.raises(SafetyError, match="lock.*changed|lock.*binding"):
        write_evidence_candidate_tree(_result(), paths)

    assert displaced.is_file()
    assert lock_path.is_file()
    assert not (paths.build / "evidence-candidates").exists()
    assert not list(paths.build.glob(f"{STAGING_PREFIX}*"))


@pytest.mark.parametrize(
    ("kind", "suffix"),
    [
        ("directory", "directory"),
        ("file", "file"),
        ("symlink", "symlink"),
        ("file", "%%%malformed"),
    ],
)
def test_writer_blocks_every_staging_residue_kind_before_new_staging(
    tmp_path: Path,
    kind: str,
    suffix: str,
) -> None:
    paths = _repository(tmp_path)
    residue = paths.build / f"{STAGING_PREFIX}{suffix}"
    if kind == "directory":
        residue.mkdir(mode=0o755)
    elif kind == "symlink":
        target = tmp_path / "residue-target"
        target.write_bytes(b"untouched")
        residue.symlink_to(target)
    else:
        residue.write_bytes(b"untouched")
        residue.chmod(0o644)
    before = _metadata_signature(residue)

    with pytest.raises(
        SafetyError,
        match="^Evidence candidate staging residue requires operator resolution$",
    ):
        write_evidence_candidate_tree(_result(), paths)

    assert _metadata_signature(residue) == before
    lock_metadata = os.lstat(paths.build / LOCK_NAME)
    assert stat.S_ISREG(lock_metadata.st_mode)
    assert stat.S_IMODE(lock_metadata.st_mode) == 0o644
    assert lock_metadata.st_uid == os.getuid()
    assert lock_metadata.st_nlink == 1
    assert sorted(path.name for path in paths.build.iterdir()) == sorted([LOCK_NAME, residue.name])
    assert not (paths.build / "evidence-candidates").exists()


def test_writer_residue_gate_precedes_existing_candidate_validation(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    paths = _repository(tmp_path)
    result = _result()
    published = write_evidence_candidate_tree(result, paths)
    residue = paths.build / f"{STAGING_PREFIX}operator-review"
    residue.mkdir(mode=0o755)
    before = _metadata_signature(residue)

    def forbidden(*_args: Any, **_kwargs: Any) -> None:
        raise AssertionError("residue gate must precede candidate validation")

    monkeypatch.setattr(writer_module, "_validate_exact_tree", forbidden)

    with pytest.raises(
        SafetyError,
        match="^Evidence candidate staging residue requires operator resolution$",
    ):
        write_evidence_candidate_tree(result, paths)

    assert _metadata_signature(residue) == before
    assert published.root.is_dir()


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
        if not displaced.exists():
            root = paths.build / "evidence-candidates"
            root.rename(displaced)
            _write_tree_directly(paths, result)
        real_revalidate(*args, **kwargs)

    monkeypatch.setattr(
        writer_module,
        "_revalidate_published_candidate",
        replace_then_revalidate,
    )

    with pytest.raises(SafetyError, match="changed|binding|identity"):
        write_evidence_candidate_tree(result, paths)

    replacement = paths.build / "evidence-candidates"
    assert (replacement / "candidate-manifest.json").read_bytes() == result.canonical_json_bytes
    assert displaced.is_dir()
    assert not list(paths.build.glob(f"{STAGING_PREFIX}*"))

    recovered = write_evidence_candidate_tree(result, paths)

    assert recovered.changed is False
    assert recovered.root == replacement


def test_postrename_build_fsync_failure_preserves_complete_tree_and_primary(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    paths = _repository(tmp_path)
    result = _result()
    sentinel = OSError("synthetic post-rename build fsync failure")
    real_open = writer_module.os.open
    real_fsync = writer_module._fsync_fd
    opened: list[int] = []

    def tracking_open(*args: Any, **kwargs: Any) -> int:
        fd = real_open(*args, **kwargs)
        opened.append(fd)
        return fd

    def fail_postrename_build_fsync(fd: int) -> None:
        target = os.readlink(f"/proc/self/fd/{fd}")
        if target == str(paths.build) and (paths.build / "evidence-candidates").is_dir():
            raise sentinel
        real_fsync(fd)

    monkeypatch.setattr(writer_module.os, "open", tracking_open)
    monkeypatch.setattr(writer_module, "_fsync_fd", fail_postrename_build_fsync)

    with pytest.raises(OSError) as caught:
        write_evidence_candidate_tree(result, paths)

    assert caught.value is sentinel
    published = paths.build / "evidence-candidates"
    _assert_complete_staging(published, result)
    assert not list(paths.build.glob(f"{STAGING_PREFIX}*"))
    assert opened
    for fd in opened:
        with pytest.raises(OSError):
            os.fstat(fd)

    recovered = write_evidence_candidate_tree(result, paths)

    assert recovered.changed is False


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
