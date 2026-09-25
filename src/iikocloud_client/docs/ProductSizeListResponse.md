# ProductSizeListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[NomenclatureProductSize]**](NomenclatureProductSize.md) | List of directory entries | [optional] 
**limit** | **int** | Maximum number of records in the response. Allowed values: 1 to 1000 | [optional] 
**offset** | **int** | Number of records to skip from the beginning of the list (0-based). Use together with limit for pagination | [optional] 
**total_count** | **int** | Total number of directory entries | [optional] 

## Example

```python
from iikocloud_client.models.product_size_list_response import ProductSizeListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ProductSizeListResponse from a JSON string
product_size_list_response_instance = ProductSizeListResponse.from_json(json)
# print the JSON string representation of the object
print(ProductSizeListResponse.to_json())

# convert the object into a dict
product_size_list_response_dict = product_size_list_response_instance.to_dict()
# create an instance of ProductSizeListResponse from a dict
product_size_list_response_from_dict = ProductSizeListResponse.from_dict(product_size_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


