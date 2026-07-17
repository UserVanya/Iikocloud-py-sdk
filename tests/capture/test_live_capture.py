from __future__ import annotations

import dataclasses
import json
from pathlib import Path
from typing import Any

import pytest
from pydantic import BaseModel, ConfigDict, Field

from tools.openapi_pipeline.capture import CaptureWriter, LiveCapture, RedactionHints
from tools.openapi_pipeline.errors import SafetyError
from tools.openapi_pipeline.live.session import LiveOperation


class RequestModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    organization_id: str = Field(alias="organizationId")
    mode: str


class ResponseModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    kind: str = Field(alias="type")
    name: str
    token_echo: str = Field(alias="tokenEcho")


def _schema(operation_id: str = "get_organizations") -> dict[str, Any]:
    return {
        "openapi": "3.1.0",
        "paths": {
            "/api/1/organizations": {
                "post": {
                    "operationId": operation_id,
                    "requestBody": {
                        "content": {
                            "application/json": {
                                "schema": {
                                    "type": "object",
                                    "properties": {
                                        "mode": {"enum": ["FULL"]},
                                        "organizationId": {
                                            "type": "string",
                                            "format": "uuid",
                                        },
                                    },
                                }
                            }
                        }
                    },
                    "responses": {
                        "200": {
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "type": "object",
                                        "properties": {
                                            "type": {"enum": ["ORGANIZATION"]},
                                            "name": {"type": "string"},
                                            "tokenEcho": {"type": "string"},
                                        },
                                    }
                                }
                            }
                        }
                    },
                }
            }
        },
    }


def _catalog() -> dict[str, LiveOperation]:
    return {
        "authenticate": LiveOperation("auth", None, "POST", "/api/1/access_token"),
        "get_organizations": LiveOperation("read", None, "POST", "/api/1/organizations"),
    }


def _capture(tmp_path: Path, *, known_secrets: tuple[str, ...] = ()) -> LiveCapture:
    hints = RedactionHints.for_operation(_schema(), "get_organizations")
    return LiveCapture(
        writer=CaptureWriter(tmp_path, known_secrets=known_secrets),
        run_id="run",
        selected_operation="get_organizations",
        operation_catalog=_catalog(),
        hints=hints,
    )


def test_live_capture_dumps_pydantic_json_by_alias_and_uses_schema_values(
    tmp_path: Path,
) -> None:
    source_uuid = "11111111-1111-4111-8111-111111111111"
    active_token = "active-token-value"
    capture = _capture(tmp_path)
    capture.add_known_secret(active_token)

    request_path, response_path = capture.write_model_pair(
        "get_organizations",
        RequestModel(organizationId=source_uuid, mode="FULL"),
        ResponseModel(
            type="ORGANIZATION",
            name="Private venue",
            tokenEcho=f"prefix-{active_token}-suffix",
        ),
        metadata={"status": 200},
    )

    request = json.loads(request_path.read_text(encoding="utf-8"))
    response = json.loads(response_path.read_text(encoding="utf-8"))
    assert request["body"] == {
        "mode": "FULL",
        "organizationId": "00000000-0000-4000-8000-000000000001",
    }
    assert response["body"] == {
        "name": "<redacted:string>",
        "tokenEcho": "<redacted:secret>",
        "type": "ORGANIZATION",
    }
    assert active_token not in response_path.read_text(encoding="utf-8")
    assert response["metadata"]["method"] == "POST"
    assert response["metadata"]["status"] == 200


def test_live_capture_accepts_strict_json_values_for_safe_session(tmp_path: Path) -> None:
    capture = _capture(tmp_path)

    request_path, response_path = capture.write_model_pair(
        "get_organizations",
        {"mode": "FULL"},
        {"type": "ORGANIZATION", "name": "Private"},
        metadata={"status": 200, "headers": {"Content-Type": "application/json"}},
    )

    assert request_path.exists()
    assert response_path.exists()


def test_live_capture_selects_response_hints_by_status_without_union(
    tmp_path: Path,
) -> None:
    schema = _schema()
    responses = schema["paths"]["/api/1/organizations"]["post"]["responses"]
    responses["200"]["content"]["application/json"]["schema"]["properties"]["name"] = {
        "enum": ["STANDARD"]
    }
    responses["202"] = {
        "content": {"application/json": {"schema": {"properties": {"name": {"type": "string"}}}}}
    }
    hints = RedactionHints.for_operation(schema, "get_organizations")

    bodies: dict[int, dict[str, object]] = {}
    for status in (200, 202):
        capture = LiveCapture(
            writer=CaptureWriter(tmp_path / str(status)),
            run_id="run",
            selected_operation="get_organizations",
            operation_catalog=_catalog(),
            hints=hints,
        )
        request_path, response_path = capture.write_model_pair(
            "get_organizations",
            {"mode": "FULL"},
            {"name": "STANDARD"},
            metadata={"status": status},
        )
        assert json.loads(request_path.read_text())["body"]["mode"] == "FULL"
        bodies[status] = json.loads(response_path.read_text())["body"]

    assert bodies[200]["name"] == "STANDARD"
    assert bodies[202]["name"] == "<redacted:string>"

    unmapped = LiveCapture(
        writer=CaptureWriter(tmp_path / "unmapped"),
        run_id="run",
        selected_operation="get_organizations",
        operation_catalog=_catalog(),
        hints=hints,
    )
    with pytest.raises(SafetyError, match="response.*status|status.*response"):
        unmapped.write_model_pair(
            "get_organizations",
            {"mode": "FULL"},
            {"name": "STANDARD"},
            metadata={"status": 201},
        )
    assert not (tmp_path / "unmapped").exists()


def test_live_capture_copies_catalog_and_is_immutable(tmp_path: Path) -> None:
    catalog = _catalog()
    capture = LiveCapture(
        writer=CaptureWriter(tmp_path),
        run_id="run",
        selected_operation="get_organizations",
        operation_catalog=catalog,
        hints=RedactionHints.for_operation(_schema(), "get_organizations"),
    )
    catalog["get_organizations"] = LiveOperation("read", None, "GET", "/malicious")

    with pytest.raises(dataclasses.FrozenInstanceError):
        capture.selected_operation = "authenticate"  # type: ignore[misc]
    with pytest.raises(TypeError):
        capture.operation_catalog["get_organizations"] = catalog[  # type: ignore[index]
            "get_organizations"
        ]
    assert capture.operation_catalog["get_organizations"].method == "POST"


@pytest.mark.parametrize(
    ("selected", "hints_operation", "message"),
    [
        ("authenticate", "authenticate", "auth"),
        ("missing", "missing", "catalog"),
        ("get_organizations", "other_operation", "hints"),
    ],
)
def test_live_capture_refuses_auth_unknown_and_mismatched_hints_at_binding(
    tmp_path: Path,
    selected: str,
    hints_operation: str,
    message: str,
) -> None:
    hints = RedactionHints(hints_operation, {}, {})
    with pytest.raises(SafetyError, match=message):
        LiveCapture(
            writer=CaptureWriter(tmp_path),
            run_id="run",
            selected_operation=selected,
            operation_catalog=_catalog(),
            hints=hints,
        )

    assert not list(tmp_path.rglob("*.json"))


def test_live_capture_rejects_operation_or_catalog_metadata_mismatch_before_write(
    tmp_path: Path,
) -> None:
    capture = _capture(tmp_path)

    with pytest.raises(SafetyError, match="selected"):
        capture.write_model_pair("authenticate", {}, {}, metadata={"status": 200})
    with pytest.raises(SafetyError, match="method"):
        capture.write_model_pair(
            "get_organizations",
            {},
            {},
            metadata={"method": "GET", "status": 200},
        )
    with pytest.raises(SafetyError, match="path"):
        capture.write_model_pair(
            "get_organizations",
            {},
            {},
            metadata={"path": "/other", "status": 200},
        )

    assert not list(tmp_path.rglob("*.json"))


def test_live_capture_rejects_non_pydantic_custom_model(tmp_path: Path) -> None:
    class PretendModel:
        def model_dump(self, **_kwargs: object) -> dict[str, str]:
            return {"name": "private"}

    with pytest.raises(SafetyError, match="Pydantic or strict JSON"):
        _capture(tmp_path).write_model_pair(
            "get_organizations",
            PretendModel(),
            {},
            metadata={"status": 200},
        )
