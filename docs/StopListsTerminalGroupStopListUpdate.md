# StopListsTerminalGroupStopListUpdate

Out-of-stock list update for a group of front terminals.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Terminal ID. | 
**is_full** | **bool** | Whether out-of-stock list is fully updated. | 

## Example

```python
from iikocloud_client.models.stop_lists_terminal_group_stop_list_update import StopListsTerminalGroupStopListUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of StopListsTerminalGroupStopListUpdate from a JSON string
stop_lists_terminal_group_stop_list_update_instance = StopListsTerminalGroupStopListUpdate.from_json(json)
# print the JSON string representation of the object
print(StopListsTerminalGroupStopListUpdate.to_json())

# convert the object into a dict
stop_lists_terminal_group_stop_list_update_dict = stop_lists_terminal_group_stop_list_update_instance.to_dict()
# create an instance of StopListsTerminalGroupStopListUpdate from a dict
stop_lists_terminal_group_stop_list_update_from_dict = StopListsTerminalGroupStopListUpdate.from_dict(stop_lists_terminal_group_stop_list_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


