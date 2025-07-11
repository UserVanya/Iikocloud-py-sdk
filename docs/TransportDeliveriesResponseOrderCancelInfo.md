# TransportDeliveriesResponseOrderCancelInfo

Order cancellation details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**when_cancelled** | **str** | Cancellation time (Local for delivery terminal). | 
**cause** | [**TransportDeliveriesResponseOrderCancelCause**](TransportDeliveriesResponseOrderCancelCause.md) | Delivery cancellation reason. | 
**comment** | **str** | Delivery cancellation comment. | [optional] 

## Example

```python
from iikocloud_client.models.transport_deliveries_response_order_cancel_info import TransportDeliveriesResponseOrderCancelInfo

# TODO update the JSON string below
json = "{}"
# create an instance of TransportDeliveriesResponseOrderCancelInfo from a JSON string
transport_deliveries_response_order_cancel_info_instance = TransportDeliveriesResponseOrderCancelInfo.from_json(json)
# print the JSON string representation of the object
print(TransportDeliveriesResponseOrderCancelInfo.to_json())

# convert the object into a dict
transport_deliveries_response_order_cancel_info_dict = transport_deliveries_response_order_cancel_info_instance.to_dict()
# create an instance of TransportDeliveriesResponseOrderCancelInfo from a dict
transport_deliveries_response_order_cancel_info_from_dict = TransportDeliveriesResponseOrderCancelInfo.from_dict(transport_deliveries_response_order_cancel_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


