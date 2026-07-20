# StopListUpdateWebHookEventInfo

WebHook notification about stop list update.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **UUID** | Operation ID. | [optional] 
**event_info** | [**WebHookOnStopListChangeData**](WebHookOnStopListChangeData.md) | Event details. | [optional] 
**event_time** | **str** | Event date and time (UTC). | [optional] 
**event_type** | **str** | Event type. | [optional] 
**organization_id** | **UUID** | Organization ID.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | [optional] 

## Example

```python
from iikocloud_client.models.stop_list_update_web_hook_event_info import StopListUpdateWebHookEventInfo

# TODO update the JSON string below
json = "{}"
# create an instance of StopListUpdateWebHookEventInfo from a JSON string
stop_list_update_web_hook_event_info_instance = StopListUpdateWebHookEventInfo.from_json(json)
# print the JSON string representation of the object
print(StopListUpdateWebHookEventInfo.to_json())

# convert the object into a dict
stop_list_update_web_hook_event_info_dict = stop_list_update_web_hook_event_info_instance.to_dict()
# create an instance of StopListUpdateWebHookEventInfo from a dict
stop_list_update_web_hook_event_info_from_dict = StopListUpdateWebHookEventInfo.from_dict(stop_list_update_web_hook_event_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


