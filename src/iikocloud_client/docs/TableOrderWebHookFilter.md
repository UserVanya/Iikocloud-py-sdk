# TableOrderWebHookFilter

Filter for table orders.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | **bool** | Flag for updates. | [optional] 
**item_statuses** | [**List[OrderItemStatus]**](OrderItemStatus.md) | Statuses of order items, when changing which need to send a notification. | [optional] 
**order_statuses** | [**List[OrderStatus]**](OrderStatus.md) | Statuses of orders, when changing which need to send a notification. | [optional] 

## Example

```python
from iikocloud_client.models.table_order_web_hook_filter import TableOrderWebHookFilter

# TODO update the JSON string below
json = "{}"
# create an instance of TableOrderWebHookFilter from a JSON string
table_order_web_hook_filter_instance = TableOrderWebHookFilter.from_json(json)
# print the JSON string representation of the object
print(TableOrderWebHookFilter.to_json())

# convert the object into a dict
table_order_web_hook_filter_dict = table_order_web_hook_filter_instance.to_dict()
# create an instance of TableOrderWebHookFilter from a dict
table_order_web_hook_filter_from_dict = TableOrderWebHookFilter.from_dict(table_order_web_hook_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


