# ComboGroupItemDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_id** | **str** |  | 
**forbidden_modifiers** | **List[object]** | Id of the item&#39;s modifier that is forbidden to sell | [optional] 
**size_id** | **str** |  | [optional] 
**price_modification_amount** | **float** |  | [optional] 
**sizes** | [**List[ComboGroupItemSizeDto]**](ComboGroupItemSizeDto.md) |  | [optional] 

## Example

```python
from iikocloud_client.models.combo_group_item_dto import ComboGroupItemDto

# TODO update the JSON string below
json = "{}"
# create an instance of ComboGroupItemDto from a JSON string
combo_group_item_dto_instance = ComboGroupItemDto.from_json(json)
# print the JSON string representation of the object
print(ComboGroupItemDto.to_json())

# convert the object into a dict
combo_group_item_dto_dict = combo_group_item_dto_instance.to_dict()
# create an instance of ComboGroupItemDto from a dict
combo_group_item_dto_from_dict = ComboGroupItemDto.from_dict(combo_group_item_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


