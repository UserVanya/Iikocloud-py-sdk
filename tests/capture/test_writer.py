import json
import os
import unicodedata
from pathlib import Path

import pytest

import tools.openapi_pipeline.capture as capture_module
from tools.openapi_pipeline.capture import CaptureWriter
from tools.openapi_pipeline.errors import SafetyError


def test_capture_writer_forbids_auth_body_and_writes_only_after_scan(
    tmp_path: Path,
) -> None:
    writer = CaptureWriter(tmp_path, known_secrets=("secret-token",))
    with pytest.raises(SafetyError, match="auth body"):
        writer.write(
            run_id="run",
            operation_id="authenticate",
            kind="auth",
            request_json={"apiLogin": "secret-token"},
            response_json={"token": "secret-token"},
            metadata={
                "method": "POST",
                "path": "/api/1/access_token",
                "status": 200,
            },
        )

    assert list(tmp_path.rglob("*.json")) == []


def test_capture_writer_sanitizes_before_writing_mode_0600(tmp_path: Path) -> None:
    writer = CaptureWriter(tmp_path, known_secrets=("secret-token",))

    writer.write(
        run_id="run",
        operation_id="get_organizations",
        kind="read",
        request_json={"organizationId": "11111111-1111-4111-8111-111111111111"},
        response_json={"name": "Private venue", "token": "secret-token"},
        metadata={
            "method": "POST",
            "path": "/api/1/organizations",
            "status": 200,
        },
    )

    response_path = tmp_path / "run/get_organizations/response.json"
    contents = response_path.read_text(encoding="utf-8")
    assert response_path.exists()
    assert response_path.stat().st_mode & 0o777 == 0o600
    assert "secret-token" not in contents
    assert "Private venue" not in contents


def _write_pair(writer: CaptureWriter, **overrides: object) -> tuple[Path, Path]:
    arguments: dict[str, object] = {
        "run_id": "run",
        "operation_id": "get_organizations",
        "kind": "read",
        "request_json": {"value": 1},
        "response_json": {"value": 2},
        "metadata": {
            "method": "POST",
            "path": "/api/1/organizations",
            "status": 200,
        },
    }
    arguments.update(overrides)
    return writer.write(**arguments)  # type: ignore[arg-type]


def test_capture_writer_publishes_pair_as_one_directory_transaction(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    root = tmp_path / "captures"
    writer = CaptureWriter(root)
    real_write = capture_module.write_json_atomic
    writes = 0

    def fail_second_write(path: Path, value: object, mode: int = 0o644) -> None:
        nonlocal writes
        writes += 1
        if writes == 2:
            raise OSError("synthetic second-file failure")
        real_write(path, value, mode)

    monkeypatch.setattr(capture_module, "write_json_atomic", fail_second_write)

    with pytest.raises(OSError, match="synthetic"):
        _write_pair(writer)

    assert not (root / "run/get_organizations").exists()
    assert not list(root.rglob("*.json"))
    assert not list(root.rglob("*.tmp-*"))


def test_capture_writer_rejects_overwrite_and_preserves_first_pair(tmp_path: Path) -> None:
    root = tmp_path / "captures"
    writer = CaptureWriter(root)
    request_path, response_path = _write_pair(writer)
    before = (request_path.read_bytes(), response_path.read_bytes())

    with pytest.raises(SafetyError, match="overwrite"):
        _write_pair(writer, response_json={"value": 3})

    assert (request_path.read_bytes(), response_path.read_bytes()) == before


def test_capture_writer_sets_private_directory_and_file_modes(tmp_path: Path) -> None:
    root = tmp_path / "captures"
    request_path, response_path = _write_pair(CaptureWriter(root))

    for directory in (root, root / "run", root / "run/get_organizations"):
        assert directory.stat().st_mode & 0o777 == 0o700
    for file in (request_path, response_path):
        assert file.stat().st_mode & 0o777 == 0o600


def test_capture_writer_creates_every_missing_private_parent_as_0700(
    tmp_path: Path,
) -> None:
    private = tmp_path / "private"
    root = private / "captures"

    _write_pair(CaptureWriter(root))

    assert private.stat().st_mode & 0o777 == 0o700
    assert root.stat().st_mode & 0o777 == 0o700


def test_capture_writer_strips_headers_and_links_path_uuid_to_body(tmp_path: Path) -> None:
    source_uuid = "11111111-1111-4111-8111-111111111111"
    known_secret = "known-secret"
    request_path, _response_path = _write_pair(
        CaptureWriter(tmp_path, known_secrets=(known_secret,)),
        request_json={"organizationId": source_uuid},
        metadata={
            "method": "POST",
            "path": f"/api/1/organizations/{source_uuid}/{known_secret}",
            "status": 200,
            "duration": 0.125,
            "headers": {
                "Authorization": f"Bearer {known_secret}",
                "Content-Type": "application/json",
                "X-Correlation-ID": source_uuid,
                "X-Private": "venue-name",
            },
        },
    )

    request = json.loads(request_path.read_text(encoding="utf-8"))
    metadata = request["metadata"]
    alias = request["body"]["organizationId"]
    serialized = request_path.read_text(encoding="utf-8")
    assert known_secret not in serialized
    assert "Authorization" not in serialized
    assert "X-Private" not in serialized
    assert metadata["headers"] == {
        "content-type": "application/json",
        "x-correlation-id": alias,
    }
    assert alias in metadata["path"]
    assert metadata["duration"] == 0.125


@pytest.mark.parametrize(
    "metadata",
    [
        {"method": "post", "path": "/api/1/value", "status": 200},
        {"method": "POST", "path": "https://example.invalid/api?token=x", "status": 200},
        {"method": "POST", "path": "/api/1/value?token=x", "status": 200},
        {"method": "POST", "path": "/api/1/value", "status": True},
        {
            "method": "POST",
            "path": "/api/1/value",
            "status": 200,
            "headers": {"X-Ignored": b"binary"},
        },
        {
            "method": "POST",
            "path": "/api/1/value",
            "status": 200,
            "unexpected": "field",
        },
    ],
)
def test_capture_writer_rejects_unsafe_metadata_before_filesystem_mutation(
    tmp_path: Path, metadata: object
) -> None:
    root = tmp_path / "captures"
    with pytest.raises(SafetyError):
        _write_pair(CaptureWriter(root), metadata=metadata)

    assert not root.exists()


@pytest.mark.parametrize(
    "body",
    [b"binary", {"nested": b"binary"}, {"value": float("nan")}],
)
def test_capture_writer_rejects_non_json_body_before_filesystem_mutation(
    tmp_path: Path, body: object
) -> None:
    root = tmp_path / "captures"
    with pytest.raises(SafetyError):
        _write_pair(CaptureWriter(root), response_json=body)

    assert not root.exists()


def test_final_scan_catches_escaped_and_normalized_secret_before_writes(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    known = 'Caf\u00e9-"secret\\value'
    equivalent = unicodedata.normalize("NFD", known)
    root = tmp_path / "captures"
    writer = CaptureWriter(root, known_secrets=(known,))

    def unsafe_passthrough(
        value: object, **_kwargs: object
    ) -> object:  # simulate a sanitizer regression
        return value

    monkeypatch.setattr(writer._sanitizer, "sanitize", unsafe_passthrough)

    with pytest.raises(SafetyError, match="final secret/PII scan") as caught:
        _write_pair(writer, response_json={"value": f"prefix-{equivalent}-suffix"})

    assert known not in str(caught.value)
    assert not root.exists()


def test_capture_writer_rejects_wide_symlink_and_existing_operation_paths(
    tmp_path: Path,
) -> None:
    wide = tmp_path / "wide"
    wide.mkdir(mode=0o700)
    wide.chmod(0o755)
    with pytest.raises(SafetyError, match="0700"):
        _write_pair(CaptureWriter(wide))

    root = tmp_path / "captures"
    root.mkdir(mode=0o700)
    outside = tmp_path / "outside"
    outside.mkdir(mode=0o700)
    (root / "run").symlink_to(outside, target_is_directory=True)
    with pytest.raises(SafetyError, match="symlink"):
        _write_pair(CaptureWriter(root))
    assert not list(outside.rglob("*.json"))

    os.unlink(root / "run")
    run = root / "run"
    run.mkdir(mode=0o700)
    operation = run / "get_organizations"
    operation.mkdir(mode=0o700)
    with pytest.raises(SafetyError, match="overwrite"):
        _write_pair(CaptureWriter(root))


@pytest.mark.parametrize(
    ("run_id", "operation_id"),
    [("../escape", "safe"), ("safe", "../escape"), ("safe", "a/b")],
)
def test_capture_ids_cannot_escape_root(tmp_path: Path, run_id: str, operation_id: str) -> None:
    root = tmp_path / "captures"
    with pytest.raises(SafetyError, match="ID"):
        _write_pair(
            CaptureWriter(root),
            run_id=run_id,
            operation_id=operation_id,
        )

    assert not root.exists()
