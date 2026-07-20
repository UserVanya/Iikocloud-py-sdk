# DeliveryOrderResponseCancelCause

Delivery cancellation reason.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | ID. | 
**name** | **str** | Description. | 

## Example

```python
from iikocloud_client.models.delivery_order_response_cancel_cause import DeliveryOrderResponseCancelCause

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveryOrderResponseCancelCause from a JSON string
delivery_order_response_cancel_cause_instance = DeliveryOrderResponseCancelCause.from_json(json)
# print the JSON string representation of the object
print(DeliveryOrderResponseCancelCause.to_json())

# convert the object into a dict
delivery_order_response_cancel_cause_dict = delivery_order_response_cancel_cause_instance.to_dict()
# create an instance of DeliveryOrderResponseCancelCause from a dict
delivery_order_response_cancel_cause_from_dict = DeliveryOrderResponseCancelCause.from_dict(delivery_order_response_cancel_cause_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


