# NetNotificationSendEmailRequest

Send email request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**receiver** | **str** | Email address. Can be null. | 
**subject** | **str** | Message subject. Can be null. | 
**body** | **str** | Message body. Can be null. | 
**organization_id** | **str** | Organization id. | 

## Example

```python
from iiko_cloud_client.models.net_notification_send_email_request import NetNotificationSendEmailRequest

# TODO update the JSON string below
json = "{}"
# create an instance of NetNotificationSendEmailRequest from a JSON string
net_notification_send_email_request_instance = NetNotificationSendEmailRequest.from_json(json)
# print the JSON string representation of the object
print(NetNotificationSendEmailRequest.to_json())

# convert the object into a dict
net_notification_send_email_request_dict = net_notification_send_email_request_instance.to_dict()
# create an instance of NetNotificationSendEmailRequest from a dict
net_notification_send_email_request_from_dict = NetNotificationSendEmailRequest.from_dict(net_notification_send_email_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


