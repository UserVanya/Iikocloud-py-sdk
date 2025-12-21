# IikoTransportPublicApiContractsNomenclatureSizePrice

Price per item size.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**size_id** | **UUID** | Item size ID. | 
**price** | [**IikoTransportPublicApiContractsNomenclaturePrice**](IikoTransportPublicApiContractsNomenclaturePrice.md) | Price per this item size. | 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_nomenclature_size_price import IikoTransportPublicApiContractsNomenclatureSizePrice

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsNomenclatureSizePrice from a JSON string
iiko_transport_public_api_contracts_nomenclature_size_price_instance = IikoTransportPublicApiContractsNomenclatureSizePrice.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsNomenclatureSizePrice.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_nomenclature_size_price_dict = iiko_transport_public_api_contracts_nomenclature_size_price_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsNomenclatureSizePrice from a dict
iiko_transport_public_api_contracts_nomenclature_size_price_from_dict = IikoTransportPublicApiContractsNomenclatureSizePrice.from_dict(iiko_transport_public_api_contracts_nomenclature_size_price_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


