# NotificationSendEmailRequest

Send email request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**receiver** | **str** | Email address. Can be null. | 
**subject** | **str** | Message subject. Can be null. | 
**body** | **str** | Message body. Can be null. | 
**organization_id** | **UUID** | Organization id. | 

## Example

```python
from iikocloud_client.models.notification_send_email_request import NotificationSendEmailRequest

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationSendEmailRequest from a JSON string
notification_send_email_request_instance = NotificationSendEmailRequest.from_json(json)
# print the JSON string representation of the object
print(NotificationSendEmailRequest.to_json())

# convert the object into a dict
notification_send_email_request_dict = notification_send_email_request_instance.to_dict()
# create an instance of NotificationSendEmailRequest from a dict
notification_send_email_request_from_dict = NotificationSendEmailRequest.from_dict(notification_send_email_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


