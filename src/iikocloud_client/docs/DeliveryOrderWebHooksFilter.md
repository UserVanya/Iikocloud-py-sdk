# DeliveryOrderWebHooksFilter

Filter for delivery orders.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | **bool** | Flag for errors. | [optional] 
**item_statuses** | [**List[OrderItemStatus]**](OrderItemStatus.md) | Statuses of order items, when changing which need to send a notification. | [optional] 
**order_statuses** | [**List[DeliveryStatus]**](DeliveryStatus.md) | Statuses of orders, when changing which need to send a notification. | [optional] 
**returned_external_data_keys** | **List[str]** | Order external data keys to return in a notification. | [optional] 

## Example

```python
from iikocloud_client.models.delivery_order_web_hooks_filter import DeliveryOrderWebHooksFilter

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveryOrderWebHooksFilter from a JSON string
delivery_order_web_hooks_filter_instance = DeliveryOrderWebHooksFilter.from_json(json)
# print the JSON string representation of the object
print(DeliveryOrderWebHooksFilter.to_json())

# convert the object into a dict
delivery_order_web_hooks_filter_dict = delivery_order_web_hooks_filter_instance.to_dict()
# create an instance of DeliveryOrderWebHooksFilter from a dict
delivery_order_web_hooks_filter_from_dict = DeliveryOrderWebHooksFilter.from_dict(delivery_order_web_hooks_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


