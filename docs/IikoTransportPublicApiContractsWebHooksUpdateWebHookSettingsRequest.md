# IikoTransportPublicApiContractsWebHooksUpdateWebHookSettingsRequest

Request to add or update webhooks settings for listed api logins of the specified organization.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **UUID** | Organization UOC Id.                Can be obtained by &#x60;/organizations&#x60; operation. | 
**web_hooks_uri** | **str** | Webhook handler url. | 
**auth_token** | **str** | Authorization token to pass to the webhook handler. | [optional] 
**web_hooks_filter** | [**IikoTransportPublicApiContractsIntegrationWebHooksFiltersWebHooksFilter**](IikoTransportPublicApiContractsIntegrationWebHooksFiltersWebHooksFilter.md) | Webhooks filter. | [optional] 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_web_hooks_update_web_hook_settings_request import IikoTransportPublicApiContractsWebHooksUpdateWebHookSettingsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsWebHooksUpdateWebHookSettingsRequest from a JSON string
iiko_transport_public_api_contracts_web_hooks_update_web_hook_settings_request_instance = IikoTransportPublicApiContractsWebHooksUpdateWebHookSettingsRequest.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsWebHooksUpdateWebHookSettingsRequest.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_web_hooks_update_web_hook_settings_request_dict = iiko_transport_public_api_contracts_web_hooks_update_web_hook_settings_request_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsWebHooksUpdateWebHookSettingsRequest from a dict
iiko_transport_public_api_contracts_web_hooks_update_web_hook_settings_request_from_dict = IikoTransportPublicApiContractsWebHooksUpdateWebHookSettingsRequest.from_dict(iiko_transport_public_api_contracts_web_hooks_update_web_hook_settings_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


