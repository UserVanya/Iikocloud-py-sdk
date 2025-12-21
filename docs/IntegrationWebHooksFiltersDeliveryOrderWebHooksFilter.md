# IntegrationWebHooksFiltersDeliveryOrderWebHooksFilter

Filter for delivery orders.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_statuses** | [**List[DeliveriesCommonDeliveryStatus]**](DeliveriesCommonDeliveryStatus.md) | Statuses of orders, when changing which need to send a notification. | [optional] 
**item_statuses** | [**List[DeliveriesResponseOrderOrderItemStatus]**](DeliveriesResponseOrderOrderItemStatus.md) | Statuses of order items, when changing which need to send a notification. | [optional] 
**errors** | **bool** | Flag for errors. | [optional] 
**returned_external_data_keys** | **List[str]** | Order external data keys to return in a notification. | [optional] 

## Example

```python
from iikocloud_client.models.integration_web_hooks_filters_delivery_order_web_hooks_filter import IntegrationWebHooksFiltersDeliveryOrderWebHooksFilter

# TODO update the JSON string below
json = "{}"
# create an instance of IntegrationWebHooksFiltersDeliveryOrderWebHooksFilter from a JSON string
integration_web_hooks_filters_delivery_order_web_hooks_filter_instance = IntegrationWebHooksFiltersDeliveryOrderWebHooksFilter.from_json(json)
# print the JSON string representation of the object
print(IntegrationWebHooksFiltersDeliveryOrderWebHooksFilter.to_json())

# convert the object into a dict
integration_web_hooks_filters_delivery_order_web_hooks_filter_dict = integration_web_hooks_filters_delivery_order_web_hooks_filter_instance.to_dict()
# create an instance of IntegrationWebHooksFiltersDeliveryOrderWebHooksFilter from a dict
integration_web_hooks_filters_delivery_order_web_hooks_filter_from_dict = IntegrationWebHooksFiltersDeliveryOrderWebHooksFilter.from_dict(integration_web_hooks_filters_delivery_order_web_hooks_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


