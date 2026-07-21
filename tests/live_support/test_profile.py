from __future__ import annotations

from pathlib import Path

import pytest

from tools.openapi_pipeline.errors import SafetyError
from tools.openapi_pipeline.live.profile import load_discovery_profile, load_profile


def _write_profile(path: Path, *, allow_write: bool = False) -> None:
    path.write_text(
        'name = "test"\n'
        'base_url = "https://api.example.invalid"\n'
        'api_login_env = "IIKO_API_KEY"\n'
        'organization_id_env = "IIKO_ORG"\n'
        'external_menu_id_env = "IIKO_MENU"\n'
        'terminal_group_id_env = "IIKO_TERMINAL"\n'
        'write_product_id_env = "IIKO_PRODUCT"\n'
        f"allow_write = {'true' if allow_write else 'false'}\n"
        "allowed_organization_ids = []\n",
        encoding="utf-8",
    )
    path.chmod(0o600)


def test_profile_resolves_secrets_without_storing_them(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    profile = tmp_path / "profile.toml"
    _write_profile(profile)
    monkeypatch.setenv("IIKO_API_KEY", "secret-login")
    monkeypatch.setenv("IIKO_ORG", "00000000-0000-0000-0000-000000000001")
    monkeypatch.setenv("IIKO_MENU", "menu-1")
    monkeypatch.setenv("IIKO_TERMINAL", "terminal-1")

    resolved = load_profile(profile)

    assert resolved.api_login == "secret-login"
    assert "secret-login" not in resolved.fingerprint
    assert "secret-login" not in repr(resolved)
    assert len(resolved.fingerprint) == 64


def test_profile_reads_primary_key_from_explicit_env_file_without_fallback(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    profile = tmp_path / "profile.toml"
    _write_profile(profile)
    env_file = tmp_path / ".env"
    env_file.write_text(
        "IIKO_API_KEY=primary-login\nIIKO_API_KEY_2=secondary-login\n",
        encoding="utf-8",
    )
    env_file.chmod(0o600)
    monkeypatch.setenv("IIKO_ORG", "00000000-0000-0000-0000-000000000001")
    monkeypatch.setenv("IIKO_MENU", "menu-1")
    monkeypatch.setenv("IIKO_TERMINAL", "terminal-1")

    assert load_profile(profile, env_file=env_file).api_login == "primary-login"

    env_file.write_text("IIKO_API_KEY_2=secondary-login\n", encoding="utf-8")
    with pytest.raises(SafetyError, match="IIKO_API_KEY"):
        load_profile(profile, env_file=env_file)


def test_write_profile_requires_dedicated_terminal_and_product_env(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    profile = tmp_path / "profile.toml"
    _write_profile(profile, allow_write=True)
    monkeypatch.setenv("IIKO_API_KEY", "secret-login")
    monkeypatch.setenv("IIKO_ORG", "00000000-0000-0000-0000-000000000001")
    monkeypatch.setenv("IIKO_MENU", "menu-1")

    with pytest.raises(SafetyError, match="IIKO_TERMINAL"):
        load_profile(profile)


def _set_read_environment(monkeypatch: pytest.MonkeyPatch, *, login: str = "login") -> None:
    monkeypatch.setenv("IIKO_API_KEY", login)
    monkeypatch.setenv("IIKO_ORG", "00000000-0000-0000-0000-000000000001")
    monkeypatch.setenv("IIKO_MENU", "menu-1")
    monkeypatch.setenv("IIKO_TERMINAL", "terminal-1")


def test_read_only_profile_resolves_terminal_without_write_product(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    profile = tmp_path / "profile.toml"
    _write_profile(profile)
    profile.write_text(
        profile.read_text(encoding="utf-8").replace(
            'write_product_id_env = "IIKO_PRODUCT"\n', ""
        ),
        encoding="utf-8",
    )
    _set_read_environment(monkeypatch)

    resolved = load_profile(profile)

    assert resolved.terminal_group_id == "terminal-1"
    assert resolved.write_product_id is None


def test_read_only_profile_ignores_configured_write_product_environment(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    profile = tmp_path / "profile.toml"
    _write_profile(profile)
    _set_read_environment(monkeypatch)
    monkeypatch.setenv("IIKO_PRODUCT", "")

    resolved = load_profile(profile)

    assert resolved.terminal_group_id == "terminal-1"
    assert resolved.write_product_id is None


def test_read_only_profile_rejects_write_product_without_terminal(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    profile = tmp_path / "profile.toml"
    _write_profile(profile)
    profile.write_text(
        profile.read_text(encoding="utf-8").replace(
            'terminal_group_id_env = "IIKO_TERMINAL"\n', ""
        ),
        encoding="utf-8",
    )
    _set_read_environment(monkeypatch)

    with pytest.raises(SafetyError, match="write product requires a terminal group field"):
        load_profile(profile)


def test_write_profile_resolves_terminal_and_product(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    profile = tmp_path / "profile.toml"
    _write_profile(profile, allow_write=True)
    _set_read_environment(monkeypatch)
    monkeypatch.setenv("IIKO_PRODUCT", "product-1")

    resolved = load_profile(profile)

    assert resolved.terminal_group_id == "terminal-1"
    assert resolved.write_product_id == "product-1"


@pytest.mark.parametrize(
    "missing_field",
    ["terminal_group_id_env", "write_product_id_env"],
)
def test_write_profile_rejects_either_missing_target_field(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    missing_field: str,
) -> None:
    profile = tmp_path / "profile.toml"
    _write_profile(profile, allow_write=True)
    profile.write_text(
        "\n".join(
            line
            for line in profile.read_text(encoding="utf-8").splitlines()
            if not line.startswith(f"{missing_field} =")
        )
        + "\n",
        encoding="utf-8",
    )
    _set_read_environment(monkeypatch)
    monkeypatch.setenv("IIKO_PRODUCT", "product-1")

    with pytest.raises(SafetyError):
        load_profile(profile)


def test_discovery_profile_validates_terminal_name_without_loading_value(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    profile = tmp_path / "profile.toml"
    _write_profile(profile)
    profile.write_text(
        profile.read_text(encoding="utf-8").replace(
            'write_product_id_env = "IIKO_PRODUCT"\n', ""
        ),
        encoding="utf-8",
    )
    monkeypatch.setenv("IIKO_API_KEY", "discovery-login")
    monkeypatch.delenv("IIKO_TERMINAL", raising=False)

    assert load_discovery_profile(profile).api_login == "discovery-login"

    profile.write_text(
        profile.read_text(encoding="utf-8").replace("IIKO_TERMINAL", "lowercase"),
        encoding="utf-8",
    )
    with pytest.raises(SafetyError, match="uppercase"):
        load_discovery_profile(profile)


@pytest.mark.parametrize(
    ("old", "new", "message"),
    [
        ("allow_write = false", 'allow_write = "false"', "allow_write"),
        ("allowed_organization_ids = []", 'allowed_organization_ids = "none"', "array"),
        ('name = "test"', 'name = "../test"', "name"),
        ('api_login_env = "IIKO_API_KEY"', 'api_login_env = "lowercase"', "uppercase"),
    ],
)
def test_profile_rejects_wrong_scalar_types_and_unsafe_names(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    old: str,
    new: str,
    message: str,
) -> None:
    profile = tmp_path / "profile.toml"
    _write_profile(profile)
    profile.write_text(profile.read_text(encoding="utf-8").replace(old, new), encoding="utf-8")
    _set_read_environment(monkeypatch)

    with pytest.raises(SafetyError, match=message):
        load_profile(profile)


@pytest.mark.parametrize(
    "base_url",
    [
        "http://api.example.invalid",
        "https://user:password@api.example.invalid",
        "https://api.example.invalid/path",
        "https://api.example.invalid?query=1",
        "https://api.example.invalid#fragment",
        "https://api.example.invalid:443",
        "https://localhost",
        "https://api_example.invalid",
    ],
)
def test_profile_rejects_unsafe_base_urls(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, base_url: str
) -> None:
    profile = tmp_path / "profile.toml"
    _write_profile(profile)
    profile.write_text(
        profile.read_text(encoding="utf-8").replace("https://api.example.invalid", base_url),
        encoding="utf-8",
    )
    _set_read_environment(monkeypatch)

    with pytest.raises(SafetyError, match="base_url|hostname"):
        load_profile(profile)


def test_profile_rejects_unknown_missing_and_duplicate_toml_fields(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    _set_read_environment(monkeypatch)
    profile = tmp_path / "profile.toml"
    _write_profile(profile)
    original = profile.read_text(encoding="utf-8")

    profile.write_text(original + "unknown = true\n", encoding="utf-8")
    with pytest.raises(SafetyError, match="documented fields"):
        load_profile(profile)

    profile.write_text(original.replace('name = "test"\n', ""), encoding="utf-8")
    with pytest.raises(SafetyError, match="documented fields"):
        load_profile(profile)

    profile.write_text(original + 'name = "again"\n', encoding="utf-8")
    with pytest.raises(SafetyError, match="strict TOML"):
        load_profile(profile)


@pytest.mark.parametrize("mode", [0o644, 0o640, 0o400])
def test_profile_requires_exact_mode_0600(tmp_path: Path, mode: int) -> None:
    profile = tmp_path / "profile.toml"
    _write_profile(profile)
    profile.chmod(mode)
    with pytest.raises(SafetyError, match="0600"):
        load_profile(profile)


def test_profile_rejects_symlink_special_file_and_hardlink(tmp_path: Path) -> None:
    target = tmp_path / "target.toml"
    _write_profile(target)
    symlink = tmp_path / "link.toml"
    symlink.symlink_to(target)
    with pytest.raises(SafetyError, match="symlink"):
        load_profile(symlink)

    directory = tmp_path / "profile-dir"
    directory.mkdir(mode=0o700)
    with pytest.raises(SafetyError, match="regular file"):
        load_profile(directory)

    hardlink = tmp_path / "hardlink.toml"
    hardlink.hardlink_to(target)
    with pytest.raises(SafetyError, match="multiple hard links"):
        load_profile(hardlink)


def test_process_environment_has_precedence_and_empty_value_never_falls_back(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    profile = tmp_path / "profile.toml"
    _write_profile(profile)
    env_file = tmp_path / ".env"
    env_file.write_text(
        "IIKO_API_KEY=file-login\nIIKO_ORG=file-org\nIIKO_MENU=file-menu\n",
        encoding="utf-8",
    )
    env_file.chmod(0o600)
    monkeypatch.setenv("IIKO_API_KEY", "process-login")
    monkeypatch.setenv("IIKO_ORG", "process-org")
    monkeypatch.setenv("IIKO_MENU", "process-menu")
    monkeypatch.setenv("IIKO_TERMINAL", "process-terminal")
    assert load_profile(profile, env_file=env_file).api_login == "process-login"

    monkeypatch.setenv("IIKO_API_KEY", "")
    with pytest.raises(SafetyError, match="IIKO_API_KEY"):
        load_profile(profile, env_file=env_file)


def test_dotenv_interpolation_is_disabled(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    profile = tmp_path / "profile.toml"
    _write_profile(profile)
    env_file = tmp_path / ".env"
    env_file.write_text(
        "IIKO_API_KEY=${IIKO_API_KEY_2}\n"
        "IIKO_ORG=org\n"
        "IIKO_MENU=menu\n"
        "IIKO_TERMINAL=terminal\n",
        encoding="utf-8",
    )
    env_file.chmod(0o600)
    monkeypatch.delenv("IIKO_API_KEY", raising=False)
    monkeypatch.setenv("IIKO_API_KEY_2", "secondary-secret")

    resolved = load_profile(profile, env_file=env_file)

    assert resolved.api_login == "${IIKO_API_KEY_2}"
    assert "secondary-secret" not in repr(resolved)


def test_fingerprint_binds_only_stable_profile_name_and_base_url(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    profile = tmp_path / "profile.toml"
    _write_profile(profile)
    _set_read_environment(monkeypatch, login="first-login")
    first = load_profile(profile)

    monkeypatch.setenv("IIKO_API_KEY", "rotated-login")
    rotated = load_profile(profile)
    assert rotated.fingerprint == first.fingerprint

    alternate = tmp_path / "alternate.toml"
    alternate.write_text(
        profile.read_text(encoding="utf-8").replace("IIKO_API_KEY", "IIKO_API_KEY_2"),
        encoding="utf-8",
    )
    alternate.chmod(0o600)
    monkeypatch.setenv("IIKO_API_KEY_2", "alternate-login")
    assert load_profile(alternate).fingerprint == first.fingerprint

    monkeypatch.setenv("IIKO_MENU", "different-menu")
    monkeypatch.setenv("IIKO_ORG", "different-organization")
    assert load_profile(profile).fingerprint == first.fingerprint

    changed_name = tmp_path / "changed-name.toml"
    changed_name.write_text(
        profile.read_text(encoding="utf-8").replace('name = "test"', 'name = "other"'),
        encoding="utf-8",
    )
    changed_name.chmod(0o600)
    assert load_profile(changed_name).fingerprint != first.fingerprint


def test_discovery_profile_requires_only_primary_login_and_refuses_write_profile(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    profile = tmp_path / "profile.toml"
    _write_profile(profile)
    env_file = tmp_path / ".env"
    env_file.write_text("IIKO_API_KEY=discovery-login\n", encoding="utf-8")
    env_file.chmod(0o600)
    monkeypatch.delenv("IIKO_API_KEY", raising=False)
    monkeypatch.delenv("IIKO_ORG", raising=False)
    monkeypatch.delenv("IIKO_MENU", raising=False)

    resolved = load_discovery_profile(
        profile,
        env_file=env_file,
        required_api_login_env="IIKO_API_KEY",
    )

    assert resolved.name == "test"
    assert resolved.base_url == "https://api.example.invalid"
    assert resolved.api_login == "discovery-login"
    assert "discovery-login" not in repr(resolved)

    _write_profile(profile, allow_write=True)
    with pytest.raises(SafetyError, match="allow_write=false"):
        load_discovery_profile(profile, env_file=env_file)


def test_profile_can_require_the_production_primary_login_name(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    profile = tmp_path / "profile.toml"
    _write_profile(profile)
    profile.write_text(
        profile.read_text(encoding="utf-8").replace("IIKO_API_KEY", "IIKO_API_KEY_2"),
        encoding="utf-8",
    )
    _set_read_environment(monkeypatch)
    monkeypatch.setenv("IIKO_API_KEY_2", "alternate")

    with pytest.raises(SafetyError, match="IIKO_API_KEY"):
        load_profile(profile, required_api_login_env="IIKO_API_KEY")
