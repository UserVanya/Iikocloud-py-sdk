# IikoNetServiceContractsApiIikoTransportLoyaltyResultCalculateCheckinResponse

Loyalty result for order.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**loyalty_program_results** | [**List[IikoNetServiceContractsApiIikoTransportLoyaltyResultLoyaltyProgramResult]**](IikoNetServiceContractsApiIikoTransportLoyaltyResultLoyaltyProgramResult.md) | Loyalty program results. | [optional] 
**available_payments** | [**List[IikoNetServiceContractsApiIikoTransportLoyaltyResultAvailablePayment]**](IikoNetServiceContractsApiIikoTransportLoyaltyResultAvailablePayment.md) | Marketing campaigns with available payments. | [optional] 
**validation_warnings** | **List[str]** | Warnings about errors, not blocking loyalty calculation. | [optional] 
**warnings** | [**List[IikoNetServiceContractsApiIikoTransportLoyaltyResultWarningInfo]**](IikoNetServiceContractsApiIikoTransportLoyaltyResultWarningInfo.md) | Warnings about errors, not blocking loyalty calculation. | [optional] 
**loyalty_trace** | **str** | Loyalty trace. Can be null. | [optional] 

## Example

```python
from iikocloud_client.models.iiko_net_service_contracts_api_iiko_transport_loyalty_result_calculate_checkin_response import IikoNetServiceContractsApiIikoTransportLoyaltyResultCalculateCheckinResponse

# TODO update the JSON string below
json = "{}"
# create an instance of IikoNetServiceContractsApiIikoTransportLoyaltyResultCalculateCheckinResponse from a JSON string
iiko_net_service_contracts_api_iiko_transport_loyalty_result_calculate_checkin_response_instance = IikoNetServiceContractsApiIikoTransportLoyaltyResultCalculateCheckinResponse.from_json(json)
# print the JSON string representation of the object
print(IikoNetServiceContractsApiIikoTransportLoyaltyResultCalculateCheckinResponse.to_json())

# convert the object into a dict
iiko_net_service_contracts_api_iiko_transport_loyalty_result_calculate_checkin_response_dict = iiko_net_service_contracts_api_iiko_transport_loyalty_result_calculate_checkin_response_instance.to_dict()
# create an instance of IikoNetServiceContractsApiIikoTransportLoyaltyResultCalculateCheckinResponse from a dict
iiko_net_service_contracts_api_iiko_transport_loyalty_result_calculate_checkin_response_from_dict = IikoNetServiceContractsApiIikoTransportLoyaltyResultCalculateCheckinResponse.from_dict(iiko_net_service_contracts_api_iiko_transport_loyalty_result_calculate_checkin_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


