# IikoTransportPublicApiContractsWebHooksGetWebHookSettingsResponse

Response to get webhooks settings for specified organization.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **UUID** | Operation ID. | 
**api_login_name** | **str** | Api login name. | 
**web_hooks_uri** | **str** | Webhook handler url. | 
**auth_token** | **str** | Authorization token to pass to the webhook handler. | [optional] 
**web_hooks_filter** | [**IikoTransportPublicApiContractsIntegrationWebHooksFiltersWebHooksFilter**](IikoTransportPublicApiContractsIntegrationWebHooksFiltersWebHooksFilter.md) | Webhooks filter. | [optional] 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_web_hooks_get_web_hook_settings_response import IikoTransportPublicApiContractsWebHooksGetWebHookSettingsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsWebHooksGetWebHookSettingsResponse from a JSON string
iiko_transport_public_api_contracts_web_hooks_get_web_hook_settings_response_instance = IikoTransportPublicApiContractsWebHooksGetWebHookSettingsResponse.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsWebHooksGetWebHookSettingsResponse.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_web_hooks_get_web_hook_settings_response_dict = iiko_transport_public_api_contracts_web_hooks_get_web_hook_settings_response_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsWebHooksGetWebHookSettingsResponse from a dict
iiko_transport_public_api_contracts_web_hooks_get_web_hook_settings_response_from_dict = IikoTransportPublicApiContractsWebHooksGetWebHookSettingsResponse.from_dict(iiko_transport_public_api_contracts_web_hooks_get_web_hook_settings_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


