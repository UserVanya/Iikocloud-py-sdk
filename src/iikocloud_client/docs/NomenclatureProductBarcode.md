# NomenclatureProductBarcode


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**barcode** | **str** | Barcode value | 
**container_id** | **UUID** | Container ID represents a specific type of packaging or container for an item (e.g., a barrel, box, or bottle). Specify the container using its ID. Leave this field blank or pass null to automatically use the default container. | [optional] 
**type** | **str** | Barcode type | 

## Example

```python
from iikocloud_client.models.nomenclature_product_barcode import NomenclatureProductBarcode

# TODO update the JSON string below
json = "{}"
# create an instance of NomenclatureProductBarcode from a JSON string
nomenclature_product_barcode_instance = NomenclatureProductBarcode.from_json(json)
# print the JSON string representation of the object
print(NomenclatureProductBarcode.to_json())

# convert the object into a dict
nomenclature_product_barcode_dict = nomenclature_product_barcode_instance.to_dict()
# create an instance of NomenclatureProductBarcode from a dict
nomenclature_product_barcode_from_dict = NomenclatureProductBarcode.from_dict(nomenclature_product_barcode_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


