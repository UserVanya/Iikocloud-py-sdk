# IikoTransportPublicApiContractsOrderTypesOrderTypesResponse

Response to request for order types by organization.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **UUID** | Operation ID. | 
**order_types** | [**List[RmsItemsResponseWrapperOrderTypesOrderType]**](RmsItemsResponseWrapperOrderTypesOrderType.md) | List of order types. | 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_order_types_order_types_response import IikoTransportPublicApiContractsOrderTypesOrderTypesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsOrderTypesOrderTypesResponse from a JSON string
iiko_transport_public_api_contracts_order_types_order_types_response_instance = IikoTransportPublicApiContractsOrderTypesOrderTypesResponse.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsOrderTypesOrderTypesResponse.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_order_types_order_types_response_dict = iiko_transport_public_api_contracts_order_types_order_types_response_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsOrderTypesOrderTypesResponse from a dict
iiko_transport_public_api_contracts_order_types_order_types_response_from_dict = IikoTransportPublicApiContractsOrderTypesOrderTypesResponse.from_dict(iiko_transport_public_api_contracts_order_types_order_types_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


