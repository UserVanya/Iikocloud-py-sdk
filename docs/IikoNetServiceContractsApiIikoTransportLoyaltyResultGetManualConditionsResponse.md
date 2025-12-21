# IikoNetServiceContractsApiIikoTransportLoyaltyResultGetManualConditionsResponse

Get manual conditions response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**manual_conditions** | [**List[IikoNetServiceContractsApiIikoTransportLoyaltyResultManualConditionInfo]**](IikoNetServiceContractsApiIikoTransportLoyaltyResultManualConditionInfo.md) | Info about manual conditions. | [optional] 

## Example

```python
from iikocloud_client.models.iiko_net_service_contracts_api_iiko_transport_loyalty_result_get_manual_conditions_response import IikoNetServiceContractsApiIikoTransportLoyaltyResultGetManualConditionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of IikoNetServiceContractsApiIikoTransportLoyaltyResultGetManualConditionsResponse from a JSON string
iiko_net_service_contracts_api_iiko_transport_loyalty_result_get_manual_conditions_response_instance = IikoNetServiceContractsApiIikoTransportLoyaltyResultGetManualConditionsResponse.from_json(json)
# print the JSON string representation of the object
print(IikoNetServiceContractsApiIikoTransportLoyaltyResultGetManualConditionsResponse.to_json())

# convert the object into a dict
iiko_net_service_contracts_api_iiko_transport_loyalty_result_get_manual_conditions_response_dict = iiko_net_service_contracts_api_iiko_transport_loyalty_result_get_manual_conditions_response_instance.to_dict()
# create an instance of IikoNetServiceContractsApiIikoTransportLoyaltyResultGetManualConditionsResponse from a dict
iiko_net_service_contracts_api_iiko_transport_loyalty_result_get_manual_conditions_response_from_dict = IikoNetServiceContractsApiIikoTransportLoyaltyResultGetManualConditionsResponse.from_dict(iiko_net_service_contracts_api_iiko_transport_loyalty_result_get_manual_conditions_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


