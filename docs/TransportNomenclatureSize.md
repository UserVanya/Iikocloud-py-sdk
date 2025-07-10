# TransportNomenclatureSize

Item size.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID. | [optional] 
**name** | **str** | Name. | [optional] 
**priority** | **int** | Priority (serial number) of the size in the size scale. | [optional] 
**is_default** | **bool** | Is the default size in the size scale. | [optional] 

## Example

```python
from iiko_cloud_client.models.transport_nomenclature_size import TransportNomenclatureSize

# TODO update the JSON string below
json = "{}"
# create an instance of TransportNomenclatureSize from a JSON string
transport_nomenclature_size_instance = TransportNomenclatureSize.from_json(json)
# print the JSON string representation of the object
print(TransportNomenclatureSize.to_json())

# convert the object into a dict
transport_nomenclature_size_dict = transport_nomenclature_size_instance.to_dict()
# create an instance of TransportNomenclatureSize from a dict
transport_nomenclature_size_from_dict = TransportNomenclatureSize.from_dict(transport_nomenclature_size_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


