# GetWebHookSettingsResponse

Response to get webhooks settings for specified organization.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_login_name** | **str** | Api login name. | 
**auth_token** | **str** | Authorization token to pass to the webhook handler. | [optional] 
**correlation_id** | **UUID** | Operation ID. | 
**web_hooks_filter** | [**WebHooksFilter**](WebHooksFilter.md) | Webhooks filter. | [optional] 
**web_hooks_uri** | **str** | Webhook handler url. | 

## Example

```python
from iikocloud_client.models.get_web_hook_settings_response import GetWebHookSettingsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetWebHookSettingsResponse from a JSON string
get_web_hook_settings_response_instance = GetWebHookSettingsResponse.from_json(json)
# print the JSON string representation of the object
print(GetWebHookSettingsResponse.to_json())

# convert the object into a dict
get_web_hook_settings_response_dict = get_web_hook_settings_response_instance.to_dict()
# create an instance of GetWebHookSettingsResponse from a dict
get_web_hook_settings_response_from_dict = GetWebHookSettingsResponse.from_dict(get_web_hook_settings_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


