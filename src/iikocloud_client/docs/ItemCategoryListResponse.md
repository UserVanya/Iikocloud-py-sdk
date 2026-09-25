# ItemCategoryListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[ItemCategory]**](ItemCategory.md) | List of fiscal categories | [optional] 
**limit** | **int** | Maximum number of records in the response. | [optional] 
**offset** | **int** | Number of records to skip from the beginning. | [optional] 
**total_count** | **int** | Total number of records matching the filters | [optional] 

## Example

```python
from iikocloud_client.models.item_category_list_response import ItemCategoryListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ItemCategoryListResponse from a JSON string
item_category_list_response_instance = ItemCategoryListResponse.from_json(json)
# print the JSON string representation of the object
print(ItemCategoryListResponse.to_json())

# convert the object into a dict
item_category_list_response_dict = item_category_list_response_instance.to_dict()
# create an instance of ItemCategoryListResponse from a dict
item_category_list_response_from_dict = ItemCategoryListResponse.from_dict(item_category_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


