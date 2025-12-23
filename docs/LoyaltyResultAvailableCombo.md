# LoyaltyResultAvailableCombo

Available combo.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**specification_id** | **str** | Id of combo specification, describing combo content. | [optional] 
**group_mapping** | [**List[LoyaltyResultComboGroupMapping]**](LoyaltyResultComboGroupMapping.md) | Groups contained in combo. If null - there is no suitable product in order yet for that group. | [optional] 

## Example

```python
from iikocloud_client.models.loyalty_result_available_combo import LoyaltyResultAvailableCombo

# TODO update the JSON string below
json = "{}"
# create an instance of LoyaltyResultAvailableCombo from a JSON string
loyalty_result_available_combo_instance = LoyaltyResultAvailableCombo.from_json(json)
# print the JSON string representation of the object
print(LoyaltyResultAvailableCombo.to_json())

# convert the object into a dict
loyalty_result_available_combo_dict = loyalty_result_available_combo_instance.to_dict()
# create an instance of LoyaltyResultAvailableCombo from a dict
loyalty_result_available_combo_from_dict = LoyaltyResultAvailableCombo.from_dict(loyalty_result_available_combo_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


