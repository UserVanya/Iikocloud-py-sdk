from pathlib import Path
from typing import Any

import pytest
import yaml

from tools.openapi_pipeline.errors import StaleOverlayError, ValidationError
from tools.openapi_pipeline.io import canonical_json_bytes, sha256_bytes
from tools.openapi_pipeline.overlay import apply_overlay, apply_overlay_files


def source_document() -> dict:
    return {
        "openapi": "3.0.1",
        "components": {
            "schemas": {
                "Ping": {"type": "object", "properties": {"enabled": {"type": "bool"}}}
            }
        },
    }


def overlay_document(*actions: Any) -> dict[str, Any]:
    return {
        "overlay": "1.1.0",
        "info": {"title": "Test overlay", "version": "1.0.0"},
        "actions": list(actions),
    }


def guarded_action(
    target: str,
    expected_values: list[Any],
    *,
    issue: str = "test-action",
    **operation: Any,
) -> dict[str, Any]:
    guarded_value = expected_values[0] if len(expected_values) == 1 else expected_values
    return {
        "target": target,
        "x-iiko-sdk-guard": {
            "issue": issue,
            "expected-matches": len(expected_values),
            "expected-sha256": sha256_bytes(canonical_json_bytes(guarded_value)),
        },
        **operation,
    }


def test_guarded_primitive_update_does_not_mutate_source() -> None:
    overlay = yaml.safe_load(Path("tests/fixtures/openapi/types.overlay.yaml").read_text())
    assert overlay["actions"][0]["x-iiko-sdk-guard"]["expected-sha256"] == sha256_bytes(
        canonical_json_bytes("bool")
    )
    source = source_document()

    effective = apply_overlay(source, overlay)

    assert source["components"]["schemas"]["Ping"]["properties"]["enabled"]["type"] == "bool"
    assert (
        effective["components"]["schemas"]["Ping"]["properties"]["enabled"]["type"]
        == "boolean"
    )


def test_changed_upstream_fragment_makes_overlay_stale() -> None:
    overlay = yaml.safe_load(Path("tests/fixtures/openapi/types.overlay.yaml").read_text())
    source = source_document()
    source["components"]["schemas"]["Ping"]["properties"]["enabled"]["type"] = "boolean"

    with pytest.raises(StaleOverlayError, match="upstream-invalid-bool"):
        apply_overlay(source, overlay)


def test_changed_match_count_makes_overlay_stale() -> None:
    overlay = overlay_document(
        guarded_action("$.missing", ["old-value"], issue="missing-upstream", update="new-value")
    )

    with pytest.raises(
        StaleOverlayError, match="missing-upstream: expected 1 matches, found 0"
    ):
        apply_overlay(source_document(), overlay)


def test_actions_are_applied_sequentially() -> None:
    source = {"value": "first"}
    overlay = overlay_document(
        guarded_action("$.value", ["first"], update="second"),
        guarded_action("$.value", ["second"], update="third"),
    )

    assert apply_overlay(source, overlay) == {"value": "third"}
    assert source == {"value": "first"}


def test_update_merges_objects_appends_arrays_and_copy_is_independent() -> None:
    source = {
        "template": {"nested": {"left": 1}, "items": [1]},
        "destination": {"nested": {"existing": 2}, "items": [0]},
    }
    overlay = overlay_document(
        guarded_action(
            "$.template",
            [source["template"]],
            update={"nested": {"right": 3}, "items": [2]},
        ),
        guarded_action(
            "$.destination",
            [source["destination"]],
            copy="$.template",
        ),
    )

    effective = apply_overlay(source, overlay)

    assert effective == {
        "template": {"nested": {"left": 1, "right": 3}, "items": [1, 2]},
        "destination": {
            "nested": {"existing": 2, "left": 1, "right": 3},
            "items": [0, 1, 2],
        },
    }
    effective["destination"]["nested"]["left"] = 99
    assert effective["template"]["nested"]["left"] == 1
    assert source["destination"] == {"nested": {"existing": 2}, "items": [0]}


def test_remove_handles_multiple_array_indices_and_object_members() -> None:
    source = {"items": ["first", "middle", "last"], "metadata": {"keep": 1, "drop": 2}}
    overlay = overlay_document(
        guarded_action("$.items[0,2]", ["first", "last"], remove=True),
        guarded_action("$.metadata.drop", [2], remove=True),
    )

    assert apply_overlay(source, overlay) == {"items": ["middle"], "metadata": {"keep": 1}}
    assert source == {
        "items": ["first", "middle", "last"],
        "metadata": {"keep": 1, "drop": 2},
    }


def test_root_update_is_visible_to_later_actions() -> None:
    source = {"value": "first"}
    overlay = overlay_document(
        guarded_action("$", [source], update={"added": "second"}),
        guarded_action("$.added", ["second"], update="third"),
    )

    assert apply_overlay(source, overlay) == {"value": "first", "added": "third"}
    assert source == {"value": "first"}


def test_overlay_files_apply_in_order_without_mutating_source(tmp_path: Path) -> None:
    source = {"value": "first"}
    first = tmp_path / "first.overlay.yaml"
    second = tmp_path / "second.overlay.yaml"
    first.write_text(
        yaml.safe_dump(
            overlay_document(guarded_action("$.value", ["first"], update="second")),
            sort_keys=False,
        ),
        encoding="utf-8",
    )
    second.write_text(
        yaml.safe_dump(
            overlay_document(guarded_action("$.value", ["second"], update="third")),
            sort_keys=False,
        ),
        encoding="utf-8",
    )

    assert apply_overlay_files(source, [first, second]) == {"value": "third"}
    assert source == {"value": "first"}


@pytest.mark.parametrize(
    ("overlay", "message"),
    [
        ([], "Overlay must be an object"),
        ({}, "Only Overlay 1.1.0 is supported"),
        (
            {"overlay": "1.0.0", "info": {"title": "x", "version": "1"}, "actions": [{}]},
            "Only Overlay 1.1.0 is supported",
        ),
        (
            {"overlay": "1.1.0", "info": {"title": "x"}, "actions": [{}]},
            "Overlay info.title and info.version must be non-empty strings",
        ),
        (
            {"overlay": "1.1.0", "info": {"title": "x", "version": "1"}, "actions": []},
            "Overlay actions must be a non-empty list",
        ),
    ],
)
def test_overlay_schema_is_validated(overlay: Any, message: str) -> None:
    with pytest.raises(ValidationError, match=message):
        apply_overlay(source_document(), overlay)


@pytest.mark.parametrize(
    ("action", "message"),
    [
        ("not-an-object", "Overlay action must be an object"),
        ({}, "Overlay action.target must be a JSONPath string"),
        (
            {"target": "not-jsonpath", "x-iiko-sdk-guard": {}},
            "Invalid overlay target JSONPath",
        ),
        (
            {"target": "$.openapi", "update": "3.1.0"},
            "Every overlay action requires x-iiko-sdk-guard",
        ),
        (
            {
                "target": "$.openapi",
                "update": "3.1.0",
                "x-iiko-sdk-guard": {"issue": [], "expected-matches": 1},
            },
            "Overlay guard.issue must be a non-empty string",
        ),
        (
            {
                "target": "$.openapi",
                "update": "3.1.0",
                "x-iiko-sdk-guard": {"issue": "bad-count", "expected-matches": True},
            },
            "Overlay guard.expected-matches must be a non-negative integer",
        ),
        (
            {
                "target": "$.openapi",
                "update": "3.1.0",
                "x-iiko-sdk-guard": {
                    "issue": "bad-hash",
                    "expected-matches": 1,
                    "expected-sha256": "not-a-sha256",
                },
            },
            "Overlay guard.expected-sha256 must be a lowercase SHA-256 digest",
        ),
    ],
)
def test_actions_and_guards_are_validated(action: Any, message: str) -> None:
    with pytest.raises(ValidationError, match=message):
        apply_overlay(source_document(), overlay_document(action))


@pytest.mark.parametrize(
    ("operation", "message"),
    [
        ({}, "Overlay action requires exactly one of update, copy, or remove"),
        (
            {"update": "new", "remove": True},
            "Overlay action requires exactly one of update, copy, or remove",
        ),
        ({"remove": False}, "Overlay action.remove must be true"),
        ({"copy": 3}, "Overlay action.copy must be a JSONPath string"),
    ],
)
def test_action_operation_is_validated(operation: dict[str, Any], message: str) -> None:
    action = guarded_action("$.openapi", ["3.0.1"], **operation)

    with pytest.raises(ValidationError, match=message):
        apply_overlay(source_document(), overlay_document(action))


def test_copy_requires_exactly_one_source() -> None:
    source = {"values": [1, 2], "destination": 0}
    overlay = overlay_document(
        guarded_action("$.destination", [0], copy="$.values[*]")
    )

    with pytest.raises(ValidationError, match="Overlay copy must select exactly one source node"):
        apply_overlay(source, overlay)


def test_incompatible_update_types_are_rejected() -> None:
    source = {"value": {"nested": True}}
    overlay = overlay_document(guarded_action("$.value", [source["value"]], update=[]))

    with pytest.raises(ValidationError, match="Overlay update types are incompatible"):
        apply_overlay(source, overlay)


def test_document_root_cannot_be_removed() -> None:
    source = {"value": 1}
    overlay = overlay_document(guarded_action("$", [source], remove=True))

    with pytest.raises(ValidationError, match="Overlay cannot remove the document root"):
        apply_overlay(source, overlay)


def test_overlay_file_must_contain_an_object(tmp_path: Path) -> None:
    path = tmp_path / "invalid.overlay.yaml"
    path.write_text("- not-an-object\n", encoding="utf-8")

    with pytest.raises(ValidationError, match="Overlay is not an object"):
        apply_overlay_files(source_document(), [path])
