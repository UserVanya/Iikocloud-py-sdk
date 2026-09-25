# NomenclatureGroupUndeleteRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_ids** | **List[UUID]** | List of nomenclature group UUIDs to restore | 
**recursively** | **bool** | true - recursively restore all child groups and their products; false - restore only the specified top-level groups | [optional] 

## Example

```python
from iikocloud_client.models.nomenclature_group_undelete_request import NomenclatureGroupUndeleteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of NomenclatureGroupUndeleteRequest from a JSON string
nomenclature_group_undelete_request_instance = NomenclatureGroupUndeleteRequest.from_json(json)
# print the JSON string representation of the object
print(NomenclatureGroupUndeleteRequest.to_json())

# convert the object into a dict
nomenclature_group_undelete_request_dict = nomenclature_group_undelete_request_instance.to_dict()
# create an instance of NomenclatureGroupUndeleteRequest from a dict
nomenclature_group_undelete_request_from_dict = NomenclatureGroupUndeleteRequest.from_dict(nomenclature_group_undelete_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


