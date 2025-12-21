# IikoTransportPublicApiContractsRemovalTypesRemovalTypesRequest

Request for organization's removal types (reasons for deletion).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_ids** | **List[UUID]** | Organizations ids which removal types needs to be returned.                Can be obtained by &#x60;/organizations&#x60; operation. | 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_removal_types_removal_types_request import IikoTransportPublicApiContractsRemovalTypesRemovalTypesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsRemovalTypesRemovalTypesRequest from a JSON string
iiko_transport_public_api_contracts_removal_types_removal_types_request_instance = IikoTransportPublicApiContractsRemovalTypesRemovalTypesRequest.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsRemovalTypesRemovalTypesRequest.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_removal_types_removal_types_request_dict = iiko_transport_public_api_contracts_removal_types_removal_types_request_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsRemovalTypesRemovalTypesRequest from a dict
iiko_transport_public_api_contracts_removal_types_removal_types_request_from_dict = IikoTransportPublicApiContractsRemovalTypesRemovalTypesRequest.from_dict(iiko_transport_public_api_contracts_removal_types_removal_types_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


