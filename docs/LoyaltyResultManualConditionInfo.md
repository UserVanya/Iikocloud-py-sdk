# LoyaltyResultManualConditionInfo

Manual condition.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Id. | [optional] 
**caption** | **str** | Name of manual condition. | [optional] 
**is_dynamic_discount** | **bool** | Arbitrary discount attribute. | [optional] 
**is_applicable_on_cashier_screen** | **bool** | Flag of applicability on the cashier screen.. | [optional] 

## Example

```python
from iikocloud_client.models.loyalty_result_manual_condition_info import LoyaltyResultManualConditionInfo

# TODO update the JSON string below
json = "{}"
# create an instance of LoyaltyResultManualConditionInfo from a JSON string
loyalty_result_manual_condition_info_instance = LoyaltyResultManualConditionInfo.from_json(json)
# print the JSON string representation of the object
print(LoyaltyResultManualConditionInfo.to_json())

# convert the object into a dict
loyalty_result_manual_condition_info_dict = loyalty_result_manual_condition_info_instance.to_dict()
# create an instance of LoyaltyResultManualConditionInfo from a dict
loyalty_result_manual_condition_info_from_dict = LoyaltyResultManualConditionInfo.from_dict(loyalty_result_manual_condition_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


