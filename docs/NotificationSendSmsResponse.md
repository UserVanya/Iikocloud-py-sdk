# NotificationSendSmsResponse

Send sms response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sms_id** | **str** | Sms id. | [optional] 

## Example

```python
from iikocloud_client.models.notification_send_sms_response import NotificationSendSmsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationSendSmsResponse from a JSON string
notification_send_sms_response_instance = NotificationSendSmsResponse.from_json(json)
# print the JSON string representation of the object
print(NotificationSendSmsResponse.to_json())

# convert the object into a dict
notification_send_sms_response_dict = notification_send_sms_response_instance.to_dict()
# create an instance of NotificationSendSmsResponse from a dict
notification_send_sms_response_from_dict = NotificationSendSmsResponse.from_dict(notification_send_sms_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


