# IikoNetServiceContractsApiIikoTransportNotificationSmsSendingPossibilityResponse

Sms sending possibility response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**IikoNetServiceContractsApiIikoTransportNotificationNotificationSendingCapabilityCheckStatus**](IikoNetServiceContractsApiIikoTransportNotificationNotificationSendingCapabilityCheckStatus.md) | Notification sending capability check status. | [optional] 
**available_sms_count** | **int** | Available sms count. | [optional] 

## Example

```python
from iikocloud_client.models.iiko_net_service_contracts_api_iiko_transport_notification_sms_sending_possibility_response import IikoNetServiceContractsApiIikoTransportNotificationSmsSendingPossibilityResponse

# TODO update the JSON string below
json = "{}"
# create an instance of IikoNetServiceContractsApiIikoTransportNotificationSmsSendingPossibilityResponse from a JSON string
iiko_net_service_contracts_api_iiko_transport_notification_sms_sending_possibility_response_instance = IikoNetServiceContractsApiIikoTransportNotificationSmsSendingPossibilityResponse.from_json(json)
# print the JSON string representation of the object
print(IikoNetServiceContractsApiIikoTransportNotificationSmsSendingPossibilityResponse.to_json())

# convert the object into a dict
iiko_net_service_contracts_api_iiko_transport_notification_sms_sending_possibility_response_dict = iiko_net_service_contracts_api_iiko_transport_notification_sms_sending_possibility_response_instance.to_dict()
# create an instance of IikoNetServiceContractsApiIikoTransportNotificationSmsSendingPossibilityResponse from a dict
iiko_net_service_contracts_api_iiko_transport_notification_sms_sending_possibility_response_from_dict = IikoNetServiceContractsApiIikoTransportNotificationSmsSendingPossibilityResponse.from_dict(iiko_net_service_contracts_api_iiko_transport_notification_sms_sending_possibility_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


