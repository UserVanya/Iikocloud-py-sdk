# PersonalShiftWebHookEventInfo

WebHook notification about employee personal shift update.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **UUID** | Operation ID. | [optional] 
**event_info** | [**PersonalShift**](PersonalShift.md) | Event details. | [optional] 
**event_time** | **str** | Event date and time (UTC). | [optional] 
**event_type** | **str** | Event type. | [optional] 
**organization_id** | **UUID** | Organization ID.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | [optional] 

## Example

```python
from iikocloud_client.models.personal_shift_web_hook_event_info import PersonalShiftWebHookEventInfo

# TODO update the JSON string below
json = "{}"
# create an instance of PersonalShiftWebHookEventInfo from a JSON string
personal_shift_web_hook_event_info_instance = PersonalShiftWebHookEventInfo.from_json(json)
# print the JSON string representation of the object
print(PersonalShiftWebHookEventInfo.to_json())

# convert the object into a dict
personal_shift_web_hook_event_info_dict = personal_shift_web_hook_event_info_instance.to_dict()
# create an instance of PersonalShiftWebHookEventInfo from a dict
personal_shift_web_hook_event_info_from_dict = PersonalShiftWebHookEventInfo.from_dict(personal_shift_web_hook_event_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


