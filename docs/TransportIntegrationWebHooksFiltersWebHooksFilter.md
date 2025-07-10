# TransportIntegrationWebHooksFiltersWebHooksFilter

Webhooks filter.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delivery_order_filter** | [**TransportIntegrationWebHooksFiltersDeliveryOrderWebHooksFilter**](TransportIntegrationWebHooksFiltersDeliveryOrderWebHooksFilter.md) | Filter for delivery orders. | [optional] 
**table_order_filter** | [**TransportIntegrationWebHooksFiltersTableOrderWebHookFilter**](TransportIntegrationWebHooksFiltersTableOrderWebHookFilter.md) | Filter for table orders. | [optional] 
**reserve_filter** | [**TransportIntegrationWebHooksFiltersReserveWebHookFilter**](TransportIntegrationWebHooksFiltersReserveWebHookFilter.md) | Filter for banquets/reserves. | [optional] 
**stop_list_update_filter** | [**TransportIntegrationWebHooksFiltersWebHookShortFilter**](TransportIntegrationWebHooksFiltersWebHookShortFilter.md) | Filter for stop-lists changes. | [optional] 
**personal_shift_filter** | [**TransportIntegrationWebHooksFiltersWebHookShortFilter**](TransportIntegrationWebHooksFiltersWebHookShortFilter.md) | Filter for personal shift. | [optional] 
**nomenclature_update_filter** | [**TransportIntegrationWebHooksFiltersWebHookShortFilter**](TransportIntegrationWebHooksFiltersWebHookShortFilter.md) | Filter for nomenclature changes. | [optional] 

## Example

```python
from iiko_cloud_client.models.transport_integration_web_hooks_filters_web_hooks_filter import TransportIntegrationWebHooksFiltersWebHooksFilter

# TODO update the JSON string below
json = "{}"
# create an instance of TransportIntegrationWebHooksFiltersWebHooksFilter from a JSON string
transport_integration_web_hooks_filters_web_hooks_filter_instance = TransportIntegrationWebHooksFiltersWebHooksFilter.from_json(json)
# print the JSON string representation of the object
print(TransportIntegrationWebHooksFiltersWebHooksFilter.to_json())

# convert the object into a dict
transport_integration_web_hooks_filters_web_hooks_filter_dict = transport_integration_web_hooks_filters_web_hooks_filter_instance.to_dict()
# create an instance of TransportIntegrationWebHooksFiltersWebHooksFilter from a dict
transport_integration_web_hooks_filters_web_hooks_filter_from_dict = TransportIntegrationWebHooksFiltersWebHooksFilter.from_dict(transport_integration_web_hooks_filters_web_hooks_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


