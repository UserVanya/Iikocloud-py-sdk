from __future__ import annotations

import secrets
from collections.abc import Callable, Mapping
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from .capture import CaptureWriter, LiveCapture, RedactionHints
from .errors import SafetyError
from .live.lock import LiveProcessLock
from .live.profile import ResolvedLiveProfile
from .live.pytest_support import resolve_locked_live_profile
from .live.rates import LiveRateGuard, RateCatalog
from .live.session import LiveOperation, SafeLiveSession, load_operation_contract
from .live.state import LiveStateStore
from .paths import RepoPaths
from .pipeline import compose_reviewed_bootstrap_candidate

_EVIDENCE_OPERATION = "get_external_menu_by_id"
_EVIDENCE_VERSIONS = frozenset({2, 3, 4})


@dataclass(frozen=True)
class CaptureEvidenceDependencies:
    paths: RepoPaths
    rate_catalog_loader: Callable[[Path], RateCatalog]
    candidate_composer: Callable[[RepoPaths], tuple[dict[str, Any], dict[str, str]]]
    operation_contract_loader: Callable[[Path], Mapping[str, LiveOperation]]
    hints_builder: Callable[[dict[str, Any], str], RedactionHints]
    lock_factory: Callable[[Path], LiveProcessLock]
    profile_resolver: Callable[..., ResolvedLiveProfile]
    state_factory: Callable[..., LiveStateStore]
    guard_factory: Callable[..., LiveRateGuard]
    writer_factory: Callable[[Path], CaptureWriter]
    capture_factory: Callable[..., LiveCapture]
    session_factory: Callable[..., SafeLiveSession]
    run_id_factory: Callable[[], str]


def _new_run_id() -> str:
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    return f"{timestamp}-{secrets.token_hex(4)}"


def default_capture_evidence_dependencies(
    paths: RepoPaths | None = None,
) -> CaptureEvidenceDependencies:
    return CaptureEvidenceDependencies(
        paths=paths or RepoPaths.discover(),
        rate_catalog_loader=RateCatalog.load,
        candidate_composer=compose_reviewed_bootstrap_candidate,
        operation_contract_loader=load_operation_contract,
        hints_builder=RedactionHints.for_operation,
        lock_factory=LiveProcessLock,
        profile_resolver=resolve_locked_live_profile,
        state_factory=LiveStateStore,
        guard_factory=LiveRateGuard,
        writer_factory=CaptureWriter,
        capture_factory=LiveCapture,
        session_factory=SafeLiveSession,
        run_id_factory=_new_run_id,
    )


def _validate_selection(operation: object, menu_version: object) -> tuple[str, int]:
    if operation != _EVIDENCE_OPERATION:
        raise SafetyError("Evidence operation is not explicitly approved")
    if type(menu_version) is not int or menu_version not in _EVIDENCE_VERSIONS:
        raise SafetyError("Evidence menu version must be exactly 2, 3, or 4")
    return _EVIDENCE_OPERATION, menu_version


async def capture_evidence(
    *,
    live_profile: str,
    env_file: str,
    operation: str,
    menu_version: int,
    dependencies: CaptureEvidenceDependencies | None = None,
) -> None:
    selected_operation, selected_version = _validate_selection(operation, menu_version)
    selected = dependencies or default_capture_evidence_dependencies()
    paths = selected.paths

    # Both public rate contracts must be verified before schema composition, lock/state
    # creation, profile parsing, environment access, or HTTP client construction.
    catalog = selected.rate_catalog_loader(paths.root / "contracts/rate-limits.yaml")
    catalog.operation_budget("authenticate")
    catalog.operation_budget(selected_operation)

    effective_schema, _model_mappings = selected.candidate_composer(paths)
    operation_catalog = selected.operation_contract_loader(
        paths.root / "contracts/live-operations.yaml"
    )
    authentication = operation_catalog.get("authenticate")
    if (
        authentication is None
        or authentication.kind != "auth"
        or authentication.cleanup is not None
        or authentication.method != "POST"
        or authentication.path != "/api/1/access_token"
    ):
        raise SafetyError("Evidence authentication contract is not the approved endpoint")
    contract = operation_catalog.get(selected_operation)
    if (
        contract is None
        or contract.kind != "read"
        or contract.cleanup is not None
        or contract.method != "POST"
        or contract.path != "/api/2/menu/by_id"
    ):
        raise SafetyError("Evidence operation contract is not the approved read endpoint")
    hints = selected.hints_builder(effective_schema, selected_operation)

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
        writer = selected.writer_factory(paths.root / "private/captures")
        capture = selected.capture_factory(
            writer=writer,
            run_id=selected.run_id_factory(),
            selected_operation=selected_operation,
            operation_catalog=operation_catalog,
            hints=hints,
        )
        session = selected.session_factory(
            profile=profile,
            guard=guard,
            state=state,
            operation_contract=operation_catalog,
            capture=capture,
        )
        try:
            await session.authenticate()
            await session.request_json(
                selected_operation,
                contract.method,
                contract.path,
                {
                    "externalMenuId": profile.external_menu_id,
                    "organizationIds": [profile.organization_id],
                    "version": selected_version,
                },
            )
        finally:
            await session.close()
