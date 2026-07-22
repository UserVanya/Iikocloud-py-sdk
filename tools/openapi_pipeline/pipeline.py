from __future__ import annotations

import copy
import json
import keyword
import os
import re
import shutil
import stat
import sys
from collections.abc import Callable
from contextlib import suppress
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml

if sys.version_info >= (3, 11):
    import tomllib
else:  # pragma: no cover - exercised on supported Python 3.10
    import tomli as tomllib

from .errors import PipelineError
from .fetch import FetchResult, fetch_candidate
from .generator import Toolchain, run_generator
from .io import (
    canonical_json_bytes,
    load_json,
    sha256_bytes,
    write_bytes_atomic,
    write_json_atomic,
)
from .live.safety import OperationSafetyCatalog
from .naming import (
    inject_operation_ids,
    normalize_generator_schema_names,
    normalize_model_name,
)
from .normalization import build_types_overlay
from .overlay import apply_overlay, apply_overlay_files
from .package_checks import verify_generated_contracts, verify_root_wheel
from .package_checks import verify_package as check_package
from .paths import RepoPaths
from .promotion import (
    PromotionItem,
    build_generated_manifest,
    copy_regular_tree,
    load_generated_manifest,
    promote_transaction,
    regular_tree_files,
)
from .reports import build_upstream_report, render_upstream_markdown, write_upstream_reports
from .validate import ensure_valid_effective_schema

UPSTREAM_SCHEMA_URL = "https://api-ru.iiko.services/api-docs/docs"
_MAX_REVIEWED_JSON_BYTES = 32 * 1024 * 1024
_MAX_REVIEWED_YAML_BYTES = 8 * 1024 * 1024
_EVIDENCE_OWNED_OVERLAY_NAMES = frozenset({"operations.overlay.yaml", "polymorphism.overlay.yaml"})
_OPERATION_VERBS = {
    "add",
    "authenticate",
    "cancel",
    "change",
    "close",
    "create",
    "delete",
    "get",
    "list",
    "open",
    "remove",
    "retrieve",
    "send",
    "set",
    "update",
}


@dataclass
class PipelineDependencies:
    paths: RepoPaths
    fetch: Callable[[], FetchResult]
    apply_corrections: Callable[[dict[str, Any]], tuple[dict[str, Any], dict[str, str]]]
    validate: Callable[[dict[str, Any]], None]
    generate: Callable[[dict[str, str]], Path]
    verify_package: Callable[[Path], None]
    verify_contracts: Callable[[Path], None]
    promote: Callable[[list[PromotionItem]], None] = promote_transaction
    verify_root_package: Callable[[Path], None] = verify_root_wheel


def _clean_staging(path: Path, root: Path) -> None:
    resolved = path.resolve(strict=False)
    controlled = root.resolve(strict=True)
    if path.is_symlink() or not resolved.is_relative_to(controlled) or resolved == controlled:
        raise PipelineError(f"Refusing to clean unsafe staging path: {path}")
    if path.exists():
        if path.is_dir():
            shutil.rmtree(path)
        else:
            path.unlink()


def _manual_paths(path: Path) -> tuple[Path, ...]:
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except (OSError, UnicodeError) as error:
        raise PipelineError(f"Cannot read manual file allowlist: {path}") from error
    result: list[Path] = []
    for line in lines:
        value = line.strip()
        if not value or value.startswith("#"):
            continue
        relative = Path(value)
        if (
            relative.is_absolute()
            or "\\" in value
            or relative.parts[:1] != ("iikocloud_client",)
            or any(part in {"", ".", ".."} for part in relative.parts)
            or relative.as_posix() != value
        ):
            raise PipelineError(f"Unsafe manual file allowlist entry: {value!r}")
        if relative in result:
            raise PipelineError(f"Duplicate manual file allowlist entry: {value}")
        result.append(relative)
    return tuple(result)


def _copy_manual_files(paths: RepoPaths, staged_package: Path) -> None:
    package_root = paths.root / "src/iikocloud_client"
    for relative in _manual_paths(paths.root / "generator/manual-files.txt"):
        package_relative = relative.relative_to("iikocloud_client")
        source = _validated_manual_source(package_root, package_relative)
        if source is None:
            continue
        destination = staged_package / package_relative
        if destination.exists() or destination.is_symlink():
            raise PipelineError(f"Generated/manual file collision: {relative.as_posix()}")
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, destination, follow_symlinks=False)


def _validated_manual_source(package_root: Path, relative: Path) -> Path | None:
    current = package_root
    components = (
        package_root,
        *(
            package_root / Path(*relative.parts[:index])
            for index in range(1, len(relative.parts) + 1)
        ),
    )
    resolved_root: Path | None = None
    for index, component in enumerate(components):
        current = component
        try:
            mode = current.lstat().st_mode
        except FileNotFoundError:
            return None
        except OSError as error:
            raise PipelineError(f"Cannot inspect manual file source: {current}") from error
        if stat.S_ISLNK(mode):
            raise PipelineError(f"Manual file source contains a symlink: {current}")
        is_leaf = index == len(components) - 1
        if is_leaf:
            if not stat.S_ISREG(mode):
                raise PipelineError(f"Manual file source is not a regular file: {current}")
        elif not stat.S_ISDIR(mode):
            raise PipelineError(f"Manual file source parent is not a directory: {current}")
        if index == 0:
            resolved_root = current.resolve(strict=True)
    if resolved_root is None or not current.resolve(strict=True).is_relative_to(resolved_root):
        raise PipelineError(f"Manual file source escapes package root: {current}")
    return current


def _verify_contract_copy(dependencies: PipelineDependencies, package: Path) -> None:
    check_root = dependencies.paths.build / "contract-check"
    _clean_staging(check_root, dependencies.paths.root)
    checked_package = check_root / "src/iikocloud_client"
    copy_regular_tree(package, checked_package, label="Generated contract package")
    dependencies.verify_contracts(checked_package)


def _load_document(path: Path, *, label: str) -> dict[str, Any]:
    try:
        value = load_json(path)
    except (OSError, UnicodeError, ValueError) as error:
        raise PipelineError(f"Cannot load {label}: {path}") from error
    if not isinstance(value, dict):
        raise PipelineError(f"{label.capitalize()} must be a JSON object")
    return value


def _load_yaml(path: Path, *, label: str) -> Any:
    try:
        return yaml.safe_load(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, yaml.YAMLError) as error:
        raise PipelineError(f"Cannot load {label}: {path}") from error


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
                "found duplicate key",
                key_node.start_mark,
            )
        result[key] = loader.construct_object(value_node, deep=deep)
    return result


_UniqueKeySafeLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
    _construct_unique_mapping,
)


def _read_fd_limited(descriptor: int, maximum: int, *, label: str) -> bytes:
    chunks: list[bytes] = []
    remaining = maximum + 1
    while remaining > 0:
        chunk = os.read(descriptor, min(65536, remaining))
        if not chunk:
            break
        chunks.append(chunk)
        remaining -= len(chunk)
    body = b"".join(chunks)
    if len(body) > maximum:
        raise PipelineError(f"{label} exceeds its reviewed size limit")
    return body


def _reviewed_regular_bytes(
    root: Path,
    path: Path,
    *,
    label: str,
    maximum: int,
    required: bool = True,
) -> bytes | None:
    """Read one repository-owned reviewed file without following path links."""
    lexical_root = Path(os.path.abspath(root))
    lexical_path = Path(os.path.abspath(path))
    try:
        relative = lexical_path.relative_to(lexical_root)
    except ValueError as error:
        raise PipelineError(f"{label} escapes the controlled repository root") from error
    if not relative.parts:
        raise PipelineError(f"{label} must be a reviewed regular file")

    directory_flags = os.O_RDONLY | os.O_CLOEXEC | os.O_DIRECTORY | getattr(os, "O_NOFOLLOW", 0)
    file_flags = os.O_RDONLY | os.O_CLOEXEC | getattr(os, "O_NOFOLLOW", 0)
    descriptors: list[int] = []
    try:
        try:
            descriptors.append(os.open(lexical_root, directory_flags))
        except OSError as error:
            raise PipelineError("Controlled repository root is not a safe directory") from error
        parent_fd = descriptors[-1]
        for part in relative.parts[:-1]:
            try:
                metadata = os.stat(part, dir_fd=parent_fd, follow_symlinks=False)
            except FileNotFoundError as error:
                if not required:
                    return None
                raise PipelineError(f"{label} is missing") from error
            except OSError as error:
                raise PipelineError(f"Cannot inspect reviewed parent for {label}") from error
            if stat.S_ISLNK(metadata.st_mode) or not stat.S_ISDIR(metadata.st_mode):
                raise PipelineError(f"{label} parent is not a non-symlink directory")
            try:
                parent_fd = os.open(part, directory_flags, dir_fd=parent_fd)
            except OSError as error:
                raise PipelineError(f"Cannot open reviewed parent for {label}") from error
            descriptors.append(parent_fd)

        leaf = relative.parts[-1]
        try:
            expected = os.stat(leaf, dir_fd=parent_fd, follow_symlinks=False)
        except FileNotFoundError as error:
            if not required:
                return None
            raise PipelineError(f"{label} is missing") from error
        except OSError as error:
            raise PipelineError(f"Cannot inspect {label}") from error
        if stat.S_ISLNK(expected.st_mode):
            raise PipelineError(f"{label} is a symlink")
        if not stat.S_ISREG(expected.st_mode):
            raise PipelineError(f"{label} must be a reviewed regular file")
        if expected.st_nlink != 1:
            raise PipelineError(f"{label} must not have multiple hard links")
        try:
            descriptor = os.open(leaf, file_flags, dir_fd=parent_fd)
        except OSError as error:
            raise PipelineError(f"Cannot open {label} safely") from error
        descriptors.append(descriptor)
        opened = os.fstat(descriptor)
        if (
            not stat.S_ISREG(opened.st_mode)
            or opened.st_nlink != 1
            or (opened.st_dev, opened.st_ino) != (expected.st_dev, expected.st_ino)
        ):
            raise PipelineError(f"{label} changed while it was opened")
        first = _read_fd_limited(descriptor, maximum, label=label)
        os.lseek(descriptor, 0, os.SEEK_SET)
        second = _read_fd_limited(descriptor, maximum, label=label)
        current = os.stat(leaf, dir_fd=parent_fd, follow_symlinks=False)
        if (
            first != second
            or (current.st_dev, current.st_ino) != (opened.st_dev, opened.st_ino)
            or current.st_nlink != 1
        ):
            raise PipelineError(f"{label} changed while it was reviewed")
        return first
    finally:
        for descriptor in reversed(descriptors):
            with suppress(OSError):
                os.close(descriptor)


def _reviewed_directory_names(root: Path, path: Path, *, label: str) -> tuple[str, ...]:
    lexical_root = Path(os.path.abspath(root))
    lexical_path = Path(os.path.abspath(path))
    try:
        relative = lexical_path.relative_to(lexical_root)
    except ValueError as error:
        raise PipelineError(f"{label} escapes the controlled repository root") from error
    directory_flags = os.O_RDONLY | os.O_CLOEXEC | os.O_DIRECTORY | getattr(os, "O_NOFOLLOW", 0)
    descriptors: list[int] = []
    try:
        descriptors.append(os.open(lexical_root, directory_flags))
        current_fd = descriptors[-1]
        for part in relative.parts:
            metadata = os.stat(part, dir_fd=current_fd, follow_symlinks=False)
            if stat.S_ISLNK(metadata.st_mode) or not stat.S_ISDIR(metadata.st_mode):
                raise PipelineError(f"{label} must be a non-symlink directory")
            current_fd = os.open(part, directory_flags, dir_fd=current_fd)
            descriptors.append(current_fd)
        return tuple(sorted(os.listdir(current_fd)))
    except (FileNotFoundError, OSError) as error:
        if isinstance(error, PipelineError):
            raise
        raise PipelineError(f"Cannot inspect {label}") from error
    finally:
        for descriptor in reversed(descriptors):
            with suppress(OSError):
                os.close(descriptor)


def _strict_reviewed_json(body: bytes, *, label: str) -> dict[str, Any]:
    def unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
        result: dict[str, Any] = {}
        for key, value in pairs:
            if key in result:
                raise ValueError("duplicate JSON key")
            result[key] = value
        return result

    def reject_constant(value: str) -> None:
        raise ValueError(f"non-finite JSON number {value}")

    try:
        value = json.loads(
            body.decode("utf-8"),
            object_pairs_hook=unique_object,
            parse_constant=reject_constant,
        )
    except (UnicodeError, ValueError) as error:
        raise PipelineError(f"{label} is not strict UTF-8 JSON") from error
    if not isinstance(value, dict):
        raise PipelineError(f"{label} must be a JSON object")
    return value


def _strict_reviewed_yaml(body: bytes, *, label: str) -> Any:
    try:
        return yaml.load(body.decode("utf-8"), Loader=_UniqueKeySafeLoader)
    except (UnicodeError, yaml.YAMLError) as error:
        raise PipelineError(f"{label} is not strict UTF-8 YAML") from error


def _yaml_bytes(value: Any) -> bytes:
    return yaml.safe_dump(
        value,
        allow_unicode=True,
        default_flow_style=False,
        sort_keys=True,
    ).encode("utf-8")


def _write_yaml(path: Path, value: Any) -> None:
    write_bytes_atomic(path, _yaml_bytes(value))


def _load_string_registry(path: Path, key: str) -> dict[str, str]:
    value = _load_yaml(path, label=f"{key} registry")
    if not isinstance(value, dict) or set(value) != {key} or not isinstance(value[key], dict):
        raise PipelineError(f"{path} must contain exactly a {key} mapping")
    registry = value[key]
    if not all(
        isinstance(source, str)
        and bool(source.strip())
        and isinstance(target, str)
        and bool(target.strip())
        for source, target in registry.items()
    ):
        raise PipelineError(f"{path} {key} entries must map non-empty strings")
    return dict(sorted(registry.items()))


def _semantic_overlays(root: Path, *, exclude_types: bool = False) -> list[Path]:
    directory = root / "openapi/overlays"
    if not directory.exists():
        return []
    if directory.is_symlink() or not directory.is_dir():
        raise PipelineError("openapi/overlays must be a regular directory")
    return [
        path
        for path in sorted(directory.glob("*.overlay.yaml"))
        if not (exclude_types and path.name == "types.overlay.yaml")
    ]


def _apply_mechanical_overlay(document: dict[str, Any], overlay: dict[str, Any]) -> dict[str, Any]:
    info = overlay.get("info")
    actions = overlay.get("actions")
    if (
        overlay.get("overlay") != "1.1.0"
        or not isinstance(info, dict)
        or any(
            not isinstance(info.get(key), str) or not info[key].strip()
            for key in ("title", "version")
        )
        or not isinstance(actions, list)
    ):
        raise PipelineError(
            "Mechanical overlay must be a valid Overlay 1.1.0 document with info and actions"
        )
    if actions == []:
        return copy.deepcopy(document)
    return apply_overlay(document, overlay)


def _model_schemas(document: dict[str, Any]) -> dict[str, Any]:
    components = document.get("components", {})
    schemas = components.get("schemas", {}) if isinstance(components, dict) else {}
    if not isinstance(schemas, dict):
        raise PipelineError("OpenAPI components.schemas must be an object")
    return schemas


def _apply_model_name_registry(
    document: dict[str, Any], overrides: dict[str, str]
) -> tuple[dict[str, Any], dict[str, str]]:
    return normalize_generator_schema_names(document, overrides)


def _apply_correction_overlays(
    root: Path,
    document: dict[str, Any],
    mechanical: dict[str, Any],
) -> dict[str, Any]:
    semantic = _semantic_overlays(root, exclude_types=True)
    contracts = [path for path in semantic if path.name == "contracts.overlay.yaml"]
    remaining = [path for path in semantic if path.name != "contracts.overlay.yaml"]
    effective = apply_overlay_files(document, contracts)
    effective = _apply_mechanical_overlay(effective, mechanical)
    return apply_overlay_files(effective, remaining)


def _apply_committed_corrections(
    paths: RepoPaths, document: dict[str, Any]
) -> tuple[dict[str, Any], dict[str, str]]:
    mechanical_path = paths.root / "openapi/overlays/types.overlay.yaml"
    mechanical = _load_yaml(mechanical_path, label="committed mechanical overlay")
    if not isinstance(mechanical, dict):
        raise PipelineError("Committed mechanical overlay must be an object")
    effective = _apply_correction_overlays(paths.root, document, mechanical)
    operations = _load_string_registry(paths.root / "openapi/operation-ids.yaml", "operations")
    effective = inject_operation_ids(effective, operations)
    models = _load_string_registry(paths.root / "openapi/model-name-overrides.yaml", "models")
    return _apply_model_name_registry(effective, models)


def compose_committed_effective_schema(paths: RepoPaths) -> dict[str, Any]:
    """Compose the effective schema from committed inputs without writing build artifacts."""
    document = _load_document(paths.upstream, label="committed upstream snapshot")
    effective, _model_mappings = _apply_committed_corrections(paths, document)
    return effective


def _load_committed_for_report(paths: RepoPaths) -> dict[str, Any] | None:
    if not paths.upstream.exists():
        return None
    return _load_document(paths.upstream, label="committed upstream snapshot")


def _stage_generated_outputs(
    dependencies: PipelineDependencies,
    *,
    snapshot: Path,
    effective: dict[str, Any],
    model_mappings: dict[str, str],
) -> tuple[list[PromotionItem], Path]:
    generated_package = dependencies.generate(model_mappings)
    toolchain = Toolchain.load(dependencies.paths.root / "generator/toolchain.lock")
    manifest = build_generated_manifest(
        generated_package,
        effective_schema_sha256=sha256_bytes(canonical_json_bytes(effective)),
        toolchain=toolchain,
    )
    promotion_root = dependencies.paths.build / "promotion"
    staged_snapshot = promotion_root / "iikocloud.openapi.json"
    staged_package = promotion_root / "iikocloud_client"
    staged_manifest = promotion_root / "generated-manifest.json"
    _clean_staging(promotion_root, dependencies.paths.root)
    promotion_root.mkdir(parents=True)
    shutil.copy2(snapshot, staged_snapshot)
    shutil.copytree(generated_package, staged_package, symlinks=True)
    staged_manifest_check = build_generated_manifest(
        staged_package,
        effective_schema_sha256=manifest["effective_schema_sha256"],
        toolchain=toolchain,
    )
    if staged_manifest_check != manifest:
        raise PipelineError("Generated package changed while it was copied to staging")
    write_json_atomic(staged_manifest, manifest)
    _copy_manual_files(dependencies.paths, staged_package)
    dependencies.verify_package(staged_package)
    _verify_contract_copy(dependencies, staged_package)
    return (
        [
            PromotionItem(staged_snapshot, dependencies.paths.upstream),
            PromotionItem(staged_package, dependencies.paths.root / "src/iikocloud_client"),
            PromotionItem(
                staged_manifest,
                dependencies.paths.root / "generator/generated-manifest.json",
            ),
        ],
        generated_package,
    )


def sync(dependencies: PipelineDependencies) -> None:
    fetched = dependencies.fetch()
    candidate = _load_document(fetched.path, label="candidate OpenAPI document")
    write_upstream_reports(
        _load_committed_for_report(dependencies.paths),
        candidate,
        dependencies.paths.build / "reports",
    )
    effective, model_mappings = dependencies.apply_corrections(candidate)
    dependencies.validate(effective)
    write_json_atomic(dependencies.paths.effective, effective)
    items, _raw_generated = _stage_generated_outputs(
        dependencies,
        snapshot=fetched.path,
        effective=effective,
        model_mappings=model_mappings,
    )
    dependencies.promote(items)


def _verify_committed_tree(
    paths: RepoPaths, manifest: dict[str, Any], manual_paths: tuple[Path, ...]
) -> None:
    package = paths.root / "src/iikocloud_client"
    if package.is_symlink() or not package.is_dir():
        raise PipelineError("Committed generated package is missing")
    manual_names = {path.as_posix() for path in manual_paths}
    actual: dict[str, str] = {}
    for path in regular_tree_files(package, label="Committed generated package"):
        relative = (Path("iikocloud_client") / path.relative_to(package)).as_posix()
        actual[relative] = sha256_bytes(path.read_bytes())
    missing_manual = sorted(manual_names - set(actual))
    if missing_manual:
        raise PipelineError("Manual files are missing: " + ", ".join(missing_manual))
    generated = {name: digest for name, digest in actual.items() if name not in manual_names}
    if generated != manifest["files"]:
        raise PipelineError("Committed generated files differ from generated-manifest.json")

    canonical_contract = paths.root / "contracts/rate-limits.yaml"
    contract_relative = "iikocloud_client/_contracts/rate-limits.yaml"
    if contract_relative in manual_names and canonical_contract.exists():
        committed_contract = paths.root / "src" / contract_relative
        if committed_contract.read_bytes() != canonical_contract.read_bytes():
            raise PipelineError("Manual rate-limits contract differs from canonical contract")


def verify(dependencies: PipelineDependencies) -> None:
    document = _load_document(dependencies.paths.upstream, label="committed upstream snapshot")
    effective, model_mappings = dependencies.apply_corrections(document)
    dependencies.validate(effective)
    write_json_atomic(dependencies.paths.effective, effective)
    generated_package = dependencies.generate(model_mappings)
    toolchain = Toolchain.load(dependencies.paths.root / "generator/toolchain.lock")
    current_manifest = build_generated_manifest(
        generated_package,
        effective_schema_sha256=sha256_bytes(canonical_json_bytes(effective)),
        toolchain=toolchain,
    )
    committed_manifest = load_generated_manifest(
        dependencies.paths.root / "generator/generated-manifest.json"
    )
    _copy_manual_files(dependencies.paths, generated_package)
    dependencies.verify_package(generated_package)
    _verify_contract_copy(dependencies, generated_package)
    dependencies.verify_root_package(dependencies.paths.root)
    if current_manifest != committed_manifest:
        raise PipelineError("Generated manifest differs from committed generated-manifest.json")
    _verify_committed_tree(
        dependencies.paths,
        committed_manifest,
        _manual_paths(dependencies.paths.root / "generator/manual-files.txt"),
    )


def upstream_check(dependencies: PipelineDependencies) -> bool:
    fetched = dependencies.fetch()
    candidate = _load_document(fetched.path, label="candidate OpenAPI document")
    report = write_upstream_reports(
        _load_committed_for_report(dependencies.paths),
        candidate,
        dependencies.paths.build / "reports",
    )
    difference = report["diff"]
    return any(
        difference[key]
        for key in (
            "added_paths",
            "removed_paths",
            "added_operations",
            "removed_operations",
            "changed_operations",
            "added_schemas",
            "removed_schemas",
            "changed_schemas",
        )
    )


def _words(value: str) -> list[str]:
    return [
        word.lower() for word in re.findall(r"[A-Z]+(?=[A-Z][a-z]|$)|[A-Z]?[a-z]+|[0-9]+", value)
    ]


def _request_schema_name(operation: dict[str, Any]) -> str | None:
    request_body = operation.get("requestBody")
    if not isinstance(request_body, dict):
        return None
    content = request_body.get("content")
    if not isinstance(content, dict):
        return None
    for media_type in sorted(content):
        media = content[media_type]
        if not isinstance(media, dict) or not isinstance(media.get("schema"), dict):
            continue
        reference = media["schema"].get("$ref")
        if isinstance(reference, str):
            leaf = reference.rsplit("/", 1)[-1]
            if leaf.endswith("Request"):
                return leaf.removesuffix("Request")
    return None


def _path_operation_base(path: str) -> str:
    segments = [segment for segment in path.strip("/").split("/") if segment]
    if len(segments) >= 2 and segments[0].lower() == "api":
        segments = segments[2:]
    normalized = "_".join(
        part
        for segment in segments
        for part in re.sub(r"[^A-Za-z0-9]+", "_", segment).strip("_").lower().split("_")
        if part
    )
    if not normalized:
        normalized = "operation"
    if normalized[0].isdigit() or keyword.iskeyword(normalized):
        normalized = f"operation_{normalized}"
    return normalized


def _operation_base(path: str, operation: dict[str, Any]) -> str:
    schema_name = _request_schema_name(operation)
    if schema_name is not None:
        words = _words(schema_name)
        for index, word in enumerate(words):
            if word in _OPERATION_VERBS:
                return "_".join(words[index:])
    return _path_operation_base(path)


def _operation_candidates(document: dict[str, Any]) -> dict[str, str]:
    candidates: list[tuple[str, str, str, str]] = []
    paths = document.get("paths", {})
    if not isinstance(paths, dict):
        raise PipelineError("OpenAPI paths must be an object")
    for path, path_item in sorted(paths.items()):
        if not isinstance(path, str) or not isinstance(path_item, dict):
            raise PipelineError("OpenAPI path items must be objects")
        for method, operation in sorted(path_item.items()):
            if method.lower() not in {
                "get",
                "put",
                "post",
                "delete",
                "patch",
                "head",
                "options",
                "trace",
            }:
                continue
            if not isinstance(operation, dict):
                raise PipelineError(f"Operation {method.upper()} {path} must be an object")
            candidates.append(
                (
                    f"{method.upper()} {path}",
                    method.lower(),
                    _operation_base(path, operation),
                    _path_operation_base(path),
                )
            )
    preferred_counts: dict[str, int] = {}
    for _key, _method, preferred, _path_base in candidates:
        preferred_counts[preferred] = preferred_counts.get(preferred, 0) + 1
    resolved = [
        (key, method, path_base if preferred_counts[preferred] > 1 else preferred)
        for key, method, preferred, path_base in candidates
    ]
    resolved_counts: dict[str, int] = {}
    for _key, _method, base in resolved:
        resolved_counts[base] = resolved_counts.get(base, 0) + 1
    result: dict[str, str] = {}
    used: set[str] = set()
    for key, method, base in resolved:
        value = f"{method}_{base}" if resolved_counts[base] > 1 else base
        if value in used:
            raise PipelineError(f"Cannot deterministically resolve operationId collision: {value}")
        used.add(value)
        result[key] = value
    return dict(sorted(result.items()))


def _model_collisions(document: dict[str, Any]) -> dict[str, list[str]]:
    groups: dict[str, list[str]] = {}
    for raw in sorted(_model_schemas(document)):
        normalized = normalize_model_name(raw)
        groups.setdefault(normalized, []).append(raw)
    return {normalized: values for normalized, values in sorted(groups.items()) if len(values) > 1}


def _reviewed_registry(value: object, key: str, *, label: str) -> dict[str, str]:
    if not isinstance(value, dict) or set(value) != {key} or not isinstance(value[key], dict):
        raise PipelineError(f"{label} must contain exactly a {key} mapping")
    registry = value[key]
    if not all(
        isinstance(source, str)
        and bool(source.strip())
        and isinstance(target, str)
        and bool(target.strip())
        for source, target in registry.items()
    ):
        raise PipelineError(f"{label} entries must map non-empty strings")
    return dict(sorted(registry.items()))


def compose_reviewed_bootstrap_candidate(
    paths: RepoPaths,
) -> tuple[dict[str, Any], dict[str, str]]:
    """Compose a reviewed pre-accept candidate without fetching, writing, or validating it."""
    return _compose_reviewed_candidate(paths, excluded_semantic_overlays=frozenset())


def compose_reviewed_evidence_base_candidate(
    paths: RepoPaths,
) -> tuple[dict[str, Any], dict[str, str]]:
    """Compose the authoritative base before applying evidence-owned candidates.

    The raw upstream candidate, reviewed bootstrap inputs, contracts overlay, and
    every non-evidence semantic overlay remain authoritative. The two tracked
    evidence-owned overlays are deliberately excluded whether or not they have
    already been accepted. ``build/openapi/effective.json`` is never read.
    """
    return _compose_reviewed_candidate(
        paths,
        excluded_semantic_overlays=_EVIDENCE_OWNED_OVERLAY_NAMES,
    )


def _compose_reviewed_candidate(
    paths: RepoPaths,
    *,
    excluded_semantic_overlays: frozenset[str],
) -> tuple[dict[str, Any], dict[str, str]]:
    root = paths.root
    bootstrap_root = paths.build / "bootstrap"
    raw_body = _reviewed_regular_bytes(
        root,
        paths.candidate,
        label="Reviewed upstream candidate",
        maximum=_MAX_REVIEWED_JSON_BYTES,
    )
    assert raw_body is not None
    document = _strict_reviewed_json(raw_body, label="Reviewed upstream candidate")

    types_body = _reviewed_regular_bytes(
        root,
        bootstrap_root / "types.overlay.yaml",
        label="Reviewed bootstrap type candidate",
        maximum=_MAX_REVIEWED_YAML_BYTES,
    )
    operations_body = _reviewed_regular_bytes(
        root,
        bootstrap_root / "operation-ids.yaml",
        label="Reviewed bootstrap operation candidate",
        maximum=_MAX_REVIEWED_YAML_BYTES,
    )
    collisions_body = _reviewed_regular_bytes(
        root,
        bootstrap_root / "model-collisions.yaml",
        label="Reviewed bootstrap collision candidate",
        maximum=_MAX_REVIEWED_YAML_BYTES,
    )
    assert types_body is not None
    assert operations_body is not None
    assert collisions_body is not None
    mechanical = _strict_reviewed_yaml(types_body, label="Reviewed bootstrap type candidate")
    operations_value = _strict_reviewed_yaml(
        operations_body,
        label="Reviewed bootstrap operation candidate",
    )
    collisions_value = _strict_reviewed_yaml(
        collisions_body,
        label="Reviewed bootstrap collision candidate",
    )
    if mechanical != build_types_overlay(document):
        raise PipelineError("Reviewed bootstrap type candidate was not derived from raw candidate")
    operations = _reviewed_registry(
        operations_value,
        "operations",
        label="Reviewed bootstrap operation candidate",
    )
    expected_collisions = {"collisions": _model_collisions(document)}
    if collisions_value != expected_collisions:
        raise PipelineError(
            "Reviewed bootstrap collision candidate was not derived from raw candidate"
        )

    overlay_root = root / "openapi/overlays"
    overlay_names = tuple(
        name
        for name in _reviewed_directory_names(
            root,
            overlay_root,
            label="Reviewed semantic overlay directory",
        )
        if name.endswith(".overlay.yaml")
        and name != "types.overlay.yaml"
        and name not in excluded_semantic_overlays
    )
    if "contracts.overlay.yaml" not in overlay_names:
        raise PipelineError("Reviewed contracts overlay is missing")
    overlay_values: dict[str, dict[str, Any]] = {}
    for name in overlay_names:
        body = _reviewed_regular_bytes(
            root,
            overlay_root / name,
            label=f"Reviewed semantic overlay {name}",
            maximum=_MAX_REVIEWED_YAML_BYTES,
        )
        assert body is not None
        value = _strict_reviewed_yaml(body, label=f"Reviewed semantic overlay {name}")
        if not isinstance(value, dict):
            raise PipelineError(f"Reviewed semantic overlay {name} must be an object")
        overlay_values[name] = value

    effective = apply_overlay(document, overlay_values["contracts.overlay.yaml"])
    if not isinstance(mechanical, dict):
        raise PipelineError("Reviewed bootstrap type candidate must be an object")
    effective = _apply_mechanical_overlay(effective, mechanical)
    for name in overlay_names:
        if name != "contracts.overlay.yaml":
            effective = apply_overlay(effective, overlay_values[name])
    effective = inject_operation_ids(effective, operations)

    committed_body = _reviewed_regular_bytes(
        root,
        root / "openapi/model-name-overrides.yaml",
        label="Reviewed committed model override registry",
        maximum=_MAX_REVIEWED_YAML_BYTES,
    )
    optional_body = _reviewed_regular_bytes(
        root,
        bootstrap_root / "model-name-overrides.yaml",
        label="Reviewed bootstrap model override candidate",
        maximum=_MAX_REVIEWED_YAML_BYTES,
        required=False,
    )
    assert committed_body is not None
    overrides = _reviewed_registry(
        _strict_reviewed_yaml(
            committed_body,
            label="Reviewed committed model override registry",
        ),
        "models",
        label="Reviewed committed model override registry",
    )
    if optional_body is not None:
        overrides.update(
            _reviewed_registry(
                _strict_reviewed_yaml(
                    optional_body,
                    label="Reviewed bootstrap model override candidate",
                ),
                "models",
                label="Reviewed bootstrap model override candidate",
            )
        )
    return _apply_model_name_registry(effective, dict(sorted(overrides.items())))


def _bootstrap_preview(dependencies: PipelineDependencies) -> None:
    fetched = dependencies.fetch()
    document = _load_document(fetched.path, label="candidate OpenAPI document")
    collisions = _model_collisions(document)
    types_body = _yaml_bytes(build_types_overlay(document))
    operations_body = _yaml_bytes({"operations": _operation_candidates(document)})
    collisions_body = _yaml_bytes({"collisions": collisions})
    report = build_upstream_report(
        _load_committed_for_report(dependencies.paths),
        document,
    )
    report_body = render_upstream_markdown(report).encode("utf-8")

    bootstrap_root = dependencies.paths.build / "bootstrap"
    bootstrap_root.mkdir(parents=True, exist_ok=True)
    write_bytes_atomic(bootstrap_root / "types.overlay.yaml", types_body)
    write_bytes_atomic(bootstrap_root / "operation-ids.yaml", operations_body)
    write_bytes_atomic(bootstrap_root / "model-collisions.yaml", collisions_body)
    write_bytes_atomic(
        dependencies.paths.build / "reports/upstream-diff.md",
        report_body,
    )
    if collisions:
        raise PipelineError(
            "Bootstrap has unresolved model collisions; review model-collisions.yaml"
        )


def _assert_empty_operation_registry(path: Path) -> None:
    if not path.exists():
        return
    try:
        body = path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as error:
        raise PipelineError(f"Cannot read operation registry: {path}") from error
    if not body.strip():
        return
    operations = _load_string_registry(path, "operations")
    if operations:
        raise PipelineError("Bootstrap refuses to overwrite a non-empty operation registry")


def _preflight_optional_model_overrides(paths: RepoPaths) -> Path | None:
    candidate = paths.build / "bootstrap/model-name-overrides.yaml"
    label = "Bootstrap model-name-overrides candidate"
    lexical_root = paths.root.absolute()
    lexical_candidate = candidate.absolute()
    if lexical_candidate == lexical_root or not lexical_candidate.is_relative_to(lexical_root):
        raise PipelineError(f"{label} escapes the controlled repository root: {candidate}")

    try:
        relative = lexical_candidate.relative_to(lexical_root)
        controlled_root = paths.root.resolve(strict=True)
    except (OSError, ValueError) as error:
        raise PipelineError(
            f"Cannot establish controlled path for {label}: {candidate}"
        ) from error

    current = paths.root
    for index, part in enumerate(relative.parts):
        current /= part
        try:
            mode = current.lstat().st_mode
        except FileNotFoundError:
            return None
        except OSError as error:
            raise PipelineError(f"Cannot inspect {label}: {current}") from error
        if stat.S_ISLNK(mode):
            raise PipelineError(f"{label} path contains a symlink: {current}")
        is_leaf = index == len(relative.parts) - 1
        if is_leaf:
            if not stat.S_ISREG(mode):
                raise PipelineError(f"{label} must be a regular file: {candidate}")
        elif not stat.S_ISDIR(mode):
            raise PipelineError(f"{label} parent must be a directory: {current}")

    try:
        resolved = candidate.resolve(strict=True)
    except OSError as error:
        raise PipelineError(f"Cannot resolve {label}: {candidate}") from error
    if not resolved.is_relative_to(controlled_root):
        raise PipelineError(f"{label} escapes the controlled repository root: {candidate}")
    return candidate


def _bootstrap_overrides(paths: RepoPaths, model_candidate: Path | None) -> dict[str, str]:
    committed = paths.root / "openapi/model-name-overrides.yaml"
    result = _load_string_registry(committed, "models") if committed.exists() else {}
    if model_candidate is not None:
        result.update(_load_string_registry(model_candidate, "models"))
    return dict(sorted(result.items()))


def _accept_bootstrap(dependencies: PipelineDependencies) -> None:
    paths = dependencies.paths
    model_candidate = _preflight_optional_model_overrides(paths)
    _assert_empty_operation_registry(paths.root / "openapi/operation-ids.yaml")
    bootstrap_root = paths.build / "bootstrap"
    types_candidate = bootstrap_root / "types.overlay.yaml"
    operations_candidate = bootstrap_root / "operation-ids.yaml"
    collisions_candidate = bootstrap_root / "model-collisions.yaml"
    for candidate in (
        paths.candidate,
        types_candidate,
        operations_candidate,
        collisions_candidate,
    ):
        if candidate.is_symlink() or not candidate.is_file():
            raise PipelineError(f"Reviewed bootstrap candidate is missing: {candidate}")
    collision_data = _load_yaml(collisions_candidate, label="model collision candidates")
    if (
        not isinstance(collision_data, dict)
        or set(collision_data) != {"collisions"}
        or not isinstance(collision_data["collisions"], dict)
    ):
        raise PipelineError("model-collisions.yaml has an invalid shape")
    if not all(
        isinstance(name, str)
        and bool(name)
        and isinstance(raw_names, list)
        and all(isinstance(raw, str) and bool(raw) for raw in raw_names)
        for name, raw_names in collision_data["collisions"].items()
    ):
        raise PipelineError("model-collisions.yaml contains invalid collision entries")

    document = _load_document(paths.candidate, label="candidate OpenAPI document")
    overlay = _load_yaml(types_candidate, label="mechanical type overlay")
    if not isinstance(overlay, dict):
        raise PipelineError("Bootstrap type overlay must be an object")
    effective = _apply_correction_overlays(paths.root, document, overlay)
    effective = inject_operation_ids(
        effective,
        _load_string_registry(operations_candidate, "operations"),
    )
    effective, mappings = _apply_model_name_registry(
        effective,
        _bootstrap_overrides(paths, model_candidate),
    )
    dependencies.validate(effective)
    write_json_atomic(paths.effective, effective)
    items, _raw_generated = _stage_generated_outputs(
        dependencies,
        snapshot=paths.candidate,
        effective=effective,
        model_mappings=mappings,
    )
    mechanical_items = [
        PromotionItem(types_candidate, paths.root / "openapi/overlays/types.overlay.yaml"),
        PromotionItem(operations_candidate, paths.root / "openapi/operation-ids.yaml"),
    ]
    if model_candidate is not None:
        mechanical_items.append(
            PromotionItem(model_candidate, paths.root / "openapi/model-name-overrides.yaml")
        )
    dependencies.promote([items[0], *mechanical_items, *items[1:]])


def bootstrap(
    dependencies: PipelineDependencies, *, accept_current_upstream: bool = False
) -> None:
    if accept_current_upstream:
        _accept_bootstrap(dependencies)
    else:
        _bootstrap_preview(dependencies)


def _project_version(root: Path) -> str:
    try:
        document = tomllib.loads((root / "pyproject.toml").read_text(encoding="utf-8"))
        version = document["project"]["version"]
    except (OSError, UnicodeError, ValueError, KeyError, TypeError) as error:
        raise PipelineError("Cannot read project version from pyproject.toml") from error
    if not isinstance(version, str) or not version.strip():
        raise PipelineError("Project version must be a non-empty string")
    return version


def _validate_effective_for_pipeline(paths: RepoPaths, document: dict[str, Any]) -> None:
    ensure_valid_effective_schema(document, require_iikocloud_contracts=True)
    OperationSafetyCatalog.load(paths.operation_safety).assert_matches_openapi(document)


def default_dependencies(*, offline: bool, paths: RepoPaths | None = None) -> PipelineDependencies:
    repo_paths = paths or RepoPaths.discover()

    def fetch() -> FetchResult:
        if not offline:
            return fetch_candidate(UPSTREAM_SCHEMA_URL, repo_paths.candidate)
        if not repo_paths.upstream.is_file() or repo_paths.upstream.is_symlink():
            raise PipelineError("Offline sync requires a committed upstream snapshot")
        body = repo_paths.upstream.read_bytes()
        return FetchResult(sha256_bytes(body), repo_paths.upstream, False)

    toolchain = Toolchain.load(repo_paths.root / "generator/toolchain.lock")
    package_version = _project_version(repo_paths.root)
    return PipelineDependencies(
        paths=repo_paths,
        fetch=fetch,
        apply_corrections=lambda document: _apply_committed_corrections(repo_paths, document),
        validate=lambda document: _validate_effective_for_pipeline(repo_paths, document),
        generate=lambda mappings: run_generator(
            repo_paths.root,
            toolchain,
            mappings,
            package_version,
        ),
        verify_package=lambda package: check_package(
            package,
            build_root=repo_paths.build,
            project_root=repo_paths.root,
        ),
        verify_contracts=lambda package: verify_generated_contracts(repo_paths.root, package),
        promote=lambda items: promote_transaction(items, root=repo_paths.root),
        verify_root_package=verify_root_wheel,
    )
