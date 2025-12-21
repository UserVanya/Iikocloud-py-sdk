# IikoTransportPublicApiContractsRemovalTypesRemovalTypesResponse

Response with removal types (reasons for deletion) list.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **UUID** | Operation ID. | 
**removal_types** | [**List[IikoTransportPublicApiContractsRemovalTypesRemovalType]**](IikoTransportPublicApiContractsRemovalTypesRemovalType.md) | List of removal types. | 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_removal_types_removal_types_response import IikoTransportPublicApiContractsRemovalTypesRemovalTypesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsRemovalTypesRemovalTypesResponse from a JSON string
iiko_transport_public_api_contracts_removal_types_removal_types_response_instance = IikoTransportPublicApiContractsRemovalTypesRemovalTypesResponse.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsRemovalTypesRemovalTypesResponse.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_removal_types_removal_types_response_dict = iiko_transport_public_api_contracts_removal_types_removal_types_response_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsRemovalTypesRemovalTypesResponse from a dict
iiko_transport_public_api_contracts_removal_types_removal_types_response_from_dict = IikoTransportPublicApiContractsRemovalTypesRemovalTypesResponse.from_dict(iiko_transport_public_api_contracts_removal_types_removal_types_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


