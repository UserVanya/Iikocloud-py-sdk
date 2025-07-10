# TransportStopListsTerminalGroupStopList

Out-of-stock list status for a group of front terminals.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**terminal_group_id** | **str** | Terminal ID. | [optional] 
**items** | [**List[TransportStopListsStopListItem]**](TransportStopListsStopListItem.md) | Out-of-stock list. | 

## Example

```python
from iiko_cloud_client.models.transport_stop_lists_terminal_group_stop_list import TransportStopListsTerminalGroupStopList

# TODO update the JSON string below
json = "{}"
# create an instance of TransportStopListsTerminalGroupStopList from a JSON string
transport_stop_lists_terminal_group_stop_list_instance = TransportStopListsTerminalGroupStopList.from_json(json)
# print the JSON string representation of the object
print(TransportStopListsTerminalGroupStopList.to_json())

# convert the object into a dict
transport_stop_lists_terminal_group_stop_list_dict = transport_stop_lists_terminal_group_stop_list_instance.to_dict()
# create an instance of TransportStopListsTerminalGroupStopList from a dict
transport_stop_lists_terminal_group_stop_list_from_dict = TransportStopListsTerminalGroupStopList.from_dict(transport_stop_lists_terminal_group_stop_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


