# BarcodeDto5

Barcodes

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**barcode** | **str** |  | 
**container** | **str** |  | [optional] 

## Example

```python
from iikocloud_client.models.barcode_dto5 import BarcodeDto5

# TODO update the JSON string below
json = "{}"
# create an instance of BarcodeDto5 from a JSON string
barcode_dto5_instance = BarcodeDto5.from_json(json)
# print the JSON string representation of the object
print(BarcodeDto5.to_json())

# convert the object into a dict
barcode_dto5_dict = barcode_dto5_instance.to_dict()
# create an instance of BarcodeDto5 from a dict
barcode_dto5_from_dict = BarcodeDto5.from_dict(barcode_dto5_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


