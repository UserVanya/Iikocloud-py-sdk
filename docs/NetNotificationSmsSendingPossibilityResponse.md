# NetNotificationSmsSendingPossibilityResponse

Sms sending possibility response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**NetNotificationNotificationSendingCapabilityCheckStatus**](NetNotificationNotificationSendingCapabilityCheckStatus.md) | Notification sending capability check status. | [optional] 
**available_sms_count** | **int** | Available sms count. | [optional] 

## Example

```python
from iiko_cloud_client.models.net_notification_sms_sending_possibility_response import NetNotificationSmsSendingPossibilityResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NetNotificationSmsSendingPossibilityResponse from a JSON string
net_notification_sms_sending_possibility_response_instance = NetNotificationSmsSendingPossibilityResponse.from_json(json)
# print the JSON string representation of the object
print(NetNotificationSmsSendingPossibilityResponse.to_json())

# convert the object into a dict
net_notification_sms_sending_possibility_response_dict = net_notification_sms_sending_possibility_response_instance.to_dict()
# create an instance of NetNotificationSmsSendingPossibilityResponse from a dict
net_notification_sms_sending_possibility_response_from_dict = NetNotificationSmsSendingPossibilityResponse.from_dict(net_notification_sms_sending_possibility_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


