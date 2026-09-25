# ModifierGroup

Modifier group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**child_modifiers_have_min_max_restrictions** | **bool** | Flag indicating whether child modifiers have min/max restrictions. | [optional] 
**id** | **str** | Modifier group ID. | [optional] 
**is_hidden** | **bool** | Flag indicating whether the group is hidden. | [optional] 
**items** | [**List[ModifierItem]**](ModifierItem.md) | List of modifiers in the group. | [optional] 
**name** | **str** | Modifier group name. | 
**restrictions** | [**Restrictions**](Restrictions.md) | Modifier selection restrictions. | [optional] 
**sku** | **str** | SKU. | [optional] 
**splittable** | **bool** | Flag indicating whether the group is splittable. | [optional] 

## Example

```python
from iikocloud_client.models.modifier_group import ModifierGroup

# TODO update the JSON string below
json = "{}"
# create an instance of ModifierGroup from a JSON string
modifier_group_instance = ModifierGroup.from_json(json)
# print the JSON string representation of the object
print(ModifierGroup.to_json())

# convert the object into a dict
modifier_group_dict = modifier_group_instance.to_dict()
# create an instance of ModifierGroup from a dict
modifier_group_from_dict = ModifierGroup.from_dict(modifier_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


