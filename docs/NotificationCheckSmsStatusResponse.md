# NotificationCheckSmsStatusResponse

Check sms status response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**statuses** | [**List[NotificationSmsSendingStatusInfo]**](NotificationSmsSendingStatusInfo.md) | Information about the status of sending SMS. | 

## Example

```python
from iikocloud_client.models.notification_check_sms_status_response import NotificationCheckSmsStatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationCheckSmsStatusResponse from a JSON string
notification_check_sms_status_response_instance = NotificationCheckSmsStatusResponse.from_json(json)
# print the JSON string representation of the object
print(NotificationCheckSmsStatusResponse.to_json())

# convert the object into a dict
notification_check_sms_status_response_dict = notification_check_sms_status_response_instance.to_dict()
# create an instance of NotificationCheckSmsStatusResponse from a dict
notification_check_sms_status_response_from_dict = NotificationCheckSmsStatusResponse.from_dict(notification_check_sms_status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


