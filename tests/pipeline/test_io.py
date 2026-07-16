from tools.openapi_pipeline.io import canonical_json_bytes


def test_canonical_json_bytes_sorts_keys_and_emits_utf8_newline() -> None:
    value = {"zulu": 1, "alpha": "Привет"}

    result = canonical_json_bytes(value)

    assert result == '{"alpha":"Привет","zulu":1}\n'.encode()
