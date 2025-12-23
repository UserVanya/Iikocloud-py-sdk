# WebHooksUpdateWebHookSettingsRequest

Request to add or update webhooks settings for listed api logins of the specified organization.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **str** | Organization UOC Id.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 
**web_hooks_uri** | **str** | Webhook handler url. | 
**auth_token** | **str** | Authorization token to pass to the webhook handler. | [optional] 
**web_hooks_filter** | [**IntegrationWebHooksFiltersWebHooksFilter**](IntegrationWebHooksFiltersWebHooksFilter.md) | Webhooks filter. | [optional] 

## Example

```python
from iikocloud_client.models.web_hooks_update_web_hook_settings_request import WebHooksUpdateWebHookSettingsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WebHooksUpdateWebHookSettingsRequest from a JSON string
web_hooks_update_web_hook_settings_request_instance = WebHooksUpdateWebHookSettingsRequest.from_json(json)
# print the JSON string representation of the object
print(WebHooksUpdateWebHookSettingsRequest.to_json())

# convert the object into a dict
web_hooks_update_web_hook_settings_request_dict = web_hooks_update_web_hook_settings_request_instance.to_dict()
# create an instance of WebHooksUpdateWebHookSettingsRequest from a dict
web_hooks_update_web_hook_settings_request_from_dict = WebHooksUpdateWebHookSettingsRequest.from_dict(web_hooks_update_web_hook_settings_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


