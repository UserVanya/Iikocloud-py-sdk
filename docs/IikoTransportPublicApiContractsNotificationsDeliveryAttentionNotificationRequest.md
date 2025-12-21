# IikoTransportPublicApiContractsNotificationsDeliveryAttentionNotificationRequest

Request to notify external systems (iikoFront and iikoWeb) about a delivery requiring attention.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_source** | **str** | Order source. | 
**order_id** | **UUID** | Order ID. | 
**additional_info** | **str** | Additional info about the problem. | 
**organization_id** | **UUID** | Organization UOC Id. | 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_notifications_delivery_attention_notification_request import IikoTransportPublicApiContractsNotificationsDeliveryAttentionNotificationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsNotificationsDeliveryAttentionNotificationRequest from a JSON string
iiko_transport_public_api_contracts_notifications_delivery_attention_notification_request_instance = IikoTransportPublicApiContractsNotificationsDeliveryAttentionNotificationRequest.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsNotificationsDeliveryAttentionNotificationRequest.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_notifications_delivery_attention_notification_request_dict = iiko_transport_public_api_contracts_notifications_delivery_attention_notification_request_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsNotificationsDeliveryAttentionNotificationRequest from a dict
iiko_transport_public_api_contracts_notifications_delivery_attention_notification_request_from_dict = IikoTransportPublicApiContractsNotificationsDeliveryAttentionNotificationRequest.from_dict(iiko_transport_public_api_contracts_notifications_delivery_attention_notification_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


