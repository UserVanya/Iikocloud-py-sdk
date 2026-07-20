# OrderTypesResponse

Response to request for order types by organization.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **UUID** | Operation ID. | 
**order_types** | [**List[RmsOrderTypeItemsResponse]**](RmsOrderTypeItemsResponse.md) | List of order types. | 

## Example

```python
from iikocloud_client.models.order_types_response import OrderTypesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OrderTypesResponse from a JSON string
order_types_response_instance = OrderTypesResponse.from_json(json)
# print the JSON string representation of the object
print(OrderTypesResponse.to_json())

# convert the object into a dict
order_types_response_dict = order_types_response_instance.to_dict()
# create an instance of OrderTypesResponse from a dict
order_types_response_from_dict = OrderTypesResponse.from_dict(order_types_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


