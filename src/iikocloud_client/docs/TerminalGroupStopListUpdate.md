# TerminalGroupStopListUpdate

Out-of-stock list update for a group of front terminals.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Terminal ID. | 
**is_full** | **bool** | Whether out-of-stock list is fully updated. | 

## Example

```python
from iikocloud_client.models.terminal_group_stop_list_update import TerminalGroupStopListUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of TerminalGroupStopListUpdate from a JSON string
terminal_group_stop_list_update_instance = TerminalGroupStopListUpdate.from_json(json)
# print the JSON string representation of the object
print(TerminalGroupStopListUpdate.to_json())

# convert the object into a dict
terminal_group_stop_list_update_dict = terminal_group_stop_list_update_instance.to_dict()
# create an instance of TerminalGroupStopListUpdate from a dict
terminal_group_stop_list_update_from_dict = TerminalGroupStopListUpdate.from_dict(terminal_group_stop_list_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


