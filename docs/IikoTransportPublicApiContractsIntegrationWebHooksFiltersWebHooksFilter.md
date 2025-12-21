# IikoTransportPublicApiContractsIntegrationWebHooksFiltersWebHooksFilter

Webhooks filter.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delivery_order_filter** | [**IikoTransportPublicApiContractsIntegrationWebHooksFiltersDeliveryOrderWebHooksFilter**](IikoTransportPublicApiContractsIntegrationWebHooksFiltersDeliveryOrderWebHooksFilter.md) | Filter for delivery orders. | [optional] 
**table_order_filter** | [**IikoTransportPublicApiContractsIntegrationWebHooksFiltersTableOrderWebHookFilter**](IikoTransportPublicApiContractsIntegrationWebHooksFiltersTableOrderWebHookFilter.md) | Filter for table orders. | [optional] 
**reserve_filter** | [**IikoTransportPublicApiContractsIntegrationWebHooksFiltersReserveWebHookFilter**](IikoTransportPublicApiContractsIntegrationWebHooksFiltersReserveWebHookFilter.md) | Filter for banquets/reserves. | [optional] 
**stop_list_update_filter** | [**IikoTransportPublicApiContractsIntegrationWebHooksFiltersWebHookShortFilter**](IikoTransportPublicApiContractsIntegrationWebHooksFiltersWebHookShortFilter.md) | Filter for stop-lists changes. | [optional] 
**personal_shift_filter** | [**IikoTransportPublicApiContractsIntegrationWebHooksFiltersWebHookShortFilter**](IikoTransportPublicApiContractsIntegrationWebHooksFiltersWebHookShortFilter.md) | Filter for personal shift. | [optional] 
**nomenclature_update_filter** | [**IikoTransportPublicApiContractsIntegrationWebHooksFiltersWebHookShortFilter**](IikoTransportPublicApiContractsIntegrationWebHooksFiltersWebHookShortFilter.md) | Filter for nomenclature changes. | [optional] 
**business_hours_and_mapping_update_filter** | [**IikoTransportPublicApiContractsIntegrationWebHooksFiltersWebHookShortFilter**](IikoTransportPublicApiContractsIntegrationWebHooksFiltersWebHookShortFilter.md) | Filter for business hours and mapping changes. | [optional] 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_integration_web_hooks_filters_web_hooks_filter import IikoTransportPublicApiContractsIntegrationWebHooksFiltersWebHooksFilter

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsIntegrationWebHooksFiltersWebHooksFilter from a JSON string
iiko_transport_public_api_contracts_integration_web_hooks_filters_web_hooks_filter_instance = IikoTransportPublicApiContractsIntegrationWebHooksFiltersWebHooksFilter.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsIntegrationWebHooksFiltersWebHooksFilter.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_integration_web_hooks_filters_web_hooks_filter_dict = iiko_transport_public_api_contracts_integration_web_hooks_filters_web_hooks_filter_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsIntegrationWebHooksFiltersWebHooksFilter from a dict
iiko_transport_public_api_contracts_integration_web_hooks_filters_web_hooks_filter_from_dict = IikoTransportPublicApiContractsIntegrationWebHooksFiltersWebHooksFilter.from_dict(iiko_transport_public_api_contracts_integration_web_hooks_filters_web_hooks_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


