# ContainerListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[Container]**](Container.md) | List of directory entries | [optional] 
**limit** | **int** | Maximum number of records in the response. Allowed values: 1 to 1000 | [optional] 
**offset** | **int** | Number of records to skip from the beginning of the list (0-based). Use together with limit for pagination | [optional] 
**total_count** | **int** | Total number of directory entries | [optional] 

## Example

```python
from iikocloud_client.models.container_list_response import ContainerListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ContainerListResponse from a JSON string
container_list_response_instance = ContainerListResponse.from_json(json)
# print the JSON string representation of the object
print(ContainerListResponse.to_json())

# convert the object into a dict
container_list_response_dict = container_list_response_instance.to_dict()
# create an instance of ContainerListResponse from a dict
container_list_response_from_dict = ContainerListResponse.from_dict(container_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


