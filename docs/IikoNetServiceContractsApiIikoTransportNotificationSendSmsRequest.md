# IikoNetServiceContractsApiIikoTransportNotificationSendSmsRequest

Send sms request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**phone** | **str** | Customer&#39;s phone number. Can be null. | 
**text** | **str** | Message text. Can be null. | 
**organization_id** | **UUID** | Organization id. | 

## Example

```python
from iikocloud_client.models.iiko_net_service_contracts_api_iiko_transport_notification_send_sms_request import IikoNetServiceContractsApiIikoTransportNotificationSendSmsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IikoNetServiceContractsApiIikoTransportNotificationSendSmsRequest from a JSON string
iiko_net_service_contracts_api_iiko_transport_notification_send_sms_request_instance = IikoNetServiceContractsApiIikoTransportNotificationSendSmsRequest.from_json(json)
# print the JSON string representation of the object
print(IikoNetServiceContractsApiIikoTransportNotificationSendSmsRequest.to_json())

# convert the object into a dict
iiko_net_service_contracts_api_iiko_transport_notification_send_sms_request_dict = iiko_net_service_contracts_api_iiko_transport_notification_send_sms_request_instance.to_dict()
# create an instance of IikoNetServiceContractsApiIikoTransportNotificationSendSmsRequest from a dict
iiko_net_service_contracts_api_iiko_transport_notification_send_sms_request_from_dict = IikoNetServiceContractsApiIikoTransportNotificationSendSmsRequest.from_dict(iiko_net_service_contracts_api_iiko_transport_notification_send_sms_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


