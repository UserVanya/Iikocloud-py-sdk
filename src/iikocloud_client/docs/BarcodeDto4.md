# BarcodeDto4

Barcodes

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**barcode** | **str** |  | 
**container** | **str** |  | [optional] 

## Example

```python
from iikocloud_client.models.barcode_dto4 import BarcodeDto4

# TODO update the JSON string below
json = "{}"
# create an instance of BarcodeDto4 from a JSON string
barcode_dto4_instance = BarcodeDto4.from_json(json)
# print the JSON string representation of the object
print(BarcodeDto4.to_json())

# convert the object into a dict
barcode_dto4_dict = barcode_dto4_instance.to_dict()
# create an instance of BarcodeDto4 from a dict
barcode_dto4_from_dict = BarcodeDto4.from_dict(barcode_dto4_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


