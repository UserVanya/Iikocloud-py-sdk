from __future__ import annotations

import json
import os
from pathlib import Path

import pytest

from tools.openapi_pipeline.errors import PipelineError
from tools.openapi_pipeline.generator import Toolchain
from tools.openapi_pipeline.io import sha256_bytes
from tools.openapi_pipeline.promotion import (
    PromotionItem,
    load_generated_manifest,
    promote_transaction,
    write_generated_manifest,
)


def test_promotion_rolls_back_files_and_directories_when_replace_fails(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    old_file = tmp_path / "target/first.txt"
    old_tree = tmp_path / "target/package"
    old_file.parent.mkdir()
    old_file.write_text("old-first", encoding="utf-8")
    old_tree.mkdir()
    (old_tree / "old.py").write_text("old", encoding="utf-8")
    staged_file = tmp_path / "staging/first.txt"
    staged_tree = tmp_path / "staging/package"
    staged_file.parent.mkdir()
    staged_file.write_text("new-first", encoding="utf-8")
    staged_tree.mkdir()
    (staged_tree / "new.py").write_text("new", encoding="utf-8")

    real_replace = os.replace
    calls = 0

    def fail_second_promotion(source: str | Path, target: str | Path) -> None:
        nonlocal calls
        calls += 1
        if calls == 4:
            raise OSError("simulated promotion failure")
        real_replace(source, target)

    monkeypatch.setattr("tools.openapi_pipeline.promotion.os.replace", fail_second_promotion)

    with pytest.raises(OSError, match="simulated promotion failure"):
        promote_transaction(
            [
                PromotionItem(staged_file, old_file),
                PromotionItem(staged_tree, old_tree),
            ],
            root=tmp_path,
        )

    assert old_file.read_text(encoding="utf-8") == "old-first"
    assert (old_tree / "old.py").read_text(encoding="utf-8") == "old"
    assert not (old_tree / "new.py").exists()
    assert not list(tmp_path.rglob("*.backup-*"))


@pytest.mark.parametrize(
    "items",
    [
        lambda root: [
            PromotionItem(root / "missing", root / "target"),
        ],
        lambda root: [
            PromotionItem(root / "one", root / "target"),
            PromotionItem(root / "two", root / "target"),
        ],
        lambda root: [
            PromotionItem(root / "one", root / "target"),
            PromotionItem(root / "two", root / "target/child"),
        ],
    ],
)
def test_promotion_preflight_rejects_unsafe_batch_without_mutation(
    tmp_path: Path,
    items: object,
) -> None:
    (tmp_path / "one").write_text("one", encoding="utf-8")
    (tmp_path / "two").write_text("two", encoding="utf-8")
    target = tmp_path / "target"
    target.write_text("old", encoding="utf-8")

    with pytest.raises(PipelineError):
        promote_transaction(items(tmp_path), root=tmp_path)  # type: ignore[operator]

    assert target.read_text(encoding="utf-8") == "old"
    assert not list(tmp_path.rglob("*.backup-*"))


def test_promotion_rejects_symlink_escape(tmp_path: Path) -> None:
    outside = tmp_path.parent / f"{tmp_path.name}-outside"
    outside.mkdir()
    link = tmp_path / "escaped"
    link.symlink_to(outside, target_is_directory=True)
    staged = tmp_path / "staged"
    staged.write_text("new", encoding="utf-8")

    with pytest.raises(PipelineError, match="escapes|symlink"):
        promote_transaction(
            [PromotionItem(staged, link / "target.txt")],
            root=tmp_path,
        )

    assert not (outside / "target.txt").exists()


def test_generated_manifest_hashes_only_raw_generator_files_in_sorted_order(
    tmp_path: Path,
) -> None:
    package = tmp_path / "iikocloud_client"
    (package / "models").mkdir(parents=True)
    (package / "z.py").write_bytes(b"z\n")
    (package / "models/a.py").write_bytes(b"a\n")
    manifest_path = tmp_path / "generated-manifest.json"
    toolchain = Toolchain(
        "openapitools/openapi-generator-cli",
        "v7.22.0",
        "sha256:" + "b" * 64,
    )

    write_generated_manifest(
        package,
        manifest_path,
        effective_schema_sha256="a" * 64,
        toolchain=toolchain,
    )
    (package / "_contracts").mkdir()
    (package / "_contracts/manual.yaml").write_text("manual\n", encoding="utf-8")

    manifest = load_generated_manifest(manifest_path)
    assert manifest == {
        "effective_schema_sha256": "a" * 64,
        "generator": {
            "image": "openapitools/openapi-generator-cli",
            "version": "v7.22.0",
            "digest": "sha256:" + "b" * 64,
        },
        "files": {
            "iikocloud_client/models/a.py": sha256_bytes(b"a\n"),
            "iikocloud_client/z.py": sha256_bytes(b"z\n"),
        },
    }
    assert list(manifest["files"]) == sorted(manifest["files"])


def test_generated_manifest_loader_rejects_unsorted_or_extra_metadata(tmp_path: Path) -> None:
    manifest = tmp_path / "manifest.json"
    value = {
        "effective_schema_sha256": "a" * 64,
        "generator": {
            "image": "openapitools/openapi-generator-cli",
            "version": "v7.22.0",
            "digest": "sha256:" + "b" * 64,
        },
        "files": {
            "iikocloud_client/z.py": "c" * 64,
            "iikocloud_client/a.py": "d" * 64,
        },
    }
    manifest.write_text(json.dumps(value), encoding="utf-8")

    with pytest.raises(PipelineError, match="sorted"):
        load_generated_manifest(manifest)

    value["extra"] = True
    manifest.write_text(json.dumps(value), encoding="utf-8")
    with pytest.raises(PipelineError, match="root shape"):
        load_generated_manifest(manifest)


def test_generated_manifest_loader_rejects_path_traversal(tmp_path: Path) -> None:
    manifest = tmp_path / "manifest.json"
    manifest.write_text(
        json.dumps(
            {
                "effective_schema_sha256": "a" * 64,
                "generator": {
                    "image": "openapitools/openapi-generator-cli",
                    "version": "v7.22.0",
                    "digest": "sha256:" + "b" * 64,
                },
                "files": {"iikocloud_client/../outside.py": "c" * 64},
            }
        ),
        encoding="utf-8",
    )

    with pytest.raises(PipelineError, match="file hashes"):
        load_generated_manifest(manifest)


def test_generated_manifest_loader_rejects_noncanonical_json(tmp_path: Path) -> None:
    manifest = tmp_path / "manifest.json"
    value = {
        "effective_schema_sha256": "a" * 64,
        "files": {"iikocloud_client/a.py": "c" * 64},
        "generator": {
            "digest": "sha256:" + "b" * 64,
            "image": "openapitools/openapi-generator-cli",
            "version": "v7.22.0",
        },
    }
    manifest.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    with pytest.raises(PipelineError, match="canonical"):
        load_generated_manifest(manifest)


def test_promotion_rejects_replacing_repository_control_directories(tmp_path: Path) -> None:
    staged = tmp_path / "staged"
    staged.mkdir()

    for target in (tmp_path / ".git", tmp_path / "src", tmp_path / "generator"):
        with pytest.raises(PipelineError, match="control directory|broad"):
            promote_transaction([PromotionItem(staged, target)], root=tmp_path)
