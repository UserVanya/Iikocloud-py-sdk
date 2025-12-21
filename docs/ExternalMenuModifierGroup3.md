# ExternalMenuModifierGroup3


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Modifiers group name | [optional] [default to '']
**description** | **str** | Modifiers group description | [optional] [default to '']
**restrictions** | [**ModifierRestrictionsDto3**](ModifierRestrictionsDto3.md) |  | [optional] 
**items** | [**List[ExternalMenuModifierItem3]**](ExternalMenuModifierItem3.md) |  | [optional] 
**is_hidden** | **bool** |  | [optional] [default to False]
**child_modifiers_have_min_max_restrictions** | **bool** | Whether child modifiers can have their own restrictions, or only group ones | [optional] [default to False]
**sku** | **str** | Modifiers group code | [optional] [default to '']
**splittable** | [**bool**](Bool.md) |  | 
**id** | **str** |  | [optional] 

## Example

```python
from iikocloud_client.models.external_menu_modifier_group3 import ExternalMenuModifierGroup3

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalMenuModifierGroup3 from a JSON string
external_menu_modifier_group3_instance = ExternalMenuModifierGroup3.from_json(json)
# print the JSON string representation of the object
print(ExternalMenuModifierGroup3.to_json())

# convert the object into a dict
external_menu_modifier_group3_dict = external_menu_modifier_group3_instance.to_dict()
# create an instance of ExternalMenuModifierGroup3 from a dict
external_menu_modifier_group3_from_dict = ExternalMenuModifierGroup3.from_dict(external_menu_modifier_group3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


