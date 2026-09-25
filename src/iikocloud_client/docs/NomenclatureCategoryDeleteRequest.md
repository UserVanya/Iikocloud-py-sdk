# NomenclatureCategoryDeleteRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | UUID of the category to delete | [optional] 

## Example

```python
from iikocloud_client.models.nomenclature_category_delete_request import NomenclatureCategoryDeleteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of NomenclatureCategoryDeleteRequest from a JSON string
nomenclature_category_delete_request_instance = NomenclatureCategoryDeleteRequest.from_json(json)
# print the JSON string representation of the object
print(NomenclatureCategoryDeleteRequest.to_json())

# convert the object into a dict
nomenclature_category_delete_request_dict = nomenclature_category_delete_request_instance.to_dict()
# create an instance of NomenclatureCategoryDeleteRequest from a dict
nomenclature_category_delete_request_from_dict = NomenclatureCategoryDeleteRequest.from_dict(nomenclature_category_delete_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


