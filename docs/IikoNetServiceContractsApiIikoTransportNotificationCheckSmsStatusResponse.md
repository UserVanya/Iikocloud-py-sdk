# IikoNetServiceContractsApiIikoTransportNotificationCheckSmsStatusResponse

Check sms status response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**statuses** | [**List[IikoNetServiceContractsApiIikoTransportNotificationSmsSendingStatusInfo]**](IikoNetServiceContractsApiIikoTransportNotificationSmsSendingStatusInfo.md) | Information about the status of sending SMS. | 

## Example

```python
from iikocloud_client.models.iiko_net_service_contracts_api_iiko_transport_notification_check_sms_status_response import IikoNetServiceContractsApiIikoTransportNotificationCheckSmsStatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of IikoNetServiceContractsApiIikoTransportNotificationCheckSmsStatusResponse from a JSON string
iiko_net_service_contracts_api_iiko_transport_notification_check_sms_status_response_instance = IikoNetServiceContractsApiIikoTransportNotificationCheckSmsStatusResponse.from_json(json)
# print the JSON string representation of the object
print(IikoNetServiceContractsApiIikoTransportNotificationCheckSmsStatusResponse.to_json())

# convert the object into a dict
iiko_net_service_contracts_api_iiko_transport_notification_check_sms_status_response_dict = iiko_net_service_contracts_api_iiko_transport_notification_check_sms_status_response_instance.to_dict()
# create an instance of IikoNetServiceContractsApiIikoTransportNotificationCheckSmsStatusResponse from a dict
iiko_net_service_contracts_api_iiko_transport_notification_check_sms_status_response_from_dict = IikoNetServiceContractsApiIikoTransportNotificationCheckSmsStatusResponse.from_dict(iiko_net_service_contracts_api_iiko_transport_notification_check_sms_status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


