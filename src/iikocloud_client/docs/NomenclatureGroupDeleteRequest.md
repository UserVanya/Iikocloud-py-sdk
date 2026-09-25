# NomenclatureGroupDeleteRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_ids** | **List[UUID]** | List of nomenclature group UUIDs for recursive deletion | 

## Example

```python
from iikocloud_client.models.nomenclature_group_delete_request import NomenclatureGroupDeleteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of NomenclatureGroupDeleteRequest from a JSON string
nomenclature_group_delete_request_instance = NomenclatureGroupDeleteRequest.from_json(json)
# print the JSON string representation of the object
print(NomenclatureGroupDeleteRequest.to_json())

# convert the object into a dict
nomenclature_group_delete_request_dict = nomenclature_group_delete_request_instance.to_dict()
# create an instance of NomenclatureGroupDeleteRequest from a dict
nomenclature_group_delete_request_from_dict = NomenclatureGroupDeleteRequest.from_dict(nomenclature_group_delete_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


