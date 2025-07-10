# TransportIntegrationWebHooksFiltersReserveWebHookFilter

Filter for updates and errors.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**updates** | **bool** | Flag for updates. | [optional] 
**errors** | **bool** | Flag for errors. | [optional] 

## Example

```python
from iiko_cloud_client.models.transport_integration_web_hooks_filters_reserve_web_hook_filter import TransportIntegrationWebHooksFiltersReserveWebHookFilter

# TODO update the JSON string below
json = "{}"
# create an instance of TransportIntegrationWebHooksFiltersReserveWebHookFilter from a JSON string
transport_integration_web_hooks_filters_reserve_web_hook_filter_instance = TransportIntegrationWebHooksFiltersReserveWebHookFilter.from_json(json)
# print the JSON string representation of the object
print(TransportIntegrationWebHooksFiltersReserveWebHookFilter.to_json())

# convert the object into a dict
transport_integration_web_hooks_filters_reserve_web_hook_filter_dict = transport_integration_web_hooks_filters_reserve_web_hook_filter_instance.to_dict()
# create an instance of TransportIntegrationWebHooksFiltersReserveWebHookFilter from a dict
transport_integration_web_hooks_filters_reserve_web_hook_filter_from_dict = TransportIntegrationWebHooksFiltersReserveWebHookFilter.from_dict(transport_integration_web_hooks_filters_reserve_web_hook_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


