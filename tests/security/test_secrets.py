import json
import subprocess
from pathlib import Path
from typing import Any

import pytest

from tools.openapi_pipeline.errors import SafetyError
from tools.openapi_pipeline.secrets import (
    assert_known_secrets_absent,
    assert_secret_path_policy,
    collect_tracked_and_staged_paths,
    create_secrets_baseline,
    load_known_secrets,
    verify_no_secrets,
)


def _completed(
    argv: list[str],
    *,
    stdout: bytes = b"",
    stderr: bytes = b"",
    returncode: int = 0,
) -> subprocess.CompletedProcess[bytes]:
    return subprocess.CompletedProcess(argv, returncode, stdout, stderr)


def _empty_baseline() -> dict[str, Any]:
    return {
        "version": "1.5.0",
        "plugins_used": [],
        "filters_used": [],
        "results": {},
        "generated_at": "2026-07-21T00:00:00Z",
    }


def _write_empty_baseline(root: Path) -> None:
    (root / ".secrets.baseline").write_text(
        json.dumps(_empty_baseline()),
        encoding="utf-8",
    )


def test_exact_active_secret_blocks_publish_without_echoing_value(tmp_path: Path) -> None:
    secret = "live-api-login-value"
    tracked = tmp_path / "tracked.json"
    tracked.write_text(f'{{"value":"{secret}"}}', encoding="utf-8")

    with pytest.raises(SafetyError) as raised:
        assert_known_secrets_absent([tracked], [secret])

    assert secret not in str(raised.value)


def test_exact_scan_ignores_empty_values(tmp_path: Path) -> None:
    tracked = tmp_path / "tracked.txt"
    tracked.write_text("ordinary text", encoding="utf-8")

    assert_known_secrets_absent([tracked], [""])


@pytest.mark.parametrize(
    "path",
    [
        "private/captures/run/response.json",
        ".state/live.lock",
        "build/generated.txt",
        "dist/iikocloud.whl",
        ".env",
        ".env.local",
        "nested/.env",
        "nested/.env.local",
    ],
)
def test_secret_path_policy_rejects_private_generated_and_env_paths(path: str) -> None:
    with pytest.raises(SafetyError, match="path policy"):
        assert_secret_path_policy([path])


def test_secret_path_policy_allows_only_documented_private_files() -> None:
    assert_secret_path_policy(["private/.gitignore", "private/README.md", "src/client.py"])

    with pytest.raises(SafetyError, match="private/notes.txt"):
        assert_secret_path_policy(["private/notes.txt"])


def test_collect_paths_uses_strict_nul_git_commands(tmp_path: Path) -> None:
    calls: list[tuple[list[str], dict[str, object]]] = []

    def runner(argv: list[str], **kwargs: object) -> subprocess.CompletedProcess[bytes]:
        calls.append((argv, kwargs))
        if argv == ["git", "ls-files", "-z", "--"]:
            return _completed(argv, stdout=b"tracked.py\0space name.json\0")
        if argv == ["git", "diff", "--cached", "--name-only", "-z", "--"]:
            return _completed(argv, stdout=b"staged.yaml\0tracked.py\0")
        raise AssertionError(f"unexpected argv: {argv!r}")

    assert collect_tracked_and_staged_paths(tmp_path, runner=runner) == (
        "space name.json",
        "staged.yaml",
        "tracked.py",
    )
    assert all(kwargs["cwd"] == tmp_path.resolve() for _, kwargs in calls)
    assert all(kwargs["capture_output"] is True for _, kwargs in calls)
    assert all(kwargs["check"] is True for _, kwargs in calls)
    assert all("shell" not in kwargs for _, kwargs in calls)


def test_collect_paths_rejects_non_terminated_git_output(tmp_path: Path) -> None:
    def runner(argv: list[str], **_: object) -> subprocess.CompletedProcess[bytes]:
        if argv[:2] == ["git", "ls-files"]:
            return _completed(argv, stdout=b"tracked.py")
        return _completed(argv)

    with pytest.raises(SafetyError, match="NUL"):
        collect_tracked_and_staged_paths(tmp_path, runner=runner)


def test_verify_scans_explicit_tracked_and_staged_files_without_shell(tmp_path: Path) -> None:
    (tmp_path / "tracked.py").write_text("tracked = True\n", encoding="utf-8")
    (tmp_path / "staged file.json").write_text("{}\n", encoding="utf-8")
    _write_empty_baseline(tmp_path)
    calls: list[tuple[list[str], dict[str, object]]] = []

    def runner(argv: list[str], **kwargs: object) -> subprocess.CompletedProcess[bytes]:
        calls.append((argv, kwargs))
        if argv == ["git", "ls-files", "-z", "--"]:
            return _completed(argv, stdout=b"tracked.py\0.secrets.baseline\0")
        if argv == ["git", "diff", "--cached", "--name-only", "-z", "--"]:
            return _completed(argv, stdout=b"staged file.json\0")
        if argv == ["git", "init", "-q"]:
            return _completed(argv)
        if argv == [
            "git",
            "ls-files",
            "--stage",
            "-z",
            "--",
            "staged file.json",
        ]:
            return _completed(
                argv,
                stdout=b"100644 " + b"a" * 40 + b" 0\tstaged file.json\0",
            )
        if argv == ["git", "cat-file", "blob", "a" * 40]:
            return _completed(argv, stdout=b"{}\n")
        if argv[0] == "detect-secrets-hook":
            return _completed(argv)
        raise AssertionError(f"unexpected argv: {argv!r}")

    verify_no_secrets(tmp_path, runner=runner)

    hook_calls = [(argv, kwargs) for argv, kwargs in calls if argv[0] == "detect-secrets-hook"]
    assert len(hook_calls) == 2
    worktree_argv, worktree_kwargs = hook_calls[0]
    staged_argv, staged_kwargs = hook_calls[1]
    for hook_argv, hook_kwargs in hook_calls:
        assert hook_argv[:2] == ["detect-secrets-hook", "--no-verify"]
        assert "--baseline" in hook_argv
        assert hook_kwargs["capture_output"] is True
        assert hook_kwargs["check"] is False
        assert "shell" not in hook_kwargs
    assert worktree_argv[worktree_argv.index("--") + 1 :] == [
        "staged file.json",
        "tracked.py",
    ]
    assert worktree_kwargs["cwd"] == tmp_path.resolve()
    assert staged_argv[staged_argv.index("--") + 1 :] == ["staged file.json"]
    assert staged_kwargs["cwd"] != tmp_path.resolve()


def test_verify_sanitizes_detector_output(tmp_path: Path) -> None:
    leaked = "detector-output-must-not-be-reported"
    (tmp_path / "tracked.py").write_text("tracked = True\n", encoding="utf-8")
    _write_empty_baseline(tmp_path)

    def runner(argv: list[str], **_: object) -> subprocess.CompletedProcess[bytes]:
        if argv[:2] == ["git", "ls-files"]:
            return _completed(argv, stdout=b"tracked.py\0")
        if argv[:2] == ["git", "diff"]:
            return _completed(argv)
        return _completed(argv, returncode=1, stderr=leaked.encode())

    with pytest.raises(SafetyError) as raised:
        verify_no_secrets(tmp_path, runner=runner)

    assert leaked not in str(raised.value)


def test_verify_scans_exact_staged_blob_when_worktree_is_safe(tmp_path: Path) -> None:
    secret = "staged-only-active-secret"
    subprocess.run(["git", "init", "-q"], cwd=tmp_path, check=True, capture_output=True)
    tracked = tmp_path / "tracked.txt"
    tracked.write_text("safe before staging\n", encoding="utf-8")
    _write_empty_baseline(tmp_path)
    subprocess.run(
        ["git", "add", "--", tracked.name, ".secrets.baseline"],
        cwd=tmp_path,
        check=True,
        capture_output=True,
    )

    tracked.write_text(f"token={secret}\n", encoding="utf-8")
    subprocess.run(
        ["git", "add", "--", tracked.name],
        cwd=tmp_path,
        check=True,
        capture_output=True,
    )
    tracked.write_text("safe worktree replacement\n", encoding="utf-8")

    with pytest.raises(SafetyError) as raised:
        verify_no_secrets(tmp_path, [secret])

    assert secret not in str(raised.value)


def test_normal_verify_never_mutates_audited_baseline(tmp_path: Path) -> None:
    subprocess.run(["git", "init", "-q"], cwd=tmp_path, check=True, capture_output=True)
    canary = "".join(("Q7mN", "9vR2", "xK4p", "L8sD", "6fH3", "jT5w", "Y1cB", "0aZq"))
    tracked = tmp_path / "tracked.py"
    tracked.write_text(f'password = "{canary}"\n', encoding="utf-8")
    subprocess.run(
        ["git", "add", "--", tracked.name],
        cwd=tmp_path,
        check=True,
        capture_output=True,
    )
    baseline_path = create_secrets_baseline(tmp_path)
    baseline = json.loads(baseline_path.read_text(encoding="utf-8"))
    assert baseline["results"]
    for findings in baseline["results"].values():
        for finding in findings:
            finding["is_secret"] = False
    baseline_path.write_text(json.dumps(baseline), encoding="utf-8")
    original = baseline_path.read_bytes()
    subprocess.run(
        ["git", "add", "--", baseline_path.name],
        cwd=tmp_path,
        check=True,
        capture_output=True,
    )

    tracked.write_text(f'\npassword = "{canary}"\n', encoding="utf-8")
    with pytest.raises(SafetyError):
        verify_no_secrets(tmp_path)

    assert baseline_path.read_bytes() == original


def test_load_known_secrets_uses_only_named_values_and_process_precedence(
    tmp_path: Path,
) -> None:
    env_file = tmp_path / ".env"
    env_file.write_text(
        "IGNORED_VALUE=not-loaded\nIIKO_API_KEY=file-primary\nIIKO_API_KEY_2=shared-secondary\n",
        encoding="utf-8",
    )
    env_file.chmod(0o600)

    values = load_known_secrets(
        tmp_path,
        environ={
            "IIKO_API_KEY": "process-primary",
            "IIKO_API_KEY_2": "shared-secondary",
            "UNRELATED": "not-loaded-either",
        },
    )

    assert values == ("process-primary", "shared-secondary")


def test_load_known_secrets_rejects_non_private_or_non_root_env_file(tmp_path: Path) -> None:
    env_file = tmp_path / ".env"
    env_file.write_text("IIKO_API_KEY=synthetic-value\n", encoding="utf-8")
    env_file.chmod(0o644)

    with pytest.raises(SafetyError, match="0600"):
        load_known_secrets(tmp_path, environ={})

    other = tmp_path / "other.env"
    other.write_text("IIKO_API_KEY=synthetic-value\n", encoding="utf-8")
    other.chmod(0o600)
    with pytest.raises(SafetyError, match="root .env"):
        load_known_secrets(tmp_path, environ={}, env_file=other)


def test_load_known_secrets_rejects_duplicate_target_without_echoing(tmp_path: Path) -> None:
    first = "first-sensitive-value"
    second = "second-sensitive-value"
    env_file = tmp_path / ".env"
    env_file.write_text(
        f"IIKO_API_KEY={first}\nIIKO_API_KEY={second}\n",
        encoding="utf-8",
    )
    env_file.chmod(0o600)

    with pytest.raises(SafetyError) as raised:
        load_known_secrets(tmp_path, environ={})

    message = str(raised.value)
    assert first not in message
    assert second not in message


def test_create_baseline_scans_explicit_tracked_files_and_writes_valid_json(
    tmp_path: Path,
) -> None:
    (tmp_path / "tracked.py").write_text("tracked = True\n", encoding="utf-8")
    baseline = json.dumps(_empty_baseline()).encode()
    calls: list[list[str]] = []

    def runner(argv: list[str], **_: object) -> subprocess.CompletedProcess[bytes]:
        calls.append(argv)
        if argv == ["git", "ls-files", "-z", "--"]:
            return _completed(argv, stdout=b"tracked.py\0")
        if argv[0:2] == ["detect-secrets", "scan"]:
            return _completed(argv, stdout=baseline)
        raise AssertionError(f"unexpected argv: {argv!r}")

    target = create_secrets_baseline(tmp_path, runner=runner)

    assert target == tmp_path / ".secrets.baseline"
    assert json.loads(target.read_text(encoding="utf-8")) == _empty_baseline()
    assert calls[1] == ["detect-secrets", "scan", "--no-verify", "--", "tracked.py"]


def test_create_baseline_never_overwrites_existing_file(tmp_path: Path) -> None:
    target = tmp_path / ".secrets.baseline"
    target.write_text("keep-me", encoding="utf-8")

    def runner(argv: list[str], **_: object) -> subprocess.CompletedProcess[bytes]:
        raise AssertionError(f"runner must not be called: {argv!r}")

    with pytest.raises(SafetyError, match="already exists"):
        create_secrets_baseline(tmp_path, runner=runner)

    assert target.read_text(encoding="utf-8") == "keep-me"


def test_create_baseline_rejects_invalid_json_without_publishing(tmp_path: Path) -> None:
    (tmp_path / "tracked.py").write_text("tracked = True\n", encoding="utf-8")

    def runner(argv: list[str], **_: object) -> subprocess.CompletedProcess[bytes]:
        if argv[0] == "git":
            return _completed(argv, stdout=b"tracked.py\0")
        return _completed(argv, stdout=b'{"version": NaN}')

    with pytest.raises(SafetyError, match="JSON"):
        create_secrets_baseline(tmp_path, runner=runner)

    assert not (tmp_path / ".secrets.baseline").exists()


def test_baseline_destination_is_invisible_until_full_body_is_written(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    import tools.openapi_pipeline.secrets as secrets_module

    target = tmp_path / ".secrets.baseline"
    observed_destination_states: list[bool] = []
    real_write = secrets_module.os.write

    def guarded_write(descriptor: int, body: bytes | memoryview) -> int:
        observed_destination_states.append(target.exists())
        return real_write(descriptor, body)

    monkeypatch.setattr(secrets_module.os, "write", guarded_write)
    secrets_module._write_new_baseline(target, b'{"complete":true}\n')

    assert observed_destination_states
    assert not any(observed_destination_states)
    assert target.read_bytes() == b'{"complete":true}\n'


def test_audited_baseline_does_not_suppress_same_temporary_secret_in_new_file(
    tmp_path: Path,
) -> None:
    subprocess.run(["git", "init", "-q"], cwd=tmp_path, check=True, capture_output=True)
    canary = "".join(("Q7mN", "9vR2", "xK4p", "L8sD", "6fH3", "jT5w", "Y1cB", "0aZq"))
    existing = tmp_path / "existing.py"
    existing.write_text(f'password = "{canary}"\n', encoding="utf-8")
    subprocess.run(["git", "add", "--", existing.name], cwd=tmp_path, check=True)

    baseline_path = create_secrets_baseline(tmp_path)
    baseline = json.loads(baseline_path.read_text(encoding="utf-8"))
    assert baseline["results"]
    for findings in baseline["results"].values():
        for finding in findings:
            finding["is_secret"] = False
    baseline_path.write_text(json.dumps(baseline), encoding="utf-8")
    subprocess.run(["git", "add", "--", baseline_path.name], cwd=tmp_path, check=True)
    verify_no_secrets(tmp_path)

    new_file = tmp_path / "new.py"
    new_file.write_text(f'password = "{canary}"\n', encoding="utf-8")
    subprocess.run(["git", "add", "--", new_file.name], cwd=tmp_path, check=True)

    with pytest.raises(SafetyError) as raised:
        verify_no_secrets(tmp_path)

    assert canary not in str(raised.value)


def test_committed_synthetic_canary_is_explicitly_audited_non_secret() -> None:
    root = Path(__file__).resolve().parents[2]
    baseline = json.loads((root / ".secrets.baseline").read_text(encoding="utf-8"))
    findings = baseline["results"]["tests/fixtures/security/detect_secrets_canary.py"]

    assert findings
    assert all(finding.get("is_secret") is False for finding in findings)
