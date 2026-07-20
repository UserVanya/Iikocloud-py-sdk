# ExternalCourierAssignedNotificationRequest

Request to notify external systems (iikoFront and iikoWeb) about an external courier has been assigned for a delivery order.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**courier_car** | **str** | Courier car&#39;s model and number. | [optional] 
**courier_name** | **str** | Courier name. | [optional] 
**courier_phone** | **str** | Courier phone. | [optional] 
**order_id** | **UUID** | Order ID. | 
**order_source** | **str** | Order source. | 
**organization_id** | **UUID** | Organization UOC Id. | 

## Example

```python
from iikocloud_client.models.external_courier_assigned_notification_request import ExternalCourierAssignedNotificationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalCourierAssignedNotificationRequest from a JSON string
external_courier_assigned_notification_request_instance = ExternalCourierAssignedNotificationRequest.from_json(json)
# print the JSON string representation of the object
print(ExternalCourierAssignedNotificationRequest.to_json())

# convert the object into a dict
external_courier_assigned_notification_request_dict = external_courier_assigned_notification_request_instance.to_dict()
# create an instance of ExternalCourierAssignedNotificationRequest from a dict
external_courier_assigned_notification_request_from_dict = ExternalCourierAssignedNotificationRequest.from_dict(external_courier_assigned_notification_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


