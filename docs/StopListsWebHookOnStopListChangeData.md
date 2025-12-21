# StopListsWebHookOnStopListChangeData

Out-of-stock list update info.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**terminal_groups_stop_lists_updates** | [**List[StopListsTerminalGroupStopListUpdate]**](StopListsTerminalGroupStopListUpdate.md) | Terminal groups with out-of-stock list updates. | 

## Example

```python
from iikocloud_client.models.stop_lists_web_hook_on_stop_list_change_data import StopListsWebHookOnStopListChangeData

# TODO update the JSON string below
json = "{}"
# create an instance of StopListsWebHookOnStopListChangeData from a JSON string
stop_lists_web_hook_on_stop_list_change_data_instance = StopListsWebHookOnStopListChangeData.from_json(json)
# print the JSON string representation of the object
print(StopListsWebHookOnStopListChangeData.to_json())

# convert the object into a dict
stop_lists_web_hook_on_stop_list_change_data_dict = stop_lists_web_hook_on_stop_list_change_data_instance.to_dict()
# create an instance of StopListsWebHookOnStopListChangeData from a dict
stop_lists_web_hook_on_stop_list_change_data_from_dict = StopListsWebHookOnStopListChangeData.from_dict(stop_lists_web_hook_on_stop_list_change_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


