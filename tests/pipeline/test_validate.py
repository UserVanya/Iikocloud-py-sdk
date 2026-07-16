from typing import Any

import pytest

from tools.openapi_pipeline.errors import ValidationError
from tools.openapi_pipeline.validate import (
    LintIssue,
    ensure_valid_effective_schema,
    lint_effective_schema,
)


def valid_document() -> dict[str, Any]:
    return {
        "openapi": "3.0.1",
        "info": {"title": "fixture", "version": "1"},
        "servers": [{"url": "https://api.example.invalid"}],
        "paths": {
            "/ping": {
                "post": {
                    "operationId": "ping",
                    "responses": {"200": {"description": "ok"}},
                }
            }
        },
        "components": {"schemas": {"Ping": {"type": "object", "properties": {}}}},
    }


def test_effective_schema_rejects_invalid_types_and_broken_refs() -> None:
    document = valid_document()
    document["components"]["schemas"]["Broken"] = {
        "type": "bool",
        "allOf": [{"$ref": "#/components/schemas/Missing"}],
    }

    with pytest.raises(ValidationError) as error:
        ensure_valid_effective_schema(document)

    assert "invalid-type" in str(error.value)
    assert "broken-ref" in str(error.value)


def test_required_must_resolve_to_direct_or_allof_properties() -> None:
    document = valid_document()
    document["components"]["schemas"]["Broken"] = {
        "type": "object",
        "required": ["missing"],
        "properties": {"present": {"type": "string"}},
    }

    with pytest.raises(ValidationError, match="required-not-defined"):
        ensure_valid_effective_schema(document)


def test_required_resolves_local_refs_with_json_pointer_escaping_and_cycles() -> None:
    document = valid_document()
    document["components"]["schemas"].update(
        {
            "base/with~tokens": {
                "type": "object",
                "properties": {"fromBase": {"type": "string"}},
                "allOf": [{"$ref": "#/components/schemas/Cycle"}],
            },
            "Cycle": {
                "type": "object",
                "properties": {"fromCycle": {"type": "string"}},
                "allOf": [{"$ref": "#/components/schemas/base~1with~0tokens"}],
            },
            "Combined": {
                "type": "object",
                "required": ["direct", "fromBase", "fromCycle", "inline"],
                "properties": {"direct": {"type": "string"}},
                "allOf": [
                    {"$ref": "#/components/schemas/base~1with~0tokens"},
                    {"properties": {"inline": {"type": "string"}}},
                ],
            },
        }
    )

    ensure_valid_effective_schema(document)


@pytest.mark.parametrize(
    ("schema", "codes"),
    [
        ({"type": 3}, {"invalid-type"}),
        ({"type": "object", "properties": []}, {"invalid-properties"}),
        ({"type": "object", "required": "name"}, {"invalid-required"}),
        (
            {"type": "object", "required": ["name", 3], "properties": {}},
            {"invalid-required", "required-not-defined"},
        ),
        ({"type": "array"}, {"array-without-items"}),
        ({"type": "array", "items": []}, {"invalid-items"}),
        ({"type": "object", "allOf": {}}, {"invalid-allof"}),
        ({"type": "object", "allOf": ["bad"]}, {"invalid-allof-branch"}),
        ({"$ref": 3}, {"invalid-ref"}),
    ],
)
def test_malformed_schema_shapes_become_actionable_issues(
    schema: dict[str, Any], codes: set[str]
) -> None:
    document = valid_document()
    document["components"]["schemas"]["Broken"] = schema

    issues = lint_effective_schema(document)

    assert codes <= {issue.code for issue in issues}
    with pytest.raises(ValidationError):
        ensure_valid_effective_schema(document)


def test_request_body_required_boolean_is_not_mistaken_for_schema_required() -> None:
    document = valid_document()
    document["paths"]["/ping"]["post"]["requestBody"] = {
        "required": True,
        "content": {
            "application/json": {
                "schema": {"type": "object", "properties": {}}
            }
        },
    }

    ensure_valid_effective_schema(document)


def test_security_scheme_type_is_not_mistaken_for_schema_type() -> None:
    document = valid_document()
    document["components"]["securitySchemes"] = {
        "Bearer": {"type": "http", "scheme": "bearer"}
    }

    ensure_valid_effective_schema(document)


def test_schema_checks_still_apply_to_schema_fields_outside_components_schemas() -> None:
    document = valid_document()
    document["components"]["parameters"] = {
        "Broken": {"schema": {"type": "bool"}}
    }

    with pytest.raises(ValidationError, match="invalid-type"):
        ensure_valid_effective_schema(document)


@pytest.mark.parametrize("token", ["00", "01", "٠", "１"])
def test_json_pointer_array_indices_must_be_canonical_ascii(token: str) -> None:
    document = valid_document()
    document["x-targets"] = [{"type": "string"}, {"type": "integer"}]
    document["components"]["schemas"]["Reference"] = {
        "$ref": f"#/x-targets/{token}"
    }

    issues = lint_effective_schema(document)

    assert any(issue.code == "broken-ref" for issue in issues)


@pytest.mark.parametrize("token", ["0", "1"])
def test_json_pointer_canonical_array_indices_resolve(token: str) -> None:
    document = valid_document()
    document["x-targets"] = [{"type": "string"}, {"type": "integer"}]
    document["components"]["schemas"]["Reference"] = {
        "$ref": f"#/x-targets/{token}"
    }

    assert not any(issue.code == "broken-ref" for issue in lint_effective_schema(document))


def test_schema_data_payloads_are_opaque_to_reference_validation() -> None:
    document = valid_document()
    document["components"]["schemas"]["Payload"] = {
        "type": "object",
        "properties": {},
        "example": {"$ref": "#/missing/example"},
        "default": {"$ref": "#/missing/default"},
        "enum": [{"$ref": "#/missing/enum"}],
    }

    ensure_valid_effective_schema(document)


def test_nested_extension_payload_is_opaque_to_reference_validation() -> None:
    document = valid_document()
    document["x-private-payload"] = {
        "nested": {
            "$ref": "#/missing/extension",
            "schema": {"$ref": "#/missing/extension-schema"},
        }
    }

    ensure_valid_effective_schema(document)


def test_example_value_is_opaque_but_example_reference_object_is_structural() -> None:
    document = valid_document()
    document["components"]["examples"] = {
        "Inline": {"value": {"$ref": "#/missing/example-value"}},
        "Alias": {"$ref": "#/components/examples/Missing"},
    }

    broken_refs = [
        issue for issue in lint_effective_schema(document) if issue.code == "broken-ref"
    ]

    assert broken_refs == [
        LintIssue(
            "broken-ref",
            "#/components/examples/Alias",
            "#/components/examples/Missing",
        )
    ]


def test_broken_structural_response_reference_is_still_rejected() -> None:
    document = valid_document()
    document["components"]["responses"] = {
        "x-alias": {"$ref": "#/components/responses/Missing"}
    }

    with pytest.raises(ValidationError, match="broken-ref@#/components/responses/x-alias"):
        ensure_valid_effective_schema(document)


def test_default_response_reference_is_structural_not_default_data() -> None:
    document = valid_document()
    document["paths"]["/ping"]["post"]["responses"]["default"] = {
        "$ref": "#/components/responses/Missing"
    }

    with pytest.raises(
        ValidationError, match="broken-ref@#/paths/~1ping/post/responses/default"
    ):
        ensure_valid_effective_schema(document)


def test_only_http_methods_are_operations_and_operation_ids_are_nonempty_unique() -> None:
    document = valid_document()
    document["paths"] = {
        "/a": {
            "parameters": [],
            "summary": "not an operation",
            "x-extension": {"operationId": "ignored"},
            "get": {"operationId": "duplicate", "responses": {}},
            "post": {"operationId": "   ", "responses": {}},
        },
        "/b": {
            "get": {"operationId": "duplicate", "responses": {}},
            "delete": [],
        },
    }

    issues = lint_effective_schema(document)

    assert [issue.code for issue in issues].count("duplicate-operation-id") == 1
    assert [issue.code for issue in issues].count("missing-operation-id") == 1
    assert [issue.code for issue in issues].count("invalid-operation") == 1
    assert not any("parameters" in issue.path for issue in issues)
    assert not any("x-extension" in issue.path for issue in issues)


@pytest.mark.parametrize(
    ("paths", "code"),
    [
        ([], "invalid-paths"),
        ({"/ping": []}, "invalid-path-item"),
        ({"/ping": {3: {}}}, "invalid-path-item-key"),
    ],
)
def test_malformed_operation_containers_do_not_crash(paths: Any, code: str) -> None:
    document = valid_document()
    document["paths"] = paths

    issues = lint_effective_schema(document)

    assert code in {issue.code for issue in issues}


@pytest.mark.parametrize(
    "servers",
    [None, [], {}, ["https://api.example.invalid"], [{}], [{"url": "   "}]],
)
def test_servers_must_be_a_nonempty_list_of_url_objects(servers: Any) -> None:
    document = valid_document()
    if servers is None:
        document.pop("servers")
    else:
        document["servers"] = servers

    issues = lint_effective_schema(document)

    assert {issue.code for issue in issues} & {
        "missing-servers",
        "invalid-servers",
        "invalid-server",
    }


def test_issue_order_and_validation_summary_are_deterministic() -> None:
    first = valid_document()
    first["components"]["schemas"].update(
        {
            "Zulu": {"type": "bool"},
            "Alpha": {"type": "array"},
        }
    )
    second = valid_document()
    second["components"]["schemas"].update(
        {
            "Alpha": {"type": "array"},
            "Zulu": {"type": "bool"},
        }
    )

    first_issues = lint_effective_schema(first)
    second_issues = lint_effective_schema(second)

    assert first_issues == second_issues == sorted(first_issues)
    with pytest.raises(ValidationError) as first_error:
        ensure_valid_effective_schema(first)
    with pytest.raises(ValidationError) as second_error:
        ensure_valid_effective_schema(second)
    assert str(first_error.value) == str(second_error.value)


def test_lint_returns_frozen_orderable_issue_values() -> None:
    issue = LintIssue("code", "#", "message")

    assert sorted([LintIssue("z", "#", "last"), issue])[0] == issue
    with pytest.raises((AttributeError, TypeError)):
        issue.code = "changed"  # type: ignore[misc]


def test_non_object_document_is_reported_instead_of_crashing() -> None:
    issues = lint_effective_schema([])  # type: ignore[arg-type]

    assert issues == [LintIssue("invalid-document", "#", "document must be an object")]
    with pytest.raises(ValidationError, match="invalid-document"):
        ensure_valid_effective_schema([])  # type: ignore[arg-type]
