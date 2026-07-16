from __future__ import annotations

import json
import urllib.request
from collections.abc import Callable
from dataclasses import dataclass
from pathlib import Path

from .errors import ValidationError
from .io import sha256_bytes, write_bytes_atomic

OpenBytes = Callable[[str, float], bytes]


@dataclass(frozen=True)
class FetchResult:
    body_sha256: str
    path: Path
    changed: bool


def _urlopen(url: str, timeout: float) -> bytes:
    request = urllib.request.Request(url, headers={"Accept": "application/json"})
    with urllib.request.urlopen(request, timeout=timeout) as response:
        return response.read()


def fetch_candidate(
    url: str,
    destination: Path,
    *,
    timeout: float = 30.0,
    opener: OpenBytes = _urlopen,
) -> FetchResult:
    body = opener(url, timeout)
    try:
        document = json.loads(body)
    except json.JSONDecodeError as exc:
        raise ValidationError("Upstream response is not JSON") from exc
    if not isinstance(document, dict) or not {"openapi", "info", "paths"} <= document.keys():
        raise ValidationError("Upstream response does not contain required OpenAPI root fields")
    digest = sha256_bytes(body)
    changed = not destination.exists() or sha256_bytes(destination.read_bytes()) != digest
    write_bytes_atomic(destination, body)
    return FetchResult(digest, destination, changed)
