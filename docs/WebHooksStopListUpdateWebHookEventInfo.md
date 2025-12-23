# WebHooksStopListUpdateWebHookEventInfo

WebHook notification about stop list update.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_type** | [**ConstantStringStopListUpdate**](ConstantStringStopListUpdate.md) | Event type. | [optional] 
**event_time** | **str** | Event date and time (UTC). | [optional] 
**organization_id** | **str** | Organization ID.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | [optional] 
**correlation_id** | **str** | Operation ID. | [optional] 
**event_info** | [**StopListsWebHookOnStopListChangeData**](StopListsWebHookOnStopListChangeData.md) | Event details. | [optional] 

## Example

```python
from iikocloud_client.models.web_hooks_stop_list_update_web_hook_event_info import WebHooksStopListUpdateWebHookEventInfo

# TODO update the JSON string below
json = "{}"
# create an instance of WebHooksStopListUpdateWebHookEventInfo from a JSON string
web_hooks_stop_list_update_web_hook_event_info_instance = WebHooksStopListUpdateWebHookEventInfo.from_json(json)
# print the JSON string representation of the object
print(WebHooksStopListUpdateWebHookEventInfo.to_json())

# convert the object into a dict
web_hooks_stop_list_update_web_hook_event_info_dict = web_hooks_stop_list_update_web_hook_event_info_instance.to_dict()
# create an instance of WebHooksStopListUpdateWebHookEventInfo from a dict
web_hooks_stop_list_update_web_hook_event_info_from_dict = WebHooksStopListUpdateWebHookEventInfo.from_dict(web_hooks_stop_list_update_web_hook_event_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


