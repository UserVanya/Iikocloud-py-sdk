# TransportWebHooksGetWebHookSettingsResponse

Response to get webhooks settings for specified organization.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **str** | Operation ID. | 
**api_login_name** | **str** | Api login name. | 
**web_hooks_uri** | **str** | Webhook handler url. | 
**auth_token** | **str** | Authorization token to pass to the webhook handler. | [optional] 
**web_hooks_filter** | [**TransportIntegrationWebHooksFiltersWebHooksFilter**](TransportIntegrationWebHooksFiltersWebHooksFilter.md) | Webhooks filter. | [optional] 

## Example

```python
from iiko_cloud_client.models.transport_web_hooks_get_web_hook_settings_response import TransportWebHooksGetWebHookSettingsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TransportWebHooksGetWebHookSettingsResponse from a JSON string
transport_web_hooks_get_web_hook_settings_response_instance = TransportWebHooksGetWebHookSettingsResponse.from_json(json)
# print the JSON string representation of the object
print(TransportWebHooksGetWebHookSettingsResponse.to_json())

# convert the object into a dict
transport_web_hooks_get_web_hook_settings_response_dict = transport_web_hooks_get_web_hook_settings_response_instance.to_dict()
# create an instance of TransportWebHooksGetWebHookSettingsResponse from a dict
transport_web_hooks_get_web_hook_settings_response_from_dict = TransportWebHooksGetWebHookSettingsResponse.from_dict(transport_web_hooks_get_web_hook_settings_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


