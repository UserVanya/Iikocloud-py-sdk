# TransportNotificationsSendNotificationRequest

Request to notify external systems (iikoFront and iikoWeb).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message_type** | **str** |  | 
**organization_id** | **str** | Organization UOC Id. | 

## Example

```python
from iikocloud_client.models.transport_notifications_send_notification_request import TransportNotificationsSendNotificationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TransportNotificationsSendNotificationRequest from a JSON string
transport_notifications_send_notification_request_instance = TransportNotificationsSendNotificationRequest.from_json(json)
# print the JSON string representation of the object
print(TransportNotificationsSendNotificationRequest.to_json())

# convert the object into a dict
transport_notifications_send_notification_request_dict = transport_notifications_send_notification_request_instance.to_dict()
# create an instance of TransportNotificationsSendNotificationRequest from a dict
transport_notifications_send_notification_request_from_dict = TransportNotificationsSendNotificationRequest.from_dict(transport_notifications_send_notification_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


