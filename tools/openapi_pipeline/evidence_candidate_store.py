from __future__ import annotations

import math
import re
from collections.abc import Mapping
from dataclasses import dataclass
from types import MappingProxyType
from typing import TYPE_CHECKING, Any, cast

import yaml

from .errors import SafetyError
from .evidence_analysis import EvidenceProvenance
from .evidence_promotion import FrozenJson
from .io import canonical_json_bytes, sha256_bytes

if TYPE_CHECKING:
    from .evidence_candidates import EvidenceCandidateBundle

_MANIFEST_SCHEMA_VERSION = 1
_TOOL_NAME = "iikocloud-evidence-candidates"
_TOOL_VERSION = 1
_VERSIONS = (2, 3, 4)
_SHA256 = re.compile(r"[a-f0-9]{64}\Z")
_MAPPING_PROXY_TYPE: type[Any] = type(MappingProxyType({}))
_MAX_DEPTH = 128


@dataclass(frozen=True)
class EvidenceCandidateManifestResult:
    """A deeply immutable canonical manifest and its detached digest."""

    manifest: Mapping[str, FrozenJson]
    canonical_json_bytes: bytes
    sha256: str


def build_evidence_candidate_manifest(
    bundle: EvidenceCandidateBundle,
) -> EvidenceCandidateManifestResult:
    """Validate an in-memory candidate bundle and build its canonical manifest."""

    from .evidence_candidates import (
        EVIDENCE_CANDIDATE_PAYLOAD_PATHS,
        EVIDENCE_OPERATION_ID,
        OPERATIONS_OVERLAY_PATH,
        POLYMORPHISM_OVERLAY_PATH,
        EvidenceCandidateBundle,
    )

    if type(bundle) is not EvidenceCandidateBundle:
        raise SafetyError("Evidence candidate manifest requires an exact bundle")
    if type(bundle.operation_id) is not str or bundle.operation_id != EVIDENCE_OPERATION_ID:
        raise SafetyError("Evidence candidate manifest operation binding is invalid")
    effective_schema_sha256 = _require_sha256(
        bundle.effective_schema_sha256,
        "Evidence candidate manifest schema binding is invalid",
    )
    evidence_analysis_sha256 = _require_sha256(
        bundle.evidence_analysis_sha256,
        "Evidence candidate manifest analysis binding is invalid",
    )
    integrity_sha256 = _require_sha256(
        bundle.integrity_sha256,
        "Evidence candidate manifest integrity binding is invalid",
    )
    provenance = _validated_provenance(bundle.evidence_provenance)
    bodies, recomputed_hashes = _validated_payloads(
        bundle.canonical_bytes,
        bundle.sha256,
        EVIDENCE_CANDIDATE_PAYLOAD_PATHS,
    )
    expected_bodies = _canonical_semantic_payloads(
        bundle,
        operations_path=OPERATIONS_OVERLAY_PATH,
        polymorphism_path=POLYMORPHISM_OVERLAY_PATH,
        payload_paths=EVIDENCE_CANDIDATE_PAYLOAD_PATHS,
    )
    if any(bodies[path] != expected_bodies[path] for path in EVIDENCE_CANDIDATE_PAYLOAD_PATHS):
        raise SafetyError("Evidence candidate manifest payload body is inconsistent")

    manifest_value = _candidate_manifest_document(
        operation_id=bundle.operation_id,
        effective_schema_sha256=effective_schema_sha256,
        evidence_analysis_sha256=evidence_analysis_sha256,
        provenance=provenance,
        files=recomputed_hashes,
        payload_paths=EVIDENCE_CANDIDATE_PAYLOAD_PATHS,
    )
    body = canonical_json_bytes(manifest_value)
    digest = sha256_bytes(body)
    if digest != integrity_sha256:
        raise SafetyError("Evidence candidate manifest integrity binding is invalid")
    frozen = _freeze_json(manifest_value)
    if not isinstance(frozen, Mapping):
        raise SafetyError("Evidence candidate manifest root is invalid")
    return EvidenceCandidateManifestResult(
        manifest=frozen,
        canonical_json_bytes=body,
        sha256=digest,
    )


def _candidate_manifest_document(
    *,
    operation_id: str,
    effective_schema_sha256: str,
    evidence_analysis_sha256: str,
    provenance: Mapping[int, EvidenceProvenance],
    files: Mapping[str, str],
    payload_paths: tuple[str, ...],
) -> dict[str, Any]:
    return {
        "schema_version": _MANIFEST_SCHEMA_VERSION,
        "tool": {"name": _TOOL_NAME, "version": _TOOL_VERSION},
        "operation_id": operation_id,
        "effective_schema_sha256": effective_schema_sha256,
        "evidence_analysis_sha256": evidence_analysis_sha256,
        "evidence_provenance": {
            str(version): {
                "request_sha256": provenance[version].request_sha256,
                "response_sha256": provenance[version].response_sha256,
            }
            for version in _VERSIONS
        },
        "files": {path: files[path] for path in payload_paths},
    }


def _validated_provenance(value: object) -> dict[int, EvidenceProvenance]:
    entries = _immutable_mapping_entries(
        value,
        message="Evidence candidate manifest provenance must be immutable",
    )
    if (
        len(entries) != len(_VERSIONS)
        or any(type(version) is not int for version, _item in entries)
        or {version for version, _item in entries} != set(_VERSIONS)
    ):
        raise SafetyError("Evidence candidate manifest provenance versions are invalid")
    by_version = dict(entries)
    result: dict[int, EvidenceProvenance] = {}
    for version in _VERSIONS:
        item = by_version[version]
        if type(item) is not EvidenceProvenance:
            raise SafetyError("Evidence candidate manifest provenance is invalid")
        request_sha256 = _require_sha256(
            item.request_sha256,
            "Evidence candidate manifest provenance is invalid",
        )
        response_sha256 = _require_sha256(
            item.response_sha256,
            "Evidence candidate manifest provenance is invalid",
        )
        result[version] = EvidenceProvenance(request_sha256, response_sha256)
    return result


def _validated_payloads(
    body_value: object,
    hash_value: object,
    payload_paths: tuple[str, ...],
) -> tuple[dict[str, bytes], dict[str, str]]:
    body_entries = _immutable_mapping_entries(
        body_value,
        message="Evidence candidate manifest payload mapping must be immutable",
    )
    hash_entries = _immutable_mapping_entries(
        hash_value,
        message="Evidence candidate manifest hash mapping must be immutable",
    )
    _require_exact_paths(body_entries, payload_paths)
    _require_exact_paths(hash_entries, payload_paths)
    bodies = dict(body_entries)
    recorded_hashes = dict(hash_entries)
    recomputed_hashes: dict[str, str] = {}
    for path in payload_paths:
        body = bodies[path]
        if type(body) is not bytes or not body:
            raise SafetyError("Evidence candidate manifest payload body is invalid")
        recorded = _require_sha256(
            recorded_hashes[path],
            "Evidence candidate manifest payload hash is invalid",
        )
        recomputed = sha256_bytes(body)
        if recomputed != recorded:
            raise SafetyError("Evidence candidate manifest payload integrity is invalid")
        recomputed_hashes[path] = recomputed
    return bodies, recomputed_hashes


def _canonical_semantic_payloads(
    bundle: EvidenceCandidateBundle,
    *,
    operations_path: str,
    polymorphism_path: str,
    payload_paths: tuple[str, ...],
) -> dict[str, bytes]:
    operations = _materialize_immutable_json(
        bundle.operations_overlay,
        message="Evidence candidate manifest operations overlay is invalid",
    )
    polymorphism = _materialize_immutable_json(
        bundle.polymorphism_overlay,
        message="Evidence candidate manifest polymorphism overlay is invalid",
    )
    if type(operations) is not dict or type(polymorphism) is not dict:
        raise SafetyError("Evidence candidate manifest overlay root is invalid")
    fixture_entries = _immutable_mapping_entries(
        bundle.fixtures,
        message="Evidence candidate manifest fixtures must be immutable",
    )
    if (
        len(fixture_entries) != len(_VERSIONS)
        or any(type(version) is not int for version, _fixture in fixture_entries)
        or {version for version, _fixture in fixture_entries} != set(_VERSIONS)
    ):
        raise SafetyError("Evidence candidate manifest fixture versions are invalid")
    fixture_values = dict(fixture_entries)
    fixtures: dict[int, dict[str, Any]] = {}
    for version in _VERSIONS:
        fixture = _materialize_immutable_json(
            fixture_values[version],
            message="Evidence candidate manifest fixture is invalid",
        )
        if type(fixture) is not dict:
            raise SafetyError("Evidence candidate manifest fixture root is invalid")
        fixtures[version] = fixture

    expected = {
        operations_path: _canonical_yaml_bytes(operations),
        polymorphism_path: _canonical_yaml_bytes(polymorphism),
        **{
            f"tests/fixtures/contracts/external-menu-v{version}.json": canonical_json_bytes(
                fixtures[version]
            )
            for version in _VERSIONS
        },
    }
    if tuple(sorted(expected)) != tuple(sorted(payload_paths)):
        raise SafetyError("Evidence candidate manifest semantic payload scope is invalid")
    return expected


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
    except (SafetyError, MemoryError):
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
        except (SafetyError, MemoryError):
            raise
        except Exception:
            lookup_failed = True
            child = None
        if lookup_failed:
            raise SafetyError(message) from None
        entries.append((key, child))
    return tuple(entries)


def _require_exact_paths(
    entries: tuple[tuple[Any, Any], ...],
    payload_paths: tuple[str, ...],
) -> None:
    if (
        len(entries) != len(payload_paths)
        or any(type(path) is not str for path, _value in entries)
        or {path for path, _value in entries} != set(payload_paths)
    ):
        raise SafetyError("Evidence candidate manifest payload paths are invalid")


def _require_sha256(value: object, message: str) -> str:
    if type(value) is not str or _SHA256.fullmatch(value) is None:
        raise SafetyError(message)
    return value


def _materialize_immutable_json(
    value: object,
    *,
    message: str,
    depth: int = 0,
    active: set[int] | None = None,
) -> Any:
    if depth > _MAX_DEPTH:
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


def _canonical_yaml_bytes(value: Any) -> bytes:
    return yaml.safe_dump(
        value,
        allow_unicode=True,
        default_flow_style=False,
        sort_keys=True,
    ).encode("utf-8")


def _freeze_json(value: Any, *, depth: int = 0) -> FrozenJson:
    if depth > _MAX_DEPTH:
        raise SafetyError("Evidence candidate manifest JSON is too deep")
    if type(value) is dict:
        if any(type(key) is not str for key in value):
            raise SafetyError("Evidence candidate manifest JSON key is invalid")
        return MappingProxyType(
            {key: _freeze_json(child, depth=depth + 1) for key, child in value.items()}
        )
    if type(value) is list:
        return tuple(_freeze_json(child, depth=depth + 1) for child in value)
    if value is None or type(value) in {bool, int, str}:
        return value
    if type(value) is float and math.isfinite(value):
        return value
    raise SafetyError("Evidence candidate manifest JSON is invalid")
