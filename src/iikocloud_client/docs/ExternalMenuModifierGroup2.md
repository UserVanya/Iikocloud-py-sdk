# ExternalMenuModifierGroup2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**child_modifiers_have_min_max_restrictions** | **bool** | Whether child modifiers can have their own restrictions, or only group ones | [optional] [default to False]
**description** | **str** | Modifiers group description | [optional] [default to '']
**id** | **str** |  | [optional] 
**is_hidden** | **bool** |  | [optional] [default to False]
**items** | [**List[ExternalMenuModifierItem2]**](ExternalMenuModifierItem2.md) |  | [optional] 
**name** | **str** | Modifiers group name | [optional] [default to '']
**restrictions** | [**ModifierRestrictionsDto2**](ModifierRestrictionsDto2.md) |  | [optional] 
**sku** | **str** | Modifiers group code | [optional] [default to '']
**splittable** | **bool** |  | 

## Example

```python
from iikocloud_client.models.external_menu_modifier_group2 import ExternalMenuModifierGroup2

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalMenuModifierGroup2 from a JSON string
external_menu_modifier_group2_instance = ExternalMenuModifierGroup2.from_json(json)
# print the JSON string representation of the object
print(ExternalMenuModifierGroup2.to_json())

# convert the object into a dict
external_menu_modifier_group2_dict = external_menu_modifier_group2_instance.to_dict()
# create an instance of ExternalMenuModifierGroup2 from a dict
external_menu_modifier_group2_from_dict = ExternalMenuModifierGroup2.from_dict(external_menu_modifier_group2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


