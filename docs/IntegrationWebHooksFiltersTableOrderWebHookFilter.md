# IntegrationWebHooksFiltersTableOrderWebHookFilter

Filter for table orders.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_statuses** | [**List[OrdersCommonOrderStatus]**](OrdersCommonOrderStatus.md) | Statuses of orders, when changing which need to send a notification. | [optional] 
**item_statuses** | [**List[DeliveriesResponseOrderOrderItemStatus]**](DeliveriesResponseOrderOrderItemStatus.md) | Statuses of order items, when changing which need to send a notification. | [optional] 
**errors** | **bool** | Flag for updates. | [optional] 

## Example

```python
from iikocloud_client.models.integration_web_hooks_filters_table_order_web_hook_filter import IntegrationWebHooksFiltersTableOrderWebHookFilter

# TODO update the JSON string below
json = "{}"
# create an instance of IntegrationWebHooksFiltersTableOrderWebHookFilter from a JSON string
integration_web_hooks_filters_table_order_web_hook_filter_instance = IntegrationWebHooksFiltersTableOrderWebHookFilter.from_json(json)
# print the JSON string representation of the object
print(IntegrationWebHooksFiltersTableOrderWebHookFilter.to_json())

# convert the object into a dict
integration_web_hooks_filters_table_order_web_hook_filter_dict = integration_web_hooks_filters_table_order_web_hook_filter_instance.to_dict()
# create an instance of IntegrationWebHooksFiltersTableOrderWebHookFilter from a dict
integration_web_hooks_filters_table_order_web_hook_filter_from_dict = IntegrationWebHooksFiltersTableOrderWebHookFilter.from_dict(integration_web_hooks_filters_table_order_web_hook_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


