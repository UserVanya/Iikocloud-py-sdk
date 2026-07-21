from __future__ import annotations

import os
import re
import stat
from collections.abc import Mapping
from pathlib import Path

import yaml

from ..errors import SafetyError

_SAFE_IDENTIFIER = re.compile(r"[A-Za-z0-9][A-Za-z0-9_.:-]{0,127}\Z")
_UUID = re.compile(
    r"\b[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}\b",
    re.IGNORECASE,
)
_EMAIL = re.compile(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", re.IGNORECASE)
_BEARER = re.compile(r"\bbearer\b", re.IGNORECASE)
_JWT = re.compile(r"\b[A-Za-z0-9_-]{8,}\.[A-Za-z0-9_-]{8,}\.[A-Za-z0-9_-]{8,}\b")
_SECRET_ASSIGNMENT = re.compile(
    r"\b(?:api[ _-]?key|access[ _-]?token|token)\s*[:=]\s*\S+",
    re.IGNORECASE,
)


class _UniqueKeySafeLoader(yaml.SafeLoader):
    pass


def _construct_unique_mapping(
    loader: _UniqueKeySafeLoader,
    node: yaml.nodes.MappingNode,
    deep: bool = False,
) -> dict[object, object]:
    result: dict[object, object] = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        try:
            duplicate = key in result
        except TypeError as error:
            raise yaml.constructor.ConstructorError(
                "while constructing a mapping",
                node.start_mark,
                "found an unhashable key",
                key_node.start_mark,
            ) from error
        if duplicate:
            raise yaml.constructor.ConstructorError(
                "while constructing a mapping",
                node.start_mark,
                f"found duplicate key {key!r}",
                key_node.start_mark,
            )
        result[key] = loader.construct_object(value_node, deep=deep)
    return result


_UniqueKeySafeLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
    _construct_unique_mapping,
)


def _read_bounded_regular_file(path: Path, *, label: str, maximum_bytes: int) -> bytes:
    flags = (
        os.O_RDONLY
        | getattr(os, "O_CLOEXEC", 0)
        | getattr(os, "O_NOFOLLOW", 0)
        | getattr(os, "O_NONBLOCK", 0)
    )
    try:
        descriptor = os.open(path, flags)
    except OSError as error:
        raise SafetyError(f"Cannot read {label}: {path}") from error
    try:
        metadata = os.fstat(descriptor)
        if not stat.S_ISREG(metadata.st_mode):
            raise SafetyError(f"{label.capitalize()} must be a regular file")
        chunks: list[bytes] = []
        remaining = maximum_bytes + 1
        while remaining > 0:
            chunk = os.read(descriptor, min(65536, remaining))
            if not chunk:
                break
            chunks.append(chunk)
            remaining -= len(chunk)
    except OSError as error:
        raise SafetyError(f"Cannot read {label}: {path}") from error
    finally:
        os.close(descriptor)
    body = b"".join(chunks)
    if len(body) > maximum_bytes:
        raise SafetyError(f"{label.capitalize()} exceeds its reviewed size limit")
    return body


def load_yaml_mapping(
    path: Path,
    *,
    label: str,
    maximum_bytes: int,
) -> Mapping[object, object]:
    body = _read_bounded_regular_file(path, label=label, maximum_bytes=maximum_bytes)
    try:
        text = body.decode("utf-8")
    except UnicodeDecodeError as error:
        raise SafetyError(f"{label.capitalize()} is not valid UTF-8: {path}") from error
    try:
        if any(
            isinstance(token, (yaml.tokens.AnchorToken, yaml.tokens.AliasToken))
            for token in yaml.scan(text, Loader=_UniqueKeySafeLoader)
        ):
            raise SafetyError(f"{label.capitalize()} must not contain YAML anchors or aliases")
        value = yaml.load(text, Loader=_UniqueKeySafeLoader)
    except yaml.YAMLError as error:
        detail = "duplicate key" if "duplicate key" in str(error) else "invalid YAML"
        raise SafetyError(f"{label.capitalize()} contains {detail}: {path}") from error
    if not isinstance(value, Mapping):
        raise SafetyError(f"{label.capitalize()} root must be an object")
    return value


def exact_keys(
    value: Mapping[object, object],
    expected: set[str] | frozenset[str],
    *,
    label: str,
) -> None:
    keys = set(value)
    if keys != expected or any(not isinstance(key, str) for key in keys):
        wanted = ", ".join(sorted(expected))
        raise SafetyError(f"{label} keys must be exactly: {wanted}")


def safe_identifier(value: object, *, label: str) -> str:
    if not isinstance(value, str) or _SAFE_IDENTIFIER.fullmatch(value) is None:
        raise SafetyError(f"{label} must be a safe ASCII string of 1 to 128 characters")
    return value


def safe_source(value: object, *, label: str) -> str:
    if (
        not isinstance(value, str)
        or not 1 <= len(value) <= 256
        or value != value.strip()
        or not value.isprintable()
    ):
        raise SafetyError(
            f"{label} must be a trimmed printable string of 1 to 256 characters"
        )
    return value


def safe_review_reason(value: object, *, label: str) -> str:
    reason = safe_source(value, label=label)
    if any(
        pattern.search(reason) is not None
        for pattern in (_UUID, _EMAIL, _BEARER, _JWT, _SECRET_ASSIGNMENT)
    ):
        raise SafetyError(f"{label} must not contain identifiers or secret-like values")
    return reason
