import copy
import json
from pathlib import Path

from tools.openapi_pipeline.inventory import collect_inventory, diff_inventory
from tools.openapi_pipeline.reports import build_upstream_report, render_upstream_markdown


def test_inventory_diff_reports_added_paths_and_schemas() -> None:
    fixtures = Path("tests/fixtures/openapi")
    before = json.loads((fixtures / "minimal-v1.json").read_text())
    after = json.loads((fixtures / "minimal-v2.json").read_text())

    diff = diff_inventory(collect_inventory(before), collect_inventory(after))

    assert diff.added_paths == ("/api/1/status",)
    assert diff.added_operations == ("POST /api/1/status",)
    assert diff.added_schemas == ("Status",)


def test_collect_inventory_sorts_paths_operations_and_schemas() -> None:
    document = {
        "openapi": "3.0.1",
        "paths": {
            "/z": {"post": {}, "parameters": []},
            "/a": {"trace": {}, "get": {}},
        },
        "components": {"schemas": {"Zulu": {}, "Alpha": {}}},
    }

    inventory = collect_inventory(document)

    assert inventory.paths == ("/a", "/z")
    assert inventory.operations == ("GET /a", "POST /z", "TRACE /a")
    assert inventory.schemas == ("Alpha", "Zulu")


def test_inventory_diff_reports_sorted_removals() -> None:
    before = collect_inventory(
        {
            "openapi": "3.0.1",
            "paths": {
                "/z": {"post": {}},
                "/a": {"get": {}},
                "/m": {"delete": {}},
            },
            "components": {"schemas": {"Zulu": {}, "Alpha": {}, "Middle": {}}},
        }
    )
    after = collect_inventory(
        {
            "openapi": "3.0.1",
            "paths": {"/m": {"delete": {}}},
            "components": {"schemas": {"Middle": {}}},
        }
    )

    diff = diff_inventory(before, after)

    assert diff.removed_paths == ("/a", "/z")
    assert diff.removed_operations == ("GET /a", "POST /z")
    assert diff.removed_schemas == ("Alpha", "Zulu")


def test_inventory_diff_reports_changed_operation_and_schema_bodies() -> None:
    before_document = {
        "openapi": "3.0.1",
        "paths": {
            "/same": {
                "post": {
                    "responses": {"200": {"description": "before"}},
                    "summary": "stable name",
                }
            }
        },
        "components": {
            "schemas": {"Stable": {"type": "object", "properties": {"id": {"type": "string"}}}}
        },
    }
    after_document = {
        "components": {
            "schemas": {
                "Stable": {
                    "properties": {"id": {"format": "uuid", "type": "string"}},
                    "type": "object",
                }
            }
        },
        "paths": {
            "/same": {
                "post": {
                    "summary": "stable name",
                    "responses": {"200": {"description": "after"}},
                }
            }
        },
        "openapi": "3.0.1",
    }

    before = collect_inventory(before_document)
    after = collect_inventory(after_document)
    difference = diff_inventory(before, after)

    assert before.operations == after.operations == ("POST /same",)
    assert before.schemas == after.schemas == ("Stable",)
    assert difference.changed_operations == ("POST /same",)
    assert difference.changed_schemas == ("Stable",)
    assert (
        dict(before.operation_hashes)["POST /same"] != dict(after.operation_hashes)["POST /same"]
    )
    assert dict(before.schema_hashes)["Stable"] != dict(after.schema_hashes)["Stable"]


def test_inventory_hashes_are_canonical_and_reports_are_deterministic() -> None:
    left = {
        "openapi": "3.0.1",
        "paths": {"/same": {"post": {"responses": {}, "tags": ["one"]}}},
        "components": {"schemas": {"Stable": {"required": ["id"], "type": "object"}}},
    }
    reordered = {
        "components": {"schemas": {"Stable": {"type": "object", "required": ["id"]}}},
        "paths": {"/same": {"post": {"tags": ["one"], "responses": {}}}},
        "openapi": "3.0.1",
    }

    assert collect_inventory(left) == collect_inventory(reordered)
    first = build_upstream_report(None, left)
    second = build_upstream_report(None, reordered)
    assert first == second
    assert render_upstream_markdown(first) == render_upstream_markdown(second)


def test_markdown_escapes_untrusted_names_and_renders_changed_entries() -> None:
    dangerous = "POST /value`\n## injected\x01"
    report = {
        "diff": {
            "added_paths": [],
            "removed_paths": [],
            "added_operations": [],
            "removed_operations": [],
            "changed_operations": [dangerous],
            "added_schemas": [],
            "removed_schemas": [],
            "changed_schemas": ["Tick`Schema"],
        }
    }

    markdown = render_upstream_markdown(report)

    assert "- Changed:" in markdown
    assert "## injected" not in markdown
    assert "\x01" not in markdown
    assert "POST /value\\u0060\\n\\u0023\\u0023 injected\\u0001" in markdown
    assert "Tick\\u0060Schema" in markdown


def _operation_context_document() -> dict[str, object]:
    return {
        "openapi": "3.0.1",
        "servers": [{"url": "https://example.invalid"}],
        "security": [{"ApiKey": []}],
        "paths": {
            "/same": {
                "parameters": [{"$ref": "#/components/parameters/TenantHeader"}],
                "post": {
                    "requestBody": {"$ref": "#/components/requestBodies/Payload"},
                    "responses": {"200": {"$ref": "#/components/responses/Ok"}},
                },
            }
        },
        "components": {
            "parameters": {
                "TenantHeader": {
                    "name": "X-Tenant",
                    "in": "header",
                    "schema": {"type": "string"},
                }
            },
            "requestBodies": {
                "Payload": {
                    "content": {
                        "application/json": {"schema": {"$ref": "#/components/schemas/Input"}}
                    }
                }
            },
            "responses": {
                "Ok": {
                    "description": "ok",
                    "content": {
                        "application/json": {"schema": {"$ref": "#/components/schemas/Output"}}
                    },
                }
            },
            "schemas": {
                "Input": {"type": "object", "properties": {"id": {"type": "string"}}},
                "Output": {"type": "object"},
            },
            "securitySchemes": {"ApiKey": {"type": "apiKey", "in": "header", "name": "X-Api-Key"}},
        },
    }


def test_operation_hash_includes_path_context_and_transitive_component_contracts() -> None:
    before_document = _operation_context_document()
    variants = []

    path_parameter_changed = copy.deepcopy(before_document)
    path_parameter_changed["components"]["parameters"]["TenantHeader"]["description"] = "new"  # type: ignore[index]
    variants.append(path_parameter_changed)

    request_body_schema_changed = copy.deepcopy(before_document)
    request_body_schema_changed["components"]["schemas"]["Input"]["required"] = ["id"]  # type: ignore[index]
    variants.append(request_body_schema_changed)

    security_scheme_changed = copy.deepcopy(before_document)
    security_scheme_changed["components"]["securitySchemes"]["ApiKey"]["name"] = "X-New-Key"  # type: ignore[index]
    variants.append(security_scheme_changed)

    root_server_changed = copy.deepcopy(before_document)
    root_server_changed["servers"][0]["url"] = "https://changed.invalid"  # type: ignore[index]
    variants.append(root_server_changed)

    before = collect_inventory(before_document)
    for variant in variants:
        difference = diff_inventory(before, collect_inventory(variant))
        assert difference.changed_operations == ("POST /same",)


def test_operation_hash_resolves_percent_encoded_local_uri_fragment_tokens() -> None:
    before_document = {
        "openapi": "3.0.1",
        "paths": {
            "/space": {
                "get": {
                    "responses": {
                        "200": {
                            "content": {
                                "application/json": {
                                    "schema": {"$ref": "#/components/schemas/Foo%20Bar"}
                                }
                            }
                        }
                    }
                }
            },
            "/encoded": {
                "get": {
                    "responses": {
                        "200": {
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "$ref": ("#/components%2Fschemas%2FSlash%7E1Name~0Value")
                                    }
                                }
                            }
                        }
                    }
                }
            },
        },
        "components": {
            "schemas": {
                "Foo Bar": {"type": "string"},
                "Slash/Name~Value": {"type": "integer"},
            }
        },
    }
    before = collect_inventory(before_document)

    space_changed = copy.deepcopy(before_document)
    space_changed["components"]["schemas"]["Foo Bar"]["format"] = "uuid"  # type: ignore[index]
    encoded_changed = copy.deepcopy(before_document)
    encoded_changed["components"]["schemas"]["Slash/Name~Value"]["format"] = "int64"  # type: ignore[index]

    assert diff_inventory(before, collect_inventory(space_changed)).changed_operations == (
        "GET /space",
    )
    assert diff_inventory(before, collect_inventory(encoded_changed)).changed_operations == (
        "GET /encoded",
    )


def test_operation_hash_tracks_nested_percent_encoded_local_reference() -> None:
    before_document = {
        "openapi": "3.0.1",
        "paths": {
            "/nested": {
                "get": {
                    "responses": {
                        "200": {
                            "content": {
                                "application/json": {
                                    "schema": {"$ref": "#/components/schemas/Envelope"}
                                }
                            }
                        }
                    }
                }
            }
        },
        "components": {
            "schemas": {
                "Envelope": {
                    "type": "object",
                    "properties": {
                        "payload": {"$ref": ("#/components%2Fschemas%2FSlash%7E1Name~0Value")}
                    },
                },
                "Slash/Name~Value": {"type": "integer"},
            }
        },
    }
    before = collect_inventory(before_document)
    after_document = copy.deepcopy(before_document)
    after_document["components"]["schemas"]["Slash/Name~Value"]["format"] = "int64"  # type: ignore[index]

    assert diff_inventory(before, collect_inventory(after_document)).changed_operations == (
        "GET /nested",
    )
