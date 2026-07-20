# ComboGroupMapping

Mapping combo's group to OrderItem.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_id** | **UUID** | Id of combo group. | [optional] 
**item_id** | **UUID** | Id of item, suitable for group. | [optional] 

## Example

```python
from iikocloud_client.models.combo_group_mapping import ComboGroupMapping

# TODO update the JSON string below
json = "{}"
# create an instance of ComboGroupMapping from a JSON string
combo_group_mapping_instance = ComboGroupMapping.from_json(json)
# print the JSON string representation of the object
print(ComboGroupMapping.to_json())

# convert the object into a dict
combo_group_mapping_dict = combo_group_mapping_instance.to_dict()
# create an instance of ComboGroupMapping from a dict
combo_group_mapping_from_dict = ComboGroupMapping.from_dict(combo_group_mapping_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


