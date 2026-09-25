# ProductTagListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[ProductTag]**](ProductTag.md) | List of directory entries | [optional] 
**limit** | **int** | Maximum number of records in the response. Allowed values: 1 to 1000 | [optional] 
**offset** | **int** | Number of records to skip from the beginning of the list (0-based). Use together with limit for pagination | [optional] 
**total_count** | **int** | Total number of directory entries | [optional] 

## Example

```python
from iikocloud_client.models.product_tag_list_response import ProductTagListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ProductTagListResponse from a JSON string
product_tag_list_response_instance = ProductTagListResponse.from_json(json)
# print the JSON string representation of the object
print(ProductTagListResponse.to_json())

# convert the object into a dict
product_tag_list_response_dict = product_tag_list_response_instance.to_dict()
# create an instance of ProductTagListResponse from a dict
product_tag_list_response_from_dict = ProductTagListResponse.from_dict(product_tag_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


