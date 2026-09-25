# ConceptionListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entities** | [**List[InventoryConception]**](InventoryConception.md) | List of entities | [optional] 
**limit** | **int** | Limit value from the request | [optional] 
**offset** | **int** | Offset value from the request | [optional] 
**total_count** | **int** | Total number of records matching the filter | [optional] 

## Example

```python
from iikocloud_client.models.conception_list_response import ConceptionListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ConceptionListResponse from a JSON string
conception_list_response_instance = ConceptionListResponse.from_json(json)
# print the JSON string representation of the object
print(ConceptionListResponse.to_json())

# convert the object into a dict
conception_list_response_dict = conception_list_response_instance.to_dict()
# create an instance of ConceptionListResponse from a dict
conception_list_response_from_dict = ConceptionListResponse.from_dict(conception_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


