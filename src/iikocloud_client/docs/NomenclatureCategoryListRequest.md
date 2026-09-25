# NomenclatureCategoryListRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **List[UUID]** | UUIDs of categories to filter by | [optional] 
**include_deleted** | **bool** | Include deleted categories in the response. Default false | [optional] 
**limit** | **int** | Maximum number of records in the response. limit &lt;&#x3D; 0 - no limit, all records are returned | [optional] 
**offset** | **int** | Number of records to skip from the beginning of the list (0-based). Use together with limit for pagination | [optional] 

## Example

```python
from iikocloud_client.models.nomenclature_category_list_request import NomenclatureCategoryListRequest

# TODO update the JSON string below
json = "{}"
# create an instance of NomenclatureCategoryListRequest from a JSON string
nomenclature_category_list_request_instance = NomenclatureCategoryListRequest.from_json(json)
# print the JSON string representation of the object
print(NomenclatureCategoryListRequest.to_json())

# convert the object into a dict
nomenclature_category_list_request_dict = nomenclature_category_list_request_instance.to_dict()
# create an instance of NomenclatureCategoryListRequest from a dict
nomenclature_category_list_request_from_dict = NomenclatureCategoryListRequest.from_dict(nomenclature_category_list_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


