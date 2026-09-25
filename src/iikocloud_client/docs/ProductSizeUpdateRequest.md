# ProductSizeUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | UUID of the product size scale | [optional] 
**name** | **str** | Name of the product size scale | [optional] 
**product_sizes** | [**List[ProductSizeUpdateFields]**](ProductSizeUpdateFields.md) | List of sizes in this scale | [optional] 

## Example

```python
from iikocloud_client.models.product_size_update_request import ProductSizeUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ProductSizeUpdateRequest from a JSON string
product_size_update_request_instance = ProductSizeUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(ProductSizeUpdateRequest.to_json())

# convert the object into a dict
product_size_update_request_dict = product_size_update_request_instance.to_dict()
# create an instance of ProductSizeUpdateRequest from a dict
product_size_update_request_from_dict = ProductSizeUpdateRequest.from_dict(product_size_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


