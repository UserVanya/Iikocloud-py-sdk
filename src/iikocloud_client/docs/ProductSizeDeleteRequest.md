# ProductSizeDeleteRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | UUID of the product size scale | [optional] 

## Example

```python
from iikocloud_client.models.product_size_delete_request import ProductSizeDeleteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ProductSizeDeleteRequest from a JSON string
product_size_delete_request_instance = ProductSizeDeleteRequest.from_json(json)
# print the JSON string representation of the object
print(ProductSizeDeleteRequest.to_json())

# convert the object into a dict
product_size_delete_request_dict = product_size_delete_request_instance.to_dict()
# create an instance of ProductSizeDeleteRequest from a dict
product_size_delete_request_from_dict = ProductSizeDeleteRequest.from_dict(product_size_delete_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


