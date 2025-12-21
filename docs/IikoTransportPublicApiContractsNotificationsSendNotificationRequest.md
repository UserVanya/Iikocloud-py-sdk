# IikoTransportPublicApiContractsNotificationsSendNotificationRequest

Request to notify external systems (iikoFront and iikoWeb).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message_type** | **str** |  | 
**organization_id** | **UUID** | Organization UOC Id. | 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_notifications_send_notification_request import IikoTransportPublicApiContractsNotificationsSendNotificationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsNotificationsSendNotificationRequest from a JSON string
iiko_transport_public_api_contracts_notifications_send_notification_request_instance = IikoTransportPublicApiContractsNotificationsSendNotificationRequest.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsNotificationsSendNotificationRequest.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_notifications_send_notification_request_dict = iiko_transport_public_api_contracts_notifications_send_notification_request_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsNotificationsSendNotificationRequest from a dict
iiko_transport_public_api_contracts_notifications_send_notification_request_from_dict = IikoTransportPublicApiContractsNotificationsSendNotificationRequest.from_dict(iiko_transport_public_api_contracts_notifications_send_notification_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


