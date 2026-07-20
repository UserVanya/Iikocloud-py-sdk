# Генерация и проверка SDK

Эта инструкция описывает только команды, реализованные к Task 11. Она нужна
оператору, который обновляет OpenAPI snapshot, проверяет overlays, генерирует
SDK и при необходимости выполняет строго ограниченные read-only live checks.

## Что является источником истины

- `openapi/upstream/iikocloud.openapi.json` — точная tracked-копия upstream;
  её не исправляют вручную.
- `openapi/operation-ids.yaml` и `openapi/model-name-overrides.yaml` —
  hand-reviewed публичные имена операций и моделей.
- `openapi/overlays/*.overlay.yaml` — механические и семантические исправления
  raw snapshot. Каждое действие привязано к числу совпадений и SHA-256
  исходного фрагмента.
- `tests/fixtures/contracts/` — только минимальные синтетические contract
  fixtures. Это не копии live payloads.
- `generator/toolchain.lock` — точный Docker image и digest OpenAPI Generator.
- `generator/generated-manifest.json` — хэши generated tree до добавления
  разрешённых manual files.
- `src/iikocloud_client/_contracts/` — hand-owned файлы, которые generation
  обязана сохранить.

Generated package под `src/iikocloud_client` не является местом для ручных
fixes. Исправление должно появиться в snapshot-composition слое, registry,
generator config или тестируемом pipeline-коде.

## Предварительные условия

Нужны Python 3.10+, `uv`, Git и запущенный Docker Engine с локально доступным
image из `generator/toolchain.lock`. Генератор запускается по digest, с
отключённой сетью контейнера.

```bash
uv sync --frozen --group dev
```

Перед любой работой с pipeline или live сначала прочитайте
[troubleshooting ledger](troubleshooting.md). Повторяющийся workaround можно
добавлять туда только после воспроизведения причины и проверки решения; вывод
с секретами или private payloads в ledger не переносится.

## Основные команды

### Проверить свежий upstream

```bash
uv run --frozen python -m tools.openapi_pipeline upstream-check
```

Команда делает сетевое получение публичного OpenAPI, сохраняет кандидата и
отчёт под ignored `build/`, но не меняет tracked snapshot или generated SDK.
Проверьте как минимум `build/reports/upstream-diff.md` и raw candidate перед
любой попыткой принять обновление.

### Подготовить bootstrap-кандидаты

```bash
uv run --frozen python -m tools.openapi_pipeline bootstrap
```

Команда получает upstream и создаёт reviewable candidates в
`build/bootstrap/`: mechanical types overlay, operation IDs и model collision
report. Tracked files не продвигаются.

`bootstrap --accept-current-upstream` предназначен только для первоначального
baseline с пустыми registry. В уже инициализированном репозитории новые
reviewed записи переносятся в tracked registries/overlays, после чего
используется `sync`; флаг initial acceptance не является обычной командой
обновления.

### Регенерировать атомарно

Без сети, из текущего tracked snapshot:

```bash
uv run --frozen --offline python -m tools.openapi_pipeline sync --offline
```

После review нового публичного кандидата `sync` без `--offline` может получить
upstream заново:

```bash
uv run --frozen python -m tools.openapi_pipeline sync
```

Обе формы сначала собирают effective schema, выполняют strict lint и pinned
generator validation, генерируют во staging, проверяют imports, contracts и
wheel. Snapshot, manifest и generated package продвигаются одной транзакцией
только после успешных проверок.

### Проверить воспроизводимость

```bash
uv run --frozen --offline python -m tools.openapi_pipeline verify
```

`verify` заново строит effective schema и package, сверяет manifest, manual
contracts и wheel из корня проекта. Команда offline и не выполняет live API
calls. Для ad-hoc импортов generated package используйте
`PYTHONDONTWRITEBYTECODE=1`, иначе `__pycache__` внутри manifest-controlled
дерева будет корректно считаться незаявленным изменением; восстановить чистое
дерево можно повторным атомарным `sync --offline`.

## Как исправлять дефекты upstream

1. Не меняйте raw snapshot и generated Python.
2. Зафиксируйте точный ошибочный JSON fragment и ожидаемый контракт тестом.
3. Для operation name добавьте стабильное доменное имя в
   `openapi/operation-ids.yaml`. Для model collision или generator-invalid CLR
   generic key добавьте явное имя в `openapi/model-name-overrides.yaml`.
   Numeric suffix допустим только если число действительно относится к домену.
4. Псевдотипы вроде `bool`, `uuid` и `integer <int64>` нормализуются
   mechanical types overlay. Семантическая ошибка описывается Overlay 1.1
   action с точным JSONPath, `expected-matches` и digest исходного значения.
5. Не обновляйте guard hash вслепую. Его drift означает, что upstream fragment
   изменился и исправление нужно заново проверить. Digest должен вычисляться
   тем же canonical JSON helper, который использует pipeline.
6. Для наблюдаемого response-контракта добавьте минимальную синтетическую
   fixture и generated contract test. Live payload не копируется в tracked
   файл.
7. Запустите `sync --offline`, затем `verify` и просмотрите Git diff.

Применение overlays и physical normalization имён fail closed: отсутствующий
target, изменившийся fragment, collision, небезопасная ссылка или оставшийся
invalid schema key останавливает generation.

Текущие semantic actions и условия их удаления описаны в
[known-upstream-issues.md](known-upstream-issues.md).

## Guarded read-only live checks

Live-запуск разрешён только через project commands/pytest fixtures и только
для operation, у которой `verified: true` в `contracts/rate-limits.yaml`.
Обычный pytest и CI исключают live markers.

Создайте закрытый профиль из публичного шаблона:

```bash
install -d -m 0700 private/profiles
cp config/live-profile.example.toml private/profiles/test-server.toml
chmod 0600 private/profiles/test-server.toml .env
```

В profile остаются только имена environment variables и разрешённые target
settings. Значения API login и IDs находятся в process environment или в
явно переданном `.env`; их нельзя печатать, копировать в docs или коммитить.
Полные правила находятся в `private/README.md`.

Получить guarded список доступных организаций, terminal groups и external
menus с именами:

```bash
uv run --frozen --offline python -m tools.openapi_pipeline discover-read-targets \
  --live-profile test-server --env-file .env
```

Проверить один target organization через generated SDK:

```bash
uv run --frozen --offline pytest -m live_read_smoke -n0 \
  --live-profile test-server --env-file .env \
  tests/integration/read/test_organizations.py
```

Эти entrypoints создают process lock, используют persistent rate state,
аутентифицируются один раз и не делают retry HTTP-вызова. Один live process
может выполнить не больше одного вызова конкретной operation за run.

## JSON evidence для external menu

Каждая версия запрашивается отдельной командой. Не объединяйте команды в loop
и не запускайте их параллельно:

```bash
uv run --frozen --offline python -m tools.openapi_pipeline capture-evidence \
  --live-profile test-server --env-file .env \
  --operation get_external_menu_by_id --menu-version 2

uv run --frozen --offline python -m tools.openapi_pipeline capture-evidence \
  --live-profile test-server --env-file .env \
  --operation get_external_menu_by_id --menu-version 3

uv run --frozen --offline python -m tools.openapi_pipeline capture-evidence \
  --live-profile test-server --env-file .env \
  --operation get_external_menu_by_id --menu-version 4
```

Guard использует не только глобальный минимум 30 секунд, но и более строгий
интервал конкретной operation из tracked rate catalog. Он хранит время
последнего вызова между процессами; оператор не должен заменять его ручным
`sleep` или повторным API login.

Capture writer сохраняет sanitized request/response JSON только под ignored
`private/captures/` с закрытыми permissions. Даже sanitized capture остаётся
private и не переносится в Git.

Построить detached review candidate без изменения tracked files:

```bash
uv run --frozen --offline python -m tools.openapi_pipeline promote-evidence \
  --operation get_external_menu_by_id
```

Проверьте `build/evidence-candidates/candidate-manifest.json`, две overlay
кандидатуры и три минимальные fixtures. После отдельного human review принять
ровно этот заново проверенный candidate:

```bash
uv run --frozen --offline python -m tools.openapi_pipeline promote-evidence \
  --operation get_external_menu_by_id --accept
```

Acceptance повторно проверяет provenance, schema fragments, V2/V3/V4,
discriminator consistency, наличие combo evidence и отсутствие известных
secret/PII patterns. В tracked tree попадают только две overlays и три
synthetic fixtures.

## Что делать при 429

`429` немедленно открывает persistent circuit и прекращает весь live-run.
Запрещено:

- повторять запрос;
- продолжать следующую operation;
- автоматически или вручную переключаться на `IIKO_API_KEY_2`;
- удалять state ради обхода circuit.

Сначала расследуйте причину и сохраните circuit закрытым для новых запусков до
явного ручного решения. CLI-имя `reset-circuit` пока зарезервировано, но его
реализация не завершена; эта инструкция намеренно не предлагает фиктивную
команду сброса.

## Write-тест и восстановление cleanup

Reversible stop-list round-trip существует как отдельный `live_write` test,
но не входит ни в один обычный test run. Безопасно проверить только его
collection-контракт:

```bash
uv run --frozen --offline pytest -m live_write -n0 \
  tests/integration/write --collect-only -q
```

Реальный запуск требует одновременно `--allow-live-write`,
`--allow-audit-residue`, точный `--target-organization`, write-enabled private
profile, allowlist, отдельные terminal group/product и `-n0`. Перед
authentication проверяются rate budgets операций `get`, `add` и `remove`.
Сейчас эти три stop-list записи в `contracts/rate-limits.yaml` намеренно имеют
`verified: false`, поэтому live write останавливается до HTTP. Не меняйте этот
флаг без проверенного server limit и отдельного решения на контролируемый
запуск.

До `add` test атомарно сохраняет cleanup payload в ignored
`.state/mutations/<run-id>.json` с mode `0600`. Cleanup выполняется LIFO в
`finally`; незавершённый журнал сохраняется и блокирует успешный live receipt.
Для ручного восстановления существует только интерактивная команда:

```bash
uv run --frozen python -m tools.openapi_pipeline cleanup-orphans \
  --live-profile test-server --env-file .env
```

Она до authentication проверяет каждый journal, каждый cleanup budget,
generated-схему payload и точное совпадение organization, terminal group и
единственного dedicated product с выбранным write-профилем. Команда не
показывает payload/UUID, выводит только fingerprints и operation IDs, затем
требует точное подтверждение `cleanup N actions [y/N]`. Не повторяйте команду
после `429`, не переключайте API login и не удаляйте journal вручную. При
текущих unverified stop-list limits команда также корректно завершится до HTTP.

## Ещё не реализовано

В CLI help зарезервированы будущие команды `reset-circuit`,
`verify-no-secrets` и `publish`, но текущий dispatcher возвращает для них
`Command is not implemented yet`. Автоматический secret scan, публикация tag и
реальный write-run с верифицированными stop-list limits ещё не готовы.
