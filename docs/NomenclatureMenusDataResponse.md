# NomenclatureMenusDataResponse

Response with stock lists.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **UUID** | Operation ID. | 
**external_menus** | [**List[NomenclatureExternalMenu]**](NomenclatureExternalMenu.md) | External menu. | [optional] 
**price_categories** | [**List[NomenclaturePriceCategory]**](NomenclaturePriceCategory.md) | Price category. | [optional] 

## Example

```python
from iikocloud_client.models.nomenclature_menus_data_response import NomenclatureMenusDataResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NomenclatureMenusDataResponse from a JSON string
nomenclature_menus_data_response_instance = NomenclatureMenusDataResponse.from_json(json)
# print the JSON string representation of the object
print(NomenclatureMenusDataResponse.to_json())

# convert the object into a dict
nomenclature_menus_data_response_dict = nomenclature_menus_data_response_instance.to_dict()
# create an instance of NomenclatureMenusDataResponse from a dict
nomenclature_menus_data_response_from_dict = NomenclatureMenusDataResponse.from_dict(nomenclature_menus_data_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


