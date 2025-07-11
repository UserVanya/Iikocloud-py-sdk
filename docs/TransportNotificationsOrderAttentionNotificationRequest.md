# TransportNotificationsOrderAttentionNotificationRequest

Request to notify external systems (iikoFront and iikoWeb) about an order requiring attention.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_source** | **str** | Order source. | 
**order_id** | **str** | Order ID. | 
**additional_info** | **str** | Additional info about the problem. | 

## Example

```python
from iikocloud_client.models.transport_notifications_order_attention_notification_request import TransportNotificationsOrderAttentionNotificationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TransportNotificationsOrderAttentionNotificationRequest from a JSON string
transport_notifications_order_attention_notification_request_instance = TransportNotificationsOrderAttentionNotificationRequest.from_json(json)
# print the JSON string representation of the object
print(TransportNotificationsOrderAttentionNotificationRequest.to_json())

# convert the object into a dict
transport_notifications_order_attention_notification_request_dict = transport_notifications_order_attention_notification_request_instance.to_dict()
# create an instance of TransportNotificationsOrderAttentionNotificationRequest from a dict
transport_notifications_order_attention_notification_request_from_dict = TransportNotificationsOrderAttentionNotificationRequest.from_dict(transport_notifications_order_attention_notification_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


