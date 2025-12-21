# DeliveriesRequestCreateOrderProductOrderItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_id** | **UUID** | ID of menu item.                Can be obtained by &#x60;/api/1/nomenclature&#x60; operation. | 
**modifiers** | [**List[DeliveriesRequestCreateOrderModifier]**](DeliveriesRequestCreateOrderModifier.md) | Modifiers. | [optional] 
**price** | **float** | Price per item unit. Can be sent different from the price in the base menu. | 
**position_id** | **UUID** | Unique identifier of the item in the order.  MUST be unique for the whole system. Therefore it must be generated with Guid.NewGuid().  &gt; If sent null, it generates automatically on iikoTransport side. | [optional] 

## Example

```python
from iikocloud_client.models.deliveries_request_create_order_product_order_item import DeliveriesRequestCreateOrderProductOrderItem

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveriesRequestCreateOrderProductOrderItem from a JSON string
deliveries_request_create_order_product_order_item_instance = DeliveriesRequestCreateOrderProductOrderItem.from_json(json)
# print the JSON string representation of the object
print(DeliveriesRequestCreateOrderProductOrderItem.to_json())

# convert the object into a dict
deliveries_request_create_order_product_order_item_dict = deliveries_request_create_order_product_order_item_instance.to_dict()
# create an instance of DeliveriesRequestCreateOrderProductOrderItem from a dict
deliveries_request_create_order_product_order_item_from_dict = DeliveriesRequestCreateOrderProductOrderItem.from_dict(deliveries_request_create_order_product_order_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


