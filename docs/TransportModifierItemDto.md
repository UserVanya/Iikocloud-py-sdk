# TransportModifierItemDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prices** | [**List[TransportPriceDto]**](TransportPriceDto.md) |  | [optional] 
**sku** | **str** | Modifier&#39;s code | [optional] 
**name** | **str** | Modifier&#39;s name | [optional] 
**description** | **str** | Modifier&#39;s description | [optional] 
**button_image** | **str** | Links to images | [optional] 
**restrictions** | [**ModifierRestrictionsDto**](ModifierRestrictionsDto.md) |  | [optional] 
**allergen_groups** | [**List[AllergenGroupDto]**](AllergenGroupDto.md) |  | [optional] 
**nutrition_per_hundred_grams** | **object** |  | [optional] 
**portion_weight_grams** | **float** | Modifier&#39;s weight in gramms | [optional] 
**tags** | [**List[TagDto]**](TagDto.md) |  | [optional] 
**item_id** | **str** | Modifier&#39;s Id | [optional] 

## Example

```python
from iiko_cloud_client.models.transport_modifier_item_dto import TransportModifierItemDto

# TODO update the JSON string below
json = "{}"
# create an instance of TransportModifierItemDto from a JSON string
transport_modifier_item_dto_instance = TransportModifierItemDto.from_json(json)
# print the JSON string representation of the object
print(TransportModifierItemDto.to_json())

# convert the object into a dict
transport_modifier_item_dto_dict = transport_modifier_item_dto_instance.to_dict()
# create an instance of TransportModifierItemDto from a dict
transport_modifier_item_dto_from_dict = TransportModifierItemDto.from_dict(transport_modifier_item_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


