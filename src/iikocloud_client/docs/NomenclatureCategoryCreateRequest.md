# NomenclatureCategoryCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the product category | [optional] 

## Example

```python
from iikocloud_client.models.nomenclature_category_create_request import NomenclatureCategoryCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of NomenclatureCategoryCreateRequest from a JSON string
nomenclature_category_create_request_instance = NomenclatureCategoryCreateRequest.from_json(json)
# print the JSON string representation of the object
print(NomenclatureCategoryCreateRequest.to_json())

# convert the object into a dict
nomenclature_category_create_request_dict = nomenclature_category_create_request_instance.to_dict()
# create an instance of NomenclatureCategoryCreateRequest from a dict
nomenclature_category_create_request_from_dict = NomenclatureCategoryCreateRequest.from_dict(nomenclature_category_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


