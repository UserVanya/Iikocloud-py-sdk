# NetNotificationSmsSendingStatusInfo

Sms sending status info.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sms_id** | **str** | Sms id. | 
**status** | [**NetNotificationSmsSendingStatus**](NetNotificationSmsSendingStatus.md) | Sms sending status. | 
**internal_error** | **str** | Sms sending internal error. Can be null. | [optional] 

## Example

```python
from iikocloud_client.models.net_notification_sms_sending_status_info import NetNotificationSmsSendingStatusInfo

# TODO update the JSON string below
json = "{}"
# create an instance of NetNotificationSmsSendingStatusInfo from a JSON string
net_notification_sms_sending_status_info_instance = NetNotificationSmsSendingStatusInfo.from_json(json)
# print the JSON string representation of the object
print(NetNotificationSmsSendingStatusInfo.to_json())

# convert the object into a dict
net_notification_sms_sending_status_info_dict = net_notification_sms_sending_status_info_instance.to_dict()
# create an instance of NetNotificationSmsSendingStatusInfo from a dict
net_notification_sms_sending_status_info_from_dict = NetNotificationSmsSendingStatusInfo.from_dict(net_notification_sms_sending_status_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


