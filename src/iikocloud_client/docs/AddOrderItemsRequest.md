# AddOrderItemsRequest

Request for add order items.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**combos** | [**List[Combo]**](Combo.md) | Combos.   &gt; Allowed from version &#x60;7.6.1&#x60;. | [optional] 
**items** | [**List[DeliveryOrderCreateItem]**](DeliveryOrderCreateItem.md) | Order items (may include ProductOrderItem or CompoundOrderItem). | 
**order_id** | **UUID** | Order ID. | 
**organization_id** | **UUID** | Organization ID.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 

## Example

```python
from iikocloud_client.models.add_order_items_request import AddOrderItemsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddOrderItemsRequest from a JSON string
add_order_items_request_instance = AddOrderItemsRequest.from_json(json)
# print the JSON string representation of the object
print(AddOrderItemsRequest.to_json())

# convert the object into a dict
add_order_items_request_dict = add_order_items_request_instance.to_dict()
# create an instance of AddOrderItemsRequest from a dict
add_order_items_request_from_dict = AddOrderItemsRequest.from_dict(add_order_items_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


