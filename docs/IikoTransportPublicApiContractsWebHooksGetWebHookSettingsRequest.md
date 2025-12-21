# IikoTransportPublicApiContractsWebHooksGetWebHookSettingsRequest

Request to get webhooks settings for specified organization.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **UUID** | Organization UOC Id.                Can be obtained by &#x60;/organizations&#x60; operation. | 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_web_hooks_get_web_hook_settings_request import IikoTransportPublicApiContractsWebHooksGetWebHookSettingsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsWebHooksGetWebHookSettingsRequest from a JSON string
iiko_transport_public_api_contracts_web_hooks_get_web_hook_settings_request_instance = IikoTransportPublicApiContractsWebHooksGetWebHookSettingsRequest.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsWebHooksGetWebHookSettingsRequest.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_web_hooks_get_web_hook_settings_request_dict = iiko_transport_public_api_contracts_web_hooks_get_web_hook_settings_request_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsWebHooksGetWebHookSettingsRequest from a dict
iiko_transport_public_api_contracts_web_hooks_get_web_hook_settings_request_from_dict = IikoTransportPublicApiContractsWebHooksGetWebHookSettingsRequest.from_dict(iiko_transport_public_api_contracts_web_hooks_get_web_hook_settings_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


