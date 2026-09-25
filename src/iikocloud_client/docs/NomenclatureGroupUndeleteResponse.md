# NomenclatureGroupUndeleteResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Message confirming successful restoration | [optional] 

## Example

```python
from iikocloud_client.models.nomenclature_group_undelete_response import NomenclatureGroupUndeleteResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NomenclatureGroupUndeleteResponse from a JSON string
nomenclature_group_undelete_response_instance = NomenclatureGroupUndeleteResponse.from_json(json)
# print the JSON string representation of the object
print(NomenclatureGroupUndeleteResponse.to_json())

# convert the object into a dict
nomenclature_group_undelete_response_dict = nomenclature_group_undelete_response_instance.to_dict()
# create an instance of NomenclatureGroupUndeleteResponse from a dict
nomenclature_group_undelete_response_from_dict = NomenclatureGroupUndeleteResponse.from_dict(nomenclature_group_undelete_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


