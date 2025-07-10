# TransportWebHooksStopListUpdateWebHookEventInfo

WebHook notification about stop list update.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_type** | **str** | Event type. | [optional] 
**event_time** | **str** | Event date and time (UTC). | [optional] 
**organization_id** | **str** | Organization ID.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | [optional] 
**correlation_id** | **str** | Operation ID. | [optional] 
**event_info** | [**TransportStopListsWebHookOnStopListChangeData**](TransportStopListsWebHookOnStopListChangeData.md) | Event details. | [optional] 

## Example

```python
from iiko_cloud_client.models.transport_web_hooks_stop_list_update_web_hook_event_info import TransportWebHooksStopListUpdateWebHookEventInfo

# TODO update the JSON string below
json = "{}"
# create an instance of TransportWebHooksStopListUpdateWebHookEventInfo from a JSON string
transport_web_hooks_stop_list_update_web_hook_event_info_instance = TransportWebHooksStopListUpdateWebHookEventInfo.from_json(json)
# print the JSON string representation of the object
print(TransportWebHooksStopListUpdateWebHookEventInfo.to_json())

# convert the object into a dict
transport_web_hooks_stop_list_update_web_hook_event_info_dict = transport_web_hooks_stop_list_update_web_hook_event_info_instance.to_dict()
# create an instance of TransportWebHooksStopListUpdateWebHookEventInfo from a dict
transport_web_hooks_stop_list_update_web_hook_event_info_from_dict = TransportWebHooksStopListUpdateWebHookEventInfo.from_dict(transport_web_hooks_stop_list_update_web_hook_event_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


