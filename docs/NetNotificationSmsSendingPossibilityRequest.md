# NetNotificationSmsSendingPossibilityRequest

Sms sending possibility request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **str** | Organization id. | 

## Example

```python
from iiko_cloud_client.models.net_notification_sms_sending_possibility_request import NetNotificationSmsSendingPossibilityRequest

# TODO update the JSON string below
json = "{}"
# create an instance of NetNotificationSmsSendingPossibilityRequest from a JSON string
net_notification_sms_sending_possibility_request_instance = NetNotificationSmsSendingPossibilityRequest.from_json(json)
# print the JSON string representation of the object
print(NetNotificationSmsSendingPossibilityRequest.to_json())

# convert the object into a dict
net_notification_sms_sending_possibility_request_dict = net_notification_sms_sending_possibility_request_instance.to_dict()
# create an instance of NetNotificationSmsSendingPossibilityRequest from a dict
net_notification_sms_sending_possibility_request_from_dict = NetNotificationSmsSendingPossibilityRequest.from_dict(net_notification_sms_sending_possibility_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


