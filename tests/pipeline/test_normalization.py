import copy

from tools.openapi_pipeline.io import canonical_json_bytes, sha256_bytes
from tools.openapi_pipeline.normalization import build_types_overlay, correction_for_type
from tools.openapi_pipeline.overlay import apply_overlay


def test_known_iiko_pseudo_types_have_unambiguous_openapi_replacements() -> None:
    assert correction_for_type("bool") == {"type": "boolean"}
    assert correction_for_type("int") == {"type": "integer"}
    assert correction_for_type("float") == {"type": "number", "format": "float"}
    assert correction_for_type("uuid") == {"type": "string", "format": "uuid"}
    assert correction_for_type("integer <int64>") == {
        "type": "integer",
        "format": "int64",
    }
    assert correction_for_type("Array of strings <uuid>") == {
        "type": "array",
        "items": {"type": "string", "format": "uuid"},
    }
    assert correction_for_type("constant string 'OrderUpdate'") == {
        "type": "string",
        "enum": ["OrderUpdate"],
    }


def test_unknown_pseudo_type_is_not_guessed() -> None:
    assert correction_for_type("mystery") is None


def test_corrections_are_deeply_independent() -> None:
    first = correction_for_type("Array of strings <uuid>")
    second = correction_for_type("Array of strings <uuid>")

    assert first is not None
    assert second is not None
    first["items"]["format"] = "changed"

    assert second == {
        "type": "array",
        "items": {"type": "string", "format": "uuid"},
    }
    assert correction_for_type("Array of strings <uuid>") == second


def test_types_overlay_is_deterministic_guarded_and_does_not_mutate_input() -> None:
    document = {
        "components": {
            "schemas": {
                "Zulu": {"type": "bool"},
                "Alpha": {
                    "type": "Array of strings <uuid>",
                    "format": "legacy",
                    "items": {"type": "mystery", "format": "legacy-item"},
                },
            }
        }
    }
    reordered = {
        "components": {
            "schemas": {
                "Alpha": {
                    "items": {"format": "legacy-item", "type": "mystery"},
                    "format": "legacy",
                    "type": "Array of strings <uuid>",
                },
                "Zulu": {"type": "bool"},
            }
        }
    }
    original = copy.deepcopy(document)

    overlay = build_types_overlay(document)

    assert document == original
    assert overlay == build_types_overlay(reordered)
    assert overlay["actions"]
    for action in overlay["actions"]:
        guard = action["x-iiko-sdk-guard"]
        assert guard["expected-matches"] == 1
        assert len(guard["expected-sha256"]) == 64

    effective = apply_overlay(document, overlay)
    assert effective["components"]["schemas"]["Alpha"] == {
        "type": "array",
        "items": {"type": "string", "format": "uuid"},
    }
    assert effective["components"]["schemas"]["Zulu"] == {"type": "boolean"}
    assert document == original


def test_overlay_guards_match_each_intermediate_sequential_value() -> None:
    document = {
        "components": {
            "schemas": {
                "Value": {
                    "description": "keep",
                    "type": "uuid",
                    "format": "incorrect",
                    "items": {"type": "bool"},
                    "enum": ["first", "second"],
                }
            }
        }
    }

    overlay = build_types_overlay(document)
    effective = apply_overlay(document, overlay)

    assert effective["components"]["schemas"]["Value"] == {
        "description": "keep",
        "type": "string",
        "format": "uuid",
        "enum": ["first", "second"],
    }


def test_constant_correction_replaces_an_existing_enum() -> None:
    document = {
        "schema": {
            "type": "constant string 'OrderUpdate'",
            "enum": ["stale"],
        }
    }

    overlay = build_types_overlay(document)

    assert apply_overlay(document, overlay)["schema"] == {
        "type": "string",
        "enum": ["OrderUpdate"],
    }


def test_jsonpath_quotes_object_keys_and_guard_hashes_are_canonical() -> None:
    key = "quote' slash/ tilde~ backslash\\"
    document = {"components": {"schemas": {key: {"type": "bool"}}}}

    overlay = build_types_overlay(document)
    effective = apply_overlay(document, overlay)

    assert effective == {"components": {"schemas": {key: {"type": "boolean"}}}}
    first_action = overlay["actions"][0]
    assert first_action["target"].startswith("$[")
    assert first_action["x-iiko-sdk-guard"]["expected-sha256"] == sha256_bytes(
        canonical_json_bytes("bool")
    )


def test_document_without_known_corrections_produces_reviewable_empty_overlay() -> None:
    document = {"schema": {"type": "string"}}

    assert build_types_overlay(document) == {
        "overlay": "1.1.0",
        "info": {"title": "Normalize iiko pseudo types", "version": "1.0.0"},
        "actions": [],
    }


def test_payload_and_example_type_fields_are_not_treated_as_schema_objects() -> None:
    document = {
        "components": {
            "schemas": {
                "Payload": {
                    "type": "object",
                    "properties": {"actual": {"type": "int"}},
                    "example": {"type": "int", "nested": {"type": "bool"}},
                }
            },
            "examples": {
                "PayloadExample": {
                    "value": {"type": "int", "nested": {"type": "bool"}}
                }
            },
        }
    }

    effective = apply_overlay(document, build_types_overlay(document))

    assert effective["components"]["schemas"]["Payload"]["properties"]["actual"] == {
        "type": "integer"
    }
    assert effective["components"]["schemas"]["Payload"]["example"] == {
        "type": "int",
        "nested": {"type": "bool"},
    }
    assert effective["components"]["examples"]["PayloadExample"]["value"] == {
        "type": "int",
        "nested": {"type": "bool"},
    }


def test_only_schema_roots_and_nested_schema_keywords_are_normalized() -> None:
    document = {
        "components": {
            "schemas": {
                "Nested": {
                    "type": "object",
                    "properties": {"property": {"type": "bool"}},
                    "additionalProperties": {"type": "int"},
                    "allOf": [{"type": "uuid"}],
                    "oneOf": [{"type": "float"}],
                    "anyOf": [{"type": "string <uuid>"}],
                    "not": {"type": "enum", "enum": ["forbidden"]},
                },
                "Array": {"type": "array", "items": {"type": "integer <int32>"}},
            },
            "parameters": {"Limit": {"schema": {"type": "int"}}},
            "headers": {"RequestId": {"schema": {"type": "uuid"}}},
        },
        "paths": {
            "/payload": {
                "post": {
                    "requestBody": {
                        "content": {
                            "application/json": {"schema": {"type": "bool"}}
                        }
                    }
                }
            }
        },
        "arbitrary": {"type": "int"},
    }

    effective = apply_overlay(document, build_types_overlay(document))
    nested = effective["components"]["schemas"]["Nested"]

    assert nested["properties"]["property"]["type"] == "boolean"
    assert nested["additionalProperties"]["type"] == "integer"
    assert nested["allOf"][0] == {"type": "string", "format": "uuid"}
    assert nested["oneOf"][0] == {"type": "number", "format": "float"}
    assert nested["anyOf"][0] == {"type": "string", "format": "uuid"}
    assert nested["not"] == {"type": "string", "enum": ["forbidden"]}
    assert effective["components"]["schemas"]["Array"]["items"] == {
        "type": "integer",
        "format": "int32",
    }
    assert effective["components"]["parameters"]["Limit"]["schema"] == {
        "type": "integer"
    }
    assert effective["components"]["headers"]["RequestId"]["schema"] == {
        "type": "string",
        "format": "uuid",
    }
    request_schema = effective["paths"]["/payload"]["post"]["requestBody"]["content"][
        "application/json"
    ]["schema"]
    assert request_schema == {"type": "boolean"}
    assert effective["arbitrary"] == {"type": "int"}


def test_exact_iiko_scalar_required_marker_is_removed_for_native_and_pseudo_types() -> None:
    document = {
        "components": {
            "schemas": {
                "Native": {
                    "description": "keep",
                    "type": "string",
                    "required": ["true"],
                },
                "Pseudo": {"type": "bool", "required": ["true"]},
                "Constant": {
                    "type": "constant string 'fixed'",
                    "required": ["true"],
                },
            }
        }
    }

    effective = apply_overlay(document, build_types_overlay(document))

    assert effective["components"]["schemas"] == {
        "Native": {"description": "keep", "type": "string"},
        "Pseudo": {"type": "boolean"},
        "Constant": {"type": "string", "enum": ["fixed"]},
    }


def test_scalar_required_cleanup_is_deterministic_guarded_and_non_mutating() -> None:
    document = {
        "components": {
            "schemas": {
                "Zulu": {"type": "number", "required": ["true"]},
                "Alpha": {"type": "integer", "required": ["true"]},
            }
        }
    }
    reordered = {
        "components": {
            "schemas": {
                "Alpha": {"required": ["true"], "type": "integer"},
                "Zulu": {"required": ["true"], "type": "number"},
            }
        }
    }
    original = copy.deepcopy(document)

    overlay = build_types_overlay(document)

    assert document == original
    assert overlay == build_types_overlay(reordered)
    assert [action["target"] for action in overlay["actions"]] == [
        '$["components"]["schemas"]["Alpha"]["required"]',
        '$["components"]["schemas"]["Zulu"]["required"]',
    ]
    assert [
        action["x-iiko-sdk-guard"]["issue"] for action in overlay["actions"]
    ] == [
        "remove-malformed-scalar-required-1",
        "remove-malformed-scalar-required-2",
    ]
    for action in overlay["actions"]:
        assert action["remove"] is True
        guard = action["x-iiko-sdk-guard"]
        assert guard["expected-matches"] == 1
        assert guard["expected-sha256"] == sha256_bytes(
            canonical_json_bytes(["true"])
        )
    assert apply_overlay(document, overlay)["components"]["schemas"] == {
        "Alpha": {"type": "integer"},
        "Zulu": {"type": "number"},
    }


def test_scalar_required_cleanup_does_not_guess_other_malformed_forms() -> None:
    document = {
        "components": {
            "schemas": {
                "Object": {
                    "type": "object",
                    "properties": {"true": {"type": "string"}},
                    "required": ["true"],
                },
                "Array": {
                    "type": "array",
                    "items": {"type": "string"},
                    "required": ["true"],
                },
                "PseudoArray": {
                    "type": "Array of strings <uuid>",
                    "required": ["true"],
                },
                "Unknown": {"type": "mystery", "required": ["true"]},
                "NoType": {"required": ["true"]},
                "DifferentMarker": {"type": "string", "required": ["false"]},
                "MixedMarker": {
                    "type": "boolean",
                    "required": ["true", "other"],
                },
                "WrongShape": {"type": "number", "required": "true"},
            }
        }
    }

    effective = apply_overlay(document, build_types_overlay(document))

    assert effective["components"]["schemas"]["Object"]["required"] == ["true"]
    assert effective["components"]["schemas"]["Array"]["required"] == ["true"]
    assert effective["components"]["schemas"]["PseudoArray"]["required"] == ["true"]
    assert effective["components"]["schemas"]["PseudoArray"]["type"] == "array"
    assert effective["components"]["schemas"]["Unknown"]["required"] == ["true"]
    assert effective["components"]["schemas"]["NoType"]["required"] == ["true"]
    assert effective["components"]["schemas"]["DifferentMarker"]["required"] == ["false"]
    assert effective["components"]["schemas"]["MixedMarker"]["required"] == [
        "true",
        "other",
    ]
    assert effective["components"]["schemas"]["WrongShape"]["required"] == "true"
