# NomenclatureSize

Item size.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | ID. | [optional] 
**name** | **str** | Name. | [optional] 
**priority** | **int** | Priority (serial number) of the size in the size scale. | [optional] 
**is_default** | **bool** | Is the default size in the size scale. | [optional] 

## Example

```python
from iikocloud_client.models.nomenclature_size import NomenclatureSize

# TODO update the JSON string below
json = "{}"
# create an instance of NomenclatureSize from a JSON string
nomenclature_size_instance = NomenclatureSize.from_json(json)
# print the JSON string representation of the object
print(NomenclatureSize.to_json())

# convert the object into a dict
nomenclature_size_dict = nomenclature_size_instance.to_dict()
# create an instance of NomenclatureSize from a dict
nomenclature_size_from_dict = NomenclatureSize.from_dict(nomenclature_size_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


