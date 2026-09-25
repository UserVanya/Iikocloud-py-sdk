# NomenclatureGroupDeleteResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Message confirming successful deletion | [optional] 

## Example

```python
from iikocloud_client.models.nomenclature_group_delete_response import NomenclatureGroupDeleteResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NomenclatureGroupDeleteResponse from a JSON string
nomenclature_group_delete_response_instance = NomenclatureGroupDeleteResponse.from_json(json)
# print the JSON string representation of the object
print(NomenclatureGroupDeleteResponse.to_json())

# convert the object into a dict
nomenclature_group_delete_response_dict = nomenclature_group_delete_response_instance.to_dict()
# create an instance of NomenclatureGroupDeleteResponse from a dict
nomenclature_group_delete_response_from_dict = NomenclatureGroupDeleteResponse.from_dict(nomenclature_group_delete_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


