# ComboCategoryDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Category id(can be null) | 
**name** | **str** | Category name | [optional] 
**combos** | [**List[ComboDto]**](ComboDto.md) | Combos in category | [optional] 

## Example

```python
from iikocloud_client.models.combo_category_dto import ComboCategoryDto

# TODO update the JSON string below
json = "{}"
# create an instance of ComboCategoryDto from a JSON string
combo_category_dto_instance = ComboCategoryDto.from_json(json)
# print the JSON string representation of the object
print(ComboCategoryDto.to_json())

# convert the object into a dict
combo_category_dto_dict = combo_category_dto_instance.to_dict()
# create an instance of ComboCategoryDto from a dict
combo_category_dto_from_dict = ComboCategoryDto.from_dict(combo_category_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


