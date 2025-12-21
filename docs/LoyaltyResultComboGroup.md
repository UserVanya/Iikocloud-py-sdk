# LoyaltyResultComboGroup

Information about combos group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Id. | [optional] 
**name** | **str** | Name. | [optional] 
**is_main_group** | **bool** | Is main group. | [optional] 
**products** | [**List[LoyaltyResultComboProduct]**](LoyaltyResultComboProduct.md) | Products. | [optional] 

## Example

```python
from iikocloud_client.models.loyalty_result_combo_group import LoyaltyResultComboGroup

# TODO update the JSON string below
json = "{}"
# create an instance of LoyaltyResultComboGroup from a JSON string
loyalty_result_combo_group_instance = LoyaltyResultComboGroup.from_json(json)
# print the JSON string representation of the object
print(LoyaltyResultComboGroup.to_json())

# convert the object into a dict
loyalty_result_combo_group_dict = loyalty_result_combo_group_instance.to_dict()
# create an instance of LoyaltyResultComboGroup from a dict
loyalty_result_combo_group_from_dict = LoyaltyResultComboGroup.from_dict(loyalty_result_combo_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


