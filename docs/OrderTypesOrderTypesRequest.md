# OrderTypesOrderTypesRequest

Request for order types.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_ids** | **List[UUID]** | Organizations IDs which payment types have to be returned.                 Can be obtained by &#x60;/organizations&#x60; operation. | 

## Example

```python
from iikocloud_client.models.order_types_order_types_request import OrderTypesOrderTypesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrderTypesOrderTypesRequest from a JSON string
order_types_order_types_request_instance = OrderTypesOrderTypesRequest.from_json(json)
# print the JSON string representation of the object
print(OrderTypesOrderTypesRequest.to_json())

# convert the object into a dict
order_types_order_types_request_dict = order_types_order_types_request_instance.to_dict()
# create an instance of OrderTypesOrderTypesRequest from a dict
order_types_order_types_request_from_dict = OrderTypesOrderTypesRequest.from_dict(order_types_order_types_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


