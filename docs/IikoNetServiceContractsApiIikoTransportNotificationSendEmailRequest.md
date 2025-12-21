# IikoNetServiceContractsApiIikoTransportNotificationSendEmailRequest

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
from iikocloud_client.models.iiko_net_service_contracts_api_iiko_transport_notification_send_email_request import IikoNetServiceContractsApiIikoTransportNotificationSendEmailRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IikoNetServiceContractsApiIikoTransportNotificationSendEmailRequest from a JSON string
iiko_net_service_contracts_api_iiko_transport_notification_send_email_request_instance = IikoNetServiceContractsApiIikoTransportNotificationSendEmailRequest.from_json(json)
# print the JSON string representation of the object
print(IikoNetServiceContractsApiIikoTransportNotificationSendEmailRequest.to_json())

# convert the object into a dict
iiko_net_service_contracts_api_iiko_transport_notification_send_email_request_dict = iiko_net_service_contracts_api_iiko_transport_notification_send_email_request_instance.to_dict()
# create an instance of IikoNetServiceContractsApiIikoTransportNotificationSendEmailRequest from a dict
iiko_net_service_contracts_api_iiko_transport_notification_send_email_request_from_dict = IikoNetServiceContractsApiIikoTransportNotificationSendEmailRequest.from_dict(iiko_net_service_contracts_api_iiko_transport_notification_send_email_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


