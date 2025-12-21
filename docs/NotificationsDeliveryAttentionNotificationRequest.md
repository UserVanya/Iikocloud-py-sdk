# NotificationsDeliveryAttentionNotificationRequest

Request to notify external systems (iikoFront and iikoWeb) about a delivery requiring attention.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_source** | **str** | Order source. | 
**order_id** | **UUID** | Order ID. | 
**additional_info** | **str** | Additional info about the problem. | 
**organization_id** | **UUID** | Organization UOC Id. | 

## Example

```python
from iikocloud_client.models.notifications_delivery_attention_notification_request import NotificationsDeliveryAttentionNotificationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationsDeliveryAttentionNotificationRequest from a JSON string
notifications_delivery_attention_notification_request_instance = NotificationsDeliveryAttentionNotificationRequest.from_json(json)
# print the JSON string representation of the object
print(NotificationsDeliveryAttentionNotificationRequest.to_json())

# convert the object into a dict
notifications_delivery_attention_notification_request_dict = notifications_delivery_attention_notification_request_instance.to_dict()
# create an instance of NotificationsDeliveryAttentionNotificationRequest from a dict
notifications_delivery_attention_notification_request_from_dict = NotificationsDeliveryAttentionNotificationRequest.from_dict(notifications_delivery_attention_notification_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


