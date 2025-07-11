# TransportIntegrationWebHooksFiltersTableOrderWebHookFilter

Filter for table orders.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_statuses** | [**List[TransportOrdersCommonOrderStatus]**](TransportOrdersCommonOrderStatus.md) | Statuses of orders, when changing which need to send a notification. | [optional] 
**item_statuses** | [**List[TransportDeliveriesResponseOrderOrderItemStatus]**](TransportDeliveriesResponseOrderOrderItemStatus.md) | Statuses of order items, when changing which need to send a notification. | [optional] 
**errors** | **bool** | Flag for updates. | [optional] 

## Example

```python
from iikocloud_client.models.transport_integration_web_hooks_filters_table_order_web_hook_filter import TransportIntegrationWebHooksFiltersTableOrderWebHookFilter

# TODO update the JSON string below
json = "{}"
# create an instance of TransportIntegrationWebHooksFiltersTableOrderWebHookFilter from a JSON string
transport_integration_web_hooks_filters_table_order_web_hook_filter_instance = TransportIntegrationWebHooksFiltersTableOrderWebHookFilter.from_json(json)
# print the JSON string representation of the object
print(TransportIntegrationWebHooksFiltersTableOrderWebHookFilter.to_json())

# convert the object into a dict
transport_integration_web_hooks_filters_table_order_web_hook_filter_dict = transport_integration_web_hooks_filters_table_order_web_hook_filter_instance.to_dict()
# create an instance of TransportIntegrationWebHooksFiltersTableOrderWebHookFilter from a dict
transport_integration_web_hooks_filters_table_order_web_hook_filter_from_dict = TransportIntegrationWebHooksFiltersTableOrderWebHookFilter.from_dict(transport_integration_web_hooks_filters_table_order_web_hook_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


