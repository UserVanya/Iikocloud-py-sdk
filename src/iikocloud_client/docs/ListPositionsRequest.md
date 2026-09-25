# ListPositionsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filters** | [**List[EmployeePositionFilterItem]**](EmployeePositionFilterItem.md) | List of filters (fields: isDeleted, scheduleTypes) | [optional] 
**limit** | **int** | Maximum number of records in the response (default: 50, max: 1000) | [optional] 
**offset** | **int** | Number of records to skip from the beginning (0-based) | [optional] 
**revision_from** | **int** | Revision from which to return changed records (optional) | [optional] 

## Example

```python
from iikocloud_client.models.list_positions_request import ListPositionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ListPositionsRequest from a JSON string
list_positions_request_instance = ListPositionsRequest.from_json(json)
# print the JSON string representation of the object
print(ListPositionsRequest.to_json())

# convert the object into a dict
list_positions_request_dict = list_positions_request_instance.to_dict()
# create an instance of ListPositionsRequest from a dict
list_positions_request_from_dict = ListPositionsRequest.from_dict(list_positions_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


