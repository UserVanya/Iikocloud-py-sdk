# ComboGroup

Information about combos group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Id. | [optional] 
**is_main_group** | **bool** | Is main group. | [optional] 
**name** | **str** | Name. | [optional] 
**products** | [**List[ComboProduct]**](ComboProduct.md) | Products. | [optional] 
**skip_step** | **bool** | Skip step. | [optional] 

## Example

```python
from iikocloud_client.models.combo_group import ComboGroup

# TODO update the JSON string below
json = "{}"
# create an instance of ComboGroup from a JSON string
combo_group_instance = ComboGroup.from_json(json)
# print the JSON string representation of the object
print(ComboGroup.to_json())

# convert the object into a dict
combo_group_dict = combo_group_instance.to_dict()
# create an instance of ComboGroup from a dict
combo_group_from_dict = ComboGroup.from_dict(combo_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


