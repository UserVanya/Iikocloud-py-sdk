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
