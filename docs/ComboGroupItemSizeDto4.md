# ComboGroupItemSizeDto4


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**combo_size_id** | **str** | The size ID of the combo that is mapped to the size from the sizeId field | 
**size_id** | **str** | The size ID of the item | [optional] 
**name** | **str** | The size name of the item | [optional] [default to '']
**short_name** | **str** | The size short name of the item | [optional] [default to '']
**prices** | [**List[ExternalMenuPriceByDepartmentsDto8]**](ExternalMenuPriceByDepartmentsDto8.md) |  | [optional] 

## Example

```python
from iikocloud_client.models.combo_group_item_size_dto4 import ComboGroupItemSizeDto4

# TODO update the JSON string below
json = "{}"
# create an instance of ComboGroupItemSizeDto4 from a JSON string
combo_group_item_size_dto4_instance = ComboGroupItemSizeDto4.from_json(json)
# print the JSON string representation of the object
print(ComboGroupItemSizeDto4.to_json())

# convert the object into a dict
combo_group_item_size_dto4_dict = combo_group_item_size_dto4_instance.to_dict()
# create an instance of ComboGroupItemSizeDto4 from a dict
combo_group_item_size_dto4_from_dict = ComboGroupItemSizeDto4.from_dict(combo_group_item_size_dto4_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


