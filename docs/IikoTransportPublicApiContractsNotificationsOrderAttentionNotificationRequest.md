# IikoTransportPublicApiContractsNotificationsOrderAttentionNotificationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_source** | **str** | Order source. | 
**order_id** | **UUID** | Order ID. | 
**additional_info** | **str** | Additional info about the problem. | 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_notifications_order_attention_notification_request import IikoTransportPublicApiContractsNotificationsOrderAttentionNotificationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsNotificationsOrderAttentionNotificationRequest from a JSON string
iiko_transport_public_api_contracts_notifications_order_attention_notification_request_instance = IikoTransportPublicApiContractsNotificationsOrderAttentionNotificationRequest.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsNotificationsOrderAttentionNotificationRequest.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_notifications_order_attention_notification_request_dict = iiko_transport_public_api_contracts_notifications_order_attention_notification_request_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsNotificationsOrderAttentionNotificationRequest from a dict
iiko_transport_public_api_contracts_notifications_order_attention_notification_request_from_dict = IikoTransportPublicApiContractsNotificationsOrderAttentionNotificationRequest.from_dict(iiko_transport_public_api_contracts_notifications_order_attention_notification_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


