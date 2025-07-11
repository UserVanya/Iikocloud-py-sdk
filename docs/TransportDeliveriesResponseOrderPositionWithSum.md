# TransportDeliveriesResponseOrderPositionWithSum

Order item positions with position discount sum.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**position_id** | **str** | Order item position ID. | 
**sum** | **float** | Position discount sum. | 

## Example

```python
from iikocloud_client.models.transport_deliveries_response_order_position_with_sum import TransportDeliveriesResponseOrderPositionWithSum

# TODO update the JSON string below
json = "{}"
# create an instance of TransportDeliveriesResponseOrderPositionWithSum from a JSON string
transport_deliveries_response_order_position_with_sum_instance = TransportDeliveriesResponseOrderPositionWithSum.from_json(json)
# print the JSON string representation of the object
print(TransportDeliveriesResponseOrderPositionWithSum.to_json())

# convert the object into a dict
transport_deliveries_response_order_position_with_sum_dict = transport_deliveries_response_order_position_with_sum_instance.to_dict()
# create an instance of TransportDeliveriesResponseOrderPositionWithSum from a dict
transport_deliveries_response_order_position_with_sum_from_dict = TransportDeliveriesResponseOrderPositionWithSum.from_dict(transport_deliveries_response_order_position_with_sum_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


