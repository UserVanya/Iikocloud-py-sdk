# NetNotificationCheckSmsStatusResponse

Check sms status response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**statuses** | [**List[NetNotificationSmsSendingStatusInfo]**](NetNotificationSmsSendingStatusInfo.md) | Information about the status of sending SMS. | 

## Example

```python
from iiko_cloud_client.models.net_notification_check_sms_status_response import NetNotificationCheckSmsStatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NetNotificationCheckSmsStatusResponse from a JSON string
net_notification_check_sms_status_response_instance = NetNotificationCheckSmsStatusResponse.from_json(json)
# print the JSON string representation of the object
print(NetNotificationCheckSmsStatusResponse.to_json())

# convert the object into a dict
net_notification_check_sms_status_response_dict = net_notification_check_sms_status_response_instance.to_dict()
# create an instance of NetNotificationCheckSmsStatusResponse from a dict
net_notification_check_sms_status_response_from_dict = NetNotificationCheckSmsStatusResponse.from_dict(net_notification_check_sms_status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


