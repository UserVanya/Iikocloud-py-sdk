# NomenclatureCategoryWriteResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | UUID of the category | [optional] 

## Example

```python
from iikocloud_client.models.nomenclature_category_write_response import NomenclatureCategoryWriteResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NomenclatureCategoryWriteResponse from a JSON string
nomenclature_category_write_response_instance = NomenclatureCategoryWriteResponse.from_json(json)
# print the JSON string representation of the object
print(NomenclatureCategoryWriteResponse.to_json())

# convert the object into a dict
nomenclature_category_write_response_dict = nomenclature_category_write_response_instance.to_dict()
# create an instance of NomenclatureCategoryWriteResponse from a dict
nomenclature_category_write_response_from_dict = NomenclatureCategoryWriteResponse.from_dict(nomenclature_category_write_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


