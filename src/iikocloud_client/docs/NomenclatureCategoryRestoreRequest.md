# NomenclatureCategoryRestoreRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | UUID of the category to restore | [optional] 

## Example

```python
from iikocloud_client.models.nomenclature_category_restore_request import NomenclatureCategoryRestoreRequest

# TODO update the JSON string below
json = "{}"
# create an instance of NomenclatureCategoryRestoreRequest from a JSON string
nomenclature_category_restore_request_instance = NomenclatureCategoryRestoreRequest.from_json(json)
# print the JSON string representation of the object
print(NomenclatureCategoryRestoreRequest.to_json())

# convert the object into a dict
nomenclature_category_restore_request_dict = nomenclature_category_restore_request_instance.to_dict()
# create an instance of NomenclatureCategoryRestoreRequest from a dict
nomenclature_category_restore_request_from_dict = NomenclatureCategoryRestoreRequest.from_dict(nomenclature_category_restore_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


