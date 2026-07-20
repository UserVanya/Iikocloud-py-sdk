# MenusDataResponse

Response with stock lists.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **UUID** | Operation ID. | 
**external_menus** | [**List[ExternalMenu]**](ExternalMenu.md) | External menu. | [optional] 
**price_categories** | [**List[NomenclaturePriceCategory]**](NomenclaturePriceCategory.md) | Price category. | [optional] 

## Example

```python
from iikocloud_client.models.menus_data_response import MenusDataResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MenusDataResponse from a JSON string
menus_data_response_instance = MenusDataResponse.from_json(json)
# print the JSON string representation of the object
print(MenusDataResponse.to_json())

# convert the object into a dict
menus_data_response_dict = menus_data_response_instance.to_dict()
# create an instance of MenusDataResponse from a dict
menus_data_response_from_dict = MenusDataResponse.from_dict(menus_data_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


