# TableOrdersRequestCreateTableOrderRequest

Order creation model.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **UUID** | Organization ID.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 
**terminal_group_id** | **UUID** | Front group ID an order must be sent to.                Can be obtained by &#x60;/api/1/terminal_groups&#x60; operation. | 
**order** | [**TableOrdersRequestTableOrder**](TableOrdersRequestTableOrder.md) | Order. | [optional] 
**create_order_settings** | [**TableOrdersRequestCreateTableOrderSettings**](TableOrdersRequestCreateTableOrderSettings.md) | Order creation parameters. | [optional] 

## Example

```python
from iikocloud_client.models.table_orders_request_create_table_order_request import TableOrdersRequestCreateTableOrderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TableOrdersRequestCreateTableOrderRequest from a JSON string
table_orders_request_create_table_order_request_instance = TableOrdersRequestCreateTableOrderRequest.from_json(json)
# print the JSON string representation of the object
print(TableOrdersRequestCreateTableOrderRequest.to_json())

# convert the object into a dict
table_orders_request_create_table_order_request_dict = table_orders_request_create_table_order_request_instance.to_dict()
# create an instance of TableOrdersRequestCreateTableOrderRequest from a dict
table_orders_request_create_table_order_request_from_dict = TableOrdersRequestCreateTableOrderRequest.from_dict(table_orders_request_create_table_order_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


