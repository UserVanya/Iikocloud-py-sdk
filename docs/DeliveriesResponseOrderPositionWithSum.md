# DeliveriesResponseOrderPositionWithSum

Order item positions with position discount sum.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**position_id** | **str** | Order item position ID. | 
**sum** | **float** | Position discount sum. | 

## Example

```python
from iikocloud_client.models.deliveries_response_order_position_with_sum import DeliveriesResponseOrderPositionWithSum

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveriesResponseOrderPositionWithSum from a JSON string
deliveries_response_order_position_with_sum_instance = DeliveriesResponseOrderPositionWithSum.from_json(json)
# print the JSON string representation of the object
print(DeliveriesResponseOrderPositionWithSum.to_json())

# convert the object into a dict
deliveries_response_order_position_with_sum_dict = deliveries_response_order_position_with_sum_instance.to_dict()
# create an instance of DeliveriesResponseOrderPositionWithSum from a dict
deliveries_response_order_position_with_sum_from_dict = DeliveriesResponseOrderPositionWithSum.from_dict(deliveries_response_order_position_with_sum_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


