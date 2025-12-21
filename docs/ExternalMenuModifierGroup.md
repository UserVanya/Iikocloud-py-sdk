# ExternalMenuModifierGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Modifiers group name | [optional] [default to '']
**description** | **str** | Modifiers group description | [optional] [default to '']
**restrictions** | [**ModifierRestrictionsDto**](ModifierRestrictionsDto.md) |  | [optional] 
**items** | [**List[ExternalMenuModifierItem]**](ExternalMenuModifierItem.md) |  | [optional] 
**can_be_divided** | [**bool**](Bool.md) |  | [optional] 
**item_group_id** | **str** |  | [optional] 
**is_hidden** | **bool** |  | [optional] [default to False]
**child_modifiers_have_min_max_restrictions** | **bool** | Whether child modifiers can have their own restrictions, or only group ones | [optional] [default to False]
**sku** | **str** | Modifiers group code | [optional] [default to '']

## Example

```python
from iikocloud_client.models.external_menu_modifier_group import ExternalMenuModifierGroup

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalMenuModifierGroup from a JSON string
external_menu_modifier_group_instance = ExternalMenuModifierGroup.from_json(json)
# print the JSON string representation of the object
print(ExternalMenuModifierGroup.to_json())

# convert the object into a dict
external_menu_modifier_group_dict = external_menu_modifier_group_instance.to_dict()
# create an instance of ExternalMenuModifierGroup from a dict
external_menu_modifier_group_from_dict = ExternalMenuModifierGroup.from_dict(external_menu_modifier_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


