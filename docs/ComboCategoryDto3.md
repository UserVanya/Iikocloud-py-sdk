# ComboCategoryDto3


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Category id(can be null) | 
**name** | **str** | Category name | [optional] 
**combos** | [**List[ComboDto3]**](ComboDto3.md) | Combos in category | [optional] 

## Example

```python
from iikocloud_client.models.combo_category_dto3 import ComboCategoryDto3

# TODO update the JSON string below
json = "{}"
# create an instance of ComboCategoryDto3 from a JSON string
combo_category_dto3_instance = ComboCategoryDto3.from_json(json)
# print the JSON string representation of the object
print(ComboCategoryDto3.to_json())

# convert the object into a dict
combo_category_dto3_dict = combo_category_dto3_instance.to_dict()
# create an instance of ComboCategoryDto3 from a dict
combo_category_dto3_from_dict = ComboCategoryDto3.from_dict(combo_category_dto3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


