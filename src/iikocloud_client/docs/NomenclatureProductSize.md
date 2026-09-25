# NomenclatureProductSize


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | UUID of the directory entry | [optional] 
**is_deleted** | **bool** | Whether the directory entry is deleted | [optional] 
**name** | **str** | Name of the directory entry | [optional] 

## Example

```python
from iikocloud_client.models.nomenclature_product_size import NomenclatureProductSize

# TODO update the JSON string below
json = "{}"
# create an instance of NomenclatureProductSize from a JSON string
nomenclature_product_size_instance = NomenclatureProductSize.from_json(json)
# print the JSON string representation of the object
print(NomenclatureProductSize.to_json())

# convert the object into a dict
nomenclature_product_size_dict = nomenclature_product_size_instance.to_dict()
# create an instance of NomenclatureProductSize from a dict
nomenclature_product_size_from_dict = NomenclatureProductSize.from_dict(nomenclature_product_size_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


