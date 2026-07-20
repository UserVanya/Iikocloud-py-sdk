# ProductSize

Item size.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | ID. | 
**name** | **str** | Name. | 

## Example

```python
from iikocloud_client.models.product_size import ProductSize

# TODO update the JSON string below
json = "{}"
# create an instance of ProductSize from a JSON string
product_size_instance = ProductSize.from_json(json)
# print the JSON string representation of the object
print(ProductSize.to_json())

# convert the object into a dict
product_size_dict = product_size_instance.to_dict()
# create an instance of ProductSize from a dict
product_size_from_dict = ProductSize.from_dict(product_size_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


