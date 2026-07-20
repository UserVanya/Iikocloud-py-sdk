# OrderAttentionNotificationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_info** | **str** | Additional info about the problem. | 
**order_id** | **UUID** | Order ID. | 
**order_source** | **str** | Order source. | 

## Example

```python
from iikocloud_client.models.order_attention_notification_request import OrderAttentionNotificationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrderAttentionNotificationRequest from a JSON string
order_attention_notification_request_instance = OrderAttentionNotificationRequest.from_json(json)
# print the JSON string representation of the object
print(OrderAttentionNotificationRequest.to_json())

# convert the object into a dict
order_attention_notification_request_dict = order_attention_notification_request_instance.to_dict()
# create an instance of OrderAttentionNotificationRequest from a dict
order_attention_notification_request_from_dict = OrderAttentionNotificationRequest.from_dict(order_attention_notification_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


