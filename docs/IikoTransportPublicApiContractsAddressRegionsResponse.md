# IikoTransportPublicApiContractsAddressRegionsResponse

Service response with list of districts.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **UUID** | Operation ID. | 
**regions** | [**List[RmsItemsResponseWrapperAddressRegion]**](RmsItemsResponseWrapperAddressRegion.md) | List of districts. | 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_address_regions_response import IikoTransportPublicApiContractsAddressRegionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsAddressRegionsResponse from a JSON string
iiko_transport_public_api_contracts_address_regions_response_instance = IikoTransportPublicApiContractsAddressRegionsResponse.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsAddressRegionsResponse.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_address_regions_response_dict = iiko_transport_public_api_contracts_address_regions_response_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsAddressRegionsResponse from a dict
iiko_transport_public_api_contracts_address_regions_response_from_dict = IikoTransportPublicApiContractsAddressRegionsResponse.from_dict(iiko_transport_public_api_contracts_address_regions_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


