# FreeProductSize

Free item size info.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Id of size. | [optional] 
**name** | **str** | Name. Can be null. | [optional] 

## Example

```python
from iikocloud_client.models.free_product_size import FreeProductSize

# TODO update the JSON string below
json = "{}"
# create an instance of FreeProductSize from a JSON string
free_product_size_instance = FreeProductSize.from_json(json)
# print the JSON string representation of the object
print(FreeProductSize.to_json())

# convert the object into a dict
free_product_size_dict = free_product_size_instance.to_dict()
# create an instance of FreeProductSize from a dict
free_product_size_from_dict = FreeProductSize.from_dict(free_product_size_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


