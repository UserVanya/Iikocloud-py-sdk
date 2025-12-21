# IntegrationWebHooksFiltersWebHooksFilter

Webhooks filter.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delivery_order_filter** | [**IntegrationWebHooksFiltersDeliveryOrderWebHooksFilter**](IntegrationWebHooksFiltersDeliveryOrderWebHooksFilter.md) | Filter for delivery orders. | [optional] 
**table_order_filter** | [**IntegrationWebHooksFiltersTableOrderWebHookFilter**](IntegrationWebHooksFiltersTableOrderWebHookFilter.md) | Filter for table orders. | [optional] 
**reserve_filter** | [**IntegrationWebHooksFiltersReserveWebHookFilter**](IntegrationWebHooksFiltersReserveWebHookFilter.md) | Filter for banquets/reserves. | [optional] 
**stop_list_update_filter** | [**IntegrationWebHooksFiltersWebHookShortFilter**](IntegrationWebHooksFiltersWebHookShortFilter.md) | Filter for stop-lists changes. | [optional] 
**personal_shift_filter** | [**IntegrationWebHooksFiltersWebHookShortFilter**](IntegrationWebHooksFiltersWebHookShortFilter.md) | Filter for personal shift. | [optional] 
**nomenclature_update_filter** | [**IntegrationWebHooksFiltersWebHookShortFilter**](IntegrationWebHooksFiltersWebHookShortFilter.md) | Filter for nomenclature changes. | [optional] 
**business_hours_and_mapping_update_filter** | [**IntegrationWebHooksFiltersWebHookShortFilter**](IntegrationWebHooksFiltersWebHookShortFilter.md) | Filter for business hours and mapping changes. | [optional] 

## Example

```python
from iikocloud_client.models.integration_web_hooks_filters_web_hooks_filter import IntegrationWebHooksFiltersWebHooksFilter

# TODO update the JSON string below
json = "{}"
# create an instance of IntegrationWebHooksFiltersWebHooksFilter from a JSON string
integration_web_hooks_filters_web_hooks_filter_instance = IntegrationWebHooksFiltersWebHooksFilter.from_json(json)
# print the JSON string representation of the object
print(IntegrationWebHooksFiltersWebHooksFilter.to_json())

# convert the object into a dict
integration_web_hooks_filters_web_hooks_filter_dict = integration_web_hooks_filters_web_hooks_filter_instance.to_dict()
# create an instance of IntegrationWebHooksFiltersWebHooksFilter from a dict
integration_web_hooks_filters_web_hooks_filter_from_dict = IntegrationWebHooksFiltersWebHooksFilter.from_dict(integration_web_hooks_filters_web_hooks_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


