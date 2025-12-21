# ComboGroupItemSizeDto3


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**combo_size_id** | **UUID** | The size ID of the combo that is mapped to the size from the sizeId field | 
**size_id** | **UUID** | The size ID of the item | [optional] 
**name** | **str** | The size name of the item | [optional] [default to '']
**short_name** | **str** | The size short name of the item | [optional] [default to '']
**prices** | [**List[ExternalMenuPriceByDepartmentsDto7]**](ExternalMenuPriceByDepartmentsDto7.md) |  | [optional] 

## Example

```python
from iikocloud_client.models.combo_group_item_size_dto3 import ComboGroupItemSizeDto3

# TODO update the JSON string below
json = "{}"
# create an instance of ComboGroupItemSizeDto3 from a JSON string
combo_group_item_size_dto3_instance = ComboGroupItemSizeDto3.from_json(json)
# print the JSON string representation of the object
print(ComboGroupItemSizeDto3.to_json())

# convert the object into a dict
combo_group_item_size_dto3_dict = combo_group_item_size_dto3_instance.to_dict()
# create an instance of ComboGroupItemSizeDto3 from a dict
combo_group_item_size_dto3_from_dict = ComboGroupItemSizeDto3.from_dict(combo_group_item_size_dto3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


