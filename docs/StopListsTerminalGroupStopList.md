# StopListsTerminalGroupStopList

Out-of-stock list status for a group of front terminals.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**terminal_group_id** | **UUID** | Terminal ID. | [optional] 
**items** | [**List[StopListsStopListItem]**](StopListsStopListItem.md) | Out-of-stock list. | 

## Example

```python
from iikocloud_client.models.stop_lists_terminal_group_stop_list import StopListsTerminalGroupStopList

# TODO update the JSON string below
json = "{}"
# create an instance of StopListsTerminalGroupStopList from a JSON string
stop_lists_terminal_group_stop_list_instance = StopListsTerminalGroupStopList.from_json(json)
# print the JSON string representation of the object
print(StopListsTerminalGroupStopList.to_json())

# convert the object into a dict
stop_lists_terminal_group_stop_list_dict = stop_lists_terminal_group_stop_list_instance.to_dict()
# create an instance of StopListsTerminalGroupStopList from a dict
stop_lists_terminal_group_stop_list_from_dict = StopListsTerminalGroupStopList.from_dict(stop_lists_terminal_group_stop_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


