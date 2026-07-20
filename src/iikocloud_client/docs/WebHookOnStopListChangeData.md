# WebHookOnStopListChangeData

Out-of-stock list update info.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**terminal_groups_stop_lists_updates** | [**List[TerminalGroupStopListUpdate]**](TerminalGroupStopListUpdate.md) | Terminal groups with out-of-stock list updates. | 

## Example

```python
from iikocloud_client.models.web_hook_on_stop_list_change_data import WebHookOnStopListChangeData

# TODO update the JSON string below
json = "{}"
# create an instance of WebHookOnStopListChangeData from a JSON string
web_hook_on_stop_list_change_data_instance = WebHookOnStopListChangeData.from_json(json)
# print the JSON string representation of the object
print(WebHookOnStopListChangeData.to_json())

# convert the object into a dict
web_hook_on_stop_list_change_data_dict = web_hook_on_stop_list_change_data_instance.to_dict()
# create an instance of WebHookOnStopListChangeData from a dict
web_hook_on_stop_list_change_data_from_dict = WebHookOnStopListChangeData.from_dict(web_hook_on_stop_list_change_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


