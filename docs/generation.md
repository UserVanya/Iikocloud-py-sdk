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

Публикуемая библиотека поддерживает Python 3.10+, но для выполнения этого
операторского pipeline нужен Python 3.12. Также нужны `uv`, Git и запущенный
Docker Engine с локально доступным image из `generator/toolchain.lock`.
Генератор запускается по digest, с отключённой сетью контейнера.

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

Показанная ручная команда работает в report-only режиме: даже при drift она
сначала записывает оба `build/reports/upstream-diff.*` отчёта и завершается с
кодом 0. Scheduled workflow запускает только эту же команду с отдельным
`--fail-on-drift`: при drift отчёты уже записаны, после чего job получает
ненулевой сигнал; при неизменном inventory код остаётся 0. Artifact upload в
workflow выполняется с `if: always()`, поэтому отчёты сохраняются в обоих
случаях. Флаг `--fail-on-drift` существует только у `upstream-check`.

`upstream-check` не принимает snapshot и не перегенерирует SDK. `sync`,
напротив, собирает и продвигает reviewed tracked состояние; сетевую форму
`sync` нельзя использовать вместо review отчёта `upstream-check`.

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

Известный длинный прогон recursive evidence/schema tests может исчерпать native
stack CPython и завершиться с code 139. Не считайте повторный монолитный
`pytest -q` достаточной проверкой: используйте fresh-process split из строки
troubleshooting ledger от 2026-07-20 про native stack exhaustion. Каждый
указанный там test group запускается отдельным процессом; это offline
workaround и он не разрешает live markers. Точный executable partition также
зафиксирован в `.github/workflows/python.yml`.

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
test "$(stat -c '%a:%u' .env)" = "600:$(id -u)"
test "$(stat -c '%a:%u' private/profiles/test-server.toml)" = "600:$(id -u)"
```

В profile остаются только имена environment variables и разрешённые target
settings. Значения API login и IDs находятся в process environment или в
явно переданном `.env`; их нельзя печатать, копировать в docs или коммитить.
Полные правила находятся в `private/README.md`.

Live entrypoints принимают только точный корневой `--env-file .env` и не
подхватывают файл неявно. Process environment имеет приоритет над этим файлом.
Для API login профиль обязан ссылаться на основной `IIKO_API_KEY`; наличие
`IIKO_API_KEY_2` не включает fallback. Перед каждым запуском заново проверьте,
что `.env` и private profile принадлежат текущему пользователю и имеют mode
`0600`.

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

### Как подтвердить rate limit

Не меняйте `verified: false` экспериментом с учащением запросов. Сначала
подтвердите server limit по авторитетному источнику или отдельно согласованному
наблюдению, сохраните его безопасное описание в поле `source` и оставьте test
budget не выше 20% server limit при глобальном минимуме 30 секунд. Затем:

1. добавьте или обновите offline tests каталога и убедитесь, что неизвестная
   operation и неподтверждённый budget продолжают fail closed;
2. выделите эксклюзивное окно для одного API login и получите отдельное явное
   разрешение на один контролируемый live checkpoint;
3. выполните только один guarded serial run без параллелизма и retry;
4. меняйте `verified` на `true` только после проверки источника, budget и
   результата без `429`, в отдельном reviewable diff.

Локальный state не координирует тот же login на другой машине или в другом
приложении. Пока эксклюзивность и реальный limit не подтверждены, operation
остаётся `verified: false` и live command должна остановиться до HTTP.

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

### Запрещённый шаблон реального write-запуска

Следующий блок является исполняемым шаблоном, но запускать его сейчас
**запрещено**. Он предназначен только для будущего отдельно авторизованного
контролируемого запуска; это не команда для текущей проверки документации.

```bash
PYTHONDONTWRITEBYTECODE=1 uv run --frozen --offline pytest -m live_write -n0 \
  tests/integration/write/test_stop_list.py::test_stop_list_add_is_accepted_and_removed \
  --live-profile test-server \
  --env-file .env \
  --target-organization "${IIKO_TEST_ORGANIZATION_ID:?required}" \
  --allow-live-write \
  --allow-audit-residue
```

Шаблон остаётся запрещённым, пока одновременно не выполнены все условия:

- для `get_stop_lists`, `add_products_to_stop_list` и
  `remove_products_from_stop_list` проверены реальные server rates и выставлен
  `verified: true`;
- в write-enabled private profile и allowlist настроены выделенные целевые
  organization, terminal group и единственный test product;
- получена отдельная явная авторизация именно на этот live-write запуск.

Даже после выполнения этих условий безопасный placeholder
`IIKO_TEST_ORGANIZATION_ID` должен быть явно задан точным UUID выделенной
organization; сам текст шаблона не содержит live identifier.

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

Если scanner нашёл настоящий API login, остановите commit/publish и не
печатайте совпадение. Отзовите и замените login в iiko, удалите его из
worktree и index (а если он уже опубликован — отдельно согласуйте очистку Git
history), затем обновите локальный `.env` с mode `0600`. После ротации заново
запустите обычный `verify-no-secrets` и убедитесь, что audited baseline не
изменился. Настоящий secret никогда не помечается false positive и не
добавляется в baseline.

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

## Проверка Git tag в downstream без изменения manager

Этот pipeline не изменяет `/home/ivan/programming/Iikocloud-manager`. После
того как tag действительно опубликован, его можно проверить из каталога
manager в изолированном окружении без изменения `pyproject.toml`, `uv.lock` и
рабочего дерева:

```bash
cd /home/ivan/programming/Iikocloud-manager
uv run --isolated --no-project \
  --with "iikocloud-client @ git+ssh://git@github.com/UserVanya/Iikocloud-py-sdk.git@v0.1.0" \
  python -c "from iikocloud_client import ApiClient, Configuration; print(ApiClient.__name__, Configuration.__name__)"
```

Замените `v0.1.0` на созданный release tag. Постоянное закрепление зависимости
в manager выполняется отдельным migration change после этой проверки; не
подменяйте tag веткой.

## Как пополнять troubleshooting ledger

Запись добавляется только когда один и тот же детерминированный failure pattern
повторился, root cause установлена, а workaround проверен. В той же change set
добавьте одну строку в `docs/troubleshooting.md`: дата, sanitized context,
симптом, причина, безопасный workaround, профилактика и способ проверки. Не
записывайте предположения, `.env` values, login/token, private payload,
capture, receipt или mutation journal. Если причина или решение ещё не
подтверждены, ledger не меняется.
