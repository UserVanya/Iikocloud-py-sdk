# BarcodeDto3

Barcodes

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**barcode** | **str** |  | 
**container** | **str** |  | [optional] 

## Example

```python
from iikocloud_client.models.barcode_dto3 import BarcodeDto3

# TODO update the JSON string below
json = "{}"
# create an instance of BarcodeDto3 from a JSON string
barcode_dto3_instance = BarcodeDto3.from_json(json)
# print the JSON string representation of the object
print(BarcodeDto3.to_json())

# convert the object into a dict
barcode_dto3_dict = barcode_dto3_instance.to_dict()
# create an instance of BarcodeDto3 from a dict
barcode_dto3_from_dict = BarcodeDto3.from_dict(barcode_dto3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


