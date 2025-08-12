# TransportTableOrdersRequestAddItemsToTableOrderRequest

Request for add order items to table order.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**add_order_items_settings** | [**TransportTableOrdersRequestAddTableOrderItemsSettings**](TransportTableOrdersRequestAddTableOrderItemsSettings.md) | Add order items parameters. | [optional] 
**order_id** | **str** | Order ID. | 
**organization_id** | **str** | Organization ID.                Can be obtained by &#x60;/organizations&#x60; operation. | 
**items** | [**List[TransportDeliveriesRequestCreateOrderOrderItem]**](TransportDeliveriesRequestCreateOrderOrderItem.md) | Order items (may include ProductOrderItem or CompoundOrderItem). | 
**combos** | [**List[TransportDeliveriesRequestCreateOrderCombo]**](TransportDeliveriesRequestCreateOrderCombo.md) | Combos.   &gt; Allowed from version &#x60;7.6.1&#x60;. | [optional] 

## Example

```python
from iikocloud_client.models.transport_table_orders_request_add_items_to_table_order_request import TransportTableOrdersRequestAddItemsToTableOrderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TransportTableOrdersRequestAddItemsToTableOrderRequest from a JSON string
transport_table_orders_request_add_items_to_table_order_request_instance = TransportTableOrdersRequestAddItemsToTableOrderRequest.from_json(json)
# print the JSON string representation of the object
print(TransportTableOrdersRequestAddItemsToTableOrderRequest.to_json())

# convert the object into a dict
transport_table_orders_request_add_items_to_table_order_request_dict = transport_table_orders_request_add_items_to_table_order_request_instance.to_dict()
# create an instance of TransportTableOrdersRequestAddItemsToTableOrderRequest from a dict
transport_table_orders_request_add_items_to_table_order_request_from_dict = TransportTableOrdersRequestAddItemsToTableOrderRequest.from_dict(transport_table_orders_request_add_items_to_table_order_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


