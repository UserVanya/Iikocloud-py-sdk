# OrderTypesOrderTypesResponse

Response to request for order types by organization.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **str** | Operation ID. | 
**order_types** | [**List[WrapperOrderTypesOrderType]**](WrapperOrderTypesOrderType.md) | List of order types. | 

## Example

```python
from iikocloud_client.models.order_types_order_types_response import OrderTypesOrderTypesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OrderTypesOrderTypesResponse from a JSON string
order_types_order_types_response_instance = OrderTypesOrderTypesResponse.from_json(json)
# print the JSON string representation of the object
print(OrderTypesOrderTypesResponse.to_json())

# convert the object into a dict
order_types_order_types_response_dict = order_types_order_types_response_instance.to_dict()
# create an instance of OrderTypesOrderTypesResponse from a dict
order_types_order_types_response_from_dict = OrderTypesOrderTypesResponse.from_dict(order_types_order_types_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


