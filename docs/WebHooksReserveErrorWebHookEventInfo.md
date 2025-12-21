# WebHooksReserveErrorWebHookEventInfo

WebHook notification about reserve saving error.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_type** | [**ConstantStringReserveError**](ConstantStringReserveError.md) | Event type. | [optional] 
**event_time** | **str** | Event date and time (UTC). | [optional] 
**organization_id** | **UUID** | Organization ID.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | [optional] 
**correlation_id** | **UUID** | Operation ID. | [optional] 
**event_info** | [**ReservesReserveInfo**](ReservesReserveInfo.md) | Event details. | [optional] 

## Example

```python
from iikocloud_client.models.web_hooks_reserve_error_web_hook_event_info import WebHooksReserveErrorWebHookEventInfo

# TODO update the JSON string below
json = "{}"
# create an instance of WebHooksReserveErrorWebHookEventInfo from a JSON string
web_hooks_reserve_error_web_hook_event_info_instance = WebHooksReserveErrorWebHookEventInfo.from_json(json)
# print the JSON string representation of the object
print(WebHooksReserveErrorWebHookEventInfo.to_json())

# convert the object into a dict
web_hooks_reserve_error_web_hook_event_info_dict = web_hooks_reserve_error_web_hook_event_info_instance.to_dict()
# create an instance of WebHooksReserveErrorWebHookEventInfo from a dict
web_hooks_reserve_error_web_hook_event_info_from_dict = WebHooksReserveErrorWebHookEventInfo.from_dict(web_hooks_reserve_error_web_hook_event_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


