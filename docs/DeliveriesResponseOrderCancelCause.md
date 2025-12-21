# DeliveriesResponseOrderCancelCause

Delivery cancellation reason.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | ID. | 
**name** | **str** | Description. | 

## Example

```python
from iikocloud_client.models.deliveries_response_order_cancel_cause import DeliveriesResponseOrderCancelCause

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveriesResponseOrderCancelCause from a JSON string
deliveries_response_order_cancel_cause_instance = DeliveriesResponseOrderCancelCause.from_json(json)
# print the JSON string representation of the object
print(DeliveriesResponseOrderCancelCause.to_json())

# convert the object into a dict
deliveries_response_order_cancel_cause_dict = deliveries_response_order_cancel_cause_instance.to_dict()
# create an instance of DeliveriesResponseOrderCancelCause from a dict
deliveries_response_order_cancel_cause_from_dict = DeliveriesResponseOrderCancelCause.from_dict(deliveries_response_order_cancel_cause_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


