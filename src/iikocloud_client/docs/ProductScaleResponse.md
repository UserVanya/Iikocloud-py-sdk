# ProductScaleResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | UUID of the product size scale | [optional] 
**is_deleted** | **bool** | Whether the scale is deleted | [optional] 
**name** | **str** | Name of the product size scale | [optional] 
**product_sizes** | [**List[ProductSizeResponse]**](ProductSizeResponse.md) | List of sizes in this scale | [optional] 

## Example

```python
from iikocloud_client.models.product_scale_response import ProductScaleResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ProductScaleResponse from a JSON string
product_scale_response_instance = ProductScaleResponse.from_json(json)
# print the JSON string representation of the object
print(ProductScaleResponse.to_json())

# convert the object into a dict
product_scale_response_dict = product_scale_response_instance.to_dict()
# create an instance of ProductScaleResponse from a dict
product_scale_response_from_dict = ProductScaleResponse.from_dict(product_scale_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


