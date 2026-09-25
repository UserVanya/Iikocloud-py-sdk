# ListPositionsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[EmployeePositionDTO]**](EmployeePositionDTO.md) | List of employee positions | [optional] 
**limit** | **int** | Maximum number of records in the response | [optional] 
**offset** | **int** | Number of records to skip from the beginning (0-based) | [optional] 
**total_count** | **int** | Total number of records matching the filter | [optional] 

## Example

```python
from iikocloud_client.models.list_positions_response import ListPositionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListPositionsResponse from a JSON string
list_positions_response_instance = ListPositionsResponse.from_json(json)
# print the JSON string representation of the object
print(ListPositionsResponse.to_json())

# convert the object into a dict
list_positions_response_dict = list_positions_response_instance.to_dict()
# create an instance of ListPositionsResponse from a dict
list_positions_response_from_dict = ListPositionsResponse.from_dict(list_positions_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


