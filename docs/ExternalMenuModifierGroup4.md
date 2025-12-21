# ExternalMenuModifierGroup4


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Modifiers group name | [optional] [default to '']
**description** | **str** | Modifiers group description | [optional] [default to '']
**restrictions** | [**ModifierRestrictionsDto4**](ModifierRestrictionsDto4.md) |  | [optional] 
**items** | [**List[ExternalMenuModifierItem4]**](ExternalMenuModifierItem4.md) |  | [optional] 
**is_hidden** | **bool** |  | [optional] [default to False]
**child_modifiers_have_min_max_restrictions** | **bool** | Whether child modifiers can have their own restrictions, or only group ones | [optional] [default to False]
**sku** | **str** | Modifiers group code | [optional] [default to '']
**splittable** | [**bool**](Bool.md) |  | 
**id** | **str** |  | [optional] 

## Example

```python
from iikocloud_client.models.external_menu_modifier_group4 import ExternalMenuModifierGroup4

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalMenuModifierGroup4 from a JSON string
external_menu_modifier_group4_instance = ExternalMenuModifierGroup4.from_json(json)
# print the JSON string representation of the object
print(ExternalMenuModifierGroup4.to_json())

# convert the object into a dict
external_menu_modifier_group4_dict = external_menu_modifier_group4_instance.to_dict()
# create an instance of ExternalMenuModifierGroup4 from a dict
external_menu_modifier_group4_from_dict = ExternalMenuModifierGroup4.from_dict(external_menu_modifier_group4_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


