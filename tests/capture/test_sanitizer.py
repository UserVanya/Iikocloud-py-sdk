import copy
import unicodedata
from dataclasses import dataclass

import pytest

from tools.openapi_pipeline.capture import Sanitizer
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
        enum_keys={"type"},
        enum_values={"type": frozenset({"DISH", "OTHER"})},
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


def test_sanitizer_detects_unicode_normalized_secret_substrings() -> None:
    known = "Caf\u00e9-secret"
    equivalent = unicodedata.normalize("NFD", known)

    result = Sanitizer(known_secrets=(known,)).sanitize(
        {"type": f"prefix-{equivalent}-suffix"},
        enum_keys={"type"},
    )

    assert result["type"] == "<redacted:secret>"
