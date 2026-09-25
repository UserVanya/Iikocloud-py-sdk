# NomenclatureGroupCustomCategory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category_list_id** | **UUID** | UUID of the custom category list (CustomCategoryList) | [optional] 
**category_value_id** | **UUID** | UUID of the value from that list (CustomCategoryValue). Must belong to the specified categoryList | [optional] 

## Example

```python
from iikocloud_client.models.nomenclature_group_custom_category import NomenclatureGroupCustomCategory

# TODO update the JSON string below
json = "{}"
# create an instance of NomenclatureGroupCustomCategory from a JSON string
nomenclature_group_custom_category_instance = NomenclatureGroupCustomCategory.from_json(json)
# print the JSON string representation of the object
print(NomenclatureGroupCustomCategory.to_json())

# convert the object into a dict
nomenclature_group_custom_category_dict = nomenclature_group_custom_category_instance.to_dict()
# create an instance of NomenclatureGroupCustomCategory from a dict
nomenclature_group_custom_category_from_dict = NomenclatureGroupCustomCategory.from_dict(nomenclature_group_custom_category_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


