# Private live-test configuration

Copy `config/live-profile.example.toml` to
`private/profiles/test-server.toml`, fill only environment-variable names and
the non-secret target settings, then set the profile file to mode `0600`.
Set both `private/` and `private/profiles/` to mode `0700`.

Export the variables named by the profile. The primary API login must be read
from `IIKO_API_KEY`, either from the process environment or from the repository
root `.env` supplied explicitly with `--env-file .env`. The secondary login is
never an automatic fallback. Never share or commit a real profile, `.env`,
receipt, capture, API login, or access token.
