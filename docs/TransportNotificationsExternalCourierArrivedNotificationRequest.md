# TransportNotificationsExternalCourierArrivedNotificationRequest

Request to notify external systems (iikoFront and iikoWeb) about an external courier arrived to the restaurant to pickup an order.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_source** | **str** | Order source. | 
**order_id** | **str** | Order ID. | 
**courier_name** | **str** | Courier name. | [optional] 
**courier_car** | **str** | Courier car&#39;s model and number. | [optional] 
**courier_phone** | **str** | Courier phone. | [optional] 
**organization_id** | **str** | Organization UOC Id. | 

## Example

```python
from iikocloud_client.models.transport_notifications_external_courier_arrived_notification_request import TransportNotificationsExternalCourierArrivedNotificationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TransportNotificationsExternalCourierArrivedNotificationRequest from a JSON string
transport_notifications_external_courier_arrived_notification_request_instance = TransportNotificationsExternalCourierArrivedNotificationRequest.from_json(json)
# print the JSON string representation of the object
print(TransportNotificationsExternalCourierArrivedNotificationRequest.to_json())

# convert the object into a dict
transport_notifications_external_courier_arrived_notification_request_dict = transport_notifications_external_courier_arrived_notification_request_instance.to_dict()
# create an instance of TransportNotificationsExternalCourierArrivedNotificationRequest from a dict
transport_notifications_external_courier_arrived_notification_request_from_dict = TransportNotificationsExternalCourierArrivedNotificationRequest.from_dict(transport_notifications_external_courier_arrived_notification_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


