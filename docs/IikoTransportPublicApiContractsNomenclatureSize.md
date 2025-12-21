# IikoTransportPublicApiContractsNomenclatureSize

Item size.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | ID. | [optional] 
**name** | **str** | Name. | [optional] 
**priority** | **int** | Priority (serial number) of the size in the size scale. | [optional] 
**is_default** | **bool** | Is the default size in the size scale. | [optional] 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_nomenclature_size import IikoTransportPublicApiContractsNomenclatureSize

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsNomenclatureSize from a JSON string
iiko_transport_public_api_contracts_nomenclature_size_instance = IikoTransportPublicApiContractsNomenclatureSize.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsNomenclatureSize.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_nomenclature_size_dict = iiko_transport_public_api_contracts_nomenclature_size_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsNomenclatureSize from a dict
iiko_transport_public_api_contracts_nomenclature_size_from_dict = IikoTransportPublicApiContractsNomenclatureSize.from_dict(iiko_transport_public_api_contracts_nomenclature_size_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


