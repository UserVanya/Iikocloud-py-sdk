# IntegrationWebHooksFiltersReserveWebHookFilter

Filter for updates and errors.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**updates** | **bool** | Flag for updates. | [optional] 
**errors** | **bool** | Flag for errors. | [optional] 

## Example

```python
from iikocloud_client.models.integration_web_hooks_filters_reserve_web_hook_filter import IntegrationWebHooksFiltersReserveWebHookFilter

# TODO update the JSON string below
json = "{}"
# create an instance of IntegrationWebHooksFiltersReserveWebHookFilter from a JSON string
integration_web_hooks_filters_reserve_web_hook_filter_instance = IntegrationWebHooksFiltersReserveWebHookFilter.from_json(json)
# print the JSON string representation of the object
print(IntegrationWebHooksFiltersReserveWebHookFilter.to_json())

# convert the object into a dict
integration_web_hooks_filters_reserve_web_hook_filter_dict = integration_web_hooks_filters_reserve_web_hook_filter_instance.to_dict()
# create an instance of IntegrationWebHooksFiltersReserveWebHookFilter from a dict
integration_web_hooks_filters_reserve_web_hook_filter_from_dict = IntegrationWebHooksFiltersReserveWebHookFilter.from_dict(integration_web_hooks_filters_reserve_web_hook_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


