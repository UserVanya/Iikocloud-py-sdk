# TransportWebHooksReserveUpdateWebHookEventInfo

WebHook notification about reserve update.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_type** | **str** | Event type. | [optional] 
**event_time** | **str** | Event date and time (UTC). | [optional] 
**organization_id** | **str** | Organization ID.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | [optional] 
**correlation_id** | **str** | Operation ID. | [optional] 
**event_info** | [**TransportReservesReserveInfo**](TransportReservesReserveInfo.md) | Event details. | [optional] 

## Example

```python
from iikocloud_client.models.transport_web_hooks_reserve_update_web_hook_event_info import TransportWebHooksReserveUpdateWebHookEventInfo

# TODO update the JSON string below
json = "{}"
# create an instance of TransportWebHooksReserveUpdateWebHookEventInfo from a JSON string
transport_web_hooks_reserve_update_web_hook_event_info_instance = TransportWebHooksReserveUpdateWebHookEventInfo.from_json(json)
# print the JSON string representation of the object
print(TransportWebHooksReserveUpdateWebHookEventInfo.to_json())

# convert the object into a dict
transport_web_hooks_reserve_update_web_hook_event_info_dict = transport_web_hooks_reserve_update_web_hook_event_info_instance.to_dict()
# create an instance of TransportWebHooksReserveUpdateWebHookEventInfo from a dict
transport_web_hooks_reserve_update_web_hook_event_info_from_dict = TransportWebHooksReserveUpdateWebHookEventInfo.from_dict(transport_web_hooks_reserve_update_web_hook_event_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


