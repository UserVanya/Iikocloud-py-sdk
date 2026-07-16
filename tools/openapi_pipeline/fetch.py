from __future__ import annotations

import json
import urllib.request
from collections.abc import Callable
from dataclasses import dataclass
from pathlib import Path

from .errors import ValidationError
from .io import sha256_bytes, write_bytes_atomic

DEFAULT_MAX_RESPONSE_BYTES = 32 * 1024 * 1024

OpenBytes = Callable[[str, float], bytes]


@dataclass(frozen=True)
class FetchResult:
    body_sha256: str
    path: Path
    changed: bool


def _raise_oversized_response(max_bytes: int) -> None:
    raise ValidationError(f"Upstream response exceeds maximum size of {max_bytes} bytes")


def _urlopen(url: str, timeout: float, *, max_bytes: int = DEFAULT_MAX_RESPONSE_BYTES) -> bytes:
    request = urllib.request.Request(url, headers={"Accept": "application/json"})
    with urllib.request.urlopen(request, timeout=timeout) as response:
        if response.status != 200:
            raise ValidationError(f"Upstream returned HTTP status {response.status}; expected 200")
        content_length = response.headers.get("Content-Length")
        if content_length is not None:
            try:
                declared_length = int(content_length)
            except ValueError as exc:
                raise ValidationError(
                    "Upstream returned an invalid Content-Length header"
                ) from exc
            if declared_length < 0:
                raise ValidationError("Upstream returned an invalid Content-Length header")
            if declared_length > max_bytes:
                _raise_oversized_response(max_bytes)
        body = response.read(max_bytes + 1)
        if len(body) > max_bytes:
            _raise_oversized_response(max_bytes)
        return body


def fetch_candidate(
    url: str,
    destination: Path,
    *,
    timeout: float = 30.0,
    max_bytes: int = DEFAULT_MAX_RESPONSE_BYTES,
    opener: OpenBytes | None = None,
) -> FetchResult:
    body = (
        _urlopen(url, timeout, max_bytes=max_bytes)
        if opener is None
        else opener(url, timeout)
    )
    if len(body) > max_bytes:
        _raise_oversized_response(max_bytes)
    try:
        text = body.decode("utf-8")
        document = json.loads(text)
    except UnicodeDecodeError as exc:
        raise ValidationError("Upstream response is not valid UTF-8 JSON") from exc
    except json.JSONDecodeError as exc:
        raise ValidationError("Upstream response is not valid JSON") from exc
    if not isinstance(document, dict) or not {"openapi", "info", "paths"} <= document.keys():
        raise ValidationError("Upstream response does not contain required OpenAPI root fields")
    if not isinstance(document["openapi"], str):
        raise ValidationError("Upstream OpenAPI root field 'openapi' must be a string")
    if not isinstance(document["info"], dict):
        raise ValidationError("Upstream OpenAPI root field 'info' must be an object")
    if not isinstance(document["paths"], dict):
        raise ValidationError("Upstream OpenAPI root field 'paths' must be an object")
    if "components" in document and not isinstance(document["components"], dict):
        raise ValidationError("Upstream OpenAPI root field 'components' must be an object")
    for path, path_item in document["paths"].items():
        if not isinstance(path_item, dict):
            raise ValidationError(f"Upstream OpenAPI path item '{path}' must be an object")
    components = document.get("components", {})
    if "schemas" in components and not isinstance(components["schemas"], dict):
        raise ValidationError("Upstream OpenAPI field 'components.schemas' must be an object")
    digest = sha256_bytes(body)
    changed = not destination.exists() or sha256_bytes(destination.read_bytes()) != digest
    write_bytes_atomic(destination, body)
    return FetchResult(digest, destination, changed)
