"""Controlled acceptance of one freshly re-authorized evidence candidate.

Supported candidate writers and acceptors cooperate on the candidate lock, and
capture readers cooperate on the live lock. A same-UID process that deliberately
ignores those locks is outside the threat model because it can already mutate the
checkout directly. The existing promotion transaction provides all-or-rollback
for caught in-process failures; this module does not claim power-loss atomicity.
"""

from __future__ import annotations

import os
import secrets
import stat
from collections.abc import Mapping
from contextlib import ExitStack, suppress
from dataclasses import dataclass
from pathlib import Path

from .errors import SafetyError
from .evidence_analysis import analyze_menu_evidence
from .evidence_candidate_contract import EVIDENCE_CANDIDATE_PAYLOAD_PATHS
from .evidence_candidate_store import build_evidence_candidate_manifest
from .evidence_candidate_writer import (
    EvidenceCandidateProcessLock,
    assert_evidence_candidate_tree_matches,
)
from .evidence_candidates import build_evidence_candidate_bundle
from .evidence_promotion import CaptureEvidenceReader
from .io import canonical_json_bytes
from .live.lock import LiveProcessLock
from .paths import RepoPaths
from .pipeline import compose_reviewed_evidence_base_candidate
from .promotion import PromotionItem, promote_transaction

_CANDIDATE_DIRECTORY = "evidence-candidates"
_ACCEPT_STAGING_PREFIX = ".evidence-accept.tmp-"
_DIRECTORY_MODE = 0o755
_FILE_MODE = 0o644
_COMMITTED_ERROR = "Evidence acceptance committed with residue; operator resolution is required"
_RESIDUE_ERROR = "Evidence acceptance residue requires operator resolution"
_TARGET_ERROR = "Evidence acceptance target is unsafe"


@dataclass(frozen=True, slots=True)
class EvidenceCandidateAcceptResult:
    candidate_root: Path
    accepted_paths: tuple[Path, ...]
    manifest_sha256: str
    changed: bool


def accept_evidence_candidate(paths: RepoPaths) -> EvidenceCandidateAcceptResult:
    if type(paths) is not RepoPaths:
        raise SafetyError("Evidence acceptance requires exact repository paths")
    candidate_root = paths.build / _CANDIDATE_DIRECTORY
    accepted_paths = tuple(paths.root / relative for relative in EVIDENCE_CANDIDATE_PAYLOAD_PATHS)

    with ExitStack() as locks:
        candidate_lock = locks.enter_context(EvidenceCandidateProcessLock(paths))
        candidate_token = candidate_lock.capture_binding()
        live_lock = locks.enter_context(LiveProcessLock(paths.state / "live.lock"))
        live_token = live_lock.capture_binding_token()
        _reject_accept_residue(paths)
        _reject_promotion_residue(paths)
        candidate_lock.assert_binding(candidate_token)
        live_lock.assert_binding_token(live_token)

        base, _model_mappings = compose_reviewed_evidence_base_candidate(paths)
        base_body = _canonical_base_bytes(base)
        pairs = CaptureEvidenceReader(
            paths.root,
            base,
            process_lock=live_lock,
        ).read_menu_pairs()
        analysis = analyze_menu_evidence(pairs, base)
        bundle = build_evidence_candidate_bundle(
            analysis=analysis,
            pairs=pairs,
            effective_schema=base,
        )
        expected = build_evidence_candidate_manifest(bundle)

        recomposed, _recomposed_mappings = compose_reviewed_evidence_base_candidate(paths)
        if _canonical_base_bytes(recomposed) != base_body:
            raise SafetyError(
                "Reviewed evidence base changed during candidate acceptance"
            ) from None

        assert_evidence_candidate_tree_matches(
            expected,
            paths,
            process_lock=candidate_lock,
        )
        candidate_lock.assert_binding(candidate_token)
        live_lock.assert_binding_token(live_token)

        if _preflight_targets(paths, expected.canonical_payloads):
            candidate_lock.assert_binding(candidate_token)
            live_lock.assert_binding_token(live_token)
            return EvidenceCandidateAcceptResult(
                candidate_root=candidate_root,
                accepted_paths=accepted_paths,
                manifest_sha256=expected.sha256,
                changed=False,
            )

        staging_root = _stage_payloads(paths, expected.canonical_payloads)
        items = [
            PromotionItem(
                staged=staging_root / relative,
                target=paths.root / relative,
            )
            for relative in EVIDENCE_CANDIDATE_PAYLOAD_PATHS
        ]
        candidate_lock.assert_binding(candidate_token)
        live_lock.assert_binding_token(live_token)
        promote_transaction(items, root=paths.root)

        try:
            if not _preflight_targets(paths, expected.canonical_payloads):
                raise SafetyError(_COMMITTED_ERROR)
            _reject_promotion_residue(paths)
            _fsync_target_parents(paths)
            _remove_empty_staging_tree(staging_root)
            _fsync_directory(paths.build)
            candidate_lock.assert_binding(candidate_token)
            live_lock.assert_binding_token(live_token)
        except BaseException:
            raise SafetyError(_COMMITTED_ERROR) from None

        return EvidenceCandidateAcceptResult(
            candidate_root=candidate_root,
            accepted_paths=accepted_paths,
            manifest_sha256=expected.sha256,
            changed=True,
        )


def _canonical_base_bytes(value: object) -> bytes:
    if type(value) is not dict:
        raise SafetyError("Reviewed evidence base is not a plain JSON document")
    try:
        return canonical_json_bytes(value)
    except (TypeError, ValueError, RecursionError):
        raise SafetyError("Reviewed evidence base is not canonical JSON") from None


def _reject_accept_residue(paths: RepoPaths) -> None:
    try:
        with os.scandir(paths.build) as entries:
            if any(entry.name.startswith(_ACCEPT_STAGING_PREFIX) for entry in entries):
                raise SafetyError(_RESIDUE_ERROR)
    except SafetyError:
        raise
    except OSError:
        raise SafetyError("Cannot inspect evidence acceptance residue safely") from None


def _reject_promotion_residue(paths: RepoPaths) -> None:
    inspected: set[Path] = set()
    for relative in EVIDENCE_CANDIDATE_PAYLOAD_PATHS:
        parent = (paths.root / relative).parent
        if parent in inspected:
            continue
        inspected.add(parent)
        if not _validate_existing_parent_chain(paths.root, parent):
            continue
        prefixes = tuple(
            prefix
            for candidate_relative in EVIDENCE_CANDIDATE_PAYLOAD_PATHS
            if (paths.root / candidate_relative).parent == parent
            for prefix in (
                f".{Path(candidate_relative).name}.backup-",
                f".{Path(candidate_relative).name}.orphaned-backup-",
            )
        )
        try:
            with os.scandir(parent) as entries:
                if any(entry.name.startswith(prefixes) for entry in entries):
                    raise SafetyError(_RESIDUE_ERROR)
        except SafetyError:
            raise
        except OSError:
            raise SafetyError("Cannot inspect evidence promotion residue safely") from None


def _validate_existing_parent_chain(root: Path, parent: Path) -> bool:
    try:
        relative = parent.relative_to(root)
    except ValueError:
        raise SafetyError(_TARGET_ERROR) from None
    current = root
    missing = False
    for component in relative.parts:
        current /= component
        if missing:
            continue
        try:
            metadata = current.lstat()
        except FileNotFoundError:
            missing = True
            continue
        except OSError:
            raise SafetyError(_TARGET_ERROR) from None
        if (
            stat.S_ISLNK(metadata.st_mode)
            or not stat.S_ISDIR(metadata.st_mode)
            or stat.S_IMODE(metadata.st_mode) != _DIRECTORY_MODE
            or metadata.st_uid != os.getuid()
        ):
            raise SafetyError(_TARGET_ERROR)
    return not missing


def _preflight_targets(paths: RepoPaths, payloads: Mapping[str, bytes]) -> bool:
    if tuple(payloads) != EVIDENCE_CANDIDATE_PAYLOAD_PATHS:
        raise SafetyError("Evidence acceptance payload scope is invalid")
    all_exact = True
    for relative in EVIDENCE_CANDIDATE_PAYLOAD_PATHS:
        target = paths.root / relative
        _validate_existing_parent_chain(paths.root, target.parent)
        try:
            expected_metadata = target.lstat()
        except FileNotFoundError:
            all_exact = False
            continue
        except OSError:
            raise SafetyError(_TARGET_ERROR) from None
        if (
            _read_public_file(target, expected_metadata, len(payloads[relative]))
            != payloads[relative]
        ):
            all_exact = False
    return all_exact


def _validate_public_file_metadata(metadata: os.stat_result) -> None:
    if (
        stat.S_ISLNK(metadata.st_mode)
        or not stat.S_ISREG(metadata.st_mode)
        or stat.S_IMODE(metadata.st_mode) != _FILE_MODE
        or metadata.st_uid != os.getuid()
        or metadata.st_nlink != 1
    ):
        raise SafetyError(_TARGET_ERROR)


def _read_public_file(
    path: Path,
    expected_metadata: os.stat_result,
    expected_size: int,
) -> bytes:
    descriptor: int | None = None
    try:
        descriptor = os.open(
            path,
            os.O_RDONLY
            | os.O_CLOEXEC
            | getattr(os, "O_NOFOLLOW", 0)
            | getattr(os, "O_NONBLOCK", 0),
        )
        metadata = os.fstat(descriptor)
        _validate_public_file_metadata(metadata)
        if (metadata.st_dev, metadata.st_ino) != (
            expected_metadata.st_dev,
            expected_metadata.st_ino,
        ):
            raise SafetyError(_TARGET_ERROR)
        chunks: list[bytes] = []
        remaining = expected_size + 1
        while remaining:
            chunk = os.read(descriptor, min(65536, remaining))
            if not chunk:
                break
            chunks.append(chunk)
            remaining -= len(chunk)
        return b"".join(chunks)
    except SafetyError:
        raise
    except OSError:
        raise SafetyError(_TARGET_ERROR) from None
    finally:
        if descriptor is not None:
            with suppress(OSError):
                os.close(descriptor)


def _stage_payloads(paths: RepoPaths, payloads: Mapping[str, bytes]) -> Path:
    staging_root = _create_staging_root(paths.build)
    for relative in EVIDENCE_CANDIDATE_PAYLOAD_PATHS:
        target = staging_root / relative
        _mkdir_public_parents(staging_root, target.parent)
        _write_staged_file(target, payloads[relative])
    for directory in _staging_directories(staging_root):
        _fsync_directory(directory)
    _fsync_directory(paths.build)
    return staging_root


def _create_staging_root(build: Path) -> Path:
    for _attempt in range(16):
        candidate = build / f"{_ACCEPT_STAGING_PREFIX}{secrets.token_hex(16)}"
        try:
            candidate.mkdir(mode=_DIRECTORY_MODE)
        except FileExistsError:
            continue
        except OSError:
            raise SafetyError("Cannot create evidence acceptance staging safely") from None
        candidate.chmod(_DIRECTORY_MODE, follow_symlinks=False)
        metadata = candidate.lstat()
        if (
            not stat.S_ISDIR(metadata.st_mode)
            or stat.S_ISLNK(metadata.st_mode)
            or stat.S_IMODE(metadata.st_mode) != _DIRECTORY_MODE
            or metadata.st_uid != os.getuid()
        ):
            raise SafetyError("Evidence acceptance staging root is unsafe")
        return candidate
    raise SafetyError("Cannot allocate a unique evidence acceptance staging root")


def _mkdir_public_parents(root: Path, parent: Path) -> None:
    relative = parent.relative_to(root)
    current = root
    for component in relative.parts:
        current /= component
        try:
            current.mkdir(mode=_DIRECTORY_MODE)
            current.chmod(_DIRECTORY_MODE, follow_symlinks=False)
        except FileExistsError:
            pass
        except OSError:
            raise SafetyError("Cannot create evidence acceptance staging tree") from None
        metadata = current.lstat()
        if (
            not stat.S_ISDIR(metadata.st_mode)
            or stat.S_ISLNK(metadata.st_mode)
            or stat.S_IMODE(metadata.st_mode) != _DIRECTORY_MODE
            or metadata.st_uid != os.getuid()
        ):
            raise SafetyError("Evidence acceptance staging directory is unsafe")


def _write_staged_file(path: Path, body: bytes) -> None:
    descriptor: int | None = None
    try:
        descriptor = os.open(
            path,
            os.O_WRONLY
            | os.O_CREAT
            | os.O_EXCL
            | os.O_CLOEXEC
            | getattr(os, "O_NOFOLLOW", 0)
            | getattr(os, "O_NONBLOCK", 0),
            _FILE_MODE,
        )
        os.fchmod(descriptor, _FILE_MODE)
        view = memoryview(body)
        while view:
            written = os.write(descriptor, view)
            if written <= 0:
                raise OSError("short write")
            view = view[written:]
        os.fsync(descriptor)
        metadata = os.fstat(descriptor)
        _validate_public_file_metadata(metadata)
        if metadata.st_size != len(body):
            raise SafetyError("Evidence acceptance staging file is incomplete")
    except SafetyError:
        raise
    except OSError:
        raise SafetyError("Cannot write evidence acceptance staging file safely") from None
    finally:
        if descriptor is not None:
            with suppress(OSError):
                os.close(descriptor)


def _staging_directories(staging_root: Path) -> tuple[Path, ...]:
    directories = {staging_root}
    for relative in EVIDENCE_CANDIDATE_PAYLOAD_PATHS:
        current = (staging_root / relative).parent
        while current != staging_root:
            directories.add(current)
            current = current.parent
    return tuple(sorted(directories, key=lambda path: len(path.parts), reverse=True))


def _fsync_target_parents(paths: RepoPaths) -> None:
    parents = {paths.root / Path(relative).parent for relative in EVIDENCE_CANDIDATE_PAYLOAD_PATHS}
    for parent in sorted(parents, key=lambda path: path.as_posix()):
        _fsync_directory(parent)


def _fsync_directory(path: Path) -> None:
    descriptor: int | None = None
    try:
        descriptor = os.open(
            path,
            os.O_RDONLY | os.O_CLOEXEC | os.O_DIRECTORY | getattr(os, "O_NOFOLLOW", 0),
        )
        os.fsync(descriptor)
    except OSError:
        raise SafetyError("Cannot synchronize evidence acceptance directory") from None
    finally:
        if descriptor is not None:
            with suppress(OSError):
                os.close(descriptor)


def _remove_empty_staging_tree(staging_root: Path) -> None:
    for directory in _staging_directories(staging_root):
        try:
            directory.rmdir()
        except OSError:
            raise SafetyError(_COMMITTED_ERROR) from None
