# NotificationSmsSendingStatusInfo

Sms sending status info.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sms_id** | **UUID** | Sms id. | 
**status** | [**NotificationSmsSendingStatus**](NotificationSmsSendingStatus.md) | Sms sending status. | 
**internal_error** | **str** | Sms sending internal error. Can be null. | [optional] 

## Example

```python
from iikocloud_client.models.notification_sms_sending_status_info import NotificationSmsSendingStatusInfo

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationSmsSendingStatusInfo from a JSON string
notification_sms_sending_status_info_instance = NotificationSmsSendingStatusInfo.from_json(json)
# print the JSON string representation of the object
print(NotificationSmsSendingStatusInfo.to_json())

# convert the object into a dict
notification_sms_sending_status_info_dict = notification_sms_sending_status_info_instance.to_dict()
# create an instance of NotificationSmsSendingStatusInfo from a dict
notification_sms_sending_status_info_from_dict = NotificationSmsSendingStatusInfo.from_dict(notification_sms_sending_status_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


