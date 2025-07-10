# NetLoyaltyResultAvailableCombo

Available combo.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**specification_id** | **str** | Id of combo specification, describing combo content. | [optional] 
**group_mapping** | [**List[NetLoyaltyResultComboGroupMapping]**](NetLoyaltyResultComboGroupMapping.md) | Groups contained in combo. If null - there is no suitable product in order yet for that group. | [optional] 

## Example

```python
from iiko_cloud_client.models.net_loyalty_result_available_combo import NetLoyaltyResultAvailableCombo

# TODO update the JSON string below
json = "{}"
# create an instance of NetLoyaltyResultAvailableCombo from a JSON string
net_loyalty_result_available_combo_instance = NetLoyaltyResultAvailableCombo.from_json(json)
# print the JSON string representation of the object
print(NetLoyaltyResultAvailableCombo.to_json())

# convert the object into a dict
net_loyalty_result_available_combo_dict = net_loyalty_result_available_combo_instance.to_dict()
# create an instance of NetLoyaltyResultAvailableCombo from a dict
net_loyalty_result_available_combo_from_dict = NetLoyaltyResultAvailableCombo.from_dict(net_loyalty_result_available_combo_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


