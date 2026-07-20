from __future__ import annotations

from pathlib import Path
from typing import Any

import pytest

import tools.openapi_pipeline.evidence as evidence_module
import tools.openapi_pipeline.evidence_analysis as analysis_module
import tools.openapi_pipeline.evidence_candidate_store as store_module
import tools.openapi_pipeline.evidence_candidate_writer as writer_module
import tools.openapi_pipeline.evidence_candidates as candidates_module
import tools.openapi_pipeline.evidence_promotion as promotion_module
import tools.openapi_pipeline.pipeline as pipeline_module
from tools.openapi_pipeline.errors import SafetyError
from tools.openapi_pipeline.evidence_candidate_writer import EvidenceCandidateWriteResult
from tools.openapi_pipeline.paths import RepoPaths


def test_build_evidence_candidate_rejects_wrong_operation_before_collaborators(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    paths = RepoPaths(tmp_path)

    def forbidden(*_args: object, **_kwargs: object) -> object:
        raise AssertionError("invalid selection must not reach collaborators")

    monkeypatch.setattr(
        pipeline_module,
        "compose_reviewed_evidence_base_candidate",
        forbidden,
    )

    with pytest.raises(SafetyError, match="operation is not explicitly approved"):
        evidence_module.build_evidence_candidate(paths, operation="get_organizations")

    assert not paths.state.exists()


def test_build_evidence_candidate_requires_exact_repository_paths_before_collaborators(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    invalid_paths: Any = object()

    def forbidden(*_args: object, **_kwargs: object) -> object:
        raise AssertionError("invalid paths must not reach collaborators")

    monkeypatch.setattr(
        pipeline_module,
        "compose_reviewed_evidence_base_candidate",
        forbidden,
    )

    with pytest.raises(SafetyError, match="exact repository paths"):
        evidence_module.build_evidence_candidate(
            invalid_paths,
            operation="get_external_menu_by_id",
        )


def test_build_evidence_candidate_reads_under_live_lock_and_writes_after_release(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    paths = RepoPaths(tmp_path)
    schema: dict[str, Any] = {"openapi": "3.0.1"}
    pairs = object()
    analysis = object()
    bundle = object()
    manifest = object()
    result = EvidenceCandidateWriteResult(
        root=paths.build / "evidence-candidates",
        manifest_path=paths.build / "evidence-candidates/candidate-manifest.json",
        manifest_sha256="a" * 64,
        changed=True,
    )
    events: list[str] = []
    observed_lock: list[Any] = []

    class Reader:
        def __init__(
            self,
            repository_root: Path,
            effective_schema: dict[str, Any],
            operation: str,
            *,
            process_lock: Any,
        ) -> None:
            assert repository_root == paths.root
            assert effective_schema is schema
            assert operation == "get_external_menu_by_id"
            assert process_lock.held
            observed_lock.append(process_lock)
            events.append("reader-init")

        def read_menu_pairs(self) -> object:
            assert observed_lock[0].held
            events.append("read")
            return pairs

    def analyze(received_pairs: object, effective_schema: dict[str, Any]) -> object:
        assert received_pairs is pairs
        assert effective_schema is schema
        assert not observed_lock[0].held
        events.append("analyze")
        return analysis

    def build_bundle(**kwargs: object) -> object:
        assert kwargs == {
            "analysis": analysis,
            "pairs": pairs,
            "effective_schema": schema,
        }
        events.append("bundle")
        return bundle

    def build_manifest(received: object) -> object:
        assert received is bundle
        events.append("manifest")
        return manifest

    def write(received: object, received_paths: RepoPaths) -> EvidenceCandidateWriteResult:
        assert received is manifest
        assert received_paths is paths
        assert not observed_lock[0].held
        events.append("write")
        return result

    monkeypatch.setattr(
        pipeline_module,
        "compose_reviewed_evidence_base_candidate",
        lambda received: (schema, {}) if received is paths else forbidden(),
    )
    monkeypatch.setattr(promotion_module, "CaptureEvidenceReader", Reader)
    monkeypatch.setattr(analysis_module, "analyze_menu_evidence", analyze)
    monkeypatch.setattr(
        candidates_module,
        "build_evidence_candidate_bundle",
        build_bundle,
    )
    monkeypatch.setattr(
        store_module,
        "build_evidence_candidate_manifest",
        build_manifest,
    )
    monkeypatch.setattr(
        writer_module,
        "write_evidence_candidate_tree",
        write,
    )

    def forbidden() -> tuple[dict[str, Any], dict[str, str]]:
        raise AssertionError("unexpected repository paths")

    actual = evidence_module.build_evidence_candidate(
        paths,
        operation="get_external_menu_by_id",
    )

    assert actual is result
    assert events == ["reader-init", "read", "analyze", "bundle", "manifest", "write"]
    assert not observed_lock[0].held


def test_build_evidence_candidate_does_not_write_after_authority_failure(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    paths = RepoPaths(tmp_path)
    schema: dict[str, Any] = {"openapi": "3.0.1"}
    observed_lock: list[Any] = []

    class Reader:
        def __init__(self, *_args: object, process_lock: Any, **_kwargs: object) -> None:
            observed_lock.append(process_lock)

        def read_menu_pairs(self) -> object:
            assert observed_lock[0].held
            return object()

    monkeypatch.setattr(
        pipeline_module,
        "compose_reviewed_evidence_base_candidate",
        lambda _paths: (schema, {}),
    )
    monkeypatch.setattr(promotion_module, "CaptureEvidenceReader", Reader)
    monkeypatch.setattr(
        analysis_module,
        "analyze_menu_evidence",
        lambda *_args: (_ for _ in ()).throw(SafetyError("analysis rejected evidence")),
    )
    monkeypatch.setattr(
        writer_module,
        "write_evidence_candidate_tree",
        lambda *_args: (_ for _ in ()).throw(AssertionError("writer must not run")),
    )

    with pytest.raises(SafetyError, match="analysis rejected evidence"):
        evidence_module.build_evidence_candidate(
            paths,
            operation="get_external_menu_by_id",
        )

    assert not observed_lock[0].held
