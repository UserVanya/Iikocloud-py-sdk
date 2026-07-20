# SizePrice

Price per item size.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**price** | [**Price**](Price.md) | Price per this item size. | 
**size_id** | **UUID** | Item size ID. | 

## Example

```python
from iikocloud_client.models.size_price import SizePrice

# TODO update the JSON string below
json = "{}"
# create an instance of SizePrice from a JSON string
size_price_instance = SizePrice.from_json(json)
# print the JSON string representation of the object
print(SizePrice.to_json())

# convert the object into a dict
size_price_dict = size_price_instance.to_dict()
# create an instance of SizePrice from a dict
size_price_from_dict = SizePrice.from_dict(size_price_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


