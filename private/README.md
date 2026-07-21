# Private live-test configuration

Copy `config/live-profile.example.toml` to
`private/profiles/test-server.toml`, fill only environment-variable names and
the non-secret target settings, then set the profile file to mode `0600`.
Set both `private/` and `private/profiles/` to mode `0700`.

`terminal_group_id_env` names the read target for terminal, stop-list, and
employee checks. Its environment value is required whenever the field is
present, including when `allow_write = false`. `write_product_id_env` names a
dedicated write-only target and is ignored when writes are disabled. A
write-enabled profile requires both target fields and both environment values;
a product field without a terminal field is invalid.

Export the variables resolved by the selected mode. The primary API login must
be read from `IIKO_API_KEY`, either from the process environment or from the
repository root `.env` supplied explicitly with `--env-file .env`. The
secondary login is never an automatic fallback. Never share or commit a real
profile, `.env`, receipt, capture, API login, or access token.
