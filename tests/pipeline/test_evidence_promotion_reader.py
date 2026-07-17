from __future__ import annotations

import dataclasses
import hashlib
import json
import os
from collections.abc import Mapping
from pathlib import Path
from types import MappingProxyType
from typing import Any

import pytest

import tools.openapi_pipeline.evidence_promotion as promotion_module
from tools.openapi_pipeline.capture import CaptureWriter
from tools.openapi_pipeline.errors import SafetyError
from tools.openapi_pipeline.evidence_promotion import (
    CaptureEvidenceReader,
    EvidencePair,
    EvidenceValidator,
)
from tools.openapi_pipeline.io import canonical_json_bytes
from tools.openapi_pipeline.live.lock import LiveProcessLock

OPERATION = "get_external_menu_by_id"


def _write_menu_pair(root: Path, version: int, *, run_id: str | None = None) -> tuple[Path, Path]:
    return CaptureWriter(root).write(
        run_id=run_id or f"run-v{version}",
        operation_id=OPERATION,
        kind="read",
        request_json={
            "externalMenuId": "11111111-1111-4111-8111-111111111111",
            "organizationIds": ["22222222-2222-4222-8222-222222222222"],
            "version": version,
        },
        response_json={"formatVersion": version, "itemCategories": []},
        metadata={"method": "POST", "path": "/api/2/menu/by_id", "status": 200},
        approved_path="/api/2/menu/by_id",
    )


def _complete_tree(root: Path) -> dict[int, tuple[Path, Path]]:
    return {version: _write_menu_pair(root, version) for version in (4, 2, 3)}


def _load(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    assert type(value) is dict
    return value


def _replace_json(path: Path, value: object) -> None:
    path.write_bytes(canonical_json_bytes(value))
    path.chmod(0o600)


def _lock_for(root: Path) -> LiveProcessLock:
    return LiveProcessLock(root.parent / ".state/live.lock")


def _read(
    root: Path,
    *,
    validator: EvidenceValidator | None = None,
) -> Mapping[int, EvidencePair]:
    lock = _lock_for(root)
    with lock:
        return CaptureEvidenceReader(
            root,
            process_lock=lock,
            validator=validator,
        ).read_menu_pairs()


def test_reader_collects_one_immutable_canonical_pair_per_version_without_writes(
    tmp_path: Path,
) -> None:
    root = tmp_path / "captures"
    paths = _complete_tree(root)
    before = {
        path: (path.stat().st_ino, path.stat().st_size, path.read_bytes())
        for pair in paths.values()
        for path in pair
    }

    pairs = _read(root)

    assert isinstance(pairs, MappingProxyType)
    assert tuple(pairs) == (2, 3, 4)
    for version, pair in pairs.items():
        request_path, response_path = paths[version]
        assert pair.version == version
        assert pair.request["body"]["version"] == version
        assert pair.response["body"]["formatVersion"] == version
        assert pair.request_sha256 == hashlib.sha256(request_path.read_bytes()).hexdigest()
        assert pair.response_sha256 == hashlib.sha256(response_path.read_bytes()).hexdigest()
        assert isinstance(pair.request, MappingProxyType)
        assert isinstance(pair.request["body"], MappingProxyType)
        assert isinstance(pair.request["body"]["organizationIds"], tuple)
        with pytest.raises(dataclasses.FrozenInstanceError):
            pair.version = 9
        with pytest.raises(TypeError):
            pair.request["body"] = {}  # type: ignore[index]

    assert {
        path: (path.stat().st_ino, path.stat().st_size, path.read_bytes()) for path in before
    } == before


def test_reader_accepts_an_injected_held_canonical_live_lock(tmp_path: Path) -> None:
    root = tmp_path / "captures"
    _complete_tree(root)
    lock = LiveProcessLock(tmp_path / ".state/live.lock")

    with pytest.raises(SafetyError, match="held"):
        CaptureEvidenceReader(root, process_lock=lock).read_menu_pairs()

    with lock:
        assert tuple(CaptureEvidenceReader(root, process_lock=lock).read_menu_pairs()) == (2, 3, 4)


@pytest.mark.parametrize("missing_version", [2, 3, 4])
def test_reader_rejects_a_missing_version(tmp_path: Path, missing_version: int) -> None:
    root = tmp_path / "captures"
    for version in {2, 3, 4} - {missing_version}:
        _write_menu_pair(root, version)

    with pytest.raises(SafetyError, match="exactly one.*2, 3, and 4"):
        _read(root)


def test_reader_rejects_duplicate_and_partial_pairs(tmp_path: Path) -> None:
    duplicate_root = tmp_path / "duplicates"
    _complete_tree(duplicate_root)
    _write_menu_pair(duplicate_root, 2, run_id="second-v2")
    with pytest.raises(SafetyError, match="duplicate.*version 2"):
        _read(duplicate_root)

    partial_root = tmp_path / "partial"
    paths = _complete_tree(partial_root)
    paths[3][1].unlink()
    with pytest.raises(SafetyError, match="exactly request.json and response.json"):
        _read(partial_root)


@pytest.mark.parametrize(
    ("target", "mutation", "message"),
    [
        ("request", lambda value: {**value, "extra": None}, "envelope"),
        (
            "request",
            lambda value: {**value, "metadata": {**value["metadata"], "status": 201}},
            "metadata",
        ),
        (
            "request",
            lambda value: {
                **value,
                "body": {**value["body"], "unexpected": "<redacted:string>"},
            },
            "payload",
        ),
        (
            "request",
            lambda value: {**value, "body": {**value["body"], "version": True}},
            "version",
        ),
        (
            "response",
            lambda value: {**value, "body": {**value["body"], "formatVersion": 3}},
            "formatVersion",
        ),
    ],
)
def test_reader_rejects_invalid_envelopes_metadata_and_version_contract(
    tmp_path: Path,
    target: str,
    mutation: Any,
    message: str,
) -> None:
    root = tmp_path / "captures"
    paths = _complete_tree(root)
    path = paths[2][0 if target == "request" else 1]
    _replace_json(path, mutation(_load(path)))

    with pytest.raises(SafetyError, match=message):
        _read(root)


def test_reader_rejects_request_response_metadata_mismatch(tmp_path: Path) -> None:
    root = tmp_path / "captures"
    paths = _complete_tree(root)
    response_path = paths[2][1]
    response = _load(response_path)
    response["metadata"]["headers"] = {"accept": "application/json"}
    _replace_json(response_path, response)

    with pytest.raises(SafetyError, match="metadata.*identical"):
        _read(root)


@pytest.mark.parametrize("malformation", ["duplicate", "nan", "noncanonical", "utf8", "depth"])
def test_reader_rejects_non_strict_or_noncanonical_json(tmp_path: Path, malformation: str) -> None:
    root = tmp_path / "captures"
    paths = _complete_tree(root)
    request_path = paths[2][0]
    if malformation == "duplicate":
        body = request_path.read_bytes().replace(b'{"body":', b'{"body":null,"body":', 1)
    elif malformation == "nan":
        body = request_path.read_bytes().replace(b'"version":2', b'"version":NaN', 1)
    elif malformation == "noncanonical":
        body = json.dumps(_load(request_path), ensure_ascii=False).encode("utf-8")
    elif malformation == "utf8":
        body = b"\xff\n"
    else:
        nested: object = None
        for _index in range(66):
            nested = [nested]
        value = _load(request_path)
        value["body"]["nested"] = nested
        body = canonical_json_bytes(value)
    request_path.write_bytes(body)
    request_path.chmod(0o600)

    with pytest.raises(SafetyError, match="JSON|canonical|nesting"):
        _read(root)


@pytest.mark.parametrize("unsafe", ["extra", "symlink", "hardlink", "fifo", "directory"])
def test_reader_rejects_unsafe_or_extra_operation_entries(tmp_path: Path, unsafe: str) -> None:
    root = tmp_path / "captures"
    paths = _complete_tree(root)
    request_path, response_path = paths[2]
    operation = request_path.parent
    if unsafe == "extra":
        extra = operation / "extra.json"
        extra.write_bytes(b"{}\n")
        extra.chmod(0o600)
    elif unsafe == "symlink":
        request_path.unlink()
        request_path.symlink_to(response_path)
    elif unsafe == "hardlink":
        os.link(request_path, tmp_path / "request-alias.json")
    elif unsafe == "fifo":
        request_path.unlink()
        os.mkfifo(request_path, mode=0o600)
    else:
        request_path.unlink()
        request_path.mkdir(mode=0o700)

    with pytest.raises(SafetyError, match="exactly|private regular|symlink|hard link"):
        _read(root)


def test_reader_rejects_oversize_wide_or_wrong_owner_entries(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    oversize_root = tmp_path / "oversize"
    paths = _complete_tree(oversize_root)
    with paths[2][0].open("r+b") as stream:
        stream.truncate(32 * 1024 * 1024 + 1)
    with pytest.raises(SafetyError, match="32 MiB"):
        _read(oversize_root)

    wide_root = tmp_path / "wide"
    wide_paths = _complete_tree(wide_root)
    wide_paths[2][1].chmod(0o644)
    with pytest.raises(SafetyError, match="0600"):
        _read(wide_root)

    owner_root = tmp_path / "owner"
    _complete_tree(owner_root)
    lock = _lock_for(owner_root)
    with lock:
        actual_uid = os.getuid()
        monkeypatch.setattr(promotion_module.os, "getuid", lambda: actual_uid + 1)
        with pytest.raises(SafetyError, match="owned"):
            CaptureEvidenceReader(owner_root, process_lock=lock).read_menu_pairs()


@pytest.mark.parametrize("component", ["root", "run", "operation"])
def test_reader_requires_mode_0700_on_every_private_directory(
    tmp_path: Path, component: str
) -> None:
    root = tmp_path / "captures"
    paths = _complete_tree(root)
    target = {
        "root": root,
        "run": paths[2][0].parent.parent,
        "operation": paths[2][0].parent,
    }[component]
    target.chmod(0o755)

    with pytest.raises(SafetyError, match="0700"):
        _read(root)


def test_reader_rejects_symlinked_directory_and_unsafe_root_entries(tmp_path: Path) -> None:
    root = tmp_path / "captures"
    paths = _complete_tree(root)
    operation = paths[2][0].parent
    moved = tmp_path / "moved-operation"
    operation.rename(moved)
    operation.symlink_to(moved, target_is_directory=True)
    with pytest.raises(SafetyError, match="directory|symlink"):
        _read(root)

    other_root = tmp_path / "other-captures"
    _complete_tree(other_root)
    extra = other_root / "not-a-run"
    extra.write_bytes(b"unsafe\n")
    extra.chmod(0o600)
    with pytest.raises(SafetyError, match="run.*directory"):
        _read(other_root)


def test_reader_rejects_a_symlinked_capture_root_ancestor(tmp_path: Path) -> None:
    real_root = tmp_path / "real/private/captures"
    _complete_tree(real_root)
    linked_private = tmp_path / "linked-private"
    linked_private.symlink_to(real_root.parent, target_is_directory=True)
    linked_root = linked_private / "captures"
    lock = LiveProcessLock(tmp_path / ".state/live.lock")

    with lock, pytest.raises(SafetyError, match="symlink|ancestry"):
        CaptureEvidenceReader(linked_root, process_lock=lock).read_menu_pairs()


def test_reader_double_read_detects_a_concurrent_file_swap(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    root = tmp_path / "captures"
    paths = _complete_tree(root)
    target = paths[2][0]
    original = promotion_module._read_private_file_once
    calls = 0

    def swap_after_first_read(directory_fd: int, name: str, expected: os.stat_result) -> bytes:
        nonlocal calls
        body = original(directory_fd, name, expected)
        if name == "request.json":
            calls += 1
            if calls == 1:
                replacement = target.with_name("replacement.json")
                replacement.write_bytes(target.read_bytes())
                replacement.chmod(0o600)
                replacement.replace(target)
        return body

    monkeypatch.setattr(promotion_module, "_read_private_file_once", swap_after_first_read)

    with pytest.raises(SafetyError, match="changed|concurrent"):
        _read(root)


def test_reader_revalidates_operation_entry_list_after_read(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    root = tmp_path / "captures"
    paths = _complete_tree(root)
    operation = paths[2][0].parent
    original = promotion_module._directory_entries
    target_calls = 0

    def add_entry_after_snapshot(directory_fd: int) -> tuple[str, ...]:
        nonlocal target_calls
        entries = original(directory_fd)
        if entries == ("request.json", "response.json"):
            target_calls += 1
            if target_calls == 1:
                extra = operation / "late.json"
                extra.write_bytes(b"{}\n")
                extra.chmod(0o600)
        return entries

    monkeypatch.setattr(promotion_module, "_directory_entries", add_entry_after_snapshot)

    with pytest.raises(SafetyError, match="changed|concurrent"):
        _read(root)


def test_reader_fails_if_the_injected_lock_is_released_mid_read(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    root = tmp_path / "captures"
    _complete_tree(root)
    lock = _lock_for(root)
    lock.acquire()
    original = promotion_module._directory_entries
    released = False

    def release_after_first_snapshot(directory_fd: int) -> tuple[str, ...]:
        nonlocal released
        entries = original(directory_fd)
        if not released:
            released = True
            lock.release()
        return entries

    monkeypatch.setattr(promotion_module, "_directory_entries", release_after_first_snapshot)
    try:
        with pytest.raises(SafetyError, match="released"):
            CaptureEvidenceReader(root, process_lock=lock).read_menu_pairs()
    finally:
        lock.release()


def test_reader_runs_generic_scan_and_injected_schema_validator(tmp_path: Path) -> None:
    root = tmp_path / "captures"
    paths = _complete_tree(root)
    response_path = paths[2][1]
    response = _load(response_path)
    response["body"]["leak"] = "person@example.com"
    _replace_json(response_path, response)

    with pytest.raises(SafetyError, match="secret/PII"):
        _read(root)

    clean_root = tmp_path / "clean"
    _complete_tree(clean_root)
    validated: list[int] = []

    def validator(version: int, request: object, response: object) -> None:
        assert request is not response
        validated.append(version)

    pairs = _read(clean_root, validator=validator)
    assert tuple(pairs) == (2, 3, 4)
    assert validated == [2, 3, 4]


def test_reader_requires_a_held_lock_before_filesystem_access(tmp_path: Path) -> None:
    root = tmp_path / "missing"
    with pytest.raises(SafetyError, match="held.*lock"):
        CaptureEvidenceReader(root).read_menu_pairs()
    assert not root.exists()


def test_reader_rejects_an_unapproved_operation_before_filesystem_access(tmp_path: Path) -> None:
    root = tmp_path / "missing"
    lock = _lock_for(root)
    with lock, pytest.raises(SafetyError, match="approved"):
        CaptureEvidenceReader(
            root,
            operation="authenticate",
            process_lock=lock,
        ).read_menu_pairs()

    assert not root.exists()
