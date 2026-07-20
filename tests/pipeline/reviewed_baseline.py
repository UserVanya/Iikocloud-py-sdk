from __future__ import annotations

from pathlib import Path
from typing import Any
from unittest.mock import patch

import tools.openapi_pipeline.pipeline as pipeline_module
from tools.openapi_pipeline.paths import RepoPaths
from tools.openapi_pipeline.pipeline import (
    compose_reviewed_bootstrap_candidate,
    compose_reviewed_evidence_base_candidate,
)

_BOOTSTRAP_CANDIDATE_PATHS = (
    Path("build/upstream/candidate.json"),
    Path("build/bootstrap/types.overlay.yaml"),
    Path("build/bootstrap/operation-ids.yaml"),
    Path("build/bootstrap/model-collisions.yaml"),
)
_COMMITTED_BASELINE_PATHS = (
    Path("openapi/upstream/iikocloud.openapi.json"),
    Path("openapi/overlays/contracts.overlay.yaml"),
    Path("openapi/overlays/types.overlay.yaml"),
    Path("openapi/operation-ids.yaml"),
    Path("openapi/model-name-overrides.yaml"),
)
_EVIDENCE_OWNED_OVERLAYS = frozenset({"operations.overlay.yaml", "polymorphism.overlay.yaml"})


def has_complete_bootstrap_candidate(paths: RepoPaths) -> bool:
    return all((paths.root / relative).is_file() for relative in _BOOTSTRAP_CANDIDATE_PATHS)


def has_complete_committed_baseline(paths: RepoPaths) -> bool:
    return all((paths.root / relative).is_file() for relative in _COMMITTED_BASELINE_PATHS)


def has_current_reviewed_source(paths: RepoPaths) -> bool:
    return has_complete_bootstrap_candidate(paths) or has_complete_committed_baseline(paths)


def current_reviewed_source_path(paths: RepoPaths) -> Path:
    if has_complete_bootstrap_candidate(paths):
        return paths.candidate
    if has_complete_committed_baseline(paths):
        return paths.upstream
    raise AssertionError("No complete reviewed OpenAPI source is available")


def compose_current_reviewed_source(
    paths: RepoPaths,
) -> tuple[dict[str, Any], dict[str, str]]:
    if has_complete_bootstrap_candidate(paths):
        return compose_reviewed_bootstrap_candidate(paths)
    if not has_complete_committed_baseline(paths):
        raise AssertionError("No complete reviewed OpenAPI source is available")
    document = pipeline_module._load_document(  # noqa: SLF001 - repository contract helper
        paths.upstream,
        label="committed upstream snapshot",
    )
    return pipeline_module._apply_committed_corrections(  # noqa: SLF001
        paths,
        document,
    )


def compose_current_evidence_base(
    paths: RepoPaths,
) -> tuple[dict[str, Any], dict[str, str]]:
    if has_complete_bootstrap_candidate(paths):
        return compose_reviewed_evidence_base_candidate(paths)
    if not has_complete_committed_baseline(paths):
        raise AssertionError("No complete reviewed OpenAPI source is available")

    document = pipeline_module._load_document(  # noqa: SLF001 - repository contract helper
        paths.upstream,
        label="committed upstream snapshot",
    )
    semantic_overlays = pipeline_module._semantic_overlays(  # noqa: SLF001
        paths.root,
        exclude_types=True,
    )
    evidence_base_overlays = [
        overlay for overlay in semantic_overlays if overlay.name not in _EVIDENCE_OWNED_OVERLAYS
    ]
    with patch.object(
        pipeline_module,
        "_semantic_overlays",
        return_value=evidence_base_overlays,
    ):
        return pipeline_module._apply_committed_corrections(  # noqa: SLF001
            paths,
            document,
        )
