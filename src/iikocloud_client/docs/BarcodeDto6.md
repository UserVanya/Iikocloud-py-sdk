# BarcodeDto6

Barcodes

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**barcode** | **str** |  | 
**container** | **str** |  | [optional] 

## Example

```python
from iikocloud_client.models.barcode_dto6 import BarcodeDto6

# TODO update the JSON string below
json = "{}"
# create an instance of BarcodeDto6 from a JSON string
barcode_dto6_instance = BarcodeDto6.from_json(json)
# print the JSON string representation of the object
print(BarcodeDto6.to_json())

# convert the object into a dict
barcode_dto6_dict = barcode_dto6_instance.to_dict()
# create an instance of BarcodeDto6 from a dict
barcode_dto6_from_dict = BarcodeDto6.from_dict(barcode_dto6_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


