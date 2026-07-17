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


def test_capture_writer_redacts_metadata_path_without_explicit_approval(
    tmp_path: Path,
) -> None:
    request_path, _response_path = _write_pair(CaptureWriter(tmp_path))

    request = json.loads(request_path.read_text(encoding="utf-8"))
    assert request["metadata"]["path"] == (
        "/<redacted:string>/<redacted:string>/<redacted:string>"
    )


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


def test_capture_writer_rejects_mismatched_approved_path_before_filesystem_mutation(
    tmp_path: Path,
) -> None:
    root = tmp_path / "captures"

    with pytest.raises(SafetyError, match="approved path"):
        _write_pair(
            CaptureWriter(root),
            approved_path="/api/1/other",
        )

    assert not root.exists()


@pytest.mark.parametrize(
    "approved_path",
    [
        "/api/1/{organizationId}",
        "/api/1/organizations?token=x",
        "https://example.invalid/api/1/organizations",
        "/api/../organizations",
    ],
)
def test_capture_writer_rejects_unsafe_approved_path_before_filesystem_mutation(
    tmp_path: Path,
    approved_path: str,
) -> None:
    root = tmp_path / "captures"

    with pytest.raises(SafetyError, match="approved path|relative path|unsafe segments"):
        _write_pair(
            CaptureWriter(root),
            metadata={"method": "POST", "path": approved_path, "status": 200},
            approved_path=approved_path,
        )

    assert not root.exists()


@pytest.mark.parametrize(
    "approved_path",
    [
        pytest.param("/api/1/%", id="truncated-percent-escape"),
        pytest.param("/api/1/%GG", id="non-hex-percent-escape"),
        pytest.param("/api/1/org%61nizations", id="percent-encoded-letter"),
        pytest.param(
            "/api/1/%7BorganizationId%7D",
            id="percent-encoded-template-braces",
        ),
        pytest.param("/api/1/organization name", id="space"),
        pytest.param("/api/1/organization\tname", id="tab"),
        pytest.param("/api/1/organization\nname", id="line-feed"),
        pytest.param("/api/1/organization\vname", id="vertical-tab"),
        pytest.param("/api/1/organization\fname", id="form-feed"),
        pytest.param("/api/1/organization\rname", id="carriage-return"),
        pytest.param("/api/1/organization\x00name", id="nul-control"),
        pytest.param("/api/1/organization\x7fname", id="del-control"),
    ],
)
def test_capture_writer_rejects_noncanonical_approved_path_before_filesystem_mutation(
    tmp_path: Path,
    approved_path: str,
) -> None:
    root = tmp_path / "captures"

    with pytest.raises(SafetyError, match="approved path|relative path|unsafe segments"):
        _write_pair(
            CaptureWriter(root),
            metadata={"method": "POST", "path": approved_path, "status": 200},
            approved_path=approved_path,
        )

    assert not root.exists()


def test_capture_writer_publishes_pair_as_one_directory_transaction(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    root = tmp_path / "captures"
    writer = CaptureWriter(root)
    real_write = capture_module._write_file_at
    writes = 0

    def fail_second_write(directory_fd: int, name: str, body: bytes) -> None:
        nonlocal writes
        writes += 1
        if writes == 2:
            raise OSError("synthetic second-file failure")
        real_write(directory_fd, name, body)

    monkeypatch.setattr(capture_module, "_write_file_at", fail_second_write)

    with pytest.raises(OSError, match="synthetic"):
        _write_pair(writer)

    assert not (root / "run/get_organizations").exists()
    assert not list(root.rglob("*.json"))
    assert not list(root.rglob("*.tmp-*"))


@pytest.mark.parametrize("failure", ["parent-fsync", "staging-open"])
def test_staging_creation_failure_removes_new_directory_and_preserves_cause(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, failure: str
) -> None:
    parent = tmp_path / "run"
    parent.mkdir(mode=0o700)
    parent_fd = os.open(parent, os.O_RDONLY | os.O_DIRECTORY)
    real_open = capture_module.os.open

    if failure == "parent-fsync":

        def fail_fsync(_fd: int) -> None:
            raise OSError("synthetic staging parent fsync failure")

        monkeypatch.setattr(capture_module.os, "fsync", fail_fsync)
    else:

        def fail_staging_open(
            path: str | bytes | os.PathLike[str] | os.PathLike[bytes],
            flags: int,
            mode: int = 0o777,
            *,
            dir_fd: int | None = None,
        ) -> int:
            if type(path) is str and path.startswith(".operation.tmp-"):
                raise OSError("synthetic staging open failure")
            return real_open(path, flags, mode, dir_fd=dir_fd)

        monkeypatch.setattr(capture_module.os, "open", fail_staging_open)

    try:
        with pytest.raises((OSError, SafetyError)) as caught:
            capture_module._create_staging_directory(parent_fd, "operation")
    finally:
        os.close(parent_fd)

    failure_chain = f"{caught.value} {caught.value.__cause__}"
    assert "synthetic staging" in failure_chain
    assert list(parent.iterdir()) == []


def test_cleanup_failure_preserves_primary_error_closes_all_directories_and_continues(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    root = tmp_path / "captures"
    tracked_fds: list[int] = []
    unlink_attempts: list[str] = []
    rmdir_attempts: list[str] = []
    real_root_open = capture_module._open_absolute_private_root
    real_child_open = capture_module._open_or_create_private_child
    real_staging_open = capture_module._create_staging_directory
    real_write = capture_module._write_file_at
    real_unlink = capture_module.os.unlink
    real_rmdir = capture_module.os.rmdir
    writes = 0

    def track_root(path: Path) -> int:
        fd = real_root_open(path)
        tracked_fds.append(fd)
        return fd

    def track_child(parent_fd: int, name: str) -> int:
        fd = real_child_open(parent_fd, name)
        tracked_fds.append(fd)
        return fd

    def track_staging(parent_fd: int, operation_id: str) -> tuple[str, int]:
        name, fd = real_staging_open(parent_fd, operation_id)
        tracked_fds.append(fd)
        return name, fd

    def fail_second_write(directory_fd: int, name: str, body: bytes) -> None:
        nonlocal writes
        writes += 1
        if writes == 2:
            raise OSError("synthetic primary write failure")
        real_write(directory_fd, name, body)

    def fail_request_unlink(
        path: str | bytes,
        *,
        dir_fd: int | None = None,
    ) -> None:
        if dir_fd is not None and type(path) is str and path.endswith(".json"):
            unlink_attempts.append(path)
            if path == "request.json":
                raise OSError("synthetic cleanup unlink failure")
        real_unlink(path, dir_fd=dir_fd)

    def fail_staging_rmdir(
        path: str | bytes,
        *,
        dir_fd: int | None = None,
    ) -> None:
        if dir_fd is not None and type(path) is str and ".tmp-" in path:
            rmdir_attempts.append(path)
            raise OSError("synthetic cleanup rmdir failure")
        real_rmdir(path, dir_fd=dir_fd)

    monkeypatch.setattr(capture_module, "_open_absolute_private_root", track_root)
    monkeypatch.setattr(capture_module, "_open_or_create_private_child", track_child)
    monkeypatch.setattr(capture_module, "_create_staging_directory", track_staging)
    monkeypatch.setattr(capture_module, "_write_file_at", fail_second_write)
    monkeypatch.setattr(capture_module.os, "unlink", fail_request_unlink)
    monkeypatch.setattr(capture_module.os, "rmdir", fail_staging_rmdir)

    with pytest.raises(OSError, match="synthetic primary write failure"):
        _write_pair(CaptureWriter(root))

    assert unlink_attempts == ["request.json", "response.json"]
    assert len(rmdir_attempts) == 1
    for fd in tracked_fds:
        with pytest.raises(OSError):
            os.fstat(fd)


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


@pytest.mark.parametrize(
    "sensitive_key",
    [
        "11111111-1111-4111-8111-111111111111",
        "aaaaaaaa-aaaa-0000-0000-aaaaaaaaaaaa",
    ],
)
def test_capture_writer_rejects_uuid_like_object_key_before_filesystem_mutation(
    tmp_path: Path,
    sensitive_key: str,
) -> None:
    root = tmp_path / "captures"

    with pytest.raises(SafetyError, match="object key|sensitive") as caught:
        _write_pair(
            CaptureWriter(root),
            response_json={sensitive_key: "value"},
        )

    assert sensitive_key not in str(caught.value)
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


def test_capture_writer_rejects_existing_root_below_symlinked_ancestor(
    tmp_path: Path,
) -> None:
    external = tmp_path / "external"
    real_private = external / "private"
    real_root = real_private / "captures"
    real_root.mkdir(parents=True, mode=0o700)
    real_private.chmod(0o700)
    real_root.chmod(0o700)
    linked_parent = tmp_path / "linked-private"
    linked_parent.symlink_to(real_private, target_is_directory=True)

    with pytest.raises(SafetyError, match="symlink|ancestor|directory"):
        _write_pair(CaptureWriter(linked_parent / "captures"))

    assert not list(external.rglob("*.json"))
    assert not (real_root / "run").exists()


def test_capture_writer_rejects_wide_immediate_private_parent_before_writes(
    tmp_path: Path,
) -> None:
    private = tmp_path / "private"
    root = private / "captures"
    private.mkdir(mode=0o700)
    root.mkdir(mode=0o700)
    private.chmod(0o755)

    with pytest.raises(SafetyError, match="0700"):
        _write_pair(CaptureWriter(root))

    assert not (root / "run").exists()
    assert not list(root.rglob("*.json"))


def test_atomic_publish_refuses_concurrent_empty_operation_directory(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    root = tmp_path / "captures"
    real_rename = capture_module._rename_directory_noreplace

    def race_publish(parent_fd: int, source: str, destination: str) -> None:
        os.mkdir(destination, 0o700, dir_fd=parent_fd)
        real_rename(parent_fd, source, destination)

    monkeypatch.setattr(
        capture_module,
        "_rename_directory_noreplace",
        race_publish,
    )

    with pytest.raises(SafetyError, match="overwrite"):
        _write_pair(CaptureWriter(root))

    operation = root / "run/get_organizations"
    assert operation.is_dir()
    assert not list(operation.iterdir())
    assert not list(root.rglob("*.json"))
    assert not list(root.rglob("*.tmp-*"))


def test_held_directory_fds_prevent_parent_symlink_swap_escape(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    root = tmp_path / "captures"
    root.mkdir(mode=0o700)
    moved = tmp_path / "moved-captures"
    external = tmp_path / "external"
    external.mkdir(mode=0o700)
    real_create = capture_module._create_staging_directory

    def swap_then_create(parent_fd: int, operation_id: str) -> tuple[str, int]:
        root.rename(moved)
        root.symlink_to(external, target_is_directory=True)
        return real_create(parent_fd, operation_id)

    monkeypatch.setattr(
        capture_module,
        "_create_staging_directory",
        swap_then_create,
    )

    with pytest.raises(SafetyError, match="path|ancestor|directory"):
        _write_pair(CaptureWriter(root))

    assert not list(external.rglob("*.json"))
    assert not list(moved.rglob("*.json"))


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
