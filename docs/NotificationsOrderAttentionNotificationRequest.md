# NotificationsOrderAttentionNotificationRequest

Request to notify external systems (iikoFront and iikoWeb) about an order requiring attention.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_source** | **str** | Order source. | 
**order_id** | **str** | Order ID. | 
**additional_info** | **str** | Additional info about the problem. | 

## Example

```python
from iikocloud_client.models.notifications_order_attention_notification_request import NotificationsOrderAttentionNotificationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationsOrderAttentionNotificationRequest from a JSON string
notifications_order_attention_notification_request_instance = NotificationsOrderAttentionNotificationRequest.from_json(json)
# print the JSON string representation of the object
print(NotificationsOrderAttentionNotificationRequest.to_json())

# convert the object into a dict
notifications_order_attention_notification_request_dict = notifications_order_attention_notification_request_instance.to_dict()
# create an instance of NotificationsOrderAttentionNotificationRequest from a dict
notifications_order_attention_notification_request_from_dict = NotificationsOrderAttentionNotificationRequest.from_dict(notifications_order_attention_notification_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


