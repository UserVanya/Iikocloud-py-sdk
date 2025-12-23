# NotificationsSendNotificationRequest

Request to notify external systems (iikoFront and iikoWeb).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message_type** | **str** |  | 
**organization_id** | **str** | Organization UOC Id. | 

## Example

```python
from iikocloud_client.models.notifications_send_notification_request import NotificationsSendNotificationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationsSendNotificationRequest from a JSON string
notifications_send_notification_request_instance = NotificationsSendNotificationRequest.from_json(json)
# print the JSON string representation of the object
print(NotificationsSendNotificationRequest.to_json())

# convert the object into a dict
notifications_send_notification_request_dict = notifications_send_notification_request_instance.to_dict()
# create an instance of NotificationsSendNotificationRequest from a dict
notifications_send_notification_request_from_dict = NotificationsSendNotificationRequest.from_dict(notifications_send_notification_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


