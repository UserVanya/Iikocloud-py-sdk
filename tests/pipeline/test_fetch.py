from __future__ import annotations

import hashlib
import json
import urllib.request
from dataclasses import dataclass, field
from email.message import Message
from pathlib import Path
from types import TracebackType

import pytest

from tools.openapi_pipeline.errors import ValidationError
from tools.openapi_pipeline.fetch import fetch_candidate

VALID_OPENAPI = b'{"openapi":"3.0.1","info":{},"paths":{}}\n'


@dataclass
class FakeResponse:
    body: bytes
    status: int = 200
    headers: Message = field(default_factory=Message)
    read_sizes: list[int] = field(default_factory=list)
    entered: bool = False
    exited: bool = False

    def __enter__(self) -> FakeResponse:
        self.entered = True
        return self

    def __exit__(
        self,
        _exc_type: type[BaseException] | None,
        _exc: BaseException | None,
        _traceback: TracebackType | None,
    ) -> None:
        self.exited = True

    def read(self, size: int = -1) -> bytes:
        self.read_sizes.append(size)
        return self.body if size < 0 else self.body[:size]


@dataclass
class FakeUrlOpen:
    response: FakeResponse
    request: urllib.request.Request | None = None
    timeout: float | None = None

    def __call__(
        self,
        request: urllib.request.Request,
        *,
        timeout: float,
    ) -> FakeResponse:
        self.request = request
        self.timeout = timeout
        return self.response


def test_fetch_candidate_preserves_exact_bytes(tmp_path: Path) -> None:
    body = VALID_OPENAPI
    destination = tmp_path / "candidate.json"
    result = fetch_candidate(
        "https://example.invalid/schema",
        destination,
        opener=lambda _url, _timeout: body,
    )
    assert result.path.read_bytes() == body
    assert result.body_sha256 == hashlib.sha256(body).hexdigest()
    assert result.changed is True

    unchanged = fetch_candidate(
        "https://example.invalid/schema",
        destination,
        opener=lambda _url, _timeout: body,
    )

    assert unchanged.body_sha256 == result.body_sha256
    assert unchanged.changed is False


def test_default_reader_rejects_non_200_without_mutating_destination(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    response = FakeResponse(VALID_OPENAPI, status=206)
    urlopen = FakeUrlOpen(response)
    monkeypatch.setattr(urllib.request, "urlopen", urlopen)
    destination = tmp_path / "candidate.json"
    original = b"existing candidate\n"
    destination.write_bytes(original)

    with pytest.raises(ValidationError, match="HTTP status 206"):
        fetch_candidate("https://example.invalid/schema", destination)

    assert destination.read_bytes() == original
    assert response.read_sizes == []
    assert response.entered is True
    assert response.exited is True


def test_default_reader_rejects_oversized_content_length_before_body_read(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    max_bytes = len(VALID_OPENAPI)
    headers = Message()
    headers["Content-Length"] = str(max_bytes + 1)
    response = FakeResponse(VALID_OPENAPI, headers=headers)
    urlopen = FakeUrlOpen(response)
    monkeypatch.setattr(urllib.request, "urlopen", urlopen)
    destination = tmp_path / "candidate.json"
    original = b"existing candidate\n"
    destination.write_bytes(original)

    with pytest.raises(ValidationError, match=f"maximum size of {max_bytes} bytes"):
        fetch_candidate(
            "https://example.invalid/schema",
            destination,
            max_bytes=max_bytes,
        )

    assert destination.read_bytes() == original
    assert response.read_sizes == []
    assert response.entered is True
    assert response.exited is True


def test_default_reader_rejects_malformed_content_length_without_mutation(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    headers = Message()
    headers["Content-Length"] = "not-a-number"
    response = FakeResponse(VALID_OPENAPI, headers=headers)
    urlopen = FakeUrlOpen(response)
    monkeypatch.setattr(urllib.request, "urlopen", urlopen)
    destination = tmp_path / "candidate.json"
    original = b"existing candidate\n"
    destination.write_bytes(original)

    with pytest.raises(ValidationError, match="Content-Length"):
        fetch_candidate("https://example.invalid/schema", destination)

    assert destination.read_bytes() == original
    assert response.read_sizes == []
    assert response.entered is True
    assert response.exited is True


def test_default_reader_bounds_unknown_length_and_rejects_oversized_body(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    max_bytes = len(VALID_OPENAPI)
    response = FakeResponse(VALID_OPENAPI + b" ")
    urlopen = FakeUrlOpen(response)
    monkeypatch.setattr(urllib.request, "urlopen", urlopen)
    destination = tmp_path / "candidate.json"
    original = b"existing candidate\n"
    destination.write_bytes(original)

    with pytest.raises(ValidationError, match=f"maximum size of {max_bytes} bytes"):
        fetch_candidate(
            "https://example.invalid/schema",
            destination,
            max_bytes=max_bytes,
        )

    assert destination.read_bytes() == original
    assert response.read_sizes == [max_bytes + 1]
    assert response.entered is True
    assert response.exited is True


def test_default_reader_forwards_url_and_timeout(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    response = FakeResponse(VALID_OPENAPI)
    urlopen = FakeUrlOpen(response)
    monkeypatch.setattr(urllib.request, "urlopen", urlopen)
    destination = tmp_path / "candidate.json"
    max_bytes = len(VALID_OPENAPI)

    fetch_candidate(
        "https://example.invalid/schema",
        destination,
        timeout=7.25,
        max_bytes=max_bytes,
    )

    assert urlopen.request is not None
    assert urlopen.request.full_url == "https://example.invalid/schema"
    assert urlopen.timeout == 7.25
    assert response.read_sizes == [max_bytes + 1]
    assert response.entered is True
    assert response.exited is True
    assert destination.read_bytes() == VALID_OPENAPI


def test_fetch_candidate_rejects_non_openapi_json(tmp_path: Path) -> None:
    with pytest.raises(ValidationError, match="OpenAPI root fields"):
        fetch_candidate(
            "https://example.invalid/schema",
            tmp_path / "candidate.json",
            opener=lambda _url, _timeout: b'{"message":"error"}',
        )


@pytest.mark.parametrize(
    ("field_name", "invalid_value", "expected_type"),
    [
        ("openapi", 3, "string"),
        ("info", [], "object"),
        ("paths", [], "object"),
        ("components", [], "object"),
    ],
)
def test_fetch_candidate_rejects_wrong_openapi_root_types_without_mutation(
    tmp_path: Path,
    field_name: str,
    invalid_value: object,
    expected_type: str,
) -> None:
    document: dict[str, object] = {
        "openapi": "3.0.1",
        "info": {},
        "paths": {},
        "components": {},
    }
    document[field_name] = invalid_value
    destination = tmp_path / "candidate.json"
    original = b"existing candidate\n"
    destination.write_bytes(original)

    with pytest.raises(
        ValidationError,
        match=rf"'{field_name}'.*{expected_type}",
    ):
        fetch_candidate(
            "https://example.invalid/schema",
            destination,
            opener=lambda _url, _timeout: json.dumps(document).encode(),
        )

    assert destination.read_bytes() == original


def test_fetch_candidate_rejects_non_object_path_item_without_mutation(tmp_path: Path) -> None:
    document = {
        "openapi": "3.0.1",
        "info": {},
        "paths": {"/x": None},
    }
    destination = tmp_path / "candidate.json"
    original = b"existing candidate\n"
    destination.write_bytes(original)

    with pytest.raises(ValidationError, match=r"path item '/x'.*object"):
        fetch_candidate(
            "https://example.invalid/schema",
            destination,
            opener=lambda _url, _timeout: json.dumps(document).encode(),
        )

    assert destination.read_bytes() == original


def test_fetch_candidate_rejects_non_object_schemas_without_mutation(tmp_path: Path) -> None:
    document = {
        "openapi": "3.0.1",
        "info": {},
        "paths": {},
        "components": {"schemas": None},
    }
    destination = tmp_path / "candidate.json"
    original = b"existing candidate\n"
    destination.write_bytes(original)

    with pytest.raises(ValidationError, match=r"'components.schemas'.*object"):
        fetch_candidate(
            "https://example.invalid/schema",
            destination,
            opener=lambda _url, _timeout: json.dumps(document).encode(),
        )

    assert destination.read_bytes() == original


def test_fetch_candidate_rejects_invalid_utf8_without_mutation(tmp_path: Path) -> None:
    destination = tmp_path / "candidate.json"
    original = b"existing candidate\n"
    destination.write_bytes(original)

    with pytest.raises(ValidationError, match="UTF-8 JSON"):
        fetch_candidate(
            "https://example.invalid/schema",
            destination,
            opener=lambda _url, _timeout: b"\xff",
        )

    assert destination.read_bytes() == original


def test_fetch_candidate_rejects_utf16_json_without_mutation(tmp_path: Path) -> None:
    destination = tmp_path / "candidate.json"
    original = b"existing candidate\n"
    destination.write_bytes(original)
    utf16_body = VALID_OPENAPI.decode("utf-8").encode("utf-16")

    with pytest.raises(ValidationError, match="UTF-8 JSON"):
        fetch_candidate(
            "https://example.invalid/schema",
            destination,
            opener=lambda _url, _timeout: utf16_body,
        )

    assert destination.read_bytes() == original
