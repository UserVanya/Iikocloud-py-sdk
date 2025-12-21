# NotificationSendSmsRequest

Send sms request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**phone** | **str** | Customer&#39;s phone number. Can be null. | 
**text** | **str** | Message text. Can be null. | 
**organization_id** | **UUID** | Organization id. | 

## Example

```python
from iikocloud_client.models.notification_send_sms_request import NotificationSendSmsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationSendSmsRequest from a JSON string
notification_send_sms_request_instance = NotificationSendSmsRequest.from_json(json)
# print the JSON string representation of the object
print(NotificationSendSmsRequest.to_json())

# convert the object into a dict
notification_send_sms_request_dict = notification_send_sms_request_instance.to_dict()
# create an instance of NotificationSendSmsRequest from a dict
notification_send_sms_request_from_dict = NotificationSendSmsRequest.from_dict(notification_send_sms_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


