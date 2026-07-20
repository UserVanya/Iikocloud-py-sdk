# BarcodeDto

Barcodes

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**barcode** | **str** |  | 
**container** | **str** |  | [optional] 

## Example

```python
from iikocloud_client.models.barcode_dto import BarcodeDto

# TODO update the JSON string below
json = "{}"
# create an instance of BarcodeDto from a JSON string
barcode_dto_instance = BarcodeDto.from_json(json)
# print the JSON string representation of the object
print(BarcodeDto.to_json())

# convert the object into a dict
barcode_dto_dict = barcode_dto_instance.to_dict()
# create an instance of BarcodeDto from a dict
barcode_dto_from_dict = BarcodeDto.from_dict(barcode_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


