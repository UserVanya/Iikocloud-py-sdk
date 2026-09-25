# NomenclatureGroupListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**groups** | [**List[NomenclatureGroupResponse]**](NomenclatureGroupResponse.md) | List of nomenclature groups | [optional] 

## Example

```python
from iikocloud_client.models.nomenclature_group_list_response import NomenclatureGroupListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NomenclatureGroupListResponse from a JSON string
nomenclature_group_list_response_instance = NomenclatureGroupListResponse.from_json(json)
# print the JSON string representation of the object
print(NomenclatureGroupListResponse.to_json())

# convert the object into a dict
nomenclature_group_list_response_dict = nomenclature_group_list_response_instance.to_dict()
# create an instance of NomenclatureGroupListResponse from a dict
nomenclature_group_list_response_from_dict = NomenclatureGroupListResponse.from_dict(nomenclature_group_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


