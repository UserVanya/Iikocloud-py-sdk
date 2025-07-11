# NetLoyaltyResultComboCategory

Information about combos of organization.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Category id. | [optional] 
**name** | **str** | Category name. | [optional] 

## Example

```python
from iikocloud_client.models.net_loyalty_result_combo_category import NetLoyaltyResultComboCategory

# TODO update the JSON string below
json = "{}"
# create an instance of NetLoyaltyResultComboCategory from a JSON string
net_loyalty_result_combo_category_instance = NetLoyaltyResultComboCategory.from_json(json)
# print the JSON string representation of the object
print(NetLoyaltyResultComboCategory.to_json())

# convert the object into a dict
net_loyalty_result_combo_category_dict = net_loyalty_result_combo_category_instance.to_dict()
# create an instance of NetLoyaltyResultComboCategory from a dict
net_loyalty_result_combo_category_from_dict = NetLoyaltyResultComboCategory.from_dict(net_loyalty_result_combo_category_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


