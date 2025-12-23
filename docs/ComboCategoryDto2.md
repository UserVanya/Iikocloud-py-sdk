# ComboCategoryDto2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Category id(can be null) | 
**name** | **str** | Category name | [optional] 
**combos** | [**List[ComboDto2]**](ComboDto2.md) | Combos in category | [optional] 

## Example

```python
from iikocloud_client.models.combo_category_dto2 import ComboCategoryDto2

# TODO update the JSON string below
json = "{}"
# create an instance of ComboCategoryDto2 from a JSON string
combo_category_dto2_instance = ComboCategoryDto2.from_json(json)
# print the JSON string representation of the object
print(ComboCategoryDto2.to_json())

# convert the object into a dict
combo_category_dto2_dict = combo_category_dto2_instance.to_dict()
# create an instance of ComboCategoryDto2 from a dict
combo_category_dto2_from_dict = ComboCategoryDto2.from_dict(combo_category_dto2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


