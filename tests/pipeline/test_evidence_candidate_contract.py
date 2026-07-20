from __future__ import annotations

import ast
import inspect
import subprocess
import sys
from types import ModuleType

from test_evidence_analysis import _pairs, _plain
from test_evidence_candidates import _retained_items, _reviewed_schema

import tools.openapi_pipeline.evidence_candidate_store as store_module
import tools.openapi_pipeline.evidence_candidates as candidate_module
from tools.openapi_pipeline.evidence_analysis import analyze_menu_evidence
from tools.openapi_pipeline.evidence_candidate_contract import (
    EVIDENCE_CANDIDATE_PAYLOAD_PATHS,
    EVIDENCE_OPERATION_ID,
    MANIFEST_SCHEMA_VERSION,
    MANIFEST_TOOL_NAME,
    MANIFEST_TOOL_VERSION,
    canonical_evidence_candidate_payloads,
    evidence_candidate_manifest_document,
)
from tools.openapi_pipeline.evidence_candidates import (
    EvidenceCandidateBundle,
    build_evidence_candidate_bundle,
)
from tools.openapi_pipeline.io import canonical_json_bytes, sha256_bytes


def _bundle() -> EvidenceCandidateBundle:
    schema = _reviewed_schema()
    pairs = _pairs(schema, _retained_items(), order=(4, 2, 3))
    return build_evidence_candidate_bundle(
        analysis=analyze_menu_evidence(pairs, schema),
        pairs=pairs,
        effective_schema=schema,
    )


def _relative_imports(module: ModuleType) -> set[str]:
    tree = ast.parse(inspect.getsource(module))
    return {
        node.module
        for node in ast.walk(tree)
        if isinstance(node, ast.ImportFrom) and node.level == 1 and node.module is not None
    }


def test_contract_is_the_single_source_for_paths_manifest_and_payload_bytes() -> None:
    bundle = _bundle()
    payloads = canonical_evidence_candidate_payloads(
        operations_overlay=_plain(bundle.operations_overlay),
        polymorphism_overlay=_plain(bundle.polymorphism_overlay),
        fixtures={version: _plain(bundle.fixtures[version]) for version in (2, 3, 4)},
    )
    manifest = evidence_candidate_manifest_document(
        operation_id=bundle.operation_id,
        effective_schema_sha256=bundle.effective_schema_sha256,
        evidence_analysis_sha256=bundle.evidence_analysis_sha256,
        provenance=bundle.evidence_provenance,
        files=bundle.sha256,
    )

    assert EVIDENCE_OPERATION_ID == "get_external_menu_by_id"
    assert EVIDENCE_CANDIDATE_PAYLOAD_PATHS == (
        "openapi/overlays/operations.overlay.yaml",
        "openapi/overlays/polymorphism.overlay.yaml",
        "tests/fixtures/contracts/external-menu-v2.json",
        "tests/fixtures/contracts/external-menu-v3.json",
        "tests/fixtures/contracts/external-menu-v4.json",
    )
    assert (MANIFEST_SCHEMA_VERSION, MANIFEST_TOOL_NAME, MANIFEST_TOOL_VERSION) == (
        1,
        "iikocloud-evidence-candidates",
        1,
    )
    assert payloads == dict(bundle.canonical_bytes)
    assert {path: sha256_bytes(body) for path, body in payloads.items()} == dict(bundle.sha256)
    assert sha256_bytes(canonical_json_bytes(manifest)) == bundle.manifest_sha256


def test_candidate_modules_have_one_way_imports_and_work_in_either_order() -> None:
    candidate_imports = _relative_imports(candidate_module)
    store_imports = _relative_imports(store_module)

    assert "evidence_candidate_contract" in candidate_imports
    assert "evidence_candidate_store" not in candidate_imports
    assert {"evidence_candidate_contract", "evidence_candidates"}.issubset(store_imports)

    for statement in (
        "import tools.openapi_pipeline.evidence_candidates; "
        "import tools.openapi_pipeline.evidence_candidate_store",
        "import tools.openapi_pipeline.evidence_candidate_store; "
        "import tools.openapi_pipeline.evidence_candidates",
    ):
        subprocess.run(
            [sys.executable, "-c", statement],
            check=True,
            capture_output=True,
            text=True,
        )
