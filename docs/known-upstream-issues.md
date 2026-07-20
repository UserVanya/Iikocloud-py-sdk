# Известные проблемы upstream OpenAPI

Этот реестр описывает только проверенные corrections текущего tracked
snapshot. Он не заменяет сами overlays: точные guard hashes и полные actions
находятся в `openapi/overlays/`. Private captures и реальные IDs здесь не
публикуются.

## Как читать реестр

`issue` — стабильный `x-iiko-sdk-guard.issue`. `Fragment` — raw upstream
JSONPath или компонент, к которому привязана correction. Любой guard проверяет
ровно ожидаемое число совпадений и SHA-256 исходного fragment; изменение
upstream останавливает pipeline до нового review.

Correction можно удалить только когда новый upstream выражает тот же контракт
без overlay, generated contract tests проходят, а `verify` подтверждает
воспроизводимость. Нельзя просто обновить digest под изменившийся fragment.

## Authentication и server contract

Источник: `openapi/overlays/contracts.overlay.yaml`.

| Issue | Fragment | Correction | Основание | Условие удаления |
|---|---|---|---|---|
| `iiko-root-server` | document root | Добавить canonical iiko Cloud server URL | Generated `Configuration.host` должен иметь корректный default | Upstream содержит проверенный root `servers` |
| `iiko-bearer-scheme` | `$.components` | Добавить HTTP bearer scheme `BearerAuth` | Generated client должен формировать ровно один bearer header | Upstream объявляет эквивалентную reusable scheme |
| `remove-raw-authorization-parameters` | raw `Authorization` header parameters операций | Удалить дублирующиеся ручные header parameters | Parameter мешает стандартной generated auth configuration | Upstream больше не дублирует header в операциях |
| `require-bearer-authentication` | все API operations | Добавить `security: [{BearerAuth: []}]` | Contract test проверяет generated bearer behavior | Upstream корректно задаёт security для всех защищённых операций |
| `remove-bearer-from-post-/api/1/access_token`, `mark-post-/api/1/access_token-public` | `/api/1/access_token` POST | Явно оставить endpoint публичным | Token нельзя требовать до аутентификации | Upstream public security семантически совпадает |
| `remove-bearer-from-post-/api/v2/access_token`, `mark-post-/api/v2/access_token-public` | `/api/v2/access_token` POST | Явно оставить endpoint публичным | То же для v2 authentication | Upstream public security семантически совпадает |

## Mechanical типы и имена

Источник: `openapi/overlays/types.overlay.yaml`,
`openapi/model-name-overrides.yaml` и naming stage.

| Issue family | Fragment | Correction | Основание | Условие удаления |
|---|---|---|---|---|
| `normalize-pseudo-type-*` | schema properties с raw типами `bool`, `uuid`, `float`, `integer <int64>`, `Array of strings <uuid>` и constant-string pseudo types | Преобразовать в валидные OpenAPI `type`/`format`/`items`/`enum` | Strict schema lint и pinned generator validation | Upstream использует стандартный JSON Schema/OpenAPI shape |
| `remove-malformed-scalar-required-*` | `TaxCategoryDto*` scalar properties | Удалить boolean `required` внутри property; required-list допустим только у object schema | Strict lint | Upstream удаляет malformed scalar keyword |
| reviewed model mappings | collision-prone CLR-qualified component keys | Выдать стабильные доменные Python model names | Collision review; numeric fallback запрещён | Upstream names больше не collide и public Python names можно сохранить совместимо |
| generator-invalid CLR generic keys | CLR `RmsItemsResponseWrapper` component keys с backtick/brackets | Физически переименовать только invalid component keys по тому же reviewed mapping и переписать точные local `$ref` | Pinned generator отклонял исходные component names | Upstream публикует валидные стабильные component keys; старые refs отсутствуют |

## External menu: стабильный response union

Источник: `openapi/overlays/operations.overlay.yaml` и
`openapi/overlays/polymorphism.overlay.yaml`. Evidence acceptance потребовал
три отдельно полученных sanitized response версии 2, 3 и 4. В Git сохранены
только минимальные synthetic fixtures:
`tests/fixtures/contracts/external-menu-v2.json`,
`external-menu-v3.json` и `external-menu-v4.json`.

### Response model

| Issue | Fragment | Correction | Evidence | Условие удаления |
|---|---|---|---|---|
| `external-menu-response-title` | `/api/2/menu/by_id` POST, JSON response `200` schema | Добавить title `ExternalMenuResponse` | Generated V2/V3/V4 union contract test | Upstream даёт стабильное, совместимое имя response union |

### Корневые V2, V3 и V4

| Issues | Fragment | Correction | Evidence | Условие удаления |
|---|---|---|---|---|
| `external-menu-v2-format-version`, `external-menu-v2-required-remove`, `external-menu-v2-required` | `ExternalMenuV2` | Зафиксировать `formatVersion` как enum/default `2` и включить поле в object `required` | Sanitized V2 evidence и synthetic V2 fixture | Upstream делает V2 branch структурно взаимоисключающей |
| `external-menu-v3-format-version`, `external-menu-v3-required-remove`, `external-menu-v3-required` | `ExternalMenuV3` | Зафиксировать `formatVersion` как enum/default `3` и включить поле в `required` | Sanitized V3 evidence и synthetic V3 fixture | То же для V3 |
| `external-menu-v4-format-version`, `external-menu-v4-required-remove`, `external-menu-v4-required` | `ExternalMenuV4` | Зафиксировать `formatVersion` как enum/default `4` и включить поле в `required` | Sanitized V4 evidence и synthetic V4 fixture | То же для V4 |

Без этих actions все три upstream branches допускают недостаточно различимые
объекты, а V3/V4 ошибочно имеют default `2`. Generated test
`tests/generated/test_external_menu_response.py` требует ровно один выбранный
branch для каждой synthetic fixture.

### Неверные shapes и nullability в menu data

Все перечисленные IDs имеют префикс `external-menu-schema-`; remove-actions с
суффиксом `-remove` сначала удаляют конфликтующие `type`, `items`, `description`
или `enum`, после чего guarded update задаёт reviewed shape.

| Issue fragment(s) | Raw проблема | Correction | Evidence / removal condition |
|---|---|---|---|
| `ExternalMenuPriceByDepartmentsDto-properties-organizationId` | В properties отсутствует встречающееся поле | Добавить UUID string `organizationId` | Sanitized schema-aware menu evidence; удалить после эквивалентного upstream property |
| `ExternalMenuItem-properties-taxCategory` | Object ошибочно описан как array | Nullable `oneOf` со ссылкой на `TaxCategoryDto3` | Schema validation against accepted evidence; удалить после корректного upstream ref |
| `ExternalMenuItemSize-properties-nutritionPerHundredGrams` | Object ошибочно описан как array | Ссылка на `NutritionInfoDto` | То же |
| `ExternalMenuModifierItem-properties-nutritionPerHundredGrams` | Object ошибочно описан как array | Nullable `oneOf` с `NutritionInfoDto5` | То же |
| `ExternalMenuModifierItem{,2,3}-properties-restrictions` | Object ошибочно описан как array | Nullable `oneOf` к соответствующему `ModifierRestrictionsDto5/6/7` | V2/V3/V4 evidence; удалить только после исправления всех соответствующих upstream branches |
| `ExternalMenuV3-properties-overrideTaxCategories`, `ExternalMenuV4-properties-overrideTaxCategories` | UUID-keyed map ошибочно описан как array | Object с `additionalProperties`, значением которого является array соответствующего `OverrideTaxesDto*` | V3/V4 evidence; удалить после корректной map schema |
| `ExternalMenuItem{,2,3}-properties-type` | Enum не содержит наблюдаемый публичный literal `SERVICE` | Enum `DISH`, `COMBO`, `SERVICE` до V4 branch specialization | Schema-aware evidence hints и analyzer regressions; удалить после полного upstream enum |
| `ExternalMenuItem{,2,3}-properties-modifierSchemaId` | Реальный `null` запрещён | Добавить `nullable: true` | V2/V3/V4 evidence; удалить после upstream nullability |
| `ExternalMenuItemSize-properties-sizeId`, `ExternalMenuItemSize{2,3}-properties-id` | Default/единственный size может иметь `null` ID | Добавить `nullable: true` | Versioned menu evidence; удалить после upstream nullability |
| `ExternalMenuPriceByDepartmentsDto{,2,3}-properties-price` | Недоступный для продажи size может иметь `null` price | Добавить `nullable: true` | Versioned menu evidence; удалить после upstream nullability |

Validator также имеет узкое reviewed исключение для undeclared barcode property,
но только когда её значение строго `null` и component/property-name hashes
совпадают. Любое ненулевое или новое неизвестное поле продолжает fail closed;
это исключение удаляется, когда upstream явно опишет поле.

### V4 item discriminator и `ExternalMenuComboItem`

| Issue | Fragment | Correction | Evidence | Условие удаления |
|---|---|---|---|---|
| `external-menu-v4-discriminator` | `ExternalMenuCategory3.properties.items.items` | Discriminator `type`: `DISH` и `SERVICE` → `ExternalMenuItem3`, `COMBO` → `ExternalMenuComboItem` | Accepted V4 analysis проверил literal-to-branch consistency | Upstream содержит эквивалентный discriminator и branches остаются disjoint |
| `external-menu-item3-type-enum-remove`, `external-menu-item3-type` | `ExternalMenuItem3.properties.type` | Ограничить dish branch literals до `DISH`/`SERVICE`, default `DISH` | Analyzer и generated union regressions | Upstream item branch имеет тот же enum |
| `external-menu-item3-required-remove`, `external-menu-item3-required` | `ExternalMenuItem3.required` | Добавить `type` к реально обязательным dish fields | V4 structural matching | Upstream required-list эквивалентен |
| `external-menu-combo-item-type` | `ExternalMenuComboItem.properties.type` | Ограничить поле единственным literal `COMBO`, default `COMBO` | Promotion допускается только при наличии хотя бы одного matching combo в private sanitized V4 evidence | Upstream combo type имеет `enum: [COMBO]` |
| `external-menu-combo-required-remove`, `external-menu-combo-required` | `ExternalMenuComboItem.required` | Заменить список на `sizes`, `type`, `id` | Raw schema требовала пять полей, которых у combo component вообще нет; reviewed fragment hash и combo evidence закрепляют исключение | Upstream удаляет undefined required names и live/synthetic contract tests подтверждают новый список |

`ExternalMenuComboItem` особенно опасен для автоматической генерации: исходный
`required` ссылается на dish-only поля `itemSizes`, `modifierSchemaId`,
`orderItemType`, `allergenGroupIds` и `splittable`, отсутствующие в combo
`properties`. Одновременно его `type` является произвольной строкой. Поэтому
обычный `oneOf` не может надёжно выбрать branch. Текущая correction делает
branches disjoint и проверяется до promotion; private payload при этом не
становится частью репозитория.

## Процедура удаления correction

1. Запустите `upstream-check` и сохраните публичный diff под `build/`.
2. Убедитесь, что upstream fragment теперь выражает тот же контракт. Старый
   guard должен стать stale — это ожидаемый сигнал review, а не повод заменить
   hash.
3. Удалите только ставшую ненужной action или mapping и обновите focused test.
4. Для menu defect заново проверьте все затронутые версии; live recapture
   выполняется только если публичных synthetic fixtures недостаточно доказать
   контракт и только по guarded процедуре из `generation.md`.
5. Выполните offline `sync`, `verify`, wheel checks и просмотрите generated API
   diff до commit.
