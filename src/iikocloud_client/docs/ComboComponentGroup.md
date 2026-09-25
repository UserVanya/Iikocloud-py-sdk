# ComboComponentGroup

Combo meal component group (e.g. \"Burger\", \"Drink\", \"Fries\").  Stored inline with original UUIDs for compatibility with external systems.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Unique group ID (original UUID). | 
**is_main_group** | **bool** | Whether the group is the main one (primary combo product).  The main group usually determines the combo name. | [optional] 
**name** | **str** | Group name (e.g. \&quot;Drink\&quot;). | 
**products** | [**List[ComboComponentProduct]**](ComboComponentProduct.md) | List of products available for selection in this group.  Contains combo-specific prices (different from retail prices). | [optional] 
**skip_step** | **bool** | Skip selection step in UI (auto-select the only/default product).  Used for mandatory components without choice. | [optional] 

## Example

```python
from iikocloud_client.models.combo_component_group import ComboComponentGroup

# TODO update the JSON string below
json = "{}"
# create an instance of ComboComponentGroup from a JSON string
combo_component_group_instance = ComboComponentGroup.from_json(json)
# print the JSON string representation of the object
print(ComboComponentGroup.to_json())

# convert the object into a dict
combo_component_group_dict = combo_component_group_instance.to_dict()
# create an instance of ComboComponentGroup from a dict
combo_component_group_from_dict = ComboComponentGroup.from_dict(combo_component_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


