# TransportWebHooksGetWebHookSettingsRequest

Request to get webhooks settings for specified organization.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **str** | Organization UOC Id.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 

## Example

```python
from iiko_cloud_client.models.transport_web_hooks_get_web_hook_settings_request import TransportWebHooksGetWebHookSettingsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TransportWebHooksGetWebHookSettingsRequest from a JSON string
transport_web_hooks_get_web_hook_settings_request_instance = TransportWebHooksGetWebHookSettingsRequest.from_json(json)
# print the JSON string representation of the object
print(TransportWebHooksGetWebHookSettingsRequest.to_json())

# convert the object into a dict
transport_web_hooks_get_web_hook_settings_request_dict = transport_web_hooks_get_web_hook_settings_request_instance.to_dict()
# create an instance of TransportWebHooksGetWebHookSettingsRequest from a dict
transport_web_hooks_get_web_hook_settings_request_from_dict = TransportWebHooksGetWebHookSettingsRequest.from_dict(transport_web_hooks_get_web_hook_settings_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


