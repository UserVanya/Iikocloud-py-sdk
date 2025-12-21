# IikoTransportPublicApiContractsAddressRegionsRequest

Organization request DTO.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_ids** | **List[UUID]** | IDs of organizations that require data return.                Can be obtained by &#x60;/organizations&#x60; operation. | 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_address_regions_request import IikoTransportPublicApiContractsAddressRegionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsAddressRegionsRequest from a JSON string
iiko_transport_public_api_contracts_address_regions_request_instance = IikoTransportPublicApiContractsAddressRegionsRequest.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsAddressRegionsRequest.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_address_regions_request_dict = iiko_transport_public_api_contracts_address_regions_request_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsAddressRegionsRequest from a dict
iiko_transport_public_api_contracts_address_regions_request_from_dict = IikoTransportPublicApiContractsAddressRegionsRequest.from_dict(iiko_transport_public_api_contracts_address_regions_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


