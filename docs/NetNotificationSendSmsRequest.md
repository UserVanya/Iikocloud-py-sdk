# NetNotificationSendSmsRequest

Send sms request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**phone** | **str** | Customer&#39;s phone number. Can be null. | 
**text** | **str** | Message text. Can be null. | 
**organization_id** | **str** | Organization id. | 

## Example

```python
from iiko_cloud_client.models.net_notification_send_sms_request import NetNotificationSendSmsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of NetNotificationSendSmsRequest from a JSON string
net_notification_send_sms_request_instance = NetNotificationSendSmsRequest.from_json(json)
# print the JSON string representation of the object
print(NetNotificationSendSmsRequest.to_json())

# convert the object into a dict
net_notification_send_sms_request_dict = net_notification_send_sms_request_instance.to_dict()
# create an instance of NetNotificationSendSmsRequest from a dict
net_notification_send_sms_request_from_dict = NetNotificationSendSmsRequest.from_dict(net_notification_send_sms_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


