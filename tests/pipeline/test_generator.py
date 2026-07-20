from __future__ import annotations

import ast
import json
import subprocess
from pathlib import Path
from typing import Any

import pytest
import yaml

from tools.openapi_pipeline import generator as generator_module
from tools.openapi_pipeline.errors import PipelineError
from tools.openapi_pipeline.generator import (
    Toolchain,
    build_generate_command,
    build_validate_command,
    pin_toolchain,
    run_generator,
    write_effective_generator_config,
)

EXPECTED_IMAGE = "openapitools/openapi-generator-cli"
EXPECTED_VERSION = "v7.22.0"
VALID_DIGEST = "sha256:" + "a" * 64


def _write_base_config(path: Path) -> bytes:
    body = (
        b"additionalProperties:\n"
        b"  packageName: iikocloud_client\n"
        b"  packageVersion: old\n"
        b"  hideGenerationTimestamp: true\n"
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(body)
    return body


def _write_lock(path: Path, **updates: Any) -> None:
    value: dict[str, Any] = {
        "image": EXPECTED_IMAGE,
        "version": EXPECTED_VERSION,
        "digest": VALID_DIGEST,
    }
    value.update(updates)
    path.write_text(json.dumps(value), encoding="utf-8")


def test_repository_generator_assets_are_exact_and_loadable() -> None:
    toolchain = Toolchain.load(Path("generator/toolchain.lock"))
    config = yaml.safe_load(Path("generator/config.yaml").read_text(encoding="utf-8"))
    manual_files = Path("generator/manual-files.txt").read_text(encoding="utf-8").splitlines()

    assert toolchain.image == EXPECTED_IMAGE
    assert toolchain.version == EXPECTED_VERSION
    assert config == {
        "additionalProperties": {
            "packageName": "iikocloud_client",
            "projectName": "iikocloud-client",
            "packageVersion": "0.1.0",
            "library": "httpx",
            "generateSourceCodeOnly": True,
            "supportHttpxSync": False,
            "hideGenerationTimestamp": True,
            "lazyImports": False,
            "disallowAdditionalPropertiesIfNotPresent": False,
            "useOneOfDiscriminatorLookup": False,
            "setEnsureAsciiToFalse": True,
        }
    }
    assert manual_files == [
        "iikocloud_client/_contracts/__init__.py",
        "iikocloud_client/_contracts/rate-limits.yaml",
        "iikocloud_client/py.typed",
    ]


def test_repository_hand_owned_contracts_are_seeded_and_canonical() -> None:
    init_path = Path("src/iikocloud_client/_contracts/__init__.py")
    contract_path = Path("src/iikocloud_client/_contracts/rate-limits.yaml")
    canonical_contract = Path("contracts/rate-limits.yaml")
    typing_marker = Path("src/iikocloud_client/py.typed")

    module = ast.parse(init_path.read_text(encoding="utf-8"))

    assert len(module.body) == 1
    assert isinstance(module.body[0], ast.Expr)
    assert isinstance(module.body[0].value, ast.Constant)
    assert isinstance(module.body[0].value.value, str)
    assert module.body[0].value.value
    assert contract_path.read_bytes() == canonical_contract.read_bytes()
    assert typing_marker.is_file()
    assert not typing_marker.is_symlink()
    assert typing_marker.read_bytes() == b""


def test_toolchain_load_accepts_only_the_exact_pinned_toolchain(tmp_path: Path) -> None:
    lock = tmp_path / "toolchain.lock"
    _write_lock(lock)

    toolchain = Toolchain.load(lock)

    assert toolchain == Toolchain(EXPECTED_IMAGE, EXPECTED_VERSION, VALID_DIGEST)
    assert toolchain.pinned_image == f"{EXPECTED_IMAGE}@{VALID_DIGEST}"


@pytest.mark.parametrize(
    "body",
    [
        "not JSON",
        "[]",
        json.dumps({"image": EXPECTED_IMAGE, "version": EXPECTED_VERSION}),
        json.dumps(
            {
                "image": EXPECTED_IMAGE,
                "version": EXPECTED_VERSION,
                "digest": VALID_DIGEST,
                "extra": True,
            }
        ),
        json.dumps({"image": 3, "version": EXPECTED_VERSION, "digest": VALID_DIGEST}),
        json.dumps({"image": "other/image", "version": EXPECTED_VERSION, "digest": VALID_DIGEST}),
        json.dumps({"image": EXPECTED_IMAGE, "version": "v7.21.0", "digest": VALID_DIGEST}),
        json.dumps(
            {
                "image": EXPECTED_IMAGE,
                "version": EXPECTED_VERSION,
                "digest": "sha256:" + "A" * 64,
            }
        ),
    ],
)
def test_toolchain_load_rejects_bad_lock_actionably(tmp_path: Path, body: str) -> None:
    lock = tmp_path / "toolchain.lock"
    lock.write_text(body, encoding="utf-8")

    with pytest.raises(PipelineError) as error:
        Toolchain.load(lock)

    message = str(error.value)
    assert "generator toolchain lock" in message.lower()
    assert "KeyError" not in message
    assert body not in message


def test_toolchain_load_wraps_missing_and_invalid_utf8_files(tmp_path: Path) -> None:
    missing = tmp_path / "missing.lock"
    invalid = tmp_path / "invalid.lock"
    invalid.write_bytes(b"\xff")

    with pytest.raises(PipelineError, match="Cannot read generator toolchain lock"):
        Toolchain.load(missing)
    with pytest.raises(PipelineError, match="not valid UTF-8"):
        Toolchain.load(invalid)


def test_pin_toolchain_uses_argv_validates_inspection_and_writes_atomically(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    lock = tmp_path / "generator/toolchain.lock"
    calls: list[tuple[list[str], dict[str, Any]]] = []

    def fake_run(command: list[str], **kwargs: Any) -> subprocess.CompletedProcess[str]:
        calls.append((command, kwargs))
        stdout = (
            f"{EXPECTED_IMAGE}@{VALID_DIGEST}\n" if command[1:3] == ["image", "inspect"] else ""
        )
        return subprocess.CompletedProcess(command, 0, stdout=stdout, stderr="")

    atomic_calls: list[tuple[Path, Any]] = []

    def fake_write_json_atomic(path: Path, value: Any) -> None:
        atomic_calls.append((path, value))

    monkeypatch.setattr(generator_module.subprocess, "run", fake_run)
    monkeypatch.setattr(generator_module, "write_json_atomic", fake_write_json_atomic)

    toolchain = pin_toolchain(lock)

    tagged = f"{EXPECTED_IMAGE}:{EXPECTED_VERSION}"
    assert calls == [
        (
            ["docker", "pull", tagged],
            {"check": True, "capture_output": True, "text": True},
        ),
        (
            [
                "docker",
                "image",
                "inspect",
                tagged,
                "--format",
                "{{index .RepoDigests 0}}",
            ],
            {"check": True, "capture_output": True, "text": True},
        ),
    ]
    assert all(isinstance(command, list) for command, _ in calls)
    assert all(kwargs.get("shell") is not True for _, kwargs in calls)
    assert toolchain == Toolchain(EXPECTED_IMAGE, EXPECTED_VERSION, VALID_DIGEST)
    assert atomic_calls == [
        (
            lock,
            {
                "image": EXPECTED_IMAGE,
                "version": EXPECTED_VERSION,
                "digest": VALID_DIGEST,
            },
        )
    ]


@pytest.mark.parametrize(
    "inspection",
    [
        "",
        "malformed",
        "other/image@" + VALID_DIGEST,
        EXPECTED_IMAGE + "@sha256:" + "A" * 64,
        EXPECTED_IMAGE + "@sha256:" + "a" * 63,
        EXPECTED_IMAGE + "@" + VALID_DIGEST + "\nunexpected",
    ],
)
def test_pin_toolchain_rejects_untrusted_inspection_without_changing_lock(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, inspection: str
) -> None:
    lock = tmp_path / "toolchain.lock"
    lock.write_text("old lock\n", encoding="utf-8")

    def fake_run(command: list[str], **kwargs: Any) -> subprocess.CompletedProcess[str]:
        del kwargs
        stdout = inspection if command[1:3] == ["image", "inspect"] else ""
        return subprocess.CompletedProcess(command, 0, stdout=stdout, stderr="")

    monkeypatch.setattr(generator_module.subprocess, "run", fake_run)

    with pytest.raises(PipelineError, match="unexpected repository digest"):
        pin_toolchain(lock)

    assert lock.read_text(encoding="utf-8") == "old lock\n"


@pytest.mark.parametrize(
    "failure",
    [
        FileNotFoundError("docker"),
        subprocess.CalledProcessError(17, ["docker", "pull"]),
    ],
)
def test_pin_toolchain_wraps_docker_failures_actionably(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, failure: Exception
) -> None:
    def fake_run(command: list[str], **kwargs: Any) -> subprocess.CompletedProcess[str]:
        del command, kwargs
        raise failure

    monkeypatch.setattr(generator_module.subprocess, "run", fake_run)

    with pytest.raises(PipelineError) as error:
        pin_toolchain(tmp_path / "toolchain.lock")

    assert "Docker" in str(error.value)
    assert "OpenAPI Generator" in str(error.value)


def test_effective_config_is_deterministic_atomic_and_does_not_mutate_inputs(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    base = tmp_path / "generator/config.yaml"
    original = _write_base_config(base)
    destination = tmp_path / "build/generator-config.yaml"
    mappings = {"Zulu": "Last", "Alpha": "First"}
    writes: list[tuple[Path, bytes]] = []

    def fake_write_bytes_atomic(path: Path, body: bytes) -> None:
        writes.append((path, body))

    monkeypatch.setattr(generator_module, "write_bytes_atomic", fake_write_bytes_atomic)

    write_effective_generator_config(
        base,
        destination,
        model_mappings=mappings,
        package_version="1.2.3",
    )

    assert mappings == {"Zulu": "Last", "Alpha": "First"}
    assert base.read_bytes() == original
    assert len(writes) == 1
    assert writes[0][0] == destination
    rendered = writes[0][1]
    config = yaml.safe_load(rendered)
    assert config["modelNameMappings"] == {"Alpha": "First", "Zulu": "Last"}
    assert config["additionalProperties"]["packageVersion"] == "1.2.3"
    assert rendered.index(b"Alpha:") < rendered.index(b"Zulu:")


@pytest.mark.parametrize(
    ("body", "message"),
    [
        ("[unterminated", "valid YAML"),
        ("- item\n", "YAML object"),
        ("modelNameMappings: {}\n", "additionalProperties"),
        ("additionalProperties: []\n", "additionalProperties"),
        (
            "additionalProperties: {}\nmodelNameMappings: []\n",
            "modelNameMappings",
        ),
    ],
)
def test_effective_config_rejects_malformed_base_actionably(
    tmp_path: Path, body: str, message: str
) -> None:
    base = tmp_path / "config.yaml"
    base.write_text(body, encoding="utf-8")

    with pytest.raises(PipelineError, match=message):
        write_effective_generator_config(
            base,
            tmp_path / "effective.yaml",
            model_mappings={},
            package_version="1.0.0",
        )


@pytest.mark.parametrize(
    ("mappings", "version", "message"),
    [
        ({"": "Target"}, "1.0.0", "model mappings"),
        ({"Source": ""}, "1.0.0", "model mappings"),
        ({"Source": 3}, "1.0.0", "model mappings"),
        ({}, "", "package version"),
    ],
)
def test_effective_config_rejects_invalid_overrides(
    tmp_path: Path,
    mappings: dict[str, Any],
    version: str,
    message: str,
) -> None:
    base = tmp_path / "config.yaml"
    _write_base_config(base)

    with pytest.raises(PipelineError, match=message):
        write_effective_generator_config(
            base,
            tmp_path / "effective.yaml",
            model_mappings=mappings,  # type: ignore[arg-type]
            package_version=version,
        )


def test_commands_use_digest_disabled_network_uid_and_absolute_controlled_mount(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr(generator_module.os, "getuid", lambda: 123)
    monkeypatch.setattr(generator_module.os, "getgid", lambda: 456)
    root = tmp_path / "repo"
    root.mkdir()
    toolchain = Toolchain(EXPECTED_IMAGE, EXPECTED_VERSION, VALID_DIGEST)

    validate = build_validate_command(root, toolchain)
    generate = build_generate_command(root, toolchain)

    common_prefix = [
        "docker",
        "run",
        "--rm",
        "--network",
        "none",
        "--user",
        "123:456",
        "--mount",
        f"type=bind,source={root.resolve()},target=/workspace",
        f"{EXPECTED_IMAGE}@{VALID_DIGEST}",
    ]
    assert validate == common_prefix + [
        "validate",
        "-i",
        "/workspace/build/openapi/effective.json",
    ]
    assert generate == common_prefix + [
        "generate",
        "-i",
        "/workspace/build/openapi/effective.json",
        "-g",
        "python",
        "-c",
        "/workspace/build/generator-config.yaml",
        "-o",
        "/workspace/build/generated",
    ]
    assert "--skip-validate-spec" not in validate
    assert "--skip-validate-spec" not in generate


def test_commands_reject_missing_or_ambiguous_bind_root(tmp_path: Path) -> None:
    toolchain = Toolchain(EXPECTED_IMAGE, EXPECTED_VERSION, VALID_DIGEST)

    with pytest.raises(PipelineError, match="repository root"):
        build_validate_command(tmp_path / "missing", toolchain)
    ambiguous = tmp_path / "with,comma"
    ambiguous.mkdir()
    with pytest.raises(PipelineError, match="cannot contain a comma"):
        build_generate_command(ambiguous, toolchain)


def test_run_generator_cleans_staging_and_requires_expected_package(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    base = tmp_path / "generator/config.yaml"
    _write_base_config(base)
    stale = tmp_path / "build/generated/stale.txt"
    stale.parent.mkdir(parents=True)
    stale.write_text("stale", encoding="utf-8")
    commands: list[list[str]] = []

    def fake_run(command: list[str], **kwargs: Any) -> subprocess.CompletedProcess[str]:
        assert not stale.exists()
        commands.append(command)
        if "generate" in command:
            (tmp_path / "build/generated/iikocloud_client").mkdir(parents=True)
        return subprocess.CompletedProcess(command, 0, stdout="", stderr="")

    monkeypatch.setattr(generator_module.subprocess, "run", fake_run)

    result = run_generator(
        tmp_path,
        Toolchain(EXPECTED_IMAGE, EXPECTED_VERSION, VALID_DIGEST),
        {"Source": "Target"},
        "1.2.3",
    )

    assert result == tmp_path / "build/generated/iikocloud_client"
    assert len(commands) == 2
    assert "validate" in commands[0]
    assert "generate" in commands[1]


@pytest.mark.parametrize("failing_phase", ["validate", "generate"])
def test_run_generator_wraps_subprocess_failure_and_removes_partial_staging(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, failing_phase: str
) -> None:
    _write_base_config(tmp_path / "generator/config.yaml")
    staging = tmp_path / "build/generated"

    def fake_run(command: list[str], **kwargs: Any) -> subprocess.CompletedProcess[str]:
        del kwargs
        phase = "generate" if "generate" in command else "validate"
        staging.mkdir(parents=True, exist_ok=True)
        (staging / "partial.txt").write_text("partial", encoding="utf-8")
        if phase == failing_phase:
            raise subprocess.CalledProcessError(11, command)
        return subprocess.CompletedProcess(command, 0, stdout="", stderr="")

    monkeypatch.setattr(generator_module.subprocess, "run", fake_run)

    with pytest.raises(PipelineError) as error:
        run_generator(
            tmp_path,
            Toolchain(EXPECTED_IMAGE, EXPECTED_VERSION, VALID_DIGEST),
            {},
            "1.0.0",
        )

    assert failing_phase in str(error.value)
    assert not staging.exists()


def test_run_generator_rejects_missing_package_and_removes_output(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    _write_base_config(tmp_path / "generator/config.yaml")
    staging = tmp_path / "build/generated"

    def fake_run(command: list[str], **kwargs: Any) -> subprocess.CompletedProcess[str]:
        del kwargs
        if "generate" in command:
            staging.mkdir(parents=True)
            (staging / "wrong.txt").write_text("wrong", encoding="utf-8")
        return subprocess.CompletedProcess(command, 0, stdout="", stderr="")

    monkeypatch.setattr(generator_module.subprocess, "run", fake_run)

    with pytest.raises(PipelineError, match="expected package"):
        run_generator(
            tmp_path,
            Toolchain(EXPECTED_IMAGE, EXPECTED_VERSION, VALID_DIGEST),
            {},
            "1.0.0",
        )

    assert not staging.exists()


@pytest.mark.docker
def test_pinned_generator_validates_minimal_fixture(tmp_path: Path) -> None:
    document = json.loads(
        Path("tests/fixtures/openapi/minimal-v1.json").read_text(encoding="utf-8")
    )
    document["servers"] = [{"url": "https://api.example.invalid"}]
    document["paths"]["/api/1/ping"]["post"]["operationId"] = "ping"
    effective = tmp_path / "build/openapi/effective.json"
    effective.parent.mkdir(parents=True)
    effective.write_text(json.dumps(document), encoding="utf-8")
    toolchain = Toolchain.load(Path("generator/toolchain.lock"))

    completed = subprocess.run(build_validate_command(tmp_path, toolchain), check=False)

    assert completed.returncode == 0
