# Генерация и проверка SDK

Эта инструкция описывает текущий операторский pipeline: обновление OpenAPI
snapshot, review overlays, воспроизводимую генерацию SDK, строго ограниченные
live checks, проверку секретов и allowlisted Git-публикацию.

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

## Проверка секретов

Перед review, commit или публикацией запустите обычный read-only режим:

```bash
PYTHONDONTWRITEBYTECODE=1 uv run --frozen --offline \
  python -m tools.openapi_pipeline verify-no-secrets
```

Команда сама получает NUL-delimited списки tracked и staged файлов, проверяет
worktree и точные stage-0 blobs через audited `.secrets.baseline`, а затем ищет
точные непустые значения активных `IIKO_API_KEY` и `IIKO_API_KEY_2`. Detector
получает временную копию baseline, поэтому обычная проверка не может изменить
аудированный файл. Два значения загружаются только из process environment и,
если ключ отсутствует там, из корневого `.env` без вывода значения в
диагностику. Отсутствующий ключ просто пропускается.

Нормальная проверка никогда не изменяет baseline. Для его первоначального
создания используйте отдельный bootstrap-режим, затем вручную проаудируйте
каждую находку и снова запустите обычную проверку:

```bash
PYTHONDONTWRITEBYTECODE=1 uv run --frozen --offline \
  python -m tools.openapi_pipeline verify-no-secrets --create-baseline
uv run --frozen --offline detect-secrets audit .secrets.baseline
PYTHONDONTWRITEBYTECODE=1 uv run --frozen --offline \
  python -m tools.openapi_pipeline verify-no-secrets
```

Bootstrap получает tracked filenames самостоятельно, запускает
`detect-secrets scan --no-verify` без shell и атомарно создаёт новый baseline
только после успешной команды и разбора JSON. Он не предназначен для
перезаписи существующего baseline. В audit помечайте false positive только
после проверки; настоящую учётную запись нужно удалить из Git и ротировать, а
не добавлять в исключения. Не копируйте audit output в issue, логи или docs.

`.env`, `.env.local`, captures, receipts, rate state, mutation journals и
прочие runtime-файлы под `private/`, `.state/` и `build/` никогда не должны
быть tracked или staged. Из `private/` допустимы только hand-owned
`private/.gitignore` и `private/README.md`; secret scan fail closed на остальных
private paths.

## Allowlisted публикация

`publish` — mutating operator command, а не способ проверить реализацию. Не
запускайте её в текущем checkout как часть тестов: publish-тесты используют
только временный Git repository. Release version должна быть подготовлена до
generation и live receipt, потому что она встроена в generated runtime и его
hash. Последовательность для новой версии:

1. Измените точную строку `[project] version = "..."` в `pyproject.toml`.
2. Выполните `uv lock --offline --no-config`, затем `sync --offline`.
3. Проведите guarded live-read для получившегося generated tree.
4. Оставьте release diff unstaged: `publish` требует пустой Git index.
5. Передайте ту же уже подготовленную версию в `publish`.

Без `--push` команда создаёт commit и annotated tag, но не меняет release
version после live receipt:

```bash
PYTHONDONTWRITEBYTECODE=1 uv run --frozen --offline \
  python -m tools.openapi_pipeline publish --version 0.1.0
```

`--version` обязателен и должен совпадать с `pyproject.toml`, generated
`__version__`, User-Agent/debug report и `uv.lock`. Для отдельной, явно
подтверждённой публикации commit и tag в `origin` добавьте `--push`:

```bash
PYTHONDONTWRITEBYTECODE=1 uv run --frozen --offline \
  python -m tools.openapi_pipeline publish --version 0.1.0 --push
```

На `main` и `master` команда по умолчанию запрещена. Единственный локальный
opt-in — ignored файл `private/publish.toml` с точным
`allow_protected_branch = true`; CLI-флага для обхода этого gate нет.

До изменения Git publish требует одновременно:

- только dirty paths из `openapi/`, `contracts/`, `generator/`,
  `src/iikocloud_client/`, `tests/fixtures/contracts/`, `tests/generated/` или
  точные файлы `docs/generation.md`, `docs/known-upstream-issues.md`,
  `README.md`, `pyproject.toml`, `uv.lock`, при полностью пустом Git index;
- совпадение requested, project и generated runtime version, актуальный
  `uv.lock`, успешный полный `verify` и completed live receipt, совпадающий с
  текущими artifact hashes;
- закрытый persistent circuit для profile fingerprint из receipt и полное
  отсутствие mutation journals;
- успешный secret scan до staging.

После gates команда повторяет wheel smoke, показывает sanitized dirty-path
list и `git diff --stat`, выполняет `git add --` только для разрешённых путей и
повторяет secret scan уже по точным staged blobs. Затем создаются ровно один commit
`chore(sdk): sync iiko OpenAPI YYYY-MM-DD` и annotated tag `v{version}`. С
`--push` выполняются только non-force push текущего `HEAD`, затем отдельный
non-force push тега.

Publish gates не разрешают live write. Записи stop-list операций `get`, `add`
и `remove` в `contracts/rate-limits.yaml` всё ещё имеют `verified: false`;
write-тесты можно только собирать, но нельзя запускать live до отдельной
проверки server limits и явного контролируемого решения. CLI-имя
`reset-circuit` также остаётся зарезервированным и не должно использоваться как
фиктивный способ обойти открытый circuit.
