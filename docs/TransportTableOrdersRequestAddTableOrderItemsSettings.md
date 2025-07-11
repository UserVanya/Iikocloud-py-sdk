# TransportTableOrdersRequestAddTableOrderItemsSettings

Add table order items options.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_print** | **bool** | Auto service print is needed. | [optional] 

## Example

```python
from iikocloud_client.models.transport_table_orders_request_add_table_order_items_settings import TransportTableOrdersRequestAddTableOrderItemsSettings

# TODO update the JSON string below
json = "{}"
# create an instance of TransportTableOrdersRequestAddTableOrderItemsSettings from a JSON string
transport_table_orders_request_add_table_order_items_settings_instance = TransportTableOrdersRequestAddTableOrderItemsSettings.from_json(json)
# print the JSON string representation of the object
print(TransportTableOrdersRequestAddTableOrderItemsSettings.to_json())

# convert the object into a dict
transport_table_orders_request_add_table_order_items_settings_dict = transport_table_orders_request_add_table_order_items_settings_instance.to_dict()
# create an instance of TransportTableOrdersRequestAddTableOrderItemsSettings from a dict
transport_table_orders_request_add_table_order_items_settings_from_dict = TransportTableOrdersRequestAddTableOrderItemsSettings.from_dict(transport_table_orders_request_add_table_order_items_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


