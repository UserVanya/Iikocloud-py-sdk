# IikoNetServiceContractsApiIikoTransportLoyaltyResultGetCombosInfoResponse

Information about combos of organization.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**combo_specifications** | [**List[IikoNetServiceContractsApiIikoTransportLoyaltyResultComboSpecification]**](IikoNetServiceContractsApiIikoTransportLoyaltyResultComboSpecification.md) | Full combo&#39;s specifications. | [optional] 
**combo_categories** | [**List[IikoNetServiceContractsApiIikoTransportLoyaltyResultComboCategory]**](IikoNetServiceContractsApiIikoTransportLoyaltyResultComboCategory.md) | Combo&#39;s categories. | [optional] 
**warnings** | [**List[IikoNetServiceContractsApiIikoTransportLoyaltyResultWarningInfo]**](IikoNetServiceContractsApiIikoTransportLoyaltyResultWarningInfo.md) | Warnings about errors, not blocking loyalty calculation. | [optional] 

## Example

```python
from iikocloud_client.models.iiko_net_service_contracts_api_iiko_transport_loyalty_result_get_combos_info_response import IikoNetServiceContractsApiIikoTransportLoyaltyResultGetCombosInfoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of IikoNetServiceContractsApiIikoTransportLoyaltyResultGetCombosInfoResponse from a JSON string
iiko_net_service_contracts_api_iiko_transport_loyalty_result_get_combos_info_response_instance = IikoNetServiceContractsApiIikoTransportLoyaltyResultGetCombosInfoResponse.from_json(json)
# print the JSON string representation of the object
print(IikoNetServiceContractsApiIikoTransportLoyaltyResultGetCombosInfoResponse.to_json())

# convert the object into a dict
iiko_net_service_contracts_api_iiko_transport_loyalty_result_get_combos_info_response_dict = iiko_net_service_contracts_api_iiko_transport_loyalty_result_get_combos_info_response_instance.to_dict()
# create an instance of IikoNetServiceContractsApiIikoTransportLoyaltyResultGetCombosInfoResponse from a dict
iiko_net_service_contracts_api_iiko_transport_loyalty_result_get_combos_info_response_from_dict = IikoNetServiceContractsApiIikoTransportLoyaltyResultGetCombosInfoResponse.from_dict(iiko_net_service_contracts_api_iiko_transport_loyalty_result_get_combos_info_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


