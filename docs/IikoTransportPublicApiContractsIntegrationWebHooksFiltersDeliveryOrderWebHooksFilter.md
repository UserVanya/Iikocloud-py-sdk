# IikoTransportPublicApiContractsIntegrationWebHooksFiltersDeliveryOrderWebHooksFilter

Filter for delivery orders.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_statuses** | [**List[IikoTransportPublicApiContractsDeliveriesCommonDeliveryStatus]**](IikoTransportPublicApiContractsDeliveriesCommonDeliveryStatus.md) | Statuses of orders, when changing which need to send a notification. | [optional] 
**item_statuses** | [**List[IikoTransportPublicApiContractsDeliveriesResponseOrderOrderItemStatus]**](IikoTransportPublicApiContractsDeliveriesResponseOrderOrderItemStatus.md) | Statuses of order items, when changing which need to send a notification. | [optional] 
**errors** | **bool** | Flag for errors. | [optional] 
**returned_external_data_keys** | **List[str]** | Order external data keys to return in a notification. | [optional] 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_integration_web_hooks_filters_delivery_order_web_hooks_filter import IikoTransportPublicApiContractsIntegrationWebHooksFiltersDeliveryOrderWebHooksFilter

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsIntegrationWebHooksFiltersDeliveryOrderWebHooksFilter from a JSON string
iiko_transport_public_api_contracts_integration_web_hooks_filters_delivery_order_web_hooks_filter_instance = IikoTransportPublicApiContractsIntegrationWebHooksFiltersDeliveryOrderWebHooksFilter.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsIntegrationWebHooksFiltersDeliveryOrderWebHooksFilter.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_integration_web_hooks_filters_delivery_order_web_hooks_filter_dict = iiko_transport_public_api_contracts_integration_web_hooks_filters_delivery_order_web_hooks_filter_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsIntegrationWebHooksFiltersDeliveryOrderWebHooksFilter from a dict
iiko_transport_public_api_contracts_integration_web_hooks_filters_delivery_order_web_hooks_filter_from_dict = IikoTransportPublicApiContractsIntegrationWebHooksFiltersDeliveryOrderWebHooksFilter.from_dict(iiko_transport_public_api_contracts_integration_web_hooks_filters_delivery_order_web_hooks_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


