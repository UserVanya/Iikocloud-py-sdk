from __future__ import annotations

import re
from collections.abc import Mapping
from typing import Any

import yaml

from .capture import EMAIL_KEYS, PHONE_KEYS, SECRET_KEYS
from .errors import SafetyError
from .evidence_analysis import EvidenceProvenance
from .io import canonical_json_bytes

EVIDENCE_OPERATION_ID = "get_external_menu_by_id"
OPERATIONS_OVERLAY_PATH = "openapi/overlays/operations.overlay.yaml"
POLYMORPHISM_OVERLAY_PATH = "openapi/overlays/polymorphism.overlay.yaml"
EVIDENCE_VERSIONS = (2, 3, 4)
EVIDENCE_FIXTURE_PATHS = {
    version: f"tests/fixtures/contracts/external-menu-v{version}.json"
    for version in EVIDENCE_VERSIONS
}
EVIDENCE_CANDIDATE_PAYLOAD_PATHS = (
    OPERATIONS_OVERLAY_PATH,
    POLYMORPHISM_OVERLAY_PATH,
    *(EVIDENCE_FIXTURE_PATHS[version] for version in EVIDENCE_VERSIONS),
)
MANIFEST_SCHEMA_VERSION = 1
MANIFEST_TOOL_NAME = "iikocloud-evidence-candidates"
MANIFEST_TOOL_VERSION = 1

_REDACTION = re.compile(r"<redacted:[^>]*>", re.IGNORECASE)
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


def evidence_candidate_manifest_document(
    *,
    operation_id: str,
    effective_schema_sha256: str,
    evidence_analysis_sha256: str,
    provenance: Mapping[int, EvidenceProvenance],
    files: Mapping[str, str],
) -> dict[str, Any]:
    """Build the exact manifest value without adding a self-hash."""

    return {
        "schema_version": MANIFEST_SCHEMA_VERSION,
        "tool": {"name": MANIFEST_TOOL_NAME, "version": MANIFEST_TOOL_VERSION},
        "operation_id": operation_id,
        "effective_schema_sha256": effective_schema_sha256,
        "evidence_analysis_sha256": evidence_analysis_sha256,
        "evidence_provenance": {
            str(version): {
                "request_sha256": provenance[version].request_sha256,
                "response_sha256": provenance[version].response_sha256,
            }
            for version in EVIDENCE_VERSIONS
        },
        "files": {path: files[path] for path in EVIDENCE_CANDIDATE_PAYLOAD_PATHS},
    }


def canonical_evidence_candidate_payloads(
    *,
    operations_overlay: dict[str, Any],
    polymorphism_overlay: dict[str, Any],
    fixtures: Mapping[int, dict[str, Any]],
) -> dict[str, bytes]:
    """Validate and serialize the exact five public synthetic candidate payloads."""

    if (
        type(operations_overlay) is not dict
        or type(polymorphism_overlay) is not dict
        or not isinstance(fixtures, Mapping)
        or len(fixtures) != len(EVIDENCE_VERSIONS)
        or any(type(version) is not int for version in fixtures)
        or set(fixtures) != set(EVIDENCE_VERSIONS)
        or any(type(fixtures[version]) is not dict for version in EVIDENCE_VERSIONS)
    ):
        raise SafetyError("Evidence candidate semantic payload scope is invalid")
    semantic_values = (
        operations_overlay,
        polymorphism_overlay,
        tuple(fixtures[version] for version in EVIDENCE_VERSIONS),
    )
    assert_evidence_candidate_values_safe(semantic_values)
    payloads = {
        OPERATIONS_OVERLAY_PATH: _canonical_overlay_bytes(operations_overlay),
        POLYMORPHISM_OVERLAY_PATH: _canonical_overlay_bytes(polymorphism_overlay),
        **{
            EVIDENCE_FIXTURE_PATHS[version]: canonical_json_bytes(fixtures[version])
            for version in EVIDENCE_VERSIONS
        },
    }
    assert_evidence_candidate_bytes_safe(payloads.values())
    return payloads


def assert_evidence_candidate_values_safe(values: Any) -> None:
    """Reject secret, PII and redaction markers in semantic candidates."""

    sensitive_keys = SECRET_KEYS | EMAIL_KEYS | PHONE_KEYS
    if any(key.casefold() in sensitive_keys for key in _all_mapping_keys(values)):
        raise SafetyError("Evidence candidate failed the secret/PII key scan")
    for value in _all_strings(values):
        without_uuids = _UUID_ANY.sub("", value)
        if (
            _REDACTION.search(value)
            or _JWT.search(value)
            or _BEARER.search(value)
            or _EMAIL.search(value)
            or _PHONE.search(without_uuids)
        ):
            raise SafetyError("Evidence candidate failed the secret/PII/redaction scan")


def assert_evidence_candidate_bytes_safe(bodies: Any) -> None:
    """Decode and rescan serialized candidate payloads before they leave memory."""

    for body in bodies:
        decode_failed = False
        try:
            text = body.decode("utf-8")
        except (AttributeError, UnicodeError):
            decode_failed = True
            text = ""
        if decode_failed:
            raise SafetyError("Evidence candidate bytes are not UTF-8") from None
        assert_evidence_candidate_values_safe(text)


def _canonical_overlay_bytes(value: dict[str, Any]) -> bytes:
    return yaml.safe_dump(
        value,
        allow_unicode=True,
        default_flow_style=False,
        sort_keys=True,
    ).encode("utf-8")


def _all_mapping_keys(value: Any) -> tuple[str, ...]:
    if type(value) is dict:
        return tuple(
            key
            for candidate, child in value.items()
            for key in (
                *((candidate,) if type(candidate) is str else ()),
                *_all_mapping_keys(child),
            )
        )
    if type(value) in {list, tuple}:
        return tuple(key for child in value for key in _all_mapping_keys(child))
    return ()


def _all_strings(value: Any) -> tuple[str, ...]:
    if type(value) is str:
        return (value,)
    if type(value) is dict:
        return tuple(
            text
            for key, child in value.items()
            for text in ((*((key,) if type(key) is str else ()), *_all_strings(child)))
        )
    if type(value) in {list, tuple}:
        return tuple(text for child in value for text in _all_strings(child))
    return ()
