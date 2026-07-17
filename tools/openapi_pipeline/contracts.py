from __future__ import annotations

import copy
from typing import Any

import jsonpath_rfc9535 as jsonpath

from .errors import ValidationError
from .io import canonical_json_bytes, sha256_bytes
from .overlay import apply_overlay

IIKO_ROOT_SERVER_URL = "https://api-ru.iiko.services"
IIKO_AUTH_OPERATIONS = frozenset(
    {
        ("/api/1/access_token", "post"),
        ("/api/v2/access_token", "post"),
    }
)

_HTTP_OPERATIONS_TARGET = (
    '$.paths.*["delete","get","head","options","patch","post","put","trace"]'
)
_RAW_AUTHORIZATION_TARGET = (
    '$.paths.*.*.parameters[?@.in == "header" && @.name == "Authorization"]'
)


def _overlay_document(actions: list[dict[str, Any]]) -> dict[str, Any]:
    return {
        "overlay": "1.1.0",
        "info": {
            "title": "iiko Cloud bearer authentication contract",
            "version": "1.0.0",
        },
        "actions": actions,
    }


def _guarded_action(
    document: dict[str, Any],
    target: str,
    *,
    issue: str,
    **operation: Any,
) -> dict[str, Any]:
    try:
        values = [node.value for node in jsonpath.find(target, document)]
    except jsonpath.JSONPathError as error:
        raise ValidationError(f"Invalid contract overlay target: {target}") from error
    if not values:
        raise ValidationError(f"Contract overlay target has no matches: {target}")
    guarded_value = values[0] if len(values) == 1 else values
    return {
        "target": target,
        "x-iiko-sdk-guard": {
            "issue": issue,
            "expected-matches": len(values),
            "expected-sha256": sha256_bytes(canonical_json_bytes(guarded_value)),
        },
        **operation,
    }


def build_contracts_overlay(source: dict[str, Any]) -> dict[str, Any]:
    """Build the reviewed server and bearer contract as sequential guarded actions."""
    if not isinstance(source, dict):
        raise ValidationError("OpenAPI contract source must be an object")

    working = copy.deepcopy(source)
    actions: list[dict[str, Any]] = []

    def append(target: str, *, issue: str, **operation: Any) -> None:
        nonlocal working
        action = _guarded_action(working, target, issue=issue, **operation)
        actions.append(action)
        working = apply_overlay(working, _overlay_document([action]))

    append(
        "$",
        issue="iiko-root-server",
        update={"servers": [{"url": IIKO_ROOT_SERVER_URL}]},
    )
    append(
        "$.components",
        issue="iiko-bearer-scheme",
        update={
            "securitySchemes": {
                "BearerAuth": {"type": "http", "scheme": "bearer"}
            }
        },
    )

    raw_authorization = list(jsonpath.find(_RAW_AUTHORIZATION_TARGET, working))
    if raw_authorization:
        append(
            _RAW_AUTHORIZATION_TARGET,
            issue="remove-raw-authorization-parameters",
            remove=True,
        )

    append(
        _HTTP_OPERATIONS_TARGET,
        issue="require-bearer-authentication",
        update={"security": [{"BearerAuth": []}]},
    )

    for path, method in sorted(IIKO_AUTH_OPERATIONS):
        operation_target = f'$.paths["{path}"].{method}'
        append(
            f"{operation_target}.security",
            issue=f"remove-bearer-from-{method}-{path}",
            remove=True,
        )
        append(
            operation_target,
            issue=f"mark-{method}-{path}-public",
            update={"security": []},
        )

    return _overlay_document(actions)
