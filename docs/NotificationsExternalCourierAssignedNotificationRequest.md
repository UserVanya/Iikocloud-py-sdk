# NotificationsExternalCourierAssignedNotificationRequest

Request to notify external systems (iikoFront and iikoWeb) about an external courier has been assigned for a delivery order.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_source** | **str** | Order source. | 
**order_id** | **UUID** | Order ID. | 
**courier_name** | **str** | Courier name. | [optional] 
**courier_car** | **str** | Courier car&#39;s model and number. | [optional] 
**courier_phone** | **str** | Courier phone. | [optional] 
**organization_id** | **UUID** | Organization UOC Id. | 

## Example

```python
from iikocloud_client.models.notifications_external_courier_assigned_notification_request import NotificationsExternalCourierAssignedNotificationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationsExternalCourierAssignedNotificationRequest from a JSON string
notifications_external_courier_assigned_notification_request_instance = NotificationsExternalCourierAssignedNotificationRequest.from_json(json)
# print the JSON string representation of the object
print(NotificationsExternalCourierAssignedNotificationRequest.to_json())

# convert the object into a dict
notifications_external_courier_assigned_notification_request_dict = notifications_external_courier_assigned_notification_request_instance.to_dict()
# create an instance of NotificationsExternalCourierAssignedNotificationRequest from a dict
notifications_external_courier_assigned_notification_request_from_dict = NotificationsExternalCourierAssignedNotificationRequest.from_dict(notifications_external_courier_assigned_notification_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


