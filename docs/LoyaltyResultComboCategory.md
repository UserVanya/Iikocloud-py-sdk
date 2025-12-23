# LoyaltyResultComboCategory

Information about combos of organization.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Category id. | [optional] 
**name** | **str** | Category name. | [optional] 

## Example

```python
from iikocloud_client.models.loyalty_result_combo_category import LoyaltyResultComboCategory

# TODO update the JSON string below
json = "{}"
# create an instance of LoyaltyResultComboCategory from a JSON string
loyalty_result_combo_category_instance = LoyaltyResultComboCategory.from_json(json)
# print the JSON string representation of the object
print(LoyaltyResultComboCategory.to_json())

# convert the object into a dict
loyalty_result_combo_category_dict = loyalty_result_combo_category_instance.to_dict()
# create an instance of LoyaltyResultComboCategory from a dict
loyalty_result_combo_category_from_dict = LoyaltyResultComboCategory.from_dict(loyalty_result_combo_category_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


