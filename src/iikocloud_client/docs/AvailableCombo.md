# AvailableCombo

Available combo.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_mapping** | [**List[ComboGroupMapping]**](ComboGroupMapping.md) | Groups contained in combo. If null - there is no suitable product in order yet for that group. | [optional] 
**specification_id** | **UUID** | Id of combo specification, describing combo content. | [optional] 

## Example

```python
from iikocloud_client.models.available_combo import AvailableCombo

# TODO update the JSON string below
json = "{}"
# create an instance of AvailableCombo from a JSON string
available_combo_instance = AvailableCombo.from_json(json)
# print the JSON string representation of the object
print(AvailableCombo.to_json())

# convert the object into a dict
available_combo_dict = available_combo_instance.to_dict()
# create an instance of AvailableCombo from a dict
available_combo_from_dict = AvailableCombo.from_dict(available_combo_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


