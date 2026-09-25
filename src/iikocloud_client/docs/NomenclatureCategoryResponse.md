# NomenclatureCategoryResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | UUID of the product category | [optional] 
**is_deleted** | **bool** | Whether the category is soft-deleted | [optional] 
**name** | **str** | Name of the product category | [optional] 

## Example

```python
from iikocloud_client.models.nomenclature_category_response import NomenclatureCategoryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NomenclatureCategoryResponse from a JSON string
nomenclature_category_response_instance = NomenclatureCategoryResponse.from_json(json)
# print the JSON string representation of the object
print(NomenclatureCategoryResponse.to_json())

# convert the object into a dict
nomenclature_category_response_dict = nomenclature_category_response_instance.to_dict()
# create an instance of NomenclatureCategoryResponse from a dict
nomenclature_category_response_from_dict = NomenclatureCategoryResponse.from_dict(nomenclature_category_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


