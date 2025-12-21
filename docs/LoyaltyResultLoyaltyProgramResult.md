# LoyaltyResultLoyaltyProgramResult

Loyalty result for order.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**marketing_campaign_id** | **UUID** | Program marketing campaign id. | [optional] 
**name** | **str** | Program name. | [optional] 
**discounts** | [**List[LoyaltyResultDiscountOperation]**](LoyaltyResultDiscountOperation.md) | Discount operations applied to order items. | [optional] 
**upsales** | [**List[LoyaltyResultUpsale]**](LoyaltyResultUpsale.md) | Suggested items to add or advices for customer. | [optional] 
**free_products** | [**List[LoyaltyResultFreeProductsGroup]**](LoyaltyResultFreeProductsGroup.md) | Program free products. | [optional] 
**available_combo_specifications** | **List[UUID]** | Ids of combo specification available in current order. | [optional] 
**available_combos** | [**List[LoyaltyResultAvailableCombo]**](LoyaltyResultAvailableCombo.md) | Partially added combos, available for assembly. | [optional] 
**need_to_activate_certificate** | **bool** | Certificate number is required for activation. | [optional] 

## Example

```python
from iikocloud_client.models.loyalty_result_loyalty_program_result import LoyaltyResultLoyaltyProgramResult

# TODO update the JSON string below
json = "{}"
# create an instance of LoyaltyResultLoyaltyProgramResult from a JSON string
loyalty_result_loyalty_program_result_instance = LoyaltyResultLoyaltyProgramResult.from_json(json)
# print the JSON string representation of the object
print(LoyaltyResultLoyaltyProgramResult.to_json())

# convert the object into a dict
loyalty_result_loyalty_program_result_dict = loyalty_result_loyalty_program_result_instance.to_dict()
# create an instance of LoyaltyResultLoyaltyProgramResult from a dict
loyalty_result_loyalty_program_result_from_dict = LoyaltyResultLoyaltyProgramResult.from_dict(loyalty_result_loyalty_program_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


