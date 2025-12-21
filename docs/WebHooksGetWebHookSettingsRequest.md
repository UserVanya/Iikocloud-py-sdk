# WebHooksGetWebHookSettingsRequest

Request to get webhooks settings for specified organization.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **UUID** | Organization UOC Id.                Can be obtained by &#x60;/organizations&#x60; operation. | 

## Example

```python
from iikocloud_client.models.web_hooks_get_web_hook_settings_request import WebHooksGetWebHookSettingsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WebHooksGetWebHookSettingsRequest from a JSON string
web_hooks_get_web_hook_settings_request_instance = WebHooksGetWebHookSettingsRequest.from_json(json)
# print the JSON string representation of the object
print(WebHooksGetWebHookSettingsRequest.to_json())

# convert the object into a dict
web_hooks_get_web_hook_settings_request_dict = web_hooks_get_web_hook_settings_request_instance.to_dict()
# create an instance of WebHooksGetWebHookSettingsRequest from a dict
web_hooks_get_web_hook_settings_request_from_dict = WebHooksGetWebHookSettingsRequest.from_dict(web_hooks_get_web_hook_settings_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


