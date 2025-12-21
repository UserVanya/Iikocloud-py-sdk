# ComboGroupItemDto3


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_id** | **str** |  | 
**forbidden_modifiers** | **List[object]** | Id of the item&#39;s modifier that is forbidden to sell | [optional] 
**size_id** | **str** |  | [optional] 
**price_modification_amount** | **float** |  | [optional] 
**sizes** | [**List[ComboGroupItemSizeDto3]**](ComboGroupItemSizeDto3.md) |  | [optional] 

## Example

```python
from iikocloud_client.models.combo_group_item_dto3 import ComboGroupItemDto3

# TODO update the JSON string below
json = "{}"
# create an instance of ComboGroupItemDto3 from a JSON string
combo_group_item_dto3_instance = ComboGroupItemDto3.from_json(json)
# print the JSON string representation of the object
print(ComboGroupItemDto3.to_json())

# convert the object into a dict
combo_group_item_dto3_dict = combo_group_item_dto3_instance.to_dict()
# create an instance of ComboGroupItemDto3 from a dict
combo_group_item_dto3_from_dict = ComboGroupItemDto3.from_dict(combo_group_item_dto3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


