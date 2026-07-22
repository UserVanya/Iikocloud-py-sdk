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

## Безопасный запуск read checks

Используйте только точные serial full/selected команды из
[`docs/generation.md`](../docs/generation.md#полный-guarded-live-read). Флаг
`uv --offline` отключает только сетевой доступ `uv` к package indexes и **не
блокирует guarded HTTP к iiko**.

Full plan может выполнить 92 HTTP requests: одну authentication и 91 read.
Если все cases доходят до HTTP, минимальный cadence составляет 45 минут 30
секунд; persistent budget отдельной operation может увеличить ожидание, в том
числе до effective interval 9000 секунд для `get_external_menus`. Отсутствующий
target даёт `no_live_target` до rate budget и HTTP и тем самым сокращает run.

Selected capture выполняет canary/dependency closure, но сохраняет только
явно выбранную operation, никогда не authentication. Даже sanitized ignored
файлы под `private/captures/` остаются private и не добавляются в Git; capture
нельзя совмещать с full runner.

`passed` и `no_live_target` позволяют runner продолжить; `failed` останавливает
зависимые cases, а safety/transport/HTTP/rate failure глобально переводит
оставшиеся cases в `aborted`. **429 rule:** stop the entire run; no retry; no
second key; investigate and manually reset later. Не используйте
`IIKO_API_KEY_2`, не удаляйте rate state и не продолжайте другие operations.
