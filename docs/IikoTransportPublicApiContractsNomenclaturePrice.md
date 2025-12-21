# IikoTransportPublicApiContractsNomenclaturePrice

Price per this item size.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_price** | **float** | Current price. | 
**is_included_in_menu** | **bool** | Is on the menu. | 
**next_price** | **float** | New price | [optional] 
**next_included_in_menu** | **bool** | Will be on the menu in the future. | 
**next_date_price** | **str** | New price validity start date (Local for the terminal). | [optional] 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_nomenclature_price import IikoTransportPublicApiContractsNomenclaturePrice

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsNomenclaturePrice from a JSON string
iiko_transport_public_api_contracts_nomenclature_price_instance = IikoTransportPublicApiContractsNomenclaturePrice.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsNomenclaturePrice.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_nomenclature_price_dict = iiko_transport_public_api_contracts_nomenclature_price_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsNomenclaturePrice from a dict
iiko_transport_public_api_contracts_nomenclature_price_from_dict = IikoTransportPublicApiContractsNomenclaturePrice.from_dict(iiko_transport_public_api_contracts_nomenclature_price_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


