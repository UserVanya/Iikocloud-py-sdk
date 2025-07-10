# TransportStopListsWebHookOnStopListChangeData

Out-of-stock list update info.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**terminal_groups_stop_lists_updates** | [**List[TransportStopListsTerminalGroupStopListUpdate]**](TransportStopListsTerminalGroupStopListUpdate.md) | Terminal groups with out-of-stock list updates. | 

## Example

```python
from iiko_cloud_client.models.transport_stop_lists_web_hook_on_stop_list_change_data import TransportStopListsWebHookOnStopListChangeData

# TODO update the JSON string below
json = "{}"
# create an instance of TransportStopListsWebHookOnStopListChangeData from a JSON string
transport_stop_lists_web_hook_on_stop_list_change_data_instance = TransportStopListsWebHookOnStopListChangeData.from_json(json)
# print the JSON string representation of the object
print(TransportStopListsWebHookOnStopListChangeData.to_json())

# convert the object into a dict
transport_stop_lists_web_hook_on_stop_list_change_data_dict = transport_stop_lists_web_hook_on_stop_list_change_data_instance.to_dict()
# create an instance of TransportStopListsWebHookOnStopListChangeData from a dict
transport_stop_lists_web_hook_on_stop_list_change_data_from_dict = TransportStopListsWebHookOnStopListChangeData.from_dict(transport_stop_lists_web_hook_on_stop_list_change_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


