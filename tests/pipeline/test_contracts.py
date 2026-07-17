from __future__ import annotations

import copy
import json
from pathlib import Path
from typing import Any

import pytest
import yaml

from tools.openapi_pipeline.contracts import (
    IIKO_AUTH_OPERATIONS,
    IIKO_ROOT_SERVER_URL,
    build_contracts_overlay,
)
from tools.openapi_pipeline.io import sha256_bytes
from tools.openapi_pipeline.overlay import apply_overlay
from tools.openapi_pipeline.validate import (
    ensure_valid_effective_schema,
    lint_effective_schema,
)

AUTHORIZATION_PARAMETER = {
    "description": "Authorization token.",
    "in": "header",
    "name": "Authorization",
    "required": True,
    "schema": {"example": "Bearer public-upstream-example", "type": "string"},
}


def raw_contract_fixture() -> dict[str, Any]:
    return {
        "openapi": "3.0.1",
        "info": {"title": "fixture", "version": "1"},
        "paths": {
            "/api/1/access_token": {
                "post": {
                    "operationId": "authenticate",
                    "responses": {"200": {"description": "ok"}},
                }
            },
            "/api/1/ping": {
                "post": {
                    "operationId": "ping",
                    "parameters": [copy.deepcopy(AUTHORIZATION_PARAMETER)],
                    "responses": {"200": {"description": "ok"}},
                }
            },
            "/api/v2/access_token": {
                "post": {
                    "operationId": "authenticate_v2",
                    "responses": {"200": {"description": "ok"}},
                }
            },
        },
        "components": {"schemas": {}},
    }


def valid_iikocloud_document() -> dict[str, Any]:
    document = raw_contract_fixture()
    document["servers"] = [{"url": IIKO_ROOT_SERVER_URL}]
    document["components"]["securitySchemes"] = {
        "BearerAuth": {"type": "http", "scheme": "bearer"}
    }
    document["paths"]["/api/1/ping"]["post"]["parameters"] = []
    for path, method in IIKO_AUTH_OPERATIONS:
        document["paths"][path][method]["security"] = []
    document["paths"]["/api/1/ping"]["post"]["security"] = [
        {"BearerAuth": []}
    ]
    return document


def test_contract_overlay_builder_is_guarded_sequential_and_non_mutating() -> None:
    raw = raw_contract_fixture()
    before = copy.deepcopy(raw)

    overlay = build_contracts_overlay(raw)
    effective = apply_overlay(raw, overlay)

    assert raw == before
    assert overlay["overlay"] == "1.1.0"
    assert len(overlay["actions"]) == 8
    assert all(
        action["x-iiko-sdk-guard"]["expected-sha256"]
        for action in overlay["actions"]
    )
    assert effective == valid_iikocloud_document()
    ensure_valid_effective_schema(effective, require_iikocloud_contracts=True)


@pytest.mark.skipif(
    not Path("build/upstream/candidate.json").is_file(),
    reason="ignored bootstrap candidate is not present in a clean checkout",
)
def test_committed_contract_overlay_matches_and_applies_to_exact_raw_candidate() -> None:
    raw_path = Path("build/upstream/candidate.json")
    raw_bytes = raw_path.read_bytes()
    assert sha256_bytes(raw_bytes) == (
        "e656ab889ac1968b95bac29e78f08f1c46cd2d2f5e1c370eadbc400da5bbe89a"
    )
    raw = json.loads(raw_bytes)
    expected = build_contracts_overlay(raw)
    committed = yaml.safe_load(
        Path("openapi/overlays/contracts.overlay.yaml").read_text(encoding="utf-8")
    )

    assert committed == expected
    effective = apply_overlay(raw, committed)
    contract_issues = [
        issue
        for issue in lint_effective_schema(
            effective,
            require_iikocloud_contracts=True,
        )
        if issue.code.startswith("iiko-")
    ]
    assert contract_issues == []
    assert sha256_bytes(raw_path.read_bytes()) == sha256_bytes(raw_bytes)


def test_generic_lint_does_not_impose_iikocloud_contracts_without_opt_in() -> None:
    document = raw_contract_fixture()
    document["servers"] = [{"url": "https://api.example.invalid"}]

    codes = {issue.code for issue in lint_effective_schema(document)}

    assert not any(code.startswith("iiko-") for code in codes)


@pytest.mark.parametrize(
    ("mutation", "code"),
    [
        (
            lambda document: document.update(
                servers=[{"url": "https://api.example.invalid"}]
            ),
            "iiko-root-server",
        ),
        (
            lambda document: document["components"].update(securitySchemes={}),
            "iiko-bearer-scheme",
        ),
        (
            lambda document: document["paths"]["/api/1/ping"]["post"].update(
                security=[]
            ),
            "iiko-bearer-required",
        ),
        (
            lambda document: document["paths"]["/api/1/access_token"]["post"].update(
                security=[{"BearerAuth": []}]
            ),
            "iiko-auth-security",
        ),
    ],
)
def test_iikocloud_contract_lint_rejects_invalid_contracts(
    mutation: Any, code: str
) -> None:
    document = valid_iikocloud_document()
    mutation(document)

    issues = lint_effective_schema(document, require_iikocloud_contracts=True)

    assert code in {issue.code for issue in issues}


def test_iikocloud_contract_lint_rejects_path_and_operation_authorization_parameters() -> None:
    document = valid_iikocloud_document()
    document["paths"]["/api/1/ping"]["parameters"] = [
        copy.deepcopy(AUTHORIZATION_PARAMETER)
    ]
    document["paths"]["/api/1/ping"]["post"]["parameters"] = [
        copy.deepcopy(AUTHORIZATION_PARAMETER)
    ]

    issues = lint_effective_schema(document, require_iikocloud_contracts=True)

    raw_headers = [issue for issue in issues if issue.code == "iiko-raw-authorization"]
    assert len(raw_headers) == 2
    assert {issue.path for issue in raw_headers} == {
        "#/paths/~1api~11~1ping/parameters/0",
        "POST /api/1/ping/parameters/0",
    }
