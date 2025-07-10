# NetLoyaltyResultComboGroupMapping

Mapping combo's group to OrderItem.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_id** | **str** | Id of combo group. | [optional] 
**item_id** | **str** | Id of item, suitable for group. | [optional] 

## Example

```python
from iiko_cloud_client.models.net_loyalty_result_combo_group_mapping import NetLoyaltyResultComboGroupMapping

# TODO update the JSON string below
json = "{}"
# create an instance of NetLoyaltyResultComboGroupMapping from a JSON string
net_loyalty_result_combo_group_mapping_instance = NetLoyaltyResultComboGroupMapping.from_json(json)
# print the JSON string representation of the object
print(NetLoyaltyResultComboGroupMapping.to_json())

# convert the object into a dict
net_loyalty_result_combo_group_mapping_dict = net_loyalty_result_combo_group_mapping_instance.to_dict()
# create an instance of NetLoyaltyResultComboGroupMapping from a dict
net_loyalty_result_combo_group_mapping_from_dict = NetLoyaltyResultComboGroupMapping.from_dict(net_loyalty_result_combo_group_mapping_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


