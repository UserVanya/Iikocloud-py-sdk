# SendNotificationRequest

Request to notify external systems (iikoFront and iikoWeb).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message_type** | **str** |  | 
**organization_id** | **UUID** | Organization UOC Id. | 

## Example

```python
from iikocloud_client.models.send_notification_request import SendNotificationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SendNotificationRequest from a JSON string
send_notification_request_instance = SendNotificationRequest.from_json(json)
# print the JSON string representation of the object
print(SendNotificationRequest.to_json())

# convert the object into a dict
send_notification_request_dict = send_notification_request_instance.to_dict()
# create an instance of SendNotificationRequest from a dict
send_notification_request_from_dict = SendNotificationRequest.from_dict(send_notification_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


