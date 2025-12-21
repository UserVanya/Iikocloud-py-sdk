# NotificationCheckSmsStatusRequest

Check sms status request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sms_ids** | **List[UUID]** | Sms IDs for checking. | 
**organization_id** | **UUID** | Organization id. | 

## Example

```python
from iikocloud_client.models.notification_check_sms_status_request import NotificationCheckSmsStatusRequest

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationCheckSmsStatusRequest from a JSON string
notification_check_sms_status_request_instance = NotificationCheckSmsStatusRequest.from_json(json)
# print the JSON string representation of the object
print(NotificationCheckSmsStatusRequest.to_json())

# convert the object into a dict
notification_check_sms_status_request_dict = notification_check_sms_status_request_instance.to_dict()
# create an instance of NotificationCheckSmsStatusRequest from a dict
notification_check_sms_status_request_from_dict = NotificationCheckSmsStatusRequest.from_dict(notification_check_sms_status_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


