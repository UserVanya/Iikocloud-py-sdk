# DeliveriesResponseOrderCancelInfo

Order cancellation details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**when_cancelled** | **str** | Cancellation time (Local for delivery terminal). | 
**cause** | [**DeliveriesResponseOrderCancelCause**](DeliveriesResponseOrderCancelCause.md) | Delivery cancellation reason. | 
**comment** | **str** | Delivery cancellation comment. | [optional] 

## Example

```python
from iikocloud_client.models.deliveries_response_order_cancel_info import DeliveriesResponseOrderCancelInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveriesResponseOrderCancelInfo from a JSON string
deliveries_response_order_cancel_info_instance = DeliveriesResponseOrderCancelInfo.from_json(json)
# print the JSON string representation of the object
print(DeliveriesResponseOrderCancelInfo.to_json())

# convert the object into a dict
deliveries_response_order_cancel_info_dict = deliveries_response_order_cancel_info_instance.to_dict()
# create an instance of DeliveriesResponseOrderCancelInfo from a dict
deliveries_response_order_cancel_info_from_dict = DeliveriesResponseOrderCancelInfo.from_dict(deliveries_response_order_cancel_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


