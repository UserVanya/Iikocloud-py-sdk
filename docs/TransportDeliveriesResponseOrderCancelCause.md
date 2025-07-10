# TransportDeliveriesResponseOrderCancelCause

Delivery cancellation reason.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID. | 
**name** | **str** | Description. | 

## Example

```python
from iiko_cloud_client.models.transport_deliveries_response_order_cancel_cause import TransportDeliveriesResponseOrderCancelCause

# TODO update the JSON string below
json = "{}"
# create an instance of TransportDeliveriesResponseOrderCancelCause from a JSON string
transport_deliveries_response_order_cancel_cause_instance = TransportDeliveriesResponseOrderCancelCause.from_json(json)
# print the JSON string representation of the object
print(TransportDeliveriesResponseOrderCancelCause.to_json())

# convert the object into a dict
transport_deliveries_response_order_cancel_cause_dict = transport_deliveries_response_order_cancel_cause_instance.to_dict()
# create an instance of TransportDeliveriesResponseOrderCancelCause from a dict
transport_deliveries_response_order_cancel_cause_from_dict = TransportDeliveriesResponseOrderCancelCause.from_dict(transport_deliveries_response_order_cancel_cause_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


