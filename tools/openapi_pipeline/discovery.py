from __future__ import annotations

import json
import re
from collections.abc import Callable, Mapping
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import httpx

from .errors import SafetyError
from .live.lock import LiveProcessLock
from .live.profile import ResolvedDiscoveryProfile
from .live.pytest_support import resolve_locked_discovery_profile
from .live.rates import LiveRateGuard, RateCatalog
from .live.session import LiveOperation, SafeLiveSession, load_operation_contract
from .live.state import LiveStateStore
from .paths import RepoPaths

_SAFE_ID = re.compile(r"[A-Za-z0-9][A-Za-z0-9_.:-]{0,127}\Z")
_MAX_RESPONSE_BYTES = 8 * 1024 * 1024
_MAX_ITEMS = 10_000
_APPROVED_OPERATIONS = {
    "authenticate": ("auth", "POST", "/api/1/access_token"),
    "get_organizations": ("read", "POST", "/api/1/organizations"),
    "get_terminal_groups": ("read", "POST", "/api/1/terminal_groups"),
    "get_external_menus": ("read", "POST", "/api/2/menu"),
}


@dataclass(frozen=True, slots=True)
class DiscoveredNamedTarget:
    id: str
    name: str


@dataclass(frozen=True, slots=True)
class DiscoveredTerminalGroup:
    id: str
    name: str
    is_sleeping: bool


@dataclass(frozen=True, slots=True)
class DiscoveredOrganization:
    id: str
    name: str
    terminal_groups: tuple[DiscoveredTerminalGroup, ...]


@dataclass(frozen=True, slots=True)
class DiscoveryResult:
    organizations: tuple[DiscoveredOrganization, ...]
    external_menus: tuple[DiscoveredNamedTarget, ...]

    def to_dict(self) -> dict[str, Any]:
        return {
            "organizations": [
                {
                    "id": organization.id,
                    "name": organization.name,
                    "terminalGroups": [
                        {
                            "id": group.id,
                            "name": group.name,
                            "isSleeping": group.is_sleeping,
                        }
                        for group in organization.terminal_groups
                    ],
                }
                for organization in self.organizations
            ],
            "externalMenus": [
                {"id": menu.id, "name": menu.name} for menu in self.external_menus
            ],
        }


@dataclass(frozen=True)
class DiscoveryDependencies:
    paths: RepoPaths
    rate_catalog_loader: Callable[[Path], RateCatalog]
    operation_contract_loader: Callable[[Path], Mapping[str, LiveOperation]]
    lock_factory: Callable[[Path], LiveProcessLock]
    profile_resolver: Callable[..., ResolvedDiscoveryProfile]
    state_factory: Callable[..., LiveStateStore]
    guard_factory: Callable[..., LiveRateGuard]
    session_factory: Callable[..., SafeLiveSession]


def default_discovery_dependencies(
    paths: RepoPaths | None = None,
) -> DiscoveryDependencies:
    return DiscoveryDependencies(
        paths=paths or RepoPaths.discover(),
        rate_catalog_loader=RateCatalog.load,
        operation_contract_loader=load_operation_contract,
        lock_factory=LiveProcessLock,
        profile_resolver=resolve_locked_discovery_profile,
        state_factory=LiveStateStore,
        guard_factory=LiveRateGuard,
        session_factory=SafeLiveSession,
    )


def _unique_json_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("duplicate JSON key")
        result[key] = value
    return result


def _reject_json_constant(value: str) -> None:
    raise ValueError(f"non-finite JSON number {value}")


def _response_object(response: httpx.Response, *, label: str) -> dict[str, Any]:
    if response.status_code != 200:
        raise SafetyError(f"{label} discovery failed with HTTP {response.status_code}")
    if len(response.content) > _MAX_RESPONSE_BYTES:
        raise SafetyError(f"{label} discovery response is too large")
    content_type = response.headers.get("content-type", "").split(";", 1)[0].strip().lower()
    if content_type != "application/json":
        raise SafetyError(f"{label} discovery response is not JSON")
    try:
        value = json.loads(
            response.content.decode("utf-8"),
            object_pairs_hook=_unique_json_object,
            parse_constant=_reject_json_constant,
        )
    except (UnicodeError, ValueError):
        raise SafetyError(f"{label} discovery response is invalid JSON") from None
    if type(value) is not dict:
        raise SafetyError(f"{label} discovery response must be an object")
    return value


def _safe_id(value: object, *, label: str) -> str:
    if type(value) is not str or _SAFE_ID.fullmatch(value) is None:
        raise SafetyError(f"{label} must be a safe ID")
    return value


def _safe_name(value: object, *, label: str) -> str:
    if (
        type(value) is not str
        or not value
        or len(value) > 512
        or value != value.strip()
        or any(ord(character) < 32 or ord(character) == 127 for character in value)
    ):
        raise SafetyError(f"{label} must be a safe name")
    return value


def _safe_list(value: object, *, label: str) -> list[Any]:
    if type(value) is not list or len(value) > _MAX_ITEMS:
        raise SafetyError(f"{label} must be a bounded array")
    return value


def _named_target(value: object, *, label: str) -> DiscoveredNamedTarget:
    if type(value) is not dict:
        raise SafetyError(f"{label} must be an object")
    return DiscoveredNamedTarget(
        id=_safe_id(value.get("id"), label=f"{label} ID"),
        name=_safe_name(value.get("name"), label=f"{label} name"),
    )


def _organizations(response: httpx.Response) -> tuple[DiscoveredNamedTarget, ...]:
    root = _response_object(response, label="organization")
    items = _safe_list(root.get("organizations"), label="organizations")
    result = tuple(_named_target(item, label="organization") for item in items)
    if len({item.id for item in result}) != len(result):
        raise SafetyError("organization IDs must be unique")
    return result


def _terminal_groups(
    response: httpx.Response,
    organization_ids: set[str],
) -> dict[str, tuple[DiscoveredTerminalGroup, ...]]:
    root = _response_object(response, label="terminal group")
    grouped: dict[str, list[DiscoveredTerminalGroup]] = {
        organization_id: [] for organization_id in organization_ids
    }
    seen: set[str] = set()
    for field, sleeping in (("terminalGroups", False), ("terminalGroupsInSleep", True)):
        wrappers = _safe_list(root.get(field), label=field)
        for wrapper in wrappers:
            if type(wrapper) is not dict:
                raise SafetyError(f"{field} item must be an object")
            organization_id = _safe_id(
                wrapper.get("organizationId"), label="terminal group organization ID"
            )
            if organization_id not in grouped:
                raise SafetyError("terminal group references an unknown organization")
            for item in _safe_list(wrapper.get("items"), label="terminal group items"):
                target = _named_target(item, label="terminal group")
                if type(item) is not dict or _safe_id(
                    item.get("organizationId"), label="terminal group organization ID"
                ) != organization_id:
                    raise SafetyError("terminal group organization association is invalid")
                if target.id in seen:
                    raise SafetyError("terminal group IDs must be unique")
                seen.add(target.id)
                grouped[organization_id].append(
                    DiscoveredTerminalGroup(target.id, target.name, sleeping)
                )
    return {key: tuple(value) for key, value in grouped.items()}


def _external_menus(response: httpx.Response) -> tuple[DiscoveredNamedTarget, ...]:
    root = _response_object(response, label="external menu")
    raw = root.get("externalMenus")
    items = [] if raw is None else _safe_list(raw, label="externalMenus")
    result = tuple(_named_target(item, label="external menu") for item in items)
    if len({item.id for item in result}) != len(result):
        raise SafetyError("external menu IDs must be unique")
    return result


def _approved_contract(
    operations: Mapping[str, LiveOperation],
    operation_id: str,
) -> LiveOperation:
    expected_kind, expected_method, expected_path = _APPROVED_OPERATIONS[operation_id]
    operation = operations.get(operation_id)
    if (
        operation is None
        or operation.kind != expected_kind
        or operation.cleanup is not None
        or operation.method != expected_method
        or operation.path != expected_path
    ):
        raise SafetyError(f"Discovery operation {operation_id!r} is not approved")
    return operation


async def discover_read_targets(
    *,
    live_profile: str,
    env_file: str,
    dependencies: DiscoveryDependencies | None = None,
) -> DiscoveryResult:
    selected = dependencies or default_discovery_dependencies()
    paths = selected.paths
    catalog = selected.rate_catalog_loader(paths.root / "contracts/rate-limits.yaml")
    for operation_id in _APPROVED_OPERATIONS:
        catalog.operation_budget(operation_id)
    operations = selected.operation_contract_loader(
        paths.root / "contracts/live-operations.yaml"
    )
    approved = {
        operation_id: _approved_contract(operations, operation_id)
        for operation_id in _APPROVED_OPERATIONS
    }

    process_lock = selected.lock_factory(paths.root / ".state/live.lock")
    with process_lock:
        profile = selected.profile_resolver(
            paths.root,
            process_lock=process_lock,
            profile_name=live_profile,
            env_file_option=env_file,
        )
        state = selected.state_factory(
            paths.root / ".state/live-rate-limits.json",
            process_lock=process_lock,
        )
        guard = selected.guard_factory(
            profile_fingerprint=profile.fingerprint,
            catalog=catalog,
            state=state,
            process_lock=process_lock,
        )
        session = selected.session_factory(
            profile=profile,
            guard=guard,
            state=state,
            operation_contract=operations,
        )
        try:
            await session.authenticate()
            organization_response = await session.request_json(
                "get_organizations",
                approved["get_organizations"].method,
                approved["get_organizations"].path,
                {},
            )
            organization_targets = _organizations(organization_response)
            organization_ids = [target.id for target in organization_targets]
            terminal_response = await session.request_json(
                "get_terminal_groups",
                approved["get_terminal_groups"].method,
                approved["get_terminal_groups"].path,
                {"organizationIds": organization_ids},
            )
            grouped = _terminal_groups(terminal_response, set(organization_ids))
            menu_response = await session.request_json(
                "get_external_menus",
                approved["get_external_menus"].method,
                approved["get_external_menus"].path,
                {},
            )
            menus = _external_menus(menu_response)
            return DiscoveryResult(
                organizations=tuple(
                    DiscoveredOrganization(
                        id=target.id,
                        name=target.name,
                        terminal_groups=grouped[target.id],
                    )
                    for target in organization_targets
                ),
                external_menus=menus,
            )
        finally:
            await session.close()


def render_discovery_result(result: DiscoveryResult) -> str:
    if type(result) is not DiscoveryResult:
        raise SafetyError("Discovery result is invalid")
    return json.dumps(result.to_dict(), ensure_ascii=False, indent=2)
