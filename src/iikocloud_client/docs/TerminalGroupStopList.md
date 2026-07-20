# TerminalGroupStopList

Out-of-stock list status for a group of front terminals.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[StopListItem]**](StopListItem.md) | Out-of-stock list. | 
**terminal_group_id** | **UUID** | Terminal ID. | [optional] 

## Example

```python
from iikocloud_client.models.terminal_group_stop_list import TerminalGroupStopList

# TODO update the JSON string below
json = "{}"
# create an instance of TerminalGroupStopList from a JSON string
terminal_group_stop_list_instance = TerminalGroupStopList.from_json(json)
# print the JSON string representation of the object
print(TerminalGroupStopList.to_json())

# convert the object into a dict
terminal_group_stop_list_dict = terminal_group_stop_list_instance.to_dict()
# create an instance of TerminalGroupStopList from a dict
terminal_group_stop_list_from_dict = TerminalGroupStopList.from_dict(terminal_group_stop_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


