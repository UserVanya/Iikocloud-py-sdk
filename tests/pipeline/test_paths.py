from pathlib import Path

from tools.openapi_pipeline.paths import RepoPaths


def test_repo_paths_are_anchored_at_pyproject(tmp_path: Path) -> None:
    root = tmp_path / "repo"
    nested = root / "tools" / "openapi_pipeline"
    nested.mkdir(parents=True)
    (root / "pyproject.toml").write_text("[project]\nname='demo'\n")

    paths = RepoPaths.discover(nested)

    assert paths.root == root
    assert paths.candidate == root / "build/upstream/candidate.json"
    assert paths.effective == root / "build/openapi/effective.json"
    assert paths.private == root / "private"
    assert paths.state == root / ".state"
