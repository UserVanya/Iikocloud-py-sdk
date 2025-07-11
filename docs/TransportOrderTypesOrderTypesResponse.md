# TransportOrderTypesOrderTypesResponse

Response to request for order types by organization.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **str** | Operation ID. | 
**order_types** | [**List[TransportCommonRmsItemsResponseWrapperOrderType]**](TransportCommonRmsItemsResponseWrapperOrderType.md) | List of order types. | 

## Example

```python
from iikocloud_client.models.transport_order_types_order_types_response import TransportOrderTypesOrderTypesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TransportOrderTypesOrderTypesResponse from a JSON string
transport_order_types_order_types_response_instance = TransportOrderTypesOrderTypesResponse.from_json(json)
# print the JSON string representation of the object
print(TransportOrderTypesOrderTypesResponse.to_json())

# convert the object into a dict
transport_order_types_order_types_response_dict = transport_order_types_order_types_response_instance.to_dict()
# create an instance of TransportOrderTypesOrderTypesResponse from a dict
transport_order_types_order_types_response_from_dict = TransportOrderTypesOrderTypesResponse.from_dict(transport_order_types_order_types_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


