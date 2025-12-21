# IikoTransportPublicApiContractsTipsTypesTipsTypesResponse

Response to request for tips types by api-login`s rms group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **UUID** | Operation ID. | 
**tips_types** | [**List[IikoTransportPublicApiContractsTipsTypesTipsType]**](IikoTransportPublicApiContractsTipsTypesTipsType.md) | List of tips types for rms group. | 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_tips_types_tips_types_response import IikoTransportPublicApiContractsTipsTypesTipsTypesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsTipsTypesTipsTypesResponse from a JSON string
iiko_transport_public_api_contracts_tips_types_tips_types_response_instance = IikoTransportPublicApiContractsTipsTypesTipsTypesResponse.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsTipsTypesTipsTypesResponse.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_tips_types_tips_types_response_dict = iiko_transport_public_api_contracts_tips_types_tips_types_response_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsTipsTypesTipsTypesResponse from a dict
iiko_transport_public_api_contracts_tips_types_tips_types_response_from_dict = IikoTransportPublicApiContractsTipsTypesTipsTypesResponse.from_dict(iiko_transport_public_api_contracts_tips_types_tips_types_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


