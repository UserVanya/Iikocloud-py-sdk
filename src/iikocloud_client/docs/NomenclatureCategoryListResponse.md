# NomenclatureCategoryListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[NomenclatureCategoryResponse]**](NomenclatureCategoryResponse.md) | List of product categories | [optional] 
**limit** | **int** | Maximum number of records in the response. limit &lt;&#x3D; 0 - no limit, all records are returned | [optional] 
**offset** | **int** | Number of records to skip from the beginning of the list (0-based). Use together with limit for pagination | [optional] 
**total_count** | **int** | Total number of product categories matching the request | [optional] 

## Example

```python
from iikocloud_client.models.nomenclature_category_list_response import NomenclatureCategoryListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NomenclatureCategoryListResponse from a JSON string
nomenclature_category_list_response_instance = NomenclatureCategoryListResponse.from_json(json)
# print the JSON string representation of the object
print(NomenclatureCategoryListResponse.to_json())

# convert the object into a dict
nomenclature_category_list_response_dict = nomenclature_category_list_response_instance.to_dict()
# create an instance of NomenclatureCategoryListResponse from a dict
nomenclature_category_list_response_from_dict = NomenclatureCategoryListResponse.from_dict(nomenclature_category_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


