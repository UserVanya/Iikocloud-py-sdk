# IikoTransportPublicApiContractsAddressRegion

Delivery district DTO.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Region ID in RMS. | 
**name** | **str** | Name. | 
**external_revision** | **int** | External revision. | [optional] 
**is_deleted** | **bool** | Is-Deleted attribute. | 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_address_region import IikoTransportPublicApiContractsAddressRegion

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsAddressRegion from a JSON string
iiko_transport_public_api_contracts_address_region_instance = IikoTransportPublicApiContractsAddressRegion.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsAddressRegion.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_address_region_dict = iiko_transport_public_api_contracts_address_region_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsAddressRegion from a dict
iiko_transport_public_api_contracts_address_region_from_dict = IikoTransportPublicApiContractsAddressRegion.from_dict(iiko_transport_public_api_contracts_address_region_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


