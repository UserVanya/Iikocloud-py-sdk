# TransportNomenclatureMenusDataResponse

Response with stock lists.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **str** | Operation ID. | 
**external_menus** | [**List[TransportNomenclatureExternalMenu]**](TransportNomenclatureExternalMenu.md) | External menu. | [optional] 
**price_categories** | [**List[TransportNomenclaturePriceCategory]**](TransportNomenclaturePriceCategory.md) | Price category. | [optional] 

## Example

```python
from iikocloud_client.models.transport_nomenclature_menus_data_response import TransportNomenclatureMenusDataResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TransportNomenclatureMenusDataResponse from a JSON string
transport_nomenclature_menus_data_response_instance = TransportNomenclatureMenusDataResponse.from_json(json)
# print the JSON string representation of the object
print(TransportNomenclatureMenusDataResponse.to_json())

# convert the object into a dict
transport_nomenclature_menus_data_response_dict = transport_nomenclature_menus_data_response_instance.to_dict()
# create an instance of TransportNomenclatureMenusDataResponse from a dict
transport_nomenclature_menus_data_response_from_dict = TransportNomenclatureMenusDataResponse.from_dict(transport_nomenclature_menus_data_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


