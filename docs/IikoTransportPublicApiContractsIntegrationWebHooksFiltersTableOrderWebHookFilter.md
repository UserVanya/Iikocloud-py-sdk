# IikoTransportPublicApiContractsIntegrationWebHooksFiltersTableOrderWebHookFilter

Filter for table orders.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_statuses** | [**List[IikoTransportPublicApiContractsOrdersCommonOrderStatus]**](IikoTransportPublicApiContractsOrdersCommonOrderStatus.md) | Statuses of orders, when changing which need to send a notification. | [optional] 
**item_statuses** | [**List[IikoTransportPublicApiContractsDeliveriesResponseOrderOrderItemStatus]**](IikoTransportPublicApiContractsDeliveriesResponseOrderOrderItemStatus.md) | Statuses of order items, when changing which need to send a notification. | [optional] 
**errors** | **bool** | Flag for updates. | [optional] 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_integration_web_hooks_filters_table_order_web_hook_filter import IikoTransportPublicApiContractsIntegrationWebHooksFiltersTableOrderWebHookFilter

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsIntegrationWebHooksFiltersTableOrderWebHookFilter from a JSON string
iiko_transport_public_api_contracts_integration_web_hooks_filters_table_order_web_hook_filter_instance = IikoTransportPublicApiContractsIntegrationWebHooksFiltersTableOrderWebHookFilter.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsIntegrationWebHooksFiltersTableOrderWebHookFilter.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_integration_web_hooks_filters_table_order_web_hook_filter_dict = iiko_transport_public_api_contracts_integration_web_hooks_filters_table_order_web_hook_filter_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsIntegrationWebHooksFiltersTableOrderWebHookFilter from a dict
iiko_transport_public_api_contracts_integration_web_hooks_filters_table_order_web_hook_filter_from_dict = IikoTransportPublicApiContractsIntegrationWebHooksFiltersTableOrderWebHookFilter.from_dict(iiko_transport_public_api_contracts_integration_web_hooks_filters_table_order_web_hook_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


