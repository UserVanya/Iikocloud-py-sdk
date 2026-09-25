# NomenclatureGroupCreateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_id** | **UUID** | UUID of the created group | [optional] 
**message** | **str** | Message confirming successful creation | [optional] 

## Example

```python
from iikocloud_client.models.nomenclature_group_create_response import NomenclatureGroupCreateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NomenclatureGroupCreateResponse from a JSON string
nomenclature_group_create_response_instance = NomenclatureGroupCreateResponse.from_json(json)
# print the JSON string representation of the object
print(NomenclatureGroupCreateResponse.to_json())

# convert the object into a dict
nomenclature_group_create_response_dict = nomenclature_group_create_response_instance.to_dict()
# create an instance of NomenclatureGroupCreateResponse from a dict
nomenclature_group_create_response_from_dict = NomenclatureGroupCreateResponse.from_dict(nomenclature_group_create_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


