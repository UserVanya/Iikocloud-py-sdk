# BarcodeDto7

Barcodes

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**barcode** | **str** |  | 
**container** | **str** |  | [optional] 

## Example

```python
from iikocloud_client.models.barcode_dto7 import BarcodeDto7

# TODO update the JSON string below
json = "{}"
# create an instance of BarcodeDto7 from a JSON string
barcode_dto7_instance = BarcodeDto7.from_json(json)
# print the JSON string representation of the object
print(BarcodeDto7.to_json())

# convert the object into a dict
barcode_dto7_dict = barcode_dto7_instance.to_dict()
# create an instance of BarcodeDto7 from a dict
barcode_dto7_from_dict = BarcodeDto7.from_dict(barcode_dto7_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


