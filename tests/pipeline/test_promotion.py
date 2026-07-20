from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any

import pytest

from tools.openapi_pipeline import promotion as promotion_module
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


def test_promotion_preserves_ambiguous_directory_when_mkdir_succeeds_then_interrupts(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    staged = tmp_path / "staging/payload.txt"
    staged.parent.mkdir()
    staged.write_text("new", encoding="utf-8")
    target = tmp_path / "missing/parent/payload.txt"
    interrupted_directory = tmp_path / "missing"
    real_mkdir = Path.mkdir

    def interrupt_after_mkdir(path: Path, *args: object, **kwargs: object) -> None:
        real_mkdir(path, *args, **kwargs)  # type: ignore[arg-type]
        if path == interrupted_directory:
            raise KeyboardInterrupt

    monkeypatch.setattr(Path, "mkdir", interrupt_after_mkdir)

    with pytest.raises(KeyboardInterrupt):
        promote_transaction([PromotionItem(staged, target)], root=tmp_path)

    assert staged.read_text(encoding="utf-8") == "new"
    assert not target.exists()
    assert interrupted_directory.is_dir()
    assert list(interrupted_directory.iterdir()) == []
    assert not list(tmp_path.rglob("*.backup-*"))


def test_promotion_preserves_competitor_parent_when_mkdir_loses_race(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    staged = tmp_path / "staged.txt"
    staged.write_text("new", encoding="utf-8")
    competitor_parent = tmp_path / "competitor-parent"
    target = competitor_parent / "target.txt"
    real_mkdir = Path.mkdir

    def competitor_wins(path: Path, *args: object, **kwargs: object) -> None:
        if path == competitor_parent:
            real_mkdir(path, *args, **kwargs)  # type: ignore[arg-type]
        real_mkdir(path, *args, **kwargs)  # type: ignore[arg-type]

    monkeypatch.setattr(Path, "mkdir", competitor_wins)

    with pytest.raises(PipelineError, match="Cannot create promotion target parent safely"):
        promote_transaction([PromotionItem(staged, target)], root=tmp_path)

    assert competitor_parent.is_dir()
    assert list(competitor_parent.iterdir()) == []
    assert staged.read_text(encoding="utf-8") == "new"
    assert not target.exists()
    assert not list(tmp_path.rglob("*.backup-*"))


def test_promotion_rolls_back_backup_when_replace_succeeds_then_interrupts(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    target = tmp_path / "target.txt"
    target.write_text("old", encoding="utf-8")
    staged = tmp_path / "staged.txt"
    staged.write_text("new", encoding="utf-8")
    real_replace = os.replace

    def interrupt_after_backup(source: str | Path, destination: str | Path) -> None:
        real_replace(source, destination)
        if Path(source) == target and ".backup-" in Path(destination).name:
            raise KeyboardInterrupt

    monkeypatch.setattr(promotion_module.os, "replace", interrupt_after_backup)

    with pytest.raises(KeyboardInterrupt):
        promote_transaction([PromotionItem(staged, target)], root=tmp_path)

    assert target.read_text(encoding="utf-8") == "old"
    assert staged.read_text(encoding="utf-8") == "new"
    assert not list(tmp_path.rglob("*.backup-*"))


@pytest.mark.parametrize("target_existed", [False, True])
def test_promotion_restores_staged_file_when_replace_succeeds_then_interrupts(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    target_existed: bool,
) -> None:
    target = tmp_path / "target.txt"
    if target_existed:
        target.write_text("old", encoding="utf-8")
    staged = tmp_path / "staged.txt"
    staged.write_text("new", encoding="utf-8")
    real_replace = os.replace

    def interrupt_after_promotion(source: str | Path, destination: str | Path) -> None:
        real_replace(source, destination)
        if Path(source) == staged and Path(destination) == target:
            raise KeyboardInterrupt

    monkeypatch.setattr(promotion_module.os, "replace", interrupt_after_promotion)

    with pytest.raises(KeyboardInterrupt):
        promote_transaction([PromotionItem(staged, target)], root=tmp_path)

    assert staged.read_text(encoding="utf-8") == "new"
    if target_existed:
        assert target.read_text(encoding="utf-8") == "old"
    else:
        assert not target.exists()
    assert not list(tmp_path.rglob("*.backup-*"))


@pytest.mark.parametrize("failed_cleanup", [1, 2])
def test_promotion_cleanup_failure_after_commit_is_relabelled_and_does_not_fail(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    failed_cleanup: int,
) -> None:
    targets = [tmp_path / "target/first.txt", tmp_path / "target/second.txt"]
    staged = [tmp_path / "staging/first.txt", tmp_path / "staging/second.txt"]
    targets[0].parent.mkdir()
    staged[0].parent.mkdir()
    for index, path in enumerate(targets):
        path.write_text(f"old-{index}", encoding="utf-8")
    for index, path in enumerate(staged):
        path.write_text(f"new-{index}", encoding="utf-8")

    real_remove = promotion_module._remove
    cleanup_calls = 0

    def fail_one_backup(path: Path) -> None:
        nonlocal cleanup_calls
        if ".backup-" in path.name:
            cleanup_calls += 1
            if cleanup_calls == failed_cleanup:
                raise OSError("simulated post-commit cleanup failure")
        real_remove(path)

    monkeypatch.setattr(promotion_module, "_remove", fail_one_backup)

    promote_transaction(
        [PromotionItem(source, target) for source, target in zip(staged, targets, strict=True)],
        root=tmp_path,
    )

    assert [path.read_text(encoding="utf-8") for path in targets] == ["new-0", "new-1"]
    assert cleanup_calls == 2
    assert not list(tmp_path.rglob("*.backup-*"))
    orphans = list(tmp_path.rglob("*.orphaned-backup-*"))
    assert len(orphans) == 1
    assert orphans[0].read_text(encoding="utf-8") == f"old-{failed_cleanup - 1}"


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


def test_generated_manifest_rejects_special_files_instead_of_silently_skipping(
    tmp_path: Path,
) -> None:
    package = tmp_path / "iikocloud_client"
    package.mkdir()
    os.mkfifo(package / "generator-output.fifo")

    with pytest.raises(PipelineError, match=r"non-regular.*generator-output\.fifo"):
        write_generated_manifest(
            package,
            tmp_path / "generated-manifest.json",
            effective_schema_sha256="a" * 64,
            toolchain=Toolchain(
                "openapitools/openapi-generator-cli",
                "v7.22.0",
                "sha256:" + "b" * 64,
            ),
        )


def test_generated_manifest_loader_rejects_unsorted_or_extra_metadata(tmp_path: Path) -> None:
    manifest = tmp_path / "manifest.json"
    value: dict[str, Any] = {
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
