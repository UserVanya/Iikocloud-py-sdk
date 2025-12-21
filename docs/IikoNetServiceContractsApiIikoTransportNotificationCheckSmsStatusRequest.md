# IikoNetServiceContractsApiIikoTransportNotificationCheckSmsStatusRequest

Check sms status request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sms_ids** | **List[UUID]** | Sms IDs for checking. | 
**organization_id** | **UUID** | Organization id. | 

## Example

```python
from iikocloud_client.models.iiko_net_service_contracts_api_iiko_transport_notification_check_sms_status_request import IikoNetServiceContractsApiIikoTransportNotificationCheckSmsStatusRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IikoNetServiceContractsApiIikoTransportNotificationCheckSmsStatusRequest from a JSON string
iiko_net_service_contracts_api_iiko_transport_notification_check_sms_status_request_instance = IikoNetServiceContractsApiIikoTransportNotificationCheckSmsStatusRequest.from_json(json)
# print the JSON string representation of the object
print(IikoNetServiceContractsApiIikoTransportNotificationCheckSmsStatusRequest.to_json())

# convert the object into a dict
iiko_net_service_contracts_api_iiko_transport_notification_check_sms_status_request_dict = iiko_net_service_contracts_api_iiko_transport_notification_check_sms_status_request_instance.to_dict()
# create an instance of IikoNetServiceContractsApiIikoTransportNotificationCheckSmsStatusRequest from a dict
iiko_net_service_contracts_api_iiko_transport_notification_check_sms_status_request_from_dict = IikoNetServiceContractsApiIikoTransportNotificationCheckSmsStatusRequest.from_dict(iiko_net_service_contracts_api_iiko_transport_notification_check_sms_status_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


