# StopListsResponse

Status of out-of-stock lists for a specified organization

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **UUID** | Operation ID. | 
**terminal_group_stop_lists** | [**List[RmsTerminalGroupStopListItemsResponse]**](RmsTerminalGroupStopListItemsResponse.md) | Set of out-of-stock lists | 

## Example

```python
from iikocloud_client.models.stop_lists_response import StopListsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of StopListsResponse from a JSON string
stop_lists_response_instance = StopListsResponse.from_json(json)
# print the JSON string representation of the object
print(StopListsResponse.to_json())

# convert the object into a dict
stop_lists_response_dict = stop_lists_response_instance.to_dict()
# create an instance of StopListsResponse from a dict
stop_lists_response_from_dict = StopListsResponse.from_dict(stop_lists_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


