# NetLoyaltyResultComboGroup

Information about combos group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Id. | [optional] 
**name** | **str** | Name. | [optional] 
**is_main_group** | **bool** | Is main group. | [optional] 
**products** | [**List[NetLoyaltyResultComboProduct]**](NetLoyaltyResultComboProduct.md) | Products. | [optional] 

## Example

```python
from iiko_cloud_client.models.net_loyalty_result_combo_group import NetLoyaltyResultComboGroup

# TODO update the JSON string below
json = "{}"
# create an instance of NetLoyaltyResultComboGroup from a JSON string
net_loyalty_result_combo_group_instance = NetLoyaltyResultComboGroup.from_json(json)
# print the JSON string representation of the object
print(NetLoyaltyResultComboGroup.to_json())

# convert the object into a dict
net_loyalty_result_combo_group_dict = net_loyalty_result_combo_group_instance.to_dict()
# create an instance of NetLoyaltyResultComboGroup from a dict
net_loyalty_result_combo_group_from_dict = NetLoyaltyResultComboGroup.from_dict(net_loyalty_result_combo_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


