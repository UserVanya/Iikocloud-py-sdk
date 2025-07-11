# TransportIntegrationWebHooksFiltersDeliveryOrderWebHooksFilter

Filter for delivery orders.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_statuses** | [**List[TransportDeliveriesCommonDeliveryStatus]**](TransportDeliveriesCommonDeliveryStatus.md) | Statuses of orders, when changing which need to send a notification. | [optional] 
**item_statuses** | [**List[TransportDeliveriesResponseOrderOrderItemStatus]**](TransportDeliveriesResponseOrderOrderItemStatus.md) | Statuses of order items, when changing which need to send a notification. | [optional] 
**errors** | **bool** | Flag for errors. | [optional] 
**returned_external_data_keys** | **List[str]** | Order external data keys to return in a notification. | [optional] 

## Example

```python
from iikocloud_client.models.transport_integration_web_hooks_filters_delivery_order_web_hooks_filter import TransportIntegrationWebHooksFiltersDeliveryOrderWebHooksFilter

# TODO update the JSON string below
json = "{}"
# create an instance of TransportIntegrationWebHooksFiltersDeliveryOrderWebHooksFilter from a JSON string
transport_integration_web_hooks_filters_delivery_order_web_hooks_filter_instance = TransportIntegrationWebHooksFiltersDeliveryOrderWebHooksFilter.from_json(json)
# print the JSON string representation of the object
print(TransportIntegrationWebHooksFiltersDeliveryOrderWebHooksFilter.to_json())

# convert the object into a dict
transport_integration_web_hooks_filters_delivery_order_web_hooks_filter_dict = transport_integration_web_hooks_filters_delivery_order_web_hooks_filter_instance.to_dict()
# create an instance of TransportIntegrationWebHooksFiltersDeliveryOrderWebHooksFilter from a dict
transport_integration_web_hooks_filters_delivery_order_web_hooks_filter_from_dict = TransportIntegrationWebHooksFiltersDeliveryOrderWebHooksFilter.from_dict(transport_integration_web_hooks_filters_delivery_order_web_hooks_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


