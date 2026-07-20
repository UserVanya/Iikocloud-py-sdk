from __future__ import annotations

import json
import os
import re
import shutil
import stat
import uuid
from contextlib import suppress
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from .errors import PipelineError
from .generator import Toolchain
from .io import canonical_json_bytes, sha256_bytes, write_json_atomic

_SHA256 = re.compile(r"[0-9a-f]{64}")
_REPOSITORY_CONTROL_DIRECTORIES = {
    ".git",
    "build",
    "generator",
    "openapi",
    "src",
    "tests",
    "tools",
}


@dataclass(frozen=True)
class PromotionItem:
    staged: Path
    target: Path


def regular_tree_files(root: Path, *, label: str) -> tuple[Path, ...]:
    """Return sorted regular files while rejecting links and special entries."""

    try:
        root_mode = root.lstat().st_mode
    except OSError as error:
        raise PipelineError(f"Cannot inspect {label}: {root}") from error
    if stat.S_ISLNK(root_mode):
        raise PipelineError(f"{label} must not be a symlink: {root}")
    if not stat.S_ISDIR(root_mode):
        raise PipelineError(f"{label} is not a regular directory: {root}")

    files: list[Path] = []

    def visit(directory: Path) -> None:
        try:
            with os.scandir(directory) as iterator:
                entries = sorted(iterator, key=lambda entry: entry.name)
        except OSError as error:
            raise PipelineError(f"Cannot walk {label}: {directory}") from error
        for entry in entries:
            path = Path(entry.path)
            try:
                mode = entry.stat(follow_symlinks=False).st_mode
            except OSError as error:
                raise PipelineError(f"Cannot inspect {label} entry: {path}") from error
            if stat.S_ISLNK(mode):
                raise PipelineError(f"{label} contains a symlink: {path}")
            if stat.S_ISDIR(mode):
                visit(path)
            elif stat.S_ISREG(mode):
                files.append(path)
            else:
                raise PipelineError(f"{label} contains a non-regular entry: {path}")

    visit(root)
    return tuple(files)


def copy_regular_tree(source: Path, destination: Path, *, label: str) -> None:
    """Copy a validated tree without following links or accepting special entries."""

    regular_tree_files(source, label=label)
    if destination.exists() or destination.is_symlink():
        raise PipelineError(f"{label} destination already exists: {destination}")

    def copy_directory(source_directory: Path, destination_directory: Path) -> None:
        destination_directory.mkdir()
        try:
            with os.scandir(source_directory) as iterator:
                entries = sorted(iterator, key=lambda entry: entry.name)
        except OSError as error:
            raise PipelineError(f"Cannot copy {label}: {source_directory}") from error
        for entry in entries:
            source_path = Path(entry.path)
            destination_path = destination_directory / entry.name
            try:
                mode = entry.stat(follow_symlinks=False).st_mode
            except OSError as error:
                raise PipelineError(f"Cannot inspect {label} entry: {source_path}") from error
            if stat.S_ISLNK(mode):
                raise PipelineError(f"{label} contains a symlink: {source_path}")
            if stat.S_ISDIR(mode):
                copy_directory(source_path, destination_path)
            elif stat.S_ISREG(mode):
                try:
                    shutil.copy2(source_path, destination_path, follow_symlinks=False)
                except OSError as error:
                    raise PipelineError(f"Cannot copy {label} file: {source_path}") from error
            else:
                raise PipelineError(f"{label} contains a non-regular entry: {source_path}")

    destination.parent.mkdir(parents=True, exist_ok=True)
    copy_directory(source, destination)
    regular_tree_files(destination, label=f"Copied {label}")


def _common_control_root(items: list[PromotionItem]) -> Path:
    paths = [path.absolute() for item in items for path in (item.staged, item.target)]
    try:
        return Path(os.path.commonpath(paths)).resolve(strict=False)
    except (OSError, ValueError) as error:
        raise PipelineError("Promotion paths do not share a controlled root") from error


def _resolve_inside(path: Path, root: Path, *, label: str, strict: bool) -> Path:
    if path.is_symlink():
        raise PipelineError(f"Promotion {label} must not be a symlink: {path}")
    try:
        resolved = path.resolve(strict=strict)
    except (OSError, RuntimeError) as error:
        raise PipelineError(f"Cannot resolve promotion {label}: {path}") from error
    if not resolved.is_relative_to(root):
        raise PipelineError(f"Promotion {label} escapes the controlled repository root: {path}")
    return resolved


def _overlaps(left: Path, right: Path) -> bool:
    return left == right or left.is_relative_to(right) or right.is_relative_to(left)


def _preflight(items: list[PromotionItem], root: Path | None) -> tuple[Path, list[PromotionItem]]:
    if not items:
        raise PipelineError("Promotion transaction must contain at least one item")
    controlled_root = (root or _common_control_root(items)).resolve(strict=True)
    if not controlled_root.is_dir():
        raise PipelineError("Promotion controlled root must be a directory")

    normalized: list[PromotionItem] = []
    staged_paths: set[Path] = set()
    target_paths: list[Path] = []
    for item in items:
        staged = _resolve_inside(item.staged, controlled_root, label="source", strict=True)
        target = _resolve_inside(item.target, controlled_root, label="target", strict=False)
        if not (staged.is_file() or staged.is_dir()):
            raise PipelineError(
                f"Promotion source is not a regular file or directory: {item.staged}"
            )
        if target == controlled_root:
            raise PipelineError("Promotion cannot replace the controlled repository root")
        if target.parent == controlled_root and target.name in _REPOSITORY_CONTROL_DIRECTORIES:
            raise PipelineError(
                f"Promotion cannot broadly replace repository control directory: {target.name}"
            )
        if target.exists() and not (target.is_file() or target.is_dir()):
            raise PipelineError(
                f"Promotion target is not a regular file or directory: {item.target}"
            )
        if staged in staged_paths:
            raise PipelineError(f"Duplicate promotion source: {item.staged}")
        if any(_overlaps(target, existing) for existing in target_paths):
            raise PipelineError(
                f"Promotion targets must be unique and non-overlapping: {item.target}"
            )
        if any(_overlaps(staged, existing) for existing in target_paths) or any(
            _overlaps(target, existing) for existing in staged_paths
        ):
            raise PipelineError("Promotion sources and targets must not overlap")
        staged_paths.add(staged)
        target_paths.append(target)
        normalized.append(PromotionItem(staged, target))
    return controlled_root, normalized


def _create_parent(path: Path, root: Path, created: list[Path]) -> None:
    missing: list[Path] = []
    current = path.parent
    while current != root and not current.exists():
        missing.append(current)
        current = current.parent
    if current.is_symlink():
        raise PipelineError(f"Promotion target parent must not be a symlink: {current}")
    for directory in reversed(missing):
        created.append(directory)
        try:
            directory.mkdir(mode=0o755)
            directory.chmod(0o755, follow_symlinks=False)
            metadata = directory.lstat()
        except OSError as error:
            raise PipelineError("Cannot create promotion target parent safely") from error
        if (
            stat.S_ISLNK(metadata.st_mode)
            or not stat.S_ISDIR(metadata.st_mode)
            or stat.S_IMODE(metadata.st_mode) != 0o755
            or metadata.st_uid != os.getuid()
        ):
            raise PipelineError("Promotion-created target parent is unsafe")


def _remove(path: Path) -> None:
    if path.is_symlink() or path.is_file():
        path.unlink(missing_ok=True)
    elif path.is_dir():
        shutil.rmtree(path)


def promote_transaction(items: list[PromotionItem], *, root: Path | None = None) -> None:
    controlled_root, normalized = _preflight(items, root)
    token = uuid.uuid4().hex
    backups: list[tuple[Path, Path]] = []
    promoted: list[PromotionItem] = []
    created: list[Path] = []

    try:
        for item in normalized:
            _create_parent(item.target, controlled_root, created)
            if item.target.exists():
                backup = item.target.with_name(f".{item.target.name}.backup-{token}")
                if backup.exists() or backup.is_symlink():
                    raise PipelineError(f"Promotion backup path already exists: {backup}")
                backups.append((backup, item.target))
                os.replace(item.target, backup)
            promoted.append(item)
            os.replace(item.staged, item.target)
    except BaseException as original:
        rollback_errors: list[str] = []
        for item in reversed(promoted):
            try:
                if item.target.exists() or item.target.is_symlink():
                    os.replace(item.target, item.staged)
            except BaseException as rollback_error:
                rollback_errors.append(f"restore staged {item.staged}: {rollback_error!r}")
        for backup, target in reversed(backups):
            try:
                if backup.exists() or backup.is_symlink():
                    if target.exists() or target.is_symlink():
                        _remove(target)
                    os.replace(backup, target)
            except BaseException as rollback_error:
                rollback_errors.append(f"restore target {target}: {rollback_error!r}")
        for directory in reversed(created):
            with suppress(OSError):
                directory.rmdir()
        if rollback_errors and hasattr(original, "add_note"):
            original.add_note("Promotion rollback problems: " + "; ".join(rollback_errors))
        raise
    else:
        # Every replacement above is the transaction's commit point.  Backup
        # deletion is post-commit housekeeping and must not make a successful
        # transaction look failed.  A failed deletion is labelled for a later,
        # explicit cleanup pass while cleanup of the remaining backups continues.
        for backup, target in backups:
            try:
                _remove(backup)
            except Exception:
                orphan = target.with_name(f".{target.name}.orphaned-backup-{token}")
                with suppress(Exception):
                    os.replace(backup, orphan)


def _regular_file_hashes(package: Path) -> dict[str, str]:
    result: dict[str, str] = {}
    for path in regular_tree_files(package, label="Generated package"):
        relative = (Path(package.name) / path.relative_to(package)).as_posix()
        result[relative] = sha256_bytes(path.read_bytes())
    return result


def build_generated_manifest(
    package: Path,
    *,
    effective_schema_sha256: str,
    toolchain: Toolchain,
) -> dict[str, Any]:
    if _SHA256.fullmatch(effective_schema_sha256) is None:
        raise PipelineError("Effective schema hash must be a lowercase SHA-256 digest")
    return {
        "effective_schema_sha256": effective_schema_sha256,
        "generator": {
            "image": toolchain.image,
            "version": toolchain.version,
            "digest": toolchain.digest,
        },
        "files": _regular_file_hashes(package),
    }


def write_generated_manifest(
    package: Path,
    destination: Path,
    *,
    effective_schema_sha256: str,
    toolchain: Toolchain,
) -> None:
    write_json_atomic(
        destination,
        build_generated_manifest(
            package,
            effective_schema_sha256=effective_schema_sha256,
            toolchain=toolchain,
        ),
    )


def load_generated_manifest(path: Path) -> dict[str, Any]:
    try:
        raw = path.read_bytes()
        value = json.loads(raw.decode("utf-8"))
    except (OSError, UnicodeError, ValueError) as error:
        raise PipelineError(f"Cannot load generated manifest: {path}") from error
    if not isinstance(value, dict) or set(value) != {
        "effective_schema_sha256",
        "generator",
        "files",
    }:
        raise PipelineError("Generated manifest has an invalid root shape")
    schema_hash = value["effective_schema_sha256"]
    generator = value["generator"]
    files = value["files"]
    if not isinstance(schema_hash, str) or _SHA256.fullmatch(schema_hash) is None:
        raise PipelineError("Generated manifest has an invalid schema hash")
    if not isinstance(generator, dict) or set(generator) != {"image", "version", "digest"}:
        raise PipelineError("Generated manifest has invalid generator metadata")
    Toolchain(generator["image"], generator["version"], generator["digest"])

    def valid_file_entry(relative: Any, digest: Any) -> bool:
        if not isinstance(relative, str) or not isinstance(digest, str):
            return False
        candidate = Path(relative)
        return (
            not candidate.is_absolute()
            and "\\" not in relative
            and len(candidate.parts) >= 2
            and candidate.parts[0] == "iikocloud_client"
            and all(part not in {"", ".", ".."} for part in candidate.parts)
            and candidate.as_posix() == relative
            and _SHA256.fullmatch(digest) is not None
        )

    if not isinstance(files, dict) or not all(
        valid_file_entry(relative, digest) for relative, digest in files.items()
    ):
        raise PipelineError("Generated manifest has invalid file hashes")
    if list(files) != sorted(files):
        raise PipelineError("Generated manifest file hashes are not sorted")
    if raw != canonical_json_bytes(value):
        raise PipelineError("Generated manifest must use canonical JSON encoding")
    return value
