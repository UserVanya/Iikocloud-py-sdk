from __future__ import annotations

import dataclasses
from collections.abc import Callable, Iterator, Mapping
from types import MappingProxyType
from typing import Any, cast, get_type_hints

import pytest
from test_evidence_analysis import _pairs, _plain
from test_evidence_candidates import _retained_items, _reviewed_schema

import tools.openapi_pipeline.evidence_candidate_store as store_module
from tools.openapi_pipeline.errors import SafetyError
from tools.openapi_pipeline.evidence_analysis import (
    EvidenceProvenance,
    analyze_menu_evidence,
)
from tools.openapi_pipeline.evidence_candidate_store import (
    EvidenceCandidateManifestResult,
    build_evidence_candidate_manifest,
)
from tools.openapi_pipeline.evidence_candidates import (
    EVIDENCE_CANDIDATE_PAYLOAD_PATHS,
    EvidenceCandidateBundle,
    build_evidence_candidate_bundle,
)
from tools.openapi_pipeline.io import canonical_json_bytes, sha256_bytes

SENSITIVE_MARKER = "private-capture-raw-value"


class _CallbackMapping(Mapping[Any, Any]):
    def __init__(self, values: Mapping[Any, Any], callback: Callable[[], None]) -> None:
        self._values = values
        self._callback = callback
        self._fired = False

    def __iter__(self) -> Iterator[Any]:
        if not self._fired:
            self._fired = True
            self._callback()
        return iter(self._values)

    def __getitem__(self, key: Any) -> Any:
        return self._values[key]

    def __len__(self) -> int:
        return len(self._values)


def _bundle() -> EvidenceCandidateBundle:
    schema = _reviewed_schema()
    pairs = _pairs(schema, _retained_items(), order=(4, 2, 3))
    return build_evidence_candidate_bundle(
        analysis=analyze_menu_evidence(pairs, schema),
        pairs=pairs,
        effective_schema=schema,
    )


def _expected_manifest(bundle: EvidenceCandidateBundle) -> dict[str, Any]:
    return {
        "schema_version": 1,
        "tool": {"name": "iikocloud-evidence-candidates", "version": 1},
        "operation_id": "get_external_menu_by_id",
        "effective_schema_sha256": bundle.effective_schema_sha256,
        "evidence_analysis_sha256": bundle.evidence_analysis_sha256,
        "evidence_provenance": {
            str(version): {
                "request_sha256": bundle.evidence_provenance[version].request_sha256,
                "response_sha256": bundle.evidence_provenance[version].response_sha256,
            }
            for version in (2, 3, 4)
        },
        "files": {
            path: sha256_bytes(bundle.canonical_bytes[path])
            for path in EVIDENCE_CANDIDATE_PAYLOAD_PATHS
        },
    }


def _replace_mapping(
    original: Mapping[Any, Any],
    update: Callable[[dict[Any, Any]], None],
) -> Mapping[Any, Any]:
    changed = dict(original)
    update(changed)
    return MappingProxyType(changed)


def _assert_sanitized(error: SafetyError) -> None:
    assert SENSITIVE_MARKER not in str(error)
    assert SENSITIVE_MARKER not in repr(error)
    assert error.__cause__ is None
    assert error.__context__ is None


def test_manifest_has_exact_canonical_shape_bytes_and_hash() -> None:
    bundle = _bundle()

    result = build_evidence_candidate_manifest(bundle)
    expected = _expected_manifest(bundle)

    assert isinstance(result, EvidenceCandidateManifestResult)
    assert result.manifest == expected
    assert result.canonical_json_bytes == canonical_json_bytes(expected)
    assert result.sha256 == sha256_bytes(result.canonical_json_bytes)
    assert set(result.manifest) == {
        "schema_version",
        "tool",
        "operation_id",
        "effective_schema_sha256",
        "evidence_analysis_sha256",
        "evidence_provenance",
        "files",
    }
    assert set(result.manifest["tool"]) == {"name", "version"}
    assert tuple(result.manifest["evidence_provenance"]) == ("2", "3", "4")
    assert tuple(result.manifest["files"]) == EVIDENCE_CANDIDATE_PAYLOAD_PATHS
    assert "sha256" not in result.manifest


def test_manifest_builder_runtime_type_hints_resolve_exact_bundle() -> None:
    hints = get_type_hints(build_evidence_candidate_manifest)

    assert hints["bundle"] is EvidenceCandidateBundle
    assert hints["return"] is EvidenceCandidateManifestResult


def test_manifest_result_is_deeply_immutable() -> None:
    result = build_evidence_candidate_manifest(_bundle())
    tool = result.manifest["tool"]
    files = result.manifest["files"]
    assert isinstance(tool, Mapping)
    assert isinstance(files, Mapping)

    with pytest.raises(TypeError):
        result.manifest["schema_version"] = 2  # type: ignore[index]
    with pytest.raises(TypeError):
        tool["version"] = 2  # type: ignore[index]
    with pytest.raises(TypeError):
        files[EVIDENCE_CANDIDATE_PAYLOAD_PATHS[0]] = "0" * 64  # type: ignore[index]
    with pytest.raises(dataclasses.FrozenInstanceError):
        result.sha256 = "0" * 64  # type: ignore[misc]


def test_manifest_is_deterministic_across_all_bundle_mapping_orders() -> None:
    bundle = _bundle()
    reordered = dataclasses.replace(
        bundle,
        evidence_provenance=MappingProxyType(
            dict(reversed(tuple(bundle.evidence_provenance.items())))
        ),
        canonical_bytes=MappingProxyType(dict(reversed(tuple(bundle.canonical_bytes.items())))),
        sha256=MappingProxyType(dict(reversed(tuple(bundle.sha256.items())))),
    )

    first = build_evidence_candidate_manifest(bundle)
    second = build_evidence_candidate_manifest(reordered)

    assert first.manifest == second.manifest
    assert first.canonical_json_bytes == second.canonical_json_bytes
    assert first.sha256 == second.sha256


@pytest.mark.parametrize(
    "forge",
    [
        lambda bundle: dataclasses.replace(bundle, operation_id=SENSITIVE_MARKER),
        lambda bundle: dataclasses.replace(bundle, effective_schema_sha256="0" * 64),
        lambda bundle: dataclasses.replace(bundle, evidence_analysis_sha256="1" * 64),
        lambda bundle: dataclasses.replace(bundle, manifest_sha256="2" * 64),
    ],
    ids=["operation", "schema-hash", "analysis-hash", "manifest-checksum"],
)
def test_manifest_rejects_forged_bundle_metadata_without_echoing_it(
    forge: Callable[[EvidenceCandidateBundle], EvidenceCandidateBundle],
) -> None:
    with pytest.raises(SafetyError) as caught:
        build_evidence_candidate_manifest(forge(_bundle()))

    _assert_sanitized(caught.value)


def test_manifest_rejects_forged_body_even_with_matching_payload_hash() -> None:
    bundle = _bundle()
    path = EVIDENCE_CANDIDATE_PAYLOAD_PATHS[0]
    forged_body = bundle.canonical_bytes[path] + SENSITIVE_MARKER.encode()
    forged = dataclasses.replace(
        bundle,
        canonical_bytes=_replace_mapping(
            bundle.canonical_bytes,
            lambda values: values.__setitem__(path, forged_body),
        ),
        sha256=_replace_mapping(
            bundle.sha256,
            lambda values: values.__setitem__(path, sha256_bytes(forged_body)),
        ),
    )

    with pytest.raises(SafetyError) as caught:
        build_evidence_candidate_manifest(forged)

    _assert_sanitized(caught.value)


def test_manifest_rejects_self_consistent_secret_bearing_fixture() -> None:
    bundle = _bundle()
    fixture_path = "tests/fixtures/contracts/external-menu-v2.json"
    forged_fixture = MappingProxyType({**dict(bundle.fixtures[2]), "api_key": SENSITIVE_MARKER})
    forged_fixtures = MappingProxyType({**dict(bundle.fixtures), 2: forged_fixture})
    forged_body = canonical_json_bytes(_plain(forged_fixture))
    forged_bodies = _replace_mapping(
        bundle.canonical_bytes,
        lambda values: values.__setitem__(fixture_path, forged_body),
    )
    forged_hashes = _replace_mapping(
        bundle.sha256,
        lambda values: values.__setitem__(fixture_path, sha256_bytes(forged_body)),
    )
    preliminary = dataclasses.replace(
        bundle,
        fixtures=forged_fixtures,
        canonical_bytes=forged_bodies,
        sha256=forged_hashes,
    )
    forged = dataclasses.replace(
        preliminary,
        manifest_sha256=sha256_bytes(canonical_json_bytes(_expected_manifest(preliminary))),
    )

    with pytest.raises(SafetyError) as caught:
        build_evidence_candidate_manifest(forged)

    _assert_sanitized(caught.value)


def test_manifest_checksum_is_consistency_only_not_accept_authorization() -> None:
    bundle = _bundle()
    fixture_path = "tests/fixtures/contracts/external-menu-v2.json"
    changed_fixture = MappingProxyType(
        {**dict(bundle.fixtures[2]), "syntheticNote": "synthetic-safe-value"}
    )
    changed_fixtures = MappingProxyType({**dict(bundle.fixtures), 2: changed_fixture})
    changed_body = canonical_json_bytes(_plain(changed_fixture))
    changed_bodies = _replace_mapping(
        bundle.canonical_bytes,
        lambda values: values.__setitem__(fixture_path, changed_body),
    )
    changed_hashes = _replace_mapping(
        bundle.sha256,
        lambda values: values.__setitem__(fixture_path, sha256_bytes(changed_body)),
    )
    preliminary = dataclasses.replace(
        bundle,
        fixtures=changed_fixtures,
        canonical_bytes=changed_bodies,
        sha256=changed_hashes,
    )
    changed_manifest = _expected_manifest(preliminary)
    changed = dataclasses.replace(
        preliminary,
        manifest_sha256=sha256_bytes(canonical_json_bytes(changed_manifest)),
    )

    result = build_evidence_candidate_manifest(changed)

    assert result.manifest == changed_manifest
    assert result.sha256 == changed.manifest_sha256
    assert result.sha256 != bundle.manifest_sha256
    bundle_doc = EvidenceCandidateBundle.__doc__
    builder_doc = build_evidence_candidate_manifest.__doc__
    assert bundle_doc is not None
    assert builder_doc is not None
    assert "unkeyed" in bundle_doc.casefold()
    assert "does not authorize acceptance" in builder_doc.casefold()


def test_manifest_rejects_recorded_hash_that_does_not_match_exact_body() -> None:
    bundle = _bundle()
    path = EVIDENCE_CANDIDATE_PAYLOAD_PATHS[0]
    forged = dataclasses.replace(
        bundle,
        sha256=_replace_mapping(
            bundle.sha256,
            lambda values: values.__setitem__(path, "0" * 64),
        ),
    )

    with pytest.raises(SafetyError, match="integrity"):
        build_evidence_candidate_manifest(forged)


def test_manifest_rejects_non_allowlisted_or_missing_payload_path() -> None:
    bundle = _bundle()
    removed = EVIDENCE_CANDIDATE_PAYLOAD_PATHS[0]

    def replace_path(values: dict[Any, Any]) -> None:
        body = values.pop(removed)
        values[f"../../{SENSITIVE_MARKER}"] = body

    forged = dataclasses.replace(
        bundle,
        canonical_bytes=_replace_mapping(bundle.canonical_bytes, replace_path),
    )

    with pytest.raises(SafetyError) as caught:
        build_evidence_candidate_manifest(forged)

    _assert_sanitized(caught.value)


@pytest.mark.parametrize("version", [1, 5, "2", True])
def test_manifest_rejects_forged_provenance_version(version: object) -> None:
    bundle = _bundle()

    def replace_version(values: dict[Any, Any]) -> None:
        provenance = values.pop(2)
        values[version] = provenance

    forged = dataclasses.replace(
        bundle,
        evidence_provenance=_replace_mapping(bundle.evidence_provenance, replace_version),
    )

    with pytest.raises(SafetyError, match="provenance"):
        build_evidence_candidate_manifest(forged)


def test_manifest_rejects_forged_provenance_digest() -> None:
    bundle = _bundle()
    original = bundle.evidence_provenance[2]
    changed = EvidenceProvenance("0" * 64, original.response_sha256)
    forged = dataclasses.replace(
        bundle,
        evidence_provenance=_replace_mapping(
            bundle.evidence_provenance,
            lambda values: values.__setitem__(2, changed),
        ),
    )

    with pytest.raises(SafetyError, match="checksum"):
        build_evidence_candidate_manifest(forged)


@pytest.mark.parametrize("field", ["canonical_bytes", "sha256", "evidence_provenance"])
def test_manifest_rejects_mutable_bundle_mappings(field: str) -> None:
    bundle = _bundle()
    replacement = cast(Any, {field: dict(getattr(bundle, field))})
    forged = dataclasses.replace(bundle, **replacement)

    with pytest.raises(SafetyError, match="immutable"):
        build_evidence_candidate_manifest(forged)


def test_manifest_rejects_non_builtin_payload_bytes_and_hashes() -> None:
    class BytesSubclass(bytes):
        pass

    class StringSubclass(str):
        pass

    bundle = _bundle()
    path = EVIDENCE_CANDIDATE_PAYLOAD_PATHS[0]
    forged_body = dataclasses.replace(
        bundle,
        canonical_bytes=_replace_mapping(
            bundle.canonical_bytes,
            lambda values: values.__setitem__(path, BytesSubclass(values[path])),
        ),
    )
    forged_hash = dataclasses.replace(
        bundle,
        sha256=_replace_mapping(
            bundle.sha256,
            lambda values: values.__setitem__(path, StringSubclass(values[path])),
        ),
    )

    with pytest.raises(SafetyError):
        build_evidence_candidate_manifest(forged_body)
    with pytest.raises(SafetyError):
        build_evidence_candidate_manifest(forged_hash)


def test_manifest_contains_no_raw_capture_or_run_metadata() -> None:
    result = build_evidence_candidate_manifest(_bundle())
    body = result.canonical_json_bytes.lower()
    files = result.manifest["files"]
    assert isinstance(files, Mapping)

    for forbidden in (
        b"<redacted:",
        b"private/",
        b"capture",
        b"run_id",
        b"runid",
        b"profile",
        b"timestamp",
        b"duration",
        SENSITIVE_MARKER.encode(),
    ):
        assert forbidden not in body
    assert not any(path.startswith("/") or ".." in path for path in files)


@pytest.mark.parametrize("boundary", ["canonical-json", "sha256"])
def test_manifest_does_not_mask_trusted_internal_errors(
    boundary: str,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    sentinel = RuntimeError(f"trusted-{boundary}-failure")

    def fail(*args: Any, **kwargs: Any) -> Any:
        raise sentinel

    monkeypatch.setattr(
        store_module,
        "canonical_json_bytes" if boundary == "canonical-json" else "sha256_bytes",
        fail,
    )

    with pytest.raises(RuntimeError) as caught:
        build_evidence_candidate_manifest(_bundle())

    assert caught.value is sentinel


def test_manifest_sanitizes_untrusted_mapping_traversal_failure() -> None:
    class RaisingMapping(Mapping[str, bytes]):
        def __iter__(self) -> Iterator[str]:
            raise RuntimeError(SENSITIVE_MARKER)

        def __getitem__(self, key: str) -> bytes:
            raise RuntimeError(SENSITIVE_MARKER)

        def __len__(self) -> int:
            raise RuntimeError(SENSITIVE_MARKER)

    bundle = _bundle()
    forged = dataclasses.replace(
        bundle,
        canonical_bytes=MappingProxyType(RaisingMapping()),
    )

    with pytest.raises(SafetyError) as caught:
        build_evidence_candidate_manifest(forged)

    _assert_sanitized(caught.value)


@pytest.mark.parametrize("callback", ["iteration", "lookup"])
def test_manifest_sanitizes_caller_safety_error_from_mapping_callback(
    callback: str,
) -> None:
    sentinel = SafetyError(SENSITIVE_MARKER)

    class RaisingMapping(Mapping[str, bytes]):
        def __iter__(self) -> Iterator[str]:
            if callback == "iteration":
                raise sentinel
            return iter(EVIDENCE_CANDIDATE_PAYLOAD_PATHS)

        def __getitem__(self, key: str) -> bytes:
            raise sentinel

        def __len__(self) -> int:
            return len(EVIDENCE_CANDIDATE_PAYLOAD_PATHS)

    bundle = _bundle()
    forged = dataclasses.replace(
        bundle,
        canonical_bytes=MappingProxyType(RaisingMapping()),
    )

    with pytest.raises(SafetyError) as caught:
        build_evidence_candidate_manifest(forged)

    assert caught.value is not sentinel
    _assert_sanitized(caught.value)


def test_manifest_preserves_memory_error_from_mapping_callback() -> None:
    sentinel = MemoryError(SENSITIVE_MARKER)

    class RaisingMapping(Mapping[str, bytes]):
        def __iter__(self) -> Iterator[str]:
            raise sentinel

        def __getitem__(self, key: str) -> bytes:
            raise sentinel

        def __len__(self) -> int:
            raise sentinel

    bundle = _bundle()
    forged = dataclasses.replace(
        bundle,
        canonical_bytes=MappingProxyType(RaisingMapping()),
    )

    with pytest.raises(MemoryError) as caught:
        build_evidence_candidate_manifest(forged)

    assert caught.value is sentinel


@pytest.mark.parametrize(
    "callback_field",
    ["canonical_bytes", "evidence_provenance"],
)
def test_manifest_snapshots_bundle_fields_before_mapping_callbacks(
    callback_field: str,
) -> None:
    original = _bundle()
    forged_manifest = _expected_manifest(original)
    forged_manifest["operation_id"] = SENSITIVE_MARKER
    holder: dict[str, EvidenceCandidateBundle] = {}

    def mutate_bundle() -> None:
        object.__setattr__(holder["bundle"], "operation_id", SENSITIVE_MARKER)

    callback_value = MappingProxyType(
        _CallbackMapping(getattr(original, callback_field), mutate_bundle)
    )
    forged = dataclasses.replace(
        original,
        manifest_sha256=sha256_bytes(canonical_json_bytes(forged_manifest)),
        **cast(Any, {callback_field: callback_value}),
    )
    holder["bundle"] = forged

    try:
        result = build_evidence_candidate_manifest(forged)
    except SafetyError as error:
        _assert_sanitized(error)
    else:
        assert result.manifest["operation_id"] == "get_external_menu_by_id"
        assert SENSITIVE_MARKER.encode() not in result.canonical_json_bytes


def test_manifest_uses_all_original_top_level_references_after_callback() -> None:
    original = _bundle()
    expected = build_evidence_candidate_manifest(original)
    holder: dict[str, EvidenceCandidateBundle] = {}

    def mutate_all_top_level_fields() -> None:
        target = holder["bundle"]
        for field in dataclasses.fields(target):
            if field.name != "canonical_bytes":
                object.__setattr__(target, field.name, SENSITIVE_MARKER)
        object.__setattr__(target, "canonical_bytes", MappingProxyType({}))

    forged = dataclasses.replace(
        original,
        canonical_bytes=MappingProxyType(
            _CallbackMapping(original.canonical_bytes, mutate_all_top_level_fields)
        ),
    )
    holder["bundle"] = forged

    result = build_evidence_candidate_manifest(forged)

    assert result == expected
    assert SENSITIVE_MARKER.encode() not in result.canonical_json_bytes


def test_manifest_fails_closed_when_callback_mutates_other_backing_map() -> None:
    original = _bundle()
    path = EVIDENCE_CANDIDATE_PAYLOAD_PATHS[0]
    hash_backing = dict(original.sha256)

    def mutate_hash_backing() -> None:
        hash_backing[path] = SENSITIVE_MARKER

    forged = dataclasses.replace(
        original,
        canonical_bytes=MappingProxyType(
            _CallbackMapping(original.canonical_bytes, mutate_hash_backing)
        ),
        sha256=MappingProxyType(hash_backing),
    )

    with pytest.raises(SafetyError) as caught:
        build_evidence_candidate_manifest(forged)

    _assert_sanitized(caught.value)


def test_manifest_preserves_trusted_internal_safety_error_identity(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    sentinel = SafetyError("trusted internal validation failed")

    def fail(*args: Any, **kwargs: Any) -> Any:
        raise sentinel

    monkeypatch.setattr(store_module, "_require_sha256", fail)

    with pytest.raises(SafetyError) as caught:
        build_evidence_candidate_manifest(_bundle())

    assert caught.value is sentinel


@pytest.mark.parametrize("exception_type", [KeyboardInterrupt, SystemExit])
def test_manifest_does_not_swallow_caller_base_exceptions(
    exception_type: type[BaseException],
) -> None:
    class RaisingMapping(Mapping[str, bytes]):
        def __iter__(self) -> Iterator[str]:
            raise exception_type(SENSITIVE_MARKER)

        def __getitem__(self, key: str) -> bytes:
            raise exception_type(SENSITIVE_MARKER)

        def __len__(self) -> int:
            raise exception_type(SENSITIVE_MARKER)

    bundle = _bundle()
    forged = dataclasses.replace(
        bundle,
        canonical_bytes=MappingProxyType(RaisingMapping()),
    )

    with pytest.raises(exception_type):
        build_evidence_candidate_manifest(forged)
