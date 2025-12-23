# NotificationSmsSendingPossibilityRequest

Sms sending possibility request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **str** | Organization id. | 

## Example

```python
from iikocloud_client.models.notification_sms_sending_possibility_request import NotificationSmsSendingPossibilityRequest

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationSmsSendingPossibilityRequest from a JSON string
notification_sms_sending_possibility_request_instance = NotificationSmsSendingPossibilityRequest.from_json(json)
# print the JSON string representation of the object
print(NotificationSmsSendingPossibilityRequest.to_json())

# convert the object into a dict
notification_sms_sending_possibility_request_dict = notification_sms_sending_possibility_request_instance.to_dict()
# create an instance of NotificationSmsSendingPossibilityRequest from a dict
notification_sms_sending_possibility_request_from_dict = NotificationSmsSendingPossibilityRequest.from_dict(notification_sms_sending_possibility_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


