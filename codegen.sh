#!/bin/bash
# Скрипт для генерации Python клиента из OpenAPI спецификации
# Автоматически подготавливает спецификацию перед генерацией

set -e  # Остановка при ошибке

# Подготовка OpenAPI спецификации
echo "Подготовка OpenAPI спецификации..."
./prepare_openapi.sh

echo ""
echo "Запуск генерации кода..."
echo ""

# Генерация кода
docker run --rm \
  -v "${PWD}:/local" \
  openapitools/openapi-generator-cli generate \
  -i /local/iikocloud_openapi.json \
  -g python \
  -o /local \
  -c /local/config.yaml \
  --skip-validate-spec