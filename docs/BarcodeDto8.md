# BarcodeDto8

Barcodes

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**barcode** | **str** |  | 
**container** | **str** |  | [optional] 

## Example

```python
from iikocloud_client.models.barcode_dto8 import BarcodeDto8

# TODO update the JSON string below
json = "{}"
# create an instance of BarcodeDto8 from a JSON string
barcode_dto8_instance = BarcodeDto8.from_json(json)
# print the JSON string representation of the object
print(BarcodeDto8.to_json())

# convert the object into a dict
barcode_dto8_dict = barcode_dto8_instance.to_dict()
# create an instance of BarcodeDto8 from a dict
barcode_dto8_from_dict = BarcodeDto8.from_dict(barcode_dto8_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


