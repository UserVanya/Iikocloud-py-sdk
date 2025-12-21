# ComboGroupItemDto2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_id** | **str** |  | 
**forbidden_modifiers** | **List[object]** | Id of the item&#39;s modifier that is forbidden to sell | [optional] 
**size_id** | **str** |  | [optional] 
**price_modification_amount** | **float** |  | [optional] 
**sizes** | [**List[ComboGroupItemSizeDto2]**](ComboGroupItemSizeDto2.md) |  | [optional] 

## Example

```python
from iikocloud_client.models.combo_group_item_dto2 import ComboGroupItemDto2

# TODO update the JSON string below
json = "{}"
# create an instance of ComboGroupItemDto2 from a JSON string
combo_group_item_dto2_instance = ComboGroupItemDto2.from_json(json)
# print the JSON string representation of the object
print(ComboGroupItemDto2.to_json())

# convert the object into a dict
combo_group_item_dto2_dict = combo_group_item_dto2_instance.to_dict()
# create an instance of ComboGroupItemDto2 from a dict
combo_group_item_dto2_from_dict = ComboGroupItemDto2.from_dict(combo_group_item_dto2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


