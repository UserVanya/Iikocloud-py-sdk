# BarcodeItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**barcode** | **str** | Barcode value | [optional] 
**container_id** | **str** | Container ID represents a specific type of packaging or container for an item (e.g., a barrel, box, or bottle). Specify the container using its ID. Leave this field blank or pass null to automatically use the default container. | [optional] 
**type** | **str** | Barcode type | [optional] 

## Example

```python
from iikocloud_client.models.barcode_item import BarcodeItem

# TODO update the JSON string below
json = "{}"
# create an instance of BarcodeItem from a JSON string
barcode_item_instance = BarcodeItem.from_json(json)
# print the JSON string representation of the object
print(BarcodeItem.to_json())

# convert the object into a dict
barcode_item_dict = barcode_item_instance.to_dict()
# create an instance of BarcodeItem from a dict
barcode_item_from_dict = BarcodeItem.from_dict(barcode_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


