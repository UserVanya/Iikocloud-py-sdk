import copy
import subprocess
import sys
import unicodedata
from dataclasses import dataclass

import pytest

from tools.openapi_pipeline.capture import (
    ARRAY_ITEM,
    OBJECT_VALUE,
    HintPath,
    PathValues,
    Sanitizer,
)
from tools.openapi_pipeline.errors import SafetyError


def test_sanitizer_removes_secrets_pii_and_stabilizes_uuid_links() -> None:
    sanitizer = Sanitizer(known_secrets=("exact-api-login", "exact-token"))
    value = {
        "authToken": "exact-token",
        "email": "person@example.com",
        "phone": "+79991234567",
        "organizationId": "11111111-1111-4111-8111-111111111111",
        "items": [
            {
                "id": "11111111-1111-4111-8111-111111111111",
                "type": "DISH",
            }
        ],
        "comment": "customer free text",
    }

    sanitized = sanitizer.sanitize(value, enum_keys={"type"})

    assert sanitized["authToken"] == "<redacted:secret>"
    assert sanitized["email"] == "<redacted:email>"
    assert sanitized["phone"] == "<redacted:phone>"
    assert sanitized["organizationId"] == sanitized["items"][0]["id"]
    assert sanitized["items"][0]["type"] == "DISH"
    assert sanitized["comment"] == "<redacted:string>"


def test_sanitizer_preserves_only_explicitly_allowed_schema_strings() -> None:
    sanitizer = Sanitizer()

    sanitized = sanitizer.sanitize(
        {
            "valid": {"type": "DISH"},
            "wrong": {"type": "CUSTOMER NAME"},
            "sameNameElsewhere": {"type": "OTHER"},
        },
        path_values={
            ("valid", "type"): frozenset({"DISH"}),
            ("sameNameElsewhere", "type"): frozenset({"OTHER"}),
        },
    )

    assert sanitized["valid"]["type"] == "DISH"
    assert sanitized["wrong"]["type"] == "<redacted:string>"
    assert sanitized["sameNameElsewhere"]["type"] == "OTHER"


@pytest.mark.parametrize(
    "value",
    [
        b"binary",
        ("tuple",),
        {1: "not-a-string-key"},
        {"value": float("nan")},
        {"value": float("inf")},
    ],
)
def test_sanitizer_rejects_non_strict_json_values(value: object) -> None:
    with pytest.raises(SafetyError):
        Sanitizer().sanitize(value)


def test_sanitizer_rejects_custom_values_cycles_and_depth_bombs() -> None:
    @dataclass
    class CustomValue:
        value: str

    with pytest.raises(SafetyError, match="strict JSON"):
        Sanitizer().sanitize({"value": CustomValue("private")})

    cycle: list[object] = []
    cycle.append(cycle)
    with pytest.raises(SafetyError, match="cycle"):
        Sanitizer().sanitize(cycle)

    depth_bomb: object = None
    for _ in range(66):
        depth_bomb = [depth_bomb]
    with pytest.raises(SafetyError, match="nesting depth"):
        Sanitizer().sanitize(depth_bomb)


def test_sanitizer_never_mutates_input_and_allows_shared_noncyclic_values() -> None:
    shared = {"name": "private"}
    source = {"left": shared, "right": shared}
    before = copy.deepcopy(source)

    result = Sanitizer().sanitize(source)

    assert source == before
    assert result == {
        "left": {"name": "<redacted:string>"},
        "right": {"name": "<redacted:string>"},
    }


@pytest.mark.parametrize(
    ("value", "marker"),
    [
        ("prefix-known-secret-suffix", "<redacted:secret>"),
        ("Bearer opaque-credential", "<redacted:secret>"),
        ("aaaaaaaa.bbbbbbbb.cccccccc", "<redacted:secret>"),
        ("contact person@example.com today", "<redacted:email>"),
        ("call +7 (999) 123-45-67 today", "<redacted:phone>"),
    ],
)
def test_sanitizer_redacts_sensitive_substrings_regardless_of_key(value: str, marker: str) -> None:
    result = Sanitizer(known_secrets=("known-secret",)).sanitize(
        {"schemaEnum": value},
        enum_keys={"schemaEnum"},
    )

    assert result["schemaEnum"] == marker


def test_uuid_links_are_stable_across_separate_sanitize_calls() -> None:
    sanitizer = Sanitizer()
    source = "11111111-1111-4111-8111-111111111111"

    request = sanitizer.sanitize({"id": source})
    response = sanitizer.sanitize({"organizationId": source})

    assert request["id"] == response["organizationId"]
    assert request["id"] == "00000000-0000-4000-8000-000000000001"


def test_first_pass_sanitizer_never_trusts_alias_shaped_raw_uuid() -> None:
    alias_shaped_raw = "00000000-0000-4000-8000-000000000042"

    first_pass = Sanitizer().sanitize({"id": alias_shaped_raw})
    validation_pass = Sanitizer.for_fixed_point_validation().sanitize({"id": alias_shaped_raw})

    assert first_pass["id"] == "00000000-0000-4000-8000-000000000001"
    assert first_pass["id"] != alias_shaped_raw
    assert validation_pass["id"] == alias_shaped_raw


def test_sanitizer_detects_unicode_normalized_secret_substrings() -> None:
    known = "Caf\u00e9-secret"
    equivalent = unicodedata.normalize("NFD", known)

    result = Sanitizer(known_secrets=(known,)).sanitize(
        {"type": f"prefix-{equivalent}-suffix"},
        enum_keys={"type"},
    )

    assert result["type"] == "<redacted:secret>"


@pytest.mark.parametrize(
    "sensitive_key",
    [
        "prefix-known-secret-suffix",
        "11111111-1111-4111-8111-111111111111",
        "aaaaaaaa-aaaa-0000-0000-aaaaaaaaaaaa",
        "person@example.com",
        "+79991234567",
        "aaaaaaaa.bbbbbbbb.cccccccc",
        "Bearer opaque-credential",
    ],
)
def test_first_pass_sanitizer_rejects_sensitive_text_in_object_keys(
    sensitive_key: str,
) -> None:
    with pytest.raises(SafetyError, match="object key|sensitive") as caught:
        Sanitizer(known_secrets=("known-secret",)).sanitize({sensitive_key: "value"})

    assert sensitive_key not in str(caught.value)


def test_allowed_values_preserve_exact_minimum_wildcard_and_tie_union_semantics() -> None:
    path: HintPath = ("root", "tenant", ARRAY_ITEM, "type")
    exact: PathValues = {
        path: frozenset({"EXACT"}),
        ("root", OBJECT_VALUE, ARRAY_ITEM, "type"): frozenset({"ONE"}),
    }
    tied: PathValues = {
        (OBJECT_VALUE, "tenant", ARRAY_ITEM, "type"): frozenset({"LEFT"}),
        ("root", OBJECT_VALUE, ARRAY_ITEM, "type"): frozenset({"RIGHT"}),
        (OBJECT_VALUE, OBJECT_VALUE, ARRAY_ITEM, "type"): frozenset({"BROAD"}),
        ("root", "tenant", OBJECT_VALUE, "type"): frozenset({"NOT_ARRAY"}),
    }

    assert Sanitizer._allowed_values(path, exact) == frozenset({"EXACT"})
    assert Sanitizer._allowed_values(path, tied) == frozenset({"LEFT", "RIGHT"})


def test_allowed_values_depth_64_matching_is_bounded() -> None:
    script = """
from tools.openapi_pipeline.capture import OBJECT_VALUE, Sanitizer
path = tuple(f"key-{index}" for index in range(64))
hints = {tuple(OBJECT_VALUE for _ in path): frozenset({"SAFE"})}
assert Sanitizer._allowed_values(path, hints) == frozenset({"SAFE"})
"""
    try:
        completed = subprocess.run(
            [sys.executable, "-c", script],
            cwd=".",
            check=False,
            capture_output=True,
            text=True,
            timeout=5,
        )
    except subprocess.TimeoutExpired:
        pytest.fail("depth-64 wildcard matching exceeded the generous five-second bound")

    assert completed.returncode == 0, completed.stderr
