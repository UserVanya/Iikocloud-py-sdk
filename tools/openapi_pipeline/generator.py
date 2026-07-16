from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml

from .errors import PipelineError
from .io import write_bytes_atomic, write_json_atomic

EXPECTED_IMAGE = "openapitools/openapi-generator-cli"
EXPECTED_VERSION = "v7.22.0"
_DIGEST_PATTERN = re.compile(r"sha256:[0-9a-f]{64}")
_LOCK_KEYS = {"image", "version", "digest"}


class _DuplicateKeyError(ValueError):
    pass


def _object_without_duplicate_keys(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise _DuplicateKeyError
        result[key] = value
    return result


@dataclass(frozen=True)
class Toolchain:
    image: str
    version: str
    digest: str

    def __post_init__(self) -> None:
        if not isinstance(self.image, str) or self.image != EXPECTED_IMAGE:
            raise PipelineError(f"Generator toolchain lock image must be exactly {EXPECTED_IMAGE}")
        if not isinstance(self.version, str) or self.version != EXPECTED_VERSION:
            raise PipelineError(
                f"Generator toolchain lock version must be exactly {EXPECTED_VERSION}"
            )
        if not isinstance(self.digest, str) or _DIGEST_PATTERN.fullmatch(self.digest) is None:
            raise PipelineError(
                "Generator toolchain lock digest must be a lowercase sha256 digest"
            )

    @property
    def pinned_image(self) -> str:
        return f"{self.image}@{self.digest}"

    @classmethod
    def load(cls, path: Path) -> Toolchain:
        try:
            body = path.read_text(encoding="utf-8")
        except FileNotFoundError as error:
            raise PipelineError(
                f"Cannot read generator toolchain lock {path}: file not found"
            ) from error
        except UnicodeDecodeError as error:
            raise PipelineError(f"Generator toolchain lock {path} is not valid UTF-8") from error
        except OSError as error:
            raise PipelineError(
                f"Cannot read generator toolchain lock {path}: {error.strerror or 'I/O error'}"
            ) from error

        try:
            data = json.loads(body, object_pairs_hook=_object_without_duplicate_keys)
        except _DuplicateKeyError as error:
            raise PipelineError(
                "Generator toolchain lock must not contain duplicate JSON keys"
            ) from error
        except json.JSONDecodeError as error:
            raise PipelineError("Generator toolchain lock is not valid JSON") from error

        if not isinstance(data, dict):
            raise PipelineError("Generator toolchain lock must be a JSON object")
        if set(data) != _LOCK_KEYS:
            raise PipelineError(
                "Generator toolchain lock must contain exactly image, version, and digest"
            )
        if not all(isinstance(data[key], str) for key in _LOCK_KEYS):
            raise PipelineError("Generator toolchain lock fields must all be strings")
        return cls(image=data["image"], version=data["version"], digest=data["digest"])


def _run_pin_command(command: list[str], *, purpose: str) -> subprocess.CompletedProcess[str]:
    try:
        return subprocess.run(command, check=True, capture_output=True, text=True)
    except FileNotFoundError as error:
        raise PipelineError(
            "Docker executable was not found while pinning OpenAPI Generator; "
            "install Docker and verify it is on PATH"
        ) from error
    except subprocess.CalledProcessError as error:
        raise PipelineError(
            f"Docker {purpose} failed while pinning OpenAPI Generator "
            f"with exit status {error.returncode}; verify Docker daemon and network access"
        ) from error
    except OSError as error:
        raise PipelineError(
            f"Docker {purpose} could not start while pinning OpenAPI Generator: "
            f"{error.strerror or 'operating-system error'}"
        ) from error


def pin_toolchain(path: Path) -> Toolchain:
    tagged = f"{EXPECTED_IMAGE}:{EXPECTED_VERSION}"
    _run_pin_command(["docker", "pull", tagged], purpose="image pull")
    completed = _run_pin_command(
        [
            "docker",
            "image",
            "inspect",
            tagged,
            "--format",
            "{{index .RepoDigests 0}}",
        ],
        purpose="image inspection",
    )
    repo_digest = completed.stdout.strip()
    prefix = f"{EXPECTED_IMAGE}@"
    if not repo_digest.startswith(prefix) or repo_digest.count("@") != 1:
        raise PipelineError(
            "Docker returned an unexpected repository digest for OpenAPI Generator; "
            "the toolchain lock was not changed"
        )
    digest = repo_digest.removeprefix(prefix)
    try:
        toolchain = Toolchain(
            image=EXPECTED_IMAGE,
            version=EXPECTED_VERSION,
            digest=digest,
        )
    except PipelineError as error:
        raise PipelineError(
            "Docker returned an unexpected repository digest for OpenAPI Generator; "
            "the toolchain lock was not changed"
        ) from error

    try:
        write_json_atomic(
            path,
            {
                "image": toolchain.image,
                "version": toolchain.version,
                "digest": toolchain.digest,
            },
        )
    except OSError as error:
        raise PipelineError(
            f"Cannot write generator toolchain lock {path}: {error.strerror or 'I/O error'}"
        ) from error
    return toolchain


def _load_generator_config(path: Path) -> dict[str, Any]:
    try:
        body = path.read_text(encoding="utf-8")
    except FileNotFoundError as error:
        raise PipelineError(f"Generator config {path} does not exist") from error
    except UnicodeDecodeError as error:
        raise PipelineError(f"Generator config {path} is not valid UTF-8") from error
    except OSError as error:
        raise PipelineError(
            f"Cannot read generator config {path}: {error.strerror or 'I/O error'}"
        ) from error

    try:
        config = yaml.safe_load(body)
    except yaml.YAMLError as error:
        raise PipelineError(f"Generator config {path} is not valid YAML") from error
    if not isinstance(config, dict):
        raise PipelineError(f"Generator config {path} must be a YAML object")
    if not all(isinstance(key, str) for key in config):
        raise PipelineError(f"Generator config {path} keys must be strings")

    additional_properties = config.get("additionalProperties")
    if not isinstance(additional_properties, dict):
        raise PipelineError(f"Generator config {path} additionalProperties must be a YAML object")
    if not all(isinstance(key, str) for key in additional_properties):
        raise PipelineError(f"Generator config {path} additionalProperties keys must be strings")
    existing_mappings = config.get("modelNameMappings")
    if existing_mappings is not None and not isinstance(existing_mappings, dict):
        raise PipelineError(f"Generator config {path} modelNameMappings must be a YAML object")
    return config


def write_effective_generator_config(
    base_path: Path,
    destination: Path,
    *,
    model_mappings: dict[str, str],
    package_version: str,
) -> None:
    config = _load_generator_config(base_path)
    if not isinstance(model_mappings, dict) or not all(
        isinstance(source, str)
        and bool(source.strip())
        and isinstance(target, str)
        and bool(target.strip())
        for source, target in model_mappings.items()
    ):
        raise PipelineError("Generator model mappings must use non-empty string names")
    if not isinstance(package_version, str) or not package_version.strip():
        raise PipelineError("Generator package version must be a non-empty string")

    additional_properties = dict(config["additionalProperties"])
    additional_properties["packageVersion"] = package_version
    config["additionalProperties"] = additional_properties
    config["modelNameMappings"] = dict(sorted(model_mappings.items()))
    rendered = yaml.safe_dump(
        config,
        allow_unicode=True,
        default_flow_style=False,
        sort_keys=True,
    ).encode("utf-8")
    try:
        write_bytes_atomic(destination, rendered)
    except OSError as error:
        raise PipelineError(
            f"Cannot write effective generator config {destination}: "
            f"{error.strerror or 'I/O error'}"
        ) from error


def _controlled_root(root: Path) -> Path:
    try:
        resolved = root.resolve(strict=True)
    except (OSError, RuntimeError) as error:
        raise PipelineError(f"Generator repository root {root} does not exist") from error
    if not resolved.is_dir():
        raise PipelineError(f"Generator repository root {resolved} is not a directory")
    if "," in str(resolved):
        raise PipelineError("Generator repository root cannot contain a comma")
    if "\n" in str(resolved) or "\r" in str(resolved):
        raise PipelineError("Generator repository root cannot contain line breaks")
    return resolved


def _docker_prefix(root: Path, toolchain: Toolchain) -> list[str]:
    resolved = _controlled_root(root)
    return [
        "docker",
        "run",
        "--rm",
        "--network",
        "none",
        "--user",
        f"{os.getuid()}:{os.getgid()}",
        "--mount",
        f"type=bind,source={resolved},target=/workspace",
        toolchain.pinned_image,
    ]


def build_validate_command(root: Path, toolchain: Toolchain) -> list[str]:
    return _docker_prefix(root, toolchain) + [
        "validate",
        "-i",
        "/workspace/build/openapi/effective.json",
    ]


def build_generate_command(root: Path, toolchain: Toolchain) -> list[str]:
    return _docker_prefix(root, toolchain) + [
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


def _staging_path(root: Path) -> Path:
    staging = root / "build/generated"
    try:
        resolved = staging.resolve(strict=False)
    except (OSError, RuntimeError) as error:
        raise PipelineError("Cannot resolve generator staging path") from error
    if not resolved.is_relative_to(root):
        raise PipelineError("Generator staging path escapes the repository root")
    return staging


def _remove_staging(staging: Path) -> None:
    try:
        if staging.is_symlink() or (staging.exists() and not staging.is_dir()):
            staging.unlink()
        elif staging.exists():
            shutil.rmtree(staging)
    except OSError as error:
        raise PipelineError(
            f"Cannot clean generator staging directory {staging}: {error.strerror or 'I/O error'}"
        ) from error


def _run_generator_command(command: list[str], *, phase: str) -> None:
    try:
        subprocess.run(command, check=True, capture_output=True, text=True)
    except FileNotFoundError as error:
        raise PipelineError(
            f"OpenAPI Generator {phase} could not start because Docker was not found"
        ) from error
    except subprocess.CalledProcessError as error:
        raise PipelineError(
            f"OpenAPI Generator {phase} failed with exit status {error.returncode}; "
            "inspect the effective schema and pinned Docker image"
        ) from error
    except OSError as error:
        raise PipelineError(
            f"OpenAPI Generator {phase} could not start: "
            f"{error.strerror or 'operating-system error'}"
        ) from error


def run_generator(
    root: Path,
    toolchain: Toolchain,
    mappings: dict[str, str],
    package_version: str,
) -> Path:
    resolved_root = _controlled_root(root)
    staging = _staging_path(resolved_root)
    _remove_staging(staging)
    try:
        write_effective_generator_config(
            resolved_root / "generator/config.yaml",
            resolved_root / "build/generator-config.yaml",
            model_mappings=mappings,
            package_version=package_version,
        )
        _run_generator_command(build_validate_command(resolved_root, toolchain), phase="validate")
        _run_generator_command(build_generate_command(resolved_root, toolchain), phase="generate")
        expected = staging / "iikocloud_client"
        if expected.is_symlink() or not expected.is_dir():
            raise PipelineError(
                "OpenAPI Generator did not create the expected package "
                "build/generated/iikocloud_client"
            )
        return expected
    except Exception:
        _remove_staging(staging)
        raise
