# TableOrdersRequestAddTableOrderItemsSettings

Add table order items options.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_print** | **bool** | Auto service print is needed. | [optional] 

## Example

```python
from iikocloud_client.models.table_orders_request_add_table_order_items_settings import TableOrdersRequestAddTableOrderItemsSettings

# TODO update the JSON string below
json = "{}"
# create an instance of TableOrdersRequestAddTableOrderItemsSettings from a JSON string
table_orders_request_add_table_order_items_settings_instance = TableOrdersRequestAddTableOrderItemsSettings.from_json(json)
# print the JSON string representation of the object
print(TableOrdersRequestAddTableOrderItemsSettings.to_json())

# convert the object into a dict
table_orders_request_add_table_order_items_settings_dict = table_orders_request_add_table_order_items_settings_instance.to_dict()
# create an instance of TableOrdersRequestAddTableOrderItemsSettings from a dict
table_orders_request_add_table_order_items_settings_from_dict = TableOrdersRequestAddTableOrderItemsSettings.from_dict(table_orders_request_add_table_order_items_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


