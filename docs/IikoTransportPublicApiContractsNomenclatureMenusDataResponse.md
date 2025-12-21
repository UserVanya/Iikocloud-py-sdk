# IikoTransportPublicApiContractsNomenclatureMenusDataResponse

Response with stock lists.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **UUID** | Operation ID. | 
**external_menus** | [**List[IikoTransportPublicApiContractsNomenclatureExternalMenu]**](IikoTransportPublicApiContractsNomenclatureExternalMenu.md) | External menu. | [optional] 
**price_categories** | [**List[IikoTransportPublicApiContractsNomenclaturePriceCategory]**](IikoTransportPublicApiContractsNomenclaturePriceCategory.md) | Price category. | [optional] 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_nomenclature_menus_data_response import IikoTransportPublicApiContractsNomenclatureMenusDataResponse

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsNomenclatureMenusDataResponse from a JSON string
iiko_transport_public_api_contracts_nomenclature_menus_data_response_instance = IikoTransportPublicApiContractsNomenclatureMenusDataResponse.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsNomenclatureMenusDataResponse.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_nomenclature_menus_data_response_dict = iiko_transport_public_api_contracts_nomenclature_menus_data_response_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsNomenclatureMenusDataResponse from a dict
iiko_transport_public_api_contracts_nomenclature_menus_data_response_from_dict = IikoTransportPublicApiContractsNomenclatureMenusDataResponse.from_dict(iiko_transport_public_api_contracts_nomenclature_menus_data_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


