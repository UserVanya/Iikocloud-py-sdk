# NetLoyaltyResultLoyaltyProgramResult

Loyalty result for order.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**marketing_campaign_id** | **str** | Program marketing campaign id. | [optional] 
**name** | **str** | Program name. | [optional] 
**discounts** | [**List[NetLoyaltyResultDiscountOperation]**](NetLoyaltyResultDiscountOperation.md) | Discount operations applied to order items. | [optional] 
**upsales** | [**List[NetLoyaltyResultUpsale]**](NetLoyaltyResultUpsale.md) | Suggested items to add or advices for customer. | [optional] 
**free_products** | [**List[NetLoyaltyResultFreeProductsGroup]**](NetLoyaltyResultFreeProductsGroup.md) | Program free products. | [optional] 
**available_combo_specifications** | **List[str]** | Ids of combo specification available in current order. | [optional] 
**available_combos** | [**List[NetLoyaltyResultAvailableCombo]**](NetLoyaltyResultAvailableCombo.md) | Partially added combos, available for assembly. | [optional] 
**need_to_activate_certificate** | **bool** | Certificate number is required for activation. | [optional] 

## Example

```python
from iikocloud_client.models.net_loyalty_result_loyalty_program_result import NetLoyaltyResultLoyaltyProgramResult

# TODO update the JSON string below
json = "{}"
# create an instance of NetLoyaltyResultLoyaltyProgramResult from a JSON string
net_loyalty_result_loyalty_program_result_instance = NetLoyaltyResultLoyaltyProgramResult.from_json(json)
# print the JSON string representation of the object
print(NetLoyaltyResultLoyaltyProgramResult.to_json())

# convert the object into a dict
net_loyalty_result_loyalty_program_result_dict = net_loyalty_result_loyalty_program_result_instance.to_dict()
# create an instance of NetLoyaltyResultLoyaltyProgramResult from a dict
net_loyalty_result_loyalty_program_result_from_dict = NetLoyaltyResultLoyaltyProgramResult.from_dict(net_loyalty_result_loyalty_program_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


