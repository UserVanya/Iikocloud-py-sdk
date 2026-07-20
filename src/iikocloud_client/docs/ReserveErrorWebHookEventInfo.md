# ReserveErrorWebHookEventInfo

WebHook notification about reserve saving error.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **UUID** | Operation ID. | [optional] 
**event_info** | [**ReserveInfo**](ReserveInfo.md) | Event details. | [optional] 
**event_time** | **str** | Event date and time (UTC). | [optional] 
**event_type** | **str** | Event type. | [optional] 
**organization_id** | **UUID** | Organization ID.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | [optional] 

## Example

```python
from iikocloud_client.models.reserve_error_web_hook_event_info import ReserveErrorWebHookEventInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ReserveErrorWebHookEventInfo from a JSON string
reserve_error_web_hook_event_info_instance = ReserveErrorWebHookEventInfo.from_json(json)
# print the JSON string representation of the object
print(ReserveErrorWebHookEventInfo.to_json())

# convert the object into a dict
reserve_error_web_hook_event_info_dict = reserve_error_web_hook_event_info_instance.to_dict()
# create an instance of ReserveErrorWebHookEventInfo from a dict
reserve_error_web_hook_event_info_from_dict = ReserveErrorWebHookEventInfo.from_dict(reserve_error_web_hook_event_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


