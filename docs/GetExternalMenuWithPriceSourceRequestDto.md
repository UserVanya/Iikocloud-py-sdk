# GetExternalMenuWithPriceSourceRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | id of the requested menu | [optional] 
**price_source** | **str** | Price from the external menu or price category | [optional] 
**organizations** | **List[str]** |  | [optional] 
**price_category_id** | **str** |  | [optional] 

## Example

```python
from iiko_cloud_client.models.get_external_menu_with_price_source_request_dto import GetExternalMenuWithPriceSourceRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of GetExternalMenuWithPriceSourceRequestDto from a JSON string
get_external_menu_with_price_source_request_dto_instance = GetExternalMenuWithPriceSourceRequestDto.from_json(json)
# print the JSON string representation of the object
print(GetExternalMenuWithPriceSourceRequestDto.to_json())

# convert the object into a dict
get_external_menu_with_price_source_request_dto_dict = get_external_menu_with_price_source_request_dto_instance.to_dict()
# create an instance of GetExternalMenuWithPriceSourceRequestDto from a dict
get_external_menu_with_price_source_request_dto_from_dict = GetExternalMenuWithPriceSourceRequestDto.from_dict(get_external_menu_with_price_source_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


