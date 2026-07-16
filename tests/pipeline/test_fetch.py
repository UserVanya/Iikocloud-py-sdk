from pathlib import Path

import pytest

from tools.openapi_pipeline.errors import ValidationError
from tools.openapi_pipeline.fetch import fetch_candidate


def test_fetch_candidate_preserves_exact_bytes(tmp_path: Path) -> None:
    body = b'{"openapi":"3.0.1","info":{},"paths":{}}\n'
    result = fetch_candidate(
        "https://example.invalid/schema",
        tmp_path / "candidate.json",
        opener=lambda _url, _timeout: body,
    )
    assert result.path.read_bytes() == body
    assert len(result.body_sha256) == 64


def test_fetch_candidate_rejects_non_openapi_json(tmp_path: Path) -> None:
    with pytest.raises(ValidationError, match="OpenAPI root fields"):
        fetch_candidate(
            "https://example.invalid/schema",
            tmp_path / "candidate.json",
            opener=lambda _url, _timeout: b'{"message":"error"}',
        )
