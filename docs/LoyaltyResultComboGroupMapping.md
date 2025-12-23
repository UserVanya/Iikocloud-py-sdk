# LoyaltyResultComboGroupMapping

Mapping combo's group to OrderItem.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_id** | **str** | Id of combo group. | [optional] 
**item_id** | **str** | Id of item, suitable for group. | [optional] 

## Example

```python
from iikocloud_client.models.loyalty_result_combo_group_mapping import LoyaltyResultComboGroupMapping

# TODO update the JSON string below
json = "{}"
# create an instance of LoyaltyResultComboGroupMapping from a JSON string
loyalty_result_combo_group_mapping_instance = LoyaltyResultComboGroupMapping.from_json(json)
# print the JSON string representation of the object
print(LoyaltyResultComboGroupMapping.to_json())

# convert the object into a dict
loyalty_result_combo_group_mapping_dict = loyalty_result_combo_group_mapping_instance.to_dict()
# create an instance of LoyaltyResultComboGroupMapping from a dict
loyalty_result_combo_group_mapping_from_dict = LoyaltyResultComboGroupMapping.from_dict(loyalty_result_combo_group_mapping_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


