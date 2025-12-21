# StopListsStopListsResponse

Status of out-of-stock lists for a specified organization

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **UUID** | Operation ID. | 
**terminal_group_stop_lists** | [**List[WrapperStopListsTerminalGroupStopList]**](WrapperStopListsTerminalGroupStopList.md) | Set of out-of-stock lists | 

## Example

```python
from iikocloud_client.models.stop_lists_stop_lists_response import StopListsStopListsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of StopListsStopListsResponse from a JSON string
stop_lists_stop_lists_response_instance = StopListsStopListsResponse.from_json(json)
# print the JSON string representation of the object
print(StopListsStopListsResponse.to_json())

# convert the object into a dict
stop_lists_stop_lists_response_dict = stop_lists_stop_lists_response_instance.to_dict()
# create an instance of StopListsStopListsResponse from a dict
stop_lists_stop_lists_response_from_dict = StopListsStopListsResponse.from_dict(stop_lists_stop_lists_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


