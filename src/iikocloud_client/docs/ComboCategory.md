# ComboCategory

Information about combos of organization.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Category id. | [optional] 
**name** | **str** | Category name. | [optional] 

## Example

```python
from iikocloud_client.models.combo_category import ComboCategory

# TODO update the JSON string below
json = "{}"
# create an instance of ComboCategory from a JSON string
combo_category_instance = ComboCategory.from_json(json)
# print the JSON string representation of the object
print(ComboCategory.to_json())

# convert the object into a dict
combo_category_dict = combo_category_instance.to_dict()
# create an instance of ComboCategory from a dict
combo_category_from_dict = ComboCategory.from_dict(combo_category_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


