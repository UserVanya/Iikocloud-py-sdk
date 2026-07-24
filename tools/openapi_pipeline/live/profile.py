from __future__ import annotations

import hashlib
import os
import re
import stat
from dataclasses import dataclass, field
from io import StringIO
from pathlib import Path
from typing import Any
from urllib.parse import urlsplit

from dotenv import dotenv_values

try:
    import tomllib
except ModuleNotFoundError:  # pragma: no cover - Python 3.10 compatibility
    import tomli as tomllib  # type: ignore[import-not-found,no-redef]

from ..errors import SafetyError
from ..io import canonical_json_bytes
from .lock import validate_private_regular_file
from .read_case import ReadCapability

_ENV_NAME = re.compile(r"[A-Z_][A-Z0-9_]{0,127}\Z")
_PROFILE_NAME = re.compile(r"[a-z0-9][a-z0-9-]{0,63}\Z")
_DNS_LABEL = re.compile(r"[A-Za-z0-9](?:[A-Za-z0-9-]{0,61}[A-Za-z0-9])?\Z")
_MAX_PROFILE_BYTES = 64 * 1024
_MAX_ENV_BYTES = 1024 * 1024
_REQUIRED_FIELDS = {
    "name",
    "base_url",
    "api_login_env",
    "organization_id_env",
    "allow_write",
    "allowed_organization_ids",
}
_OPTIONAL_FIELDS = {
    "app_id_env",
    "auth_version",
    "client_secret_env",
    "disabled_read_capabilities",
    "external_menu_id_env",
    "terminal_group_id_env",
    "write_product_id_env",
}
_AUTH_VERSIONS = frozenset({"v1", "v2"})
_INVALID_DISABLED_CAPABILITIES = (
    "disabled_read_capabilities must be a duplicate-free array of known "
    "capability strings"
)


@dataclass(frozen=True)
class ResolvedLiveProfile:
    name: str
    base_url: str
    api_login: str = field(repr=False)
    organization_id: str
    external_menu_id: str | None
    terminal_group_id: str | None
    write_product_id: str | None
    allow_write: bool
    allowed_organization_ids: tuple[str, ...]
    fingerprint: str
    disabled_read_capabilities: frozenset[ReadCapability] = frozenset()
    auth_version: str = "v1"
    app_id: str | None = field(repr=False, default=None)
    client_secret: str | None = field(repr=False, default=None)


@dataclass(frozen=True)
class ResolvedDiscoveryProfile:
    name: str
    base_url: str
    api_login: str = field(repr=False)
    fingerprint: str
    auth_version: str = "v1"
    app_id: str | None = field(repr=False, default=None)
    client_secret: str | None = field(repr=False, default=None)


def is_safe_profile_name(value: object) -> bool:
    return isinstance(value, str) and _PROFILE_NAME.fullmatch(value) is not None


def _private_text(path: Path, *, label: str, maximum: int) -> str:
    try:
        expected = validate_private_regular_file(path, label=label)
    except FileNotFoundError as error:
        raise SafetyError(f"{label} is missing: {path}") from error
    flags = os.O_RDONLY | os.O_CLOEXEC | getattr(os, "O_NOFOLLOW", 0)
    try:
        descriptor = os.open(path, flags)
    except OSError as error:
        raise SafetyError(f"Cannot open {label.lower()} safely: {path}") from error
    try:
        actual = os.fstat(descriptor)
        if not stat.S_ISREG(actual.st_mode):
            raise SafetyError(f"{label} is not a regular file: {path}")
        if (actual.st_dev, actual.st_ino) != (expected.st_dev, expected.st_ino):
            raise SafetyError(f"{label} changed while it was being opened")
        chunks: list[bytes] = []
        remaining = maximum + 1
        while remaining:
            chunk = os.read(descriptor, min(65536, remaining))
            if not chunk:
                break
            chunks.append(chunk)
            remaining -= len(chunk)
        body = b"".join(chunks)
    finally:
        os.close(descriptor)
    if len(body) > maximum:
        raise SafetyError(f"{label} is larger than {maximum} bytes")
    try:
        return body.decode("utf-8")
    except UnicodeDecodeError as error:
        raise SafetyError(f"{label} is not valid UTF-8") from error


def _strict_string(value: object, *, label: str, maximum: int = 512) -> str:
    if (
        not isinstance(value, str)
        or not value
        or len(value) > maximum
        or value != value.strip()
        or any(ord(character) < 32 or ord(character) == 127 for character in value)
    ):
        raise SafetyError(f"{label} must be a non-empty safe string")
    return value


def _env_name(value: object, *, label: str) -> str:
    if not isinstance(value, str) or _ENV_NAME.fullmatch(value) is None:
        raise SafetyError(f"{label} must be an uppercase environment variable name")
    return value


def _base_url(value: object) -> str:
    raw = _strict_string(value, label="base_url", maximum=2048)
    if "\\" in raw:
        raise SafetyError("Live base_url contains an unsafe character")
    try:
        parsed = urlsplit(raw)
        port = parsed.port
    except ValueError as error:
        raise SafetyError("Live base_url is invalid") from error
    hostname = parsed.hostname
    if (
        parsed.scheme != "https"
        or not parsed.netloc
        or hostname is None
        or parsed.username is not None
        or parsed.password is not None
        or port is not None
        or parsed.query
        or parsed.fragment
        or parsed.path not in {"", "/"}
    ):
        raise SafetyError("Live base_url must be a credential-free HTTPS origin")
    labels = hostname.split(".")
    if (
        hostname.lower() == "localhost"
        or len(labels) < 2
        or len(hostname) > 253
        or any(_DNS_LABEL.fullmatch(label) is None for label in labels)
    ):
        raise SafetyError("Live base_url hostname is unsafe")
    return f"https://{hostname.lower()}"


def _load_toml(path: Path) -> dict[str, Any]:
    text = _private_text(path, label="Live profile", maximum=_MAX_PROFILE_BYTES)
    try:
        value = tomllib.loads(text)
    except (tomllib.TOMLDecodeError, ValueError) as error:
        raise SafetyError("Live profile is not valid strict TOML") from error
    if not isinstance(value, dict):  # pragma: no cover - tomllib always returns dict
        raise SafetyError("Live profile root must be a table")
    keys = set(value)
    if not _REQUIRED_FIELDS.issubset(keys) or not keys.issubset(
        _REQUIRED_FIELDS | _OPTIONAL_FIELDS
    ):
        wanted = ", ".join(sorted(_REQUIRED_FIELDS | _OPTIONAL_FIELDS))
        raise SafetyError(f"Live profile fields must be the documented fields: {wanted}")
    if "write_product_id_env" in value and "terminal_group_id_env" not in value:
        raise SafetyError("Live profile write product requires a terminal group field")
    auth_version = value.get("auth_version", "v1")
    if type(auth_version) is not str or auth_version not in _AUTH_VERSIONS:
        raise SafetyError("Live profile auth_version must be 'v1' or 'v2'")
    has_app_credentials = "app_id_env" in value or "client_secret_env" in value
    if auth_version == "v2":
        if "app_id_env" not in value or "client_secret_env" not in value:
            raise SafetyError(
                "Live profile auth_version v2 requires app_id_env and client_secret_env"
            )
    elif has_app_credentials:
        raise SafetyError(
            "Live profile application credentials require auth_version = 'v2'"
        )
    return value


def _load_env_file(path: Path | None) -> dict[str, str | None]:
    if path is None:
        return {}
    text = _private_text(path, label="Environment file", maximum=_MAX_ENV_BYTES)
    try:
        values = dotenv_values(stream=StringIO(text), interpolate=False)
    except (OSError, ValueError) as error:
        raise SafetyError("Environment file cannot be parsed safely") from error
    result: dict[str, str | None] = {}
    for name, value in values.items():
        if not isinstance(name, str):
            raise SafetyError("Environment file contains an invalid variable name")
        result[name] = value
    return result


def _required_env(name: str, file_values: dict[str, str | None]) -> str:
    if name in os.environ:
        raw: object = os.environ[name]
    else:
        raw = file_values.get(name)
    try:
        return _strict_string(raw, label=f"Environment variable {name}", maximum=4096)
    except SafetyError as error:
        raise SafetyError(f"Required environment variable is missing or unsafe: {name}") from error


def _resolve_app_credentials(
    data: dict[str, Any],
    file_values: dict[str, str | None],
) -> tuple[str, str | None, str | None]:
    auth_version = data.get("auth_version", "v1")
    if auth_version != "v2":
        return "v1", None, None
    app_id_env = _env_name(data["app_id_env"], label="app_id_env")
    client_secret_env = _env_name(data["client_secret_env"], label="client_secret_env")
    return (
        "v2",
        _required_env(app_id_env, file_values),
        _required_env(client_secret_env, file_values),
    )


def _string_list(value: object, *, label: str) -> tuple[str, ...]:
    if not isinstance(value, list):
        raise SafetyError(f"{label} must be an array of strings")
    result = tuple(_strict_string(item, label=label) for item in value)
    if len(set(result)) != len(result):
        raise SafetyError(f"{label} must not contain duplicates")
    return result


def _disabled_read_capabilities(value: object) -> frozenset[ReadCapability]:
    if type(value) is not list:
        raise SafetyError(_INVALID_DISABLED_CAPABILITIES)
    known = {capability.value: capability for capability in ReadCapability}
    resolved: list[ReadCapability] = []
    invalid = False
    for item in value:
        capability = known.get(item) if type(item) is str else None
        if capability is None:
            invalid = True
        else:
            resolved.append(capability)
    if invalid or len(set(resolved)) != len(resolved):
        raise SafetyError(_INVALID_DISABLED_CAPABILITIES)
    return frozenset(resolved)


def _profile_fingerprint(name: str, base_url: str) -> str:
    return hashlib.sha256(
        canonical_json_bytes({"base_url": base_url, "name": name})
    ).hexdigest()


def load_discovery_profile(
    path: Path,
    *,
    env_file: Path | None = None,
    allowed_api_login_envs: frozenset[str] | None = None,
) -> ResolvedDiscoveryProfile:
    """Resolve only the credentials needed to discover read-only target IDs."""

    data = _load_toml(path)
    name = data["name"]
    if not is_safe_profile_name(name):
        raise SafetyError("Live profile name must use lowercase letters, digits, and hyphens")
    base_url = _base_url(data["base_url"])
    if data["allow_write"] is not False:
        raise SafetyError("Discovery live profile must set allow_write=false")
    _string_list(data["allowed_organization_ids"], label="allowed_organization_ids")
    if "disabled_read_capabilities" in data:
        _disabled_read_capabilities(data["disabled_read_capabilities"])

    api_login_env = _env_name(data["api_login_env"], label="api_login_env")
    if allowed_api_login_envs is not None and api_login_env not in allowed_api_login_envs:
        raise SafetyError("Live profile api_login_env is not a reviewed environment name")
    _env_name(data["organization_id_env"], label="organization_id_env")
    if "external_menu_id_env" in data:
        _env_name(data["external_menu_id_env"], label="external_menu_id_env")
    if "terminal_group_id_env" in data:
        _env_name(data["terminal_group_id_env"], label="terminal_group_id_env")
    if "write_product_id_env" in data:
        _env_name(data["write_product_id_env"], label="write_product_id_env")

    file_values = _load_env_file(env_file)
    api_login = _required_env(api_login_env, file_values)
    auth_version, app_id, client_secret = _resolve_app_credentials(data, file_values)
    return ResolvedDiscoveryProfile(
        name=name,
        base_url=base_url,
        api_login=api_login,
        fingerprint=_profile_fingerprint(name, base_url),
        auth_version=auth_version,
        app_id=app_id,
        client_secret=client_secret,
    )


def load_profile(
    path: Path,
    *,
    env_file: Path | None = None,
    allowed_api_login_envs: frozenset[str] | None = None,
) -> ResolvedLiveProfile:
    data = _load_toml(path)
    name = data["name"]
    if not is_safe_profile_name(name):
        raise SafetyError("Live profile name must use lowercase letters, digits, and hyphens")
    base_url = _base_url(data["base_url"])
    if type(data["allow_write"]) is not bool:
        raise SafetyError("allow_write must be a boolean")
    allow_write = data["allow_write"]
    allowed_organization_ids = _string_list(
        data["allowed_organization_ids"], label="allowed_organization_ids"
    )
    disabled_read_capabilities = _disabled_read_capabilities(
        data.get("disabled_read_capabilities", [])
    )

    api_login_env = _env_name(data["api_login_env"], label="api_login_env")
    if allowed_api_login_envs is not None and api_login_env not in allowed_api_login_envs:
        raise SafetyError("Live profile api_login_env is not a reviewed environment name")
    organization_id_env = _env_name(data["organization_id_env"], label="organization_id_env")
    external_menu_env = (
        _env_name(data["external_menu_id_env"], label="external_menu_id_env")
        if "external_menu_id_env" in data
        else None
    )
    terminal_env = (
        _env_name(data["terminal_group_id_env"], label="terminal_group_id_env")
        if "terminal_group_id_env" in data
        else None
    )
    product_env = (
        _env_name(data["write_product_id_env"], label="write_product_id_env")
        if "write_product_id_env" in data
        else None
    )
    if allow_write and (terminal_env is None or product_env is None):
        raise SafetyError("Write-enabled profile requires dedicated terminal and product fields")

    file_values = _load_env_file(env_file)
    api_login = _required_env(api_login_env, file_values)
    organization_id = _required_env(organization_id_env, file_values)
    auth_version, app_id, client_secret = _resolve_app_credentials(data, file_values)
    external_menu_id = (
        _required_env(external_menu_env, file_values) if external_menu_env is not None else None
    )
    terminal_group_id = (
        _required_env(terminal_env, file_values) if terminal_env is not None else None
    )
    if allow_write:
        assert product_env is not None
        write_product_id = _required_env(product_env, file_values)
    else:
        write_product_id = None

    fingerprint = _profile_fingerprint(name, base_url)
    return ResolvedLiveProfile(
        name=name,
        base_url=base_url,
        api_login=api_login,
        organization_id=organization_id,
        external_menu_id=external_menu_id,
        terminal_group_id=terminal_group_id,
        write_product_id=write_product_id,
        allow_write=allow_write,
        allowed_organization_ids=allowed_organization_ids,
        fingerprint=fingerprint,
        disabled_read_capabilities=disabled_read_capabilities,
        auth_version=auth_version,
        app_id=app_id,
        client_secret=client_secret,
    )
