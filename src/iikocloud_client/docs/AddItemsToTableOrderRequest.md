# AddItemsToTableOrderRequest

Request for add order items to table order.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**add_order_items_settings** | [**AddTableOrderItemsSettings**](AddTableOrderItemsSettings.md) | Add order items parameters. | [optional] 
**combos** | [**List[Combo]**](Combo.md) | Combos.   &gt; Allowed from version &#x60;7.6.1&#x60;. | [optional] 
**items** | [**List[DeliveryOrderCreateItem]**](DeliveryOrderCreateItem.md) | Order items (may include ProductOrderItem or CompoundOrderItem). | 
**order_id** | **UUID** | Order ID. | 
**organization_id** | **UUID** | Organization ID.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 

## Example

```python
from iikocloud_client.models.add_items_to_table_order_request import AddItemsToTableOrderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddItemsToTableOrderRequest from a JSON string
add_items_to_table_order_request_instance = AddItemsToTableOrderRequest.from_json(json)
# print the JSON string representation of the object
print(AddItemsToTableOrderRequest.to_json())

# convert the object into a dict
add_items_to_table_order_request_dict = add_items_to_table_order_request_instance.to_dict()
# create an instance of AddItemsToTableOrderRequest from a dict
add_items_to_table_order_request_from_dict = AddItemsToTableOrderRequest.from_dict(add_items_to_table_order_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


