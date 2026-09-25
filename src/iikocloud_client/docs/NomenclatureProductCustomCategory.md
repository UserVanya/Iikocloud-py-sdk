# NomenclatureProductCustomCategory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category_list_id** | **UUID** | UUID of the custom category list (CustomCategoryList). The list of values can be retrieved via the \&quot;Get a list of custom categories\&quot; method in the \&quot;Directories\&quot; category | [optional] 
**category_value_id** | **UUID** | UUID of the value from that list (CustomCategoryValue). Must belong to the specified categoryList. The list of values can be retrieved via the \&quot;Get a list of custom categories\&quot; method in the \&quot;Directories\&quot; category | [optional] 

## Example

```python
from iikocloud_client.models.nomenclature_product_custom_category import NomenclatureProductCustomCategory

# TODO update the JSON string below
json = "{}"
# create an instance of NomenclatureProductCustomCategory from a JSON string
nomenclature_product_custom_category_instance = NomenclatureProductCustomCategory.from_json(json)
# print the JSON string representation of the object
print(NomenclatureProductCustomCategory.to_json())

# convert the object into a dict
nomenclature_product_custom_category_dict = nomenclature_product_custom_category_instance.to_dict()
# create an instance of NomenclatureProductCustomCategory from a dict
nomenclature_product_custom_category_from_dict = NomenclatureProductCustomCategory.from_dict(nomenclature_product_custom_category_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


