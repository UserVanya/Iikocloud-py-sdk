# ProductSizeResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default** | **bool** | Whether this size is the default for the scale | [optional] 
**id** | **UUID** | UUID of the size (null when creating a new size inside update) | [optional] 
**is_deleted** | **bool** | Whether this size is deleted | [optional] 
**name** | **str** | Name of the size | [optional] 
**priority** | **int** | Display priority (order) | [optional] 
**short_name** | **str** | Short name of the size. null is treated as empty string | [optional] 

## Example

```python
from iikocloud_client.models.product_size_response import ProductSizeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ProductSizeResponse from a JSON string
product_size_response_instance = ProductSizeResponse.from_json(json)
# print the JSON string representation of the object
print(ProductSizeResponse.to_json())

# convert the object into a dict
product_size_response_dict = product_size_response_instance.to_dict()
# create an instance of ProductSizeResponse from a dict
product_size_response_from_dict = ProductSizeResponse.from_dict(product_size_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


