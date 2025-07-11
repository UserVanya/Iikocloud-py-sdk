# TransportNotificationsDeliveryAttentionNotificationRequest

Request to notify external systems (iikoFront and iikoWeb) about a delivery requiring attention.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_source** | **str** | Order source. | 
**order_id** | **str** | Order ID. | 
**additional_info** | **str** | Additional info about the problem. | 
**organization_id** | **str** | Organization UOC Id. | 

## Example

```python
from iikocloud_client.models.transport_notifications_delivery_attention_notification_request import TransportNotificationsDeliveryAttentionNotificationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TransportNotificationsDeliveryAttentionNotificationRequest from a JSON string
transport_notifications_delivery_attention_notification_request_instance = TransportNotificationsDeliveryAttentionNotificationRequest.from_json(json)
# print the JSON string representation of the object
print(TransportNotificationsDeliveryAttentionNotificationRequest.to_json())

# convert the object into a dict
transport_notifications_delivery_attention_notification_request_dict = transport_notifications_delivery_attention_notification_request_instance.to_dict()
# create an instance of TransportNotificationsDeliveryAttentionNotificationRequest from a dict
transport_notifications_delivery_attention_notification_request_from_dict = TransportNotificationsDeliveryAttentionNotificationRequest.from_dict(transport_notifications_delivery_attention_notification_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


