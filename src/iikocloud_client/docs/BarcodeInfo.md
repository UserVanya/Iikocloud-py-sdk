# BarcodeInfo

Barcode.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**barcode** | **str** | Barcode. | 
**container** | **str** | Container. | [optional] 
**product_fiscal_code** | **str** | Product fiscal code. | [optional] 

## Example

```python
from iikocloud_client.models.barcode_info import BarcodeInfo

# TODO update the JSON string below
json = "{}"
# create an instance of BarcodeInfo from a JSON string
barcode_info_instance = BarcodeInfo.from_json(json)
# print the JSON string representation of the object
print(BarcodeInfo.to_json())

# convert the object into a dict
barcode_info_dict = barcode_info_instance.to_dict()
# create an instance of BarcodeInfo from a dict
barcode_info_from_dict = BarcodeInfo.from_dict(barcode_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


