# NetNotificationSendSmsResponse

Send sms response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sms_id** | **str** | Sms id. | [optional] 

## Example

```python
from iikocloud_client.models.net_notification_send_sms_response import NetNotificationSendSmsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NetNotificationSendSmsResponse from a JSON string
net_notification_send_sms_response_instance = NetNotificationSendSmsResponse.from_json(json)
# print the JSON string representation of the object
print(NetNotificationSendSmsResponse.to_json())

# convert the object into a dict
net_notification_send_sms_response_dict = net_notification_send_sms_response_instance.to_dict()
# create an instance of NetNotificationSendSmsResponse from a dict
net_notification_send_sms_response_from_dict = NetNotificationSendSmsResponse.from_dict(net_notification_send_sms_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


