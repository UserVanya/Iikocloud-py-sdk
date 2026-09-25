# SizePriceShort

Size price (short form).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**price** | **float** | Price. | [optional] 
**size_id** | **str** | Size ID. | [optional] 

## Example

```python
from iikocloud_client.models.size_price_short import SizePriceShort

# TODO update the JSON string below
json = "{}"
# create an instance of SizePriceShort from a JSON string
size_price_short_instance = SizePriceShort.from_json(json)
# print the JSON string representation of the object
print(SizePriceShort.to_json())

# convert the object into a dict
size_price_short_dict = size_price_short_instance.to_dict()
# create an instance of SizePriceShort from a dict
size_price_short_from_dict = SizePriceShort.from_dict(size_price_short_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


