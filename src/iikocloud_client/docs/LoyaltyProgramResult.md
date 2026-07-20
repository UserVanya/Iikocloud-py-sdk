# LoyaltyProgramResult

Loyalty result for order.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available_combo_specifications** | **List[UUID]** | Ids of combo specification available in current order. | [optional] 
**available_combos** | [**List[AvailableCombo]**](AvailableCombo.md) | Partially added combos, available for assembly. | [optional] 
**discounts** | [**List[DiscountOperation]**](DiscountOperation.md) | Discount operations applied to order items. | [optional] 
**free_products** | [**List[FreeProductsGroup]**](FreeProductsGroup.md) | Program free products. | [optional] 
**marketing_campaign_id** | **UUID** | Program marketing campaign id. | [optional] 
**name** | **str** | Program name. | [optional] 
**need_to_activate_certificate** | **bool** | Certificate number is required for activation. | [optional] 
**upsales** | [**List[Upsale]**](Upsale.md) | Suggested items to add or advices for customer. | [optional] 

## Example

```python
from iikocloud_client.models.loyalty_program_result import LoyaltyProgramResult

# TODO update the JSON string below
json = "{}"
# create an instance of LoyaltyProgramResult from a JSON string
loyalty_program_result_instance = LoyaltyProgramResult.from_json(json)
# print the JSON string representation of the object
print(LoyaltyProgramResult.to_json())

# convert the object into a dict
loyalty_program_result_dict = loyalty_program_result_instance.to_dict()
# create an instance of LoyaltyProgramResult from a dict
loyalty_program_result_from_dict = LoyaltyProgramResult.from_dict(loyalty_program_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


