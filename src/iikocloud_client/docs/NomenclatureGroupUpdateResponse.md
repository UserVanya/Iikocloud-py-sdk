# NomenclatureGroupUpdateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_id** | **UUID** | UUID of the updated group | [optional] 
**message** | **str** | Message confirming successful update | [optional] 

## Example

```python
from iikocloud_client.models.nomenclature_group_update_response import NomenclatureGroupUpdateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NomenclatureGroupUpdateResponse from a JSON string
nomenclature_group_update_response_instance = NomenclatureGroupUpdateResponse.from_json(json)
# print the JSON string representation of the object
print(NomenclatureGroupUpdateResponse.to_json())

# convert the object into a dict
nomenclature_group_update_response_dict = nomenclature_group_update_response_instance.to_dict()
# create an instance of NomenclatureGroupUpdateResponse from a dict
nomenclature_group_update_response_from_dict = NomenclatureGroupUpdateResponse.from_dict(nomenclature_group_update_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


