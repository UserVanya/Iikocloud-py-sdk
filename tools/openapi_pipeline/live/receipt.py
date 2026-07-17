from __future__ import annotations

import json
import re
import stat
from contextlib import suppress
from dataclasses import asdict, dataclass, replace
from pathlib import Path
from typing import Any

from ..errors import PipelineError, SafetyError
from ..io import canonical_json_bytes, sha256_bytes, write_json_atomic
from .lock import ensure_private_directory, validate_private_regular_file

_SHA256 = re.compile(r"[a-f0-9]{64}\Z")
_RUN_ID = re.compile(r"[0-9]{8}T[0-9]{6}Z-[a-f0-9]{8,32}\Z")
_OPERATION_ID = re.compile(r"[A-Za-z0-9][A-Za-z0-9_.:-]{0,127}\Z")
_FIELDS = {
    "run_id",
    "profile_fingerprint",
    "effective_schema_sha256",
    "generated_tree_sha256",
    "operations",
    "had_429",
    "completed",
}
_MAX_RECEIPT_BYTES = 1024 * 1024
_REQUIRED_READ_CANARY = ("authenticate", "get_organizations")


@dataclass(frozen=True)
class LiveArtifactHashes:
    effective_schema_sha256: str
    generated_tree_sha256: str


def _unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("duplicate JSON key")
        result[key] = value
    return result


def _reject_constant(value: str) -> None:
    raise ValueError(f"non-finite JSON number {value}")


@dataclass(frozen=True)
class LiveReceipt:
    run_id: str
    profile_fingerprint: str
    effective_schema_sha256: str
    generated_tree_sha256: str
    operations: tuple[str, ...]
    had_429: bool
    completed: bool

    def __post_init__(self) -> None:
        if not isinstance(self.run_id, str) or _RUN_ID.fullmatch(self.run_id) is None:
            raise SafetyError("Live receipt run_id is invalid")
        for label, digest in (
            ("profile fingerprint", self.profile_fingerprint),
            ("effective schema hash", self.effective_schema_sha256),
            ("generated tree hash", self.generated_tree_sha256),
        ):
            if not isinstance(digest, str) or _SHA256.fullmatch(digest) is None:
                raise SafetyError(f"Live receipt {label} is invalid")
        if not isinstance(self.operations, tuple) or any(
            not isinstance(item, str) or _OPERATION_ID.fullmatch(item) is None
            for item in self.operations
        ):
            raise SafetyError("Live receipt operations are invalid")
        if len(set(self.operations)) != len(self.operations):
            raise SafetyError("Live receipt operations must not contain duplicates")
        if self.operations and self.operations[0] != "authenticate":
            raise SafetyError("Live receipt operations must start with authenticate")
        if type(self.had_429) is not bool or type(self.completed) is not bool:
            raise SafetyError("Live receipt flags must be booleans")
        if self.completed and not self.has_required_read_canary:
            raise SafetyError(
                "A completed live receipt requires authenticate and get_organizations"
            )

    @property
    def has_required_read_canary(self) -> bool:
        return all(operation_id in self.operations for operation_id in _REQUIRED_READ_CANARY)

    def to_json(self) -> dict[str, Any]:
        value = asdict(self)
        value["operations"] = list(self.operations)
        return value

    def write(self, path: Path) -> None:
        ensure_private_directory(path.parent)
        with suppress(FileNotFoundError):
            validate_private_regular_file(path, label="Live receipt")
        write_json_atomic(path, self.to_json(), mode=0o600)
        validate_private_regular_file(path, label="Live receipt")

    @classmethod
    def load(cls, path: Path) -> LiveReceipt:
        try:
            validate_private_regular_file(path, label="Live receipt")
            body = path.read_bytes()
        except (FileNotFoundError, OSError) as error:
            raise SafetyError(f"Cannot read live receipt: {path}") from error
        if len(body) > _MAX_RECEIPT_BYTES:
            raise SafetyError("Live receipt is too large")
        try:
            value = json.loads(
                body.decode("utf-8"),
                object_pairs_hook=_unique_object,
                parse_constant=_reject_constant,
            )
        except (UnicodeError, ValueError) as error:
            raise SafetyError("Live receipt is not valid strict JSON") from error
        if not isinstance(value, dict) or set(value) != _FIELDS:
            raise SafetyError("Live receipt fields are invalid")
        if body != canonical_json_bytes(value):
            raise SafetyError("Live receipt must use canonical JSON encoding")
        operations = value["operations"]
        if not isinstance(operations, list):
            raise SafetyError("Live receipt operations must be an array")
        return cls(
            run_id=value["run_id"],
            profile_fingerprint=value["profile_fingerprint"],
            effective_schema_sha256=value["effective_schema_sha256"],
            generated_tree_sha256=value["generated_tree_sha256"],
            operations=tuple(operations),
            had_429=value["had_429"],
            completed=value["completed"],
        )

    def with_operation(self, operation_id: str) -> LiveReceipt:
        if self.completed:
            raise SafetyError("Cannot change a completed live receipt")
        if operation_id in self.operations:
            raise SafetyError(f"Live receipt already contains operation {operation_id!r}")
        return replace(self, operations=(*self.operations, operation_id))

    def with_429(self) -> LiveReceipt:
        return replace(self, had_429=True, completed=False)

    def as_completed(self) -> LiveReceipt:
        if self.had_429:
            raise SafetyError("A live receipt with 429 cannot be completed")
        if not self.has_required_read_canary:
            raise SafetyError(
                "A live receipt requires get_organizations before it can be completed"
            )
        return replace(self, completed=True)

    def matches(
        self,
        profile_fingerprint: str,
        effective_schema_sha256: str,
        generated_tree_sha256: str,
    ) -> bool:
        return (
            self.completed
            and not self.had_429
            and self.has_required_read_canary
            and self.profile_fingerprint == profile_fingerprint
            and self.effective_schema_sha256 == effective_schema_sha256
            and self.generated_tree_sha256 == generated_tree_sha256
        )


def _regular_bytes(path: Path, *, label: str, maximum: int = 256 * 1024 * 1024) -> bytes:
    try:
        metadata = path.lstat()
    except FileNotFoundError as error:
        raise SafetyError(f"{label} is missing: {path}") from error
    if stat.S_ISLNK(metadata.st_mode) or not stat.S_ISREG(metadata.st_mode):
        raise SafetyError(f"{label} must be a regular non-symlink file: {path}")
    try:
        body = path.read_bytes()
    except OSError as error:
        raise SafetyError(f"Cannot read {label.lower()}: {path}") from error
    if len(body) > maximum:
        raise SafetyError(f"{label} is too large: {path}")
    return body


def verify_live_artifacts(root: Path) -> LiveArtifactHashes:
    """Rebuild the effective document offline and bind it to the committed tree."""
    from .. import pipeline as pipeline_module
    from ..paths import RepoPaths
    from ..promotion import load_generated_manifest
    from ..validate import ensure_valid_effective_schema

    paths = RepoPaths(root.resolve(strict=True))
    try:
        upstream = pipeline_module._load_document(
            paths.upstream,
            label="committed upstream snapshot for live tests",
        )
        effective, _mappings = pipeline_module._apply_committed_corrections(paths, upstream)
        ensure_valid_effective_schema(effective)
        expected_effective = canonical_json_bytes(effective)
        actual_effective = _regular_bytes(
            paths.effective,
            label="Effective OpenAPI artifact",
        )
        if actual_effective != expected_effective:
            raise SafetyError(
                "Effective OpenAPI artifact is missing, stale, or noncanonical; run offline verify"
            )
        effective_hash = sha256_bytes(expected_effective)

        manifest_path = root / "generator/generated-manifest.json"
        _regular_bytes(manifest_path, label="Generated manifest")
        manifest = load_generated_manifest(manifest_path)
        if manifest["effective_schema_sha256"] != effective_hash:
            raise SafetyError("Generated manifest is stale for the effective OpenAPI artifact")
        manual_paths = pipeline_module._manual_paths(root / "generator/manual-files.txt")
        pipeline_module._verify_committed_tree(paths, manifest, manual_paths)
        published_files = dict(manifest["files"])
        for relative in manual_paths:
            published_files[relative.as_posix()] = sha256_bytes(
                _regular_bytes(
                    paths.root / "src" / relative,
                    label=f"Manual generated-tree file {relative.as_posix()}",
                )
            )
        published_files = dict(sorted(published_files.items()))
    except SafetyError:
        raise
    except PipelineError as error:
        raise SafetyError("Live artifact verification failed; run offline verify") from error
    return LiveArtifactHashes(
        effective_schema_sha256=effective_hash,
        generated_tree_sha256=sha256_bytes(canonical_json_bytes(published_files)),
    )
