# ProductSizeCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the product size scale | [optional] 
**product_sizes** | [**List[ProductSizeCreateFields]**](ProductSizeCreateFields.md) | List of sizes in this scale | [optional] 

## Example

```python
from iikocloud_client.models.product_size_create_request import ProductSizeCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ProductSizeCreateRequest from a JSON string
product_size_create_request_instance = ProductSizeCreateRequest.from_json(json)
# print the JSON string representation of the object
print(ProductSizeCreateRequest.to_json())

# convert the object into a dict
product_size_create_request_dict = product_size_create_request_instance.to_dict()
# create an instance of ProductSizeCreateRequest from a dict
product_size_create_request_from_dict = ProductSizeCreateRequest.from_dict(product_size_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


