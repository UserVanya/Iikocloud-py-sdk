# TransportWebHooksUpdateWebHookSettingsRequest

Request to add or update webhooks settings for listed api logins of the specified organization.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **str** | Organization UOC Id.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 
**web_hooks_uri** | **str** | Webhook handler url. | 
**auth_token** | **str** | Authorization token to pass to the webhook handler. | [optional] 
**web_hooks_filter** | [**TransportIntegrationWebHooksFiltersWebHooksFilter**](TransportIntegrationWebHooksFiltersWebHooksFilter.md) | Webhooks filter. | [optional] 

## Example

```python
from iiko_cloud_client.models.transport_web_hooks_update_web_hook_settings_request import TransportWebHooksUpdateWebHookSettingsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TransportWebHooksUpdateWebHookSettingsRequest from a JSON string
transport_web_hooks_update_web_hook_settings_request_instance = TransportWebHooksUpdateWebHookSettingsRequest.from_json(json)
# print the JSON string representation of the object
print(TransportWebHooksUpdateWebHookSettingsRequest.to_json())

# convert the object into a dict
transport_web_hooks_update_web_hook_settings_request_dict = transport_web_hooks_update_web_hook_settings_request_instance.to_dict()
# create an instance of TransportWebHooksUpdateWebHookSettingsRequest from a dict
transport_web_hooks_update_web_hook_settings_request_from_dict = TransportWebHooksUpdateWebHookSettingsRequest.from_dict(transport_web_hooks_update_web_hook_settings_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


