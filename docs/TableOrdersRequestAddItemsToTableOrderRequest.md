# TableOrdersRequestAddItemsToTableOrderRequest

Request for add order items to table order.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**add_order_items_settings** | [**TableOrdersRequestAddTableOrderItemsSettings**](TableOrdersRequestAddTableOrderItemsSettings.md) | Add order items parameters. | [optional] 
**order_id** | **UUID** | Order ID. | 
**organization_id** | **UUID** | Organization ID.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 
**items** | [**List[DeliveriesRequestCreateOrderOrderItem]**](DeliveriesRequestCreateOrderOrderItem.md) | Order items (may include ProductOrderItem or CompoundOrderItem). | 
**combos** | [**List[DeliveriesRequestCreateOrderCombo]**](DeliveriesRequestCreateOrderCombo.md) | Combos.   &gt; Allowed from version &#x60;7.6.1&#x60;. | [optional] 

## Example

```python
from iikocloud_client.models.table_orders_request_add_items_to_table_order_request import TableOrdersRequestAddItemsToTableOrderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TableOrdersRequestAddItemsToTableOrderRequest from a JSON string
table_orders_request_add_items_to_table_order_request_instance = TableOrdersRequestAddItemsToTableOrderRequest.from_json(json)
# print the JSON string representation of the object
print(TableOrdersRequestAddItemsToTableOrderRequest.to_json())

# convert the object into a dict
table_orders_request_add_items_to_table_order_request_dict = table_orders_request_add_items_to_table_order_request_instance.to_dict()
# create an instance of TableOrdersRequestAddItemsToTableOrderRequest from a dict
table_orders_request_add_items_to_table_order_request_from_dict = TableOrdersRequestAddItemsToTableOrderRequest.from_dict(table_orders_request_add_items_to_table_order_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


