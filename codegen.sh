docker run --rm \
  -v "${PWD}:/local" \
  openapitools/openapi-generator-cli generate \
  -i /local/iikocloud_openapi.json \
  -g python \
  -o /local \
  -c /local/config.yaml