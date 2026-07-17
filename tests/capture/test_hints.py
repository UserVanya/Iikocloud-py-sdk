from __future__ import annotations

import copy
from typing import Any

import pytest

from tools.openapi_pipeline.capture import (
    ARRAY_ITEM,
    OBJECT_VALUE,
    RedactionHints,
    Sanitizer,
)
from tools.openapi_pipeline.errors import SafetyError


def _effective_schema() -> dict[str, Any]:
    return {
        "openapi": "3.1.0",
        "paths": {
            "/api/2/menu/by_id": {
                "post": {
                    "operationId": "get_external_menu_by_id",
                    "requestBody": {"$ref": "#/components/requestBodies/MenuRequest"},
                    "responses": {
                        "200": {"$ref": "#/components/responses/MenuResponse"},
                        "202": {
                            "content": {
                                "application/json": {
                                    "schema": {"properties": {"queued": {"enum": ["QUEUED"]}}}
                                }
                            }
                        },
                    },
                }
            }
        },
        "components": {
            "requestBodies": {
                "MenuRequest": {
                    "content": {
                        "application/json": {
                            "schema": {"$ref": "#/components/schemas/MenuRequest"}
                        }
                    }
                }
            },
            "responses": {
                "MenuResponse": {
                    "content": {
                        "application/json": {
                            "schema": {"$ref": "#/components/schemas/MenuEnvelope"}
                        }
                    }
                }
            },
            "schemas": {
                "MenuRequest": {
                    "type": "object",
                    "properties": {
                        "mode": {"const": "FULL"},
                        "name": {"type": "string"},
                        "escaped": {"$ref": "#%2Fcomponents%2Fschemas%2Fmenu~1branch~0x"},
                    },
                },
                "menu/branch~x": {"type": "string", "enum": ["ESCAPED"]},
                "MenuEnvelope": {
                    "oneOf": [
                        {"$ref": "#/components/schemas/Dish"},
                        {"$ref": "#/components/schemas/Group"},
                    ],
                    "discriminator": {
                        "propertyName": "type",
                        "mapping": {
                            "DISH": "#/components/schemas/Dish",
                            "GROUP": "#/components/schemas/Group",
                        },
                    },
                },
                "Base": {
                    "type": "object",
                    "properties": {
                        "state": {"enum": ["ACTIVE", "HIDDEN"]},
                    },
                },
                "Dish": {
                    "allOf": [
                        {"$ref": "#/components/schemas/Base"},
                        {
                            "type": "object",
                            "properties": {
                                "type": {"const": "DISH"},
                                "name": {"type": "string"},
                                "comment": {"type": "string"},
                                "children": {
                                    "type": "array",
                                    "items": {"$ref": "#/components/schemas/MenuEnvelope"},
                                },
                            },
                        },
                    ]
                },
                "Group": {
                    "anyOf": [
                        {
                            "type": "object",
                            "properties": {"type": {"enum": ["GROUP"]}},
                        }
                    ]
                },
            },
        },
    }


def test_redaction_hints_resolve_json_request_success_branches_and_cycles() -> None:
    hints = RedactionHints.for_operation(_effective_schema(), "get_external_menu_by_id")

    assert hints.operation_id == "get_external_menu_by_id"
    assert hints.request_values[("escaped",)] == frozenset({"ESCAPED"})
    assert hints.request_values[("mode",)] == frozenset({"FULL"})
    assert ("type",) not in hints.request_values
    assert hints.response_values[("queued",)] == frozenset({"QUEUED"})
    assert hints.response_values[("state",)] == frozenset()
    assert hints.response_values[("type",)] == frozenset({"DISH", "GROUP"})


def test_menu_discriminator_is_retained_but_adjacent_strings_are_redacted() -> None:
    hints = RedactionHints.for_operation(_effective_schema(), "get_external_menu_by_id")
    value = {
        "type": "DISH",
        "name": "Private venue",
        "comment": "customer text",
        "children": [{"type": "NOT_IN_SCHEMA", "state": "ACTIVE", "name": "Private child"}],
    }

    sanitized = Sanitizer().sanitize(value, path_values=hints.response_values)

    assert sanitized["type"] == "DISH"
    assert sanitized["name"] == "<redacted:string>"
    assert sanitized["comment"] == "<redacted:string>"
    assert sanitized["children"][0] == {
        "type": "<redacted:string>",
        "state": "<redacted:string>",
        "name": "<redacted:string>",
    }


def test_redaction_hints_are_immutable_and_do_not_infer_observed_values() -> None:
    hints = RedactionHints.for_operation(_effective_schema(), "get_external_menu_by_id")

    with pytest.raises(TypeError):
        hints.response_values[("type",)] = frozenset({"OBSERVED"})  # type: ignore[index]
    assert "OBSERVED" not in hints.response_values[("type",)]


def test_path_hints_separate_colliding_names_request_response_arrays_and_maps() -> None:
    schema = {
        "openapi": "3.1.0",
        "paths": {
            "/collision": {
                "post": {
                    "operationId": "collision",
                    "requestBody": {
                        "content": {
                            "application/json": {
                                "schema": {
                                    "allOf": [
                                        {
                                            "properties": {
                                                "branch": {
                                                    "properties": {"kind": {"enum": ["REQUEST"]}}
                                                },
                                                "free": {
                                                    "properties": {"kind": {"type": "string"}}
                                                },
                                            }
                                        },
                                        {
                                            "properties": {
                                                "items": {
                                                    "type": "array",
                                                    "items": {
                                                        "properties": {"kind": {"const": "ITEM"}}
                                                    },
                                                },
                                                "mapped": {
                                                    "properties": {
                                                        "fixed": {
                                                            "properties": {
                                                                "kind": {"type": "string"}
                                                            }
                                                        }
                                                    },
                                                    "additionalProperties": {
                                                        "properties": {
                                                            "kind": {"enum": ["DYNAMIC"]}
                                                        }
                                                    },
                                                },
                                            }
                                        },
                                    ]
                                }
                            }
                        }
                    },
                    "responses": {
                        "200": {
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "properties": {
                                            "branch": {
                                                "properties": {"kind": {"enum": ["RESPONSE"]}}
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    },
                }
            }
        },
    }
    hints = RedactionHints.for_operation(schema, "collision")

    assert hints.request_values[("branch", "kind")] == frozenset({"REQUEST"})
    assert hints.response_values[("branch", "kind")] == frozenset({"RESPONSE"})
    assert hints.request_values[("items", ARRAY_ITEM, "kind")] == frozenset({"ITEM"})
    assert hints.request_values[("mapped", OBJECT_VALUE, "kind")] == frozenset({"DYNAMIC"})

    request = Sanitizer().sanitize(
        {
            "branch": {"kind": "REQUEST"},
            "free": {"kind": "REQUEST"},
            "items": [{"kind": "ITEM"}, {"kind": "REQUEST"}],
            "mapped": {
                "fixed": {"kind": "DYNAMIC"},
                "arbitrary": {"kind": "DYNAMIC"},
            },
        },
        path_values=hints.request_values,
    )
    response = Sanitizer().sanitize(
        {"branch": {"kind": "RESPONSE"}},
        path_values=hints.response_values,
    )

    assert request["branch"]["kind"] == "REQUEST"
    assert request["free"]["kind"] == "<redacted:string>"
    assert request["items"] == [
        {"kind": "ITEM"},
        {"kind": "<redacted:string>"},
    ]
    assert request["mapped"]["fixed"]["kind"] == "<redacted:string>"
    assert request["mapped"]["arbitrary"]["kind"] == "DYNAMIC"
    assert response["branch"]["kind"] == "RESPONSE"


def test_compositions_preserve_only_branch_safe_string_constraints() -> None:
    schema = {
        "openapi": "3.1.0",
        "paths": {
            "/composition": {
                "post": {
                    "operationId": "composition",
                    "responses": {
                        "200": {
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "properties": {
                                            "choice": {
                                                "oneOf": [
                                                    {
                                                        "properties": {
                                                            "name": {"enum": ["STANDARD"]},
                                                            "kind": {"const": "A"},
                                                            "code": {"enum": ["X"]},
                                                        }
                                                    },
                                                    {
                                                        "properties": {
                                                            "name": {"type": "string"},
                                                            "kind": {"const": "B"},
                                                            "code": {"enum": ["Y"]},
                                                        }
                                                    },
                                                ],
                                                "discriminator": {
                                                    "propertyName": "kind",
                                                    "mapping": {
                                                        "A": "#/components/schemas/A",
                                                        "B": "#/components/schemas/B",
                                                    },
                                                },
                                            },
                                            "intersection": {
                                                "allOf": [
                                                    {
                                                        "properties": {
                                                            "mode": {"enum": ["A", "B"]},
                                                            "label": {"enum": ["SAFE"]},
                                                        }
                                                    },
                                                    {
                                                        "properties": {
                                                            "mode": {"enum": ["B", "C"]},
                                                            "label": {"type": "string"},
                                                        }
                                                    },
                                                ]
                                            },
                                            "items": {
                                                "type": "array",
                                                "items": {
                                                    "anyOf": [
                                                        {"enum": ["ITEM"]},
                                                        {"type": "string"},
                                                    ]
                                                },
                                            },
                                        }
                                    }
                                }
                            }
                        }
                    },
                }
            }
        },
        "components": {
            "schemas": {
                "A": {
                    "properties": {
                        "name": {"enum": ["STANDARD"]},
                        "kind": {"const": "A"},
                        "code": {"enum": ["X"]},
                    }
                },
                "B": {
                    "properties": {
                        "name": {"type": "string"},
                        "kind": {"const": "B"},
                        "code": {"enum": ["Y"]},
                    }
                },
            }
        },
    }
    hints = RedactionHints.for_operation(schema, "composition")

    assert hints.response_values[("choice", "name")] == frozenset()
    assert hints.response_values[("choice", "kind")] == frozenset({"A", "B"})
    assert hints.response_values[("choice", "code")] == frozenset({"X", "Y"})
    assert hints.response_values[("intersection", "mode")] == frozenset({"B"})
    assert hints.response_values[("intersection", "label")] == frozenset({"SAFE"})
    assert hints.response_values[("items", ARRAY_ITEM)] == frozenset()

    sanitized = Sanitizer().sanitize(
        {
            "choice": {"name": "STANDARD", "kind": "A", "code": "X"},
            "intersection": {"mode": "B", "label": "SAFE"},
            "items": ["ITEM"],
        },
        path_values=hints.response_values,
    )
    assert sanitized["choice"] == {
        "name": "<redacted:string>",
        "kind": "A",
        "code": "X",
    }
    assert sanitized["intersection"] == {"mode": "B", "label": "SAFE"}
    assert sanitized["items"] == ["<redacted:string>"]


def test_redaction_hints_reject_unknown_or_duplicate_operation() -> None:
    schema = _effective_schema()
    with pytest.raises(SafetyError, match="Unknown capture operation"):
        RedactionHints.for_operation(schema, "missing")

    schema["paths"]["/duplicate"] = copy.deepcopy(schema["paths"]["/api/2/menu/by_id"])
    with pytest.raises(SafetyError, match="multiple"):
        RedactionHints.for_operation(schema, "get_external_menu_by_id")


@pytest.mark.parametrize(
    "mutation",
    [
        "broken-request-ref",
        "remote-response-ref",
        "malformed-one-of",
        "broken-discriminator-ref",
        "non-json-response",
        "no-success-response",
    ],
)
def test_redaction_hints_fail_closed_on_broken_or_unknown_traversal(
    mutation: str,
) -> None:
    schema = _effective_schema()
    operation = schema["paths"]["/api/2/menu/by_id"]["post"]
    if mutation == "broken-request-ref":
        operation["requestBody"]["$ref"] = "#/components/requestBodies/Missing"
    elif mutation == "remote-response-ref":
        operation["responses"]["200"]["$ref"] = "https://example.invalid/schema"
    elif mutation == "malformed-one-of":
        schema["components"]["schemas"]["MenuEnvelope"]["oneOf"] = {}
    elif mutation == "broken-discriminator-ref":
        schema["components"]["schemas"]["MenuEnvelope"]["discriminator"]["mapping"]["DISH"] = (
            "#/components/schemas/Missing"
        )
    elif mutation == "non-json-response":
        operation["responses"] = {
            "200": {"content": {"application/octet-stream": {"schema": {"type": "string"}}}}
        }
    elif mutation == "no-success-response":
        operation["responses"] = {
            "400": {"content": {"application/json": {"schema": {"type": "object"}}}}
        }

    with pytest.raises(SafetyError):
        RedactionHints.for_operation(schema, "get_external_menu_by_id")
