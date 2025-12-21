# IikoNetServiceContractsApiIikoTransportLoyaltyResultLoyaltyProgramResult

Loyalty result for order.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**marketing_campaign_id** | **UUID** | Program marketing campaign id. | [optional] 
**name** | **str** | Program name. | [optional] 
**discounts** | [**List[IikoNetServiceContractsApiIikoTransportLoyaltyResultDiscountOperation]**](IikoNetServiceContractsApiIikoTransportLoyaltyResultDiscountOperation.md) | Discount operations applied to order items. | [optional] 
**upsales** | [**List[IikoNetServiceContractsApiIikoTransportLoyaltyResultUpsale]**](IikoNetServiceContractsApiIikoTransportLoyaltyResultUpsale.md) | Suggested items to add or advices for customer. | [optional] 
**free_products** | [**List[IikoNetServiceContractsApiIikoTransportLoyaltyResultFreeProductsGroup]**](IikoNetServiceContractsApiIikoTransportLoyaltyResultFreeProductsGroup.md) | Program free products. | [optional] 
**available_combo_specifications** | **List[UUID]** | Ids of combo specification available in current order. | [optional] 
**available_combos** | [**List[IikoNetServiceContractsApiIikoTransportLoyaltyResultAvailableCombo]**](IikoNetServiceContractsApiIikoTransportLoyaltyResultAvailableCombo.md) | Partially added combos, available for assembly. | [optional] 
**need_to_activate_certificate** | **bool** | Certificate number is required for activation. | [optional] 

## Example

```python
from iikocloud_client.models.iiko_net_service_contracts_api_iiko_transport_loyalty_result_loyalty_program_result import IikoNetServiceContractsApiIikoTransportLoyaltyResultLoyaltyProgramResult

# TODO update the JSON string below
json = "{}"
# create an instance of IikoNetServiceContractsApiIikoTransportLoyaltyResultLoyaltyProgramResult from a JSON string
iiko_net_service_contracts_api_iiko_transport_loyalty_result_loyalty_program_result_instance = IikoNetServiceContractsApiIikoTransportLoyaltyResultLoyaltyProgramResult.from_json(json)
# print the JSON string representation of the object
print(IikoNetServiceContractsApiIikoTransportLoyaltyResultLoyaltyProgramResult.to_json())

# convert the object into a dict
iiko_net_service_contracts_api_iiko_transport_loyalty_result_loyalty_program_result_dict = iiko_net_service_contracts_api_iiko_transport_loyalty_result_loyalty_program_result_instance.to_dict()
# create an instance of IikoNetServiceContractsApiIikoTransportLoyaltyResultLoyaltyProgramResult from a dict
iiko_net_service_contracts_api_iiko_transport_loyalty_result_loyalty_program_result_from_dict = IikoNetServiceContractsApiIikoTransportLoyaltyResultLoyaltyProgramResult.from_dict(iiko_net_service_contracts_api_iiko_transport_loyalty_result_loyalty_program_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


