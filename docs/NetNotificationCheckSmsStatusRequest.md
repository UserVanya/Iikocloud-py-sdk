# NetNotificationCheckSmsStatusRequest

Check sms status request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sms_ids** | **List[str]** | Sms IDs for checking. | 
**organization_id** | **str** | Organization id. | 

## Example

```python
from iiko_cloud_client.models.net_notification_check_sms_status_request import NetNotificationCheckSmsStatusRequest

# TODO update the JSON string below
json = "{}"
# create an instance of NetNotificationCheckSmsStatusRequest from a JSON string
net_notification_check_sms_status_request_instance = NetNotificationCheckSmsStatusRequest.from_json(json)
# print the JSON string representation of the object
print(NetNotificationCheckSmsStatusRequest.to_json())

# convert the object into a dict
net_notification_check_sms_status_request_dict = net_notification_check_sms_status_request_instance.to_dict()
# create an instance of NetNotificationCheckSmsStatusRequest from a dict
net_notification_check_sms_status_request_from_dict = NetNotificationCheckSmsStatusRequest.from_dict(net_notification_check_sms_status_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


