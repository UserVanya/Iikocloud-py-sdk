# IikoNetServiceContractsApiIikoTransportLoyaltyResultManualConditionInfo

Manual condition.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Id. | [optional] 
**caption** | **str** | Name of manual condition. | [optional] 
**is_dynamic_discount** | **bool** | Arbitrary discount attribute. | [optional] 
**is_applicable_on_cashier_screen** | **bool** | Flag of applicability on the cashier screen.. | [optional] 

## Example

```python
from iikocloud_client.models.iiko_net_service_contracts_api_iiko_transport_loyalty_result_manual_condition_info import IikoNetServiceContractsApiIikoTransportLoyaltyResultManualConditionInfo

# TODO update the JSON string below
json = "{}"
# create an instance of IikoNetServiceContractsApiIikoTransportLoyaltyResultManualConditionInfo from a JSON string
iiko_net_service_contracts_api_iiko_transport_loyalty_result_manual_condition_info_instance = IikoNetServiceContractsApiIikoTransportLoyaltyResultManualConditionInfo.from_json(json)
# print the JSON string representation of the object
print(IikoNetServiceContractsApiIikoTransportLoyaltyResultManualConditionInfo.to_json())

# convert the object into a dict
iiko_net_service_contracts_api_iiko_transport_loyalty_result_manual_condition_info_dict = iiko_net_service_contracts_api_iiko_transport_loyalty_result_manual_condition_info_instance.to_dict()
# create an instance of IikoNetServiceContractsApiIikoTransportLoyaltyResultManualConditionInfo from a dict
iiko_net_service_contracts_api_iiko_transport_loyalty_result_manual_condition_info_from_dict = IikoNetServiceContractsApiIikoTransportLoyaltyResultManualConditionInfo.from_dict(iiko_net_service_contracts_api_iiko_transport_loyalty_result_manual_condition_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


