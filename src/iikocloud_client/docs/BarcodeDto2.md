# BarcodeDto2

Barcodes

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**barcode** | **str** |  | 
**container** | **str** |  | [optional] 

## Example

```python
from iikocloud_client.models.barcode_dto2 import BarcodeDto2

# TODO update the JSON string below
json = "{}"
# create an instance of BarcodeDto2 from a JSON string
barcode_dto2_instance = BarcodeDto2.from_json(json)
# print the JSON string representation of the object
print(BarcodeDto2.to_json())

# convert the object into a dict
barcode_dto2_dict = barcode_dto2_instance.to_dict()
# create an instance of BarcodeDto2 from a dict
barcode_dto2_from_dict = BarcodeDto2.from_dict(barcode_dto2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


