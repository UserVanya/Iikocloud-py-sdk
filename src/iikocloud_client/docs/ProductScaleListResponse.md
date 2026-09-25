# ProductScaleListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[ProductScaleResponse]**](ProductScaleResponse.md) | List of product size scales | [optional] 
**limit** | **int** | Maximum number of records in the response. limit &lt;&#x3D; 0 - no limit, all records are returned | [optional] 
**offset** | **int** | Number of records to skip from the beginning of the list (0-based). Use together with limit for pagination | [optional] 
**total_count** | **int** | Total number of product size scales | [optional] 

## Example

```python
from iikocloud_client.models.product_scale_list_response import ProductScaleListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ProductScaleListResponse from a JSON string
product_scale_list_response_instance = ProductScaleListResponse.from_json(json)
# print the JSON string representation of the object
print(ProductScaleListResponse.to_json())

# convert the object into a dict
product_scale_list_response_dict = product_scale_list_response_instance.to_dict()
# create an instance of ProductScaleListResponse from a dict
product_scale_list_response_from_dict = ProductScaleListResponse.from_dict(product_scale_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


