# TransportStopListsTerminalGroupStopListUpdate

Out-of-stock list update for a group of front terminals.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Terminal ID. | 
**is_full** | **bool** | Whether out-of-stock list is fully updated. | 

## Example

```python
from iikocloud_client.models.transport_stop_lists_terminal_group_stop_list_update import TransportStopListsTerminalGroupStopListUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of TransportStopListsTerminalGroupStopListUpdate from a JSON string
transport_stop_lists_terminal_group_stop_list_update_instance = TransportStopListsTerminalGroupStopListUpdate.from_json(json)
# print the JSON string representation of the object
print(TransportStopListsTerminalGroupStopListUpdate.to_json())

# convert the object into a dict
transport_stop_lists_terminal_group_stop_list_update_dict = transport_stop_lists_terminal_group_stop_list_update_instance.to_dict()
# create an instance of TransportStopListsTerminalGroupStopListUpdate from a dict
transport_stop_lists_terminal_group_stop_list_update_from_dict = TransportStopListsTerminalGroupStopListUpdate.from_dict(transport_stop_lists_terminal_group_stop_list_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


