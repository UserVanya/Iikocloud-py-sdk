# NotificationSmsSendingPossibilityResponse

Sms sending possibility response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**NotificationNotificationSendingCapabilityCheckStatus**](NotificationNotificationSendingCapabilityCheckStatus.md) | Notification sending capability check status. | [optional] 
**available_sms_count** | **int** | Available sms count. | [optional] 

## Example

```python
from iikocloud_client.models.notification_sms_sending_possibility_response import NotificationSmsSendingPossibilityResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationSmsSendingPossibilityResponse from a JSON string
notification_sms_sending_possibility_response_instance = NotificationSmsSendingPossibilityResponse.from_json(json)
# print the JSON string representation of the object
print(NotificationSmsSendingPossibilityResponse.to_json())

# convert the object into a dict
notification_sms_sending_possibility_response_dict = notification_sms_sending_possibility_response_instance.to_dict()
# create an instance of NotificationSmsSendingPossibilityResponse from a dict
notification_sms_sending_possibility_response_from_dict = NotificationSmsSendingPossibilityResponse.from_dict(notification_sms_sending_possibility_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


