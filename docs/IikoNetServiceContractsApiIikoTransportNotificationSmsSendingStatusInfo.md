# IikoNetServiceContractsApiIikoTransportNotificationSmsSendingStatusInfo

Sms sending status info.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sms_id** | **UUID** | Sms id. | 
**status** | [**IikoNetServiceContractsApiIikoTransportNotificationSmsSendingStatus**](IikoNetServiceContractsApiIikoTransportNotificationSmsSendingStatus.md) | Sms sending status. | 
**internal_error** | **str** | Sms sending internal error. Can be null. | [optional] 

## Example

```python
from iikocloud_client.models.iiko_net_service_contracts_api_iiko_transport_notification_sms_sending_status_info import IikoNetServiceContractsApiIikoTransportNotificationSmsSendingStatusInfo

# TODO update the JSON string below
json = "{}"
# create an instance of IikoNetServiceContractsApiIikoTransportNotificationSmsSendingStatusInfo from a JSON string
iiko_net_service_contracts_api_iiko_transport_notification_sms_sending_status_info_instance = IikoNetServiceContractsApiIikoTransportNotificationSmsSendingStatusInfo.from_json(json)
# print the JSON string representation of the object
print(IikoNetServiceContractsApiIikoTransportNotificationSmsSendingStatusInfo.to_json())

# convert the object into a dict
iiko_net_service_contracts_api_iiko_transport_notification_sms_sending_status_info_dict = iiko_net_service_contracts_api_iiko_transport_notification_sms_sending_status_info_instance.to_dict()
# create an instance of IikoNetServiceContractsApiIikoTransportNotificationSmsSendingStatusInfo from a dict
iiko_net_service_contracts_api_iiko_transport_notification_sms_sending_status_info_from_dict = IikoNetServiceContractsApiIikoTransportNotificationSmsSendingStatusInfo.from_dict(iiko_net_service_contracts_api_iiko_transport_notification_sms_sending_status_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


