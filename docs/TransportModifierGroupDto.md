# TransportModifierGroupDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[TransportModifierItemDto]**](TransportModifierItemDto.md) |  | [optional] 
**name** | **str** | Modifiers group name | [optional] 
**description** | **str** | Modifiers group description | [optional] 
**restrictions** | [**ModifierRestrictionsDto**](ModifierRestrictionsDto.md) |  | [optional] 
**can_be_divided** | **bool** | Whether the modifier can be splitted | [optional] 
**item_group_id** | **str** | Modifiers group id | [optional] 
**child_modifiers_have_min_max_restrictions** | **bool** | Whether child modifiers can have their own restrictions, or only group ones | [optional] 
**sku** | **str** | Modifiers group code | [optional] 

## Example

```python
from iikocloud_client.models.transport_modifier_group_dto import TransportModifierGroupDto

# TODO update the JSON string below
json = "{}"
# create an instance of TransportModifierGroupDto from a JSON string
transport_modifier_group_dto_instance = TransportModifierGroupDto.from_json(json)
# print the JSON string representation of the object
print(TransportModifierGroupDto.to_json())

# convert the object into a dict
transport_modifier_group_dto_dict = transport_modifier_group_dto_instance.to_dict()
# create an instance of TransportModifierGroupDto from a dict
transport_modifier_group_dto_from_dict = TransportModifierGroupDto.from_dict(transport_modifier_group_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


