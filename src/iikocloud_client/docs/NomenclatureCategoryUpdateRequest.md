# NomenclatureCategoryUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | UUID of the category to update | [optional] 
**name** | **str** | Name of the product category | [optional] 

## Example

```python
from iikocloud_client.models.nomenclature_category_update_request import NomenclatureCategoryUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of NomenclatureCategoryUpdateRequest from a JSON string
nomenclature_category_update_request_instance = NomenclatureCategoryUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(NomenclatureCategoryUpdateRequest.to_json())

# convert the object into a dict
nomenclature_category_update_request_dict = nomenclature_category_update_request_instance.to_dict()
# create an instance of NomenclatureCategoryUpdateRequest from a dict
nomenclature_category_update_request_from_dict = NomenclatureCategoryUpdateRequest.from_dict(nomenclature_category_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


