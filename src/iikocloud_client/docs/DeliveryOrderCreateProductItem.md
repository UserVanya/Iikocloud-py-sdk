# DeliveryOrderCreateProductItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**modifiers** | [**List[Modifier]**](Modifier.md) | Modifiers. | [optional] 
**position_id** | **UUID** | Unique identifier of the item in the order.  MUST be unique for the whole system. Therefore it must be generated with Guid.NewGuid().  &gt; If sent null, it generates automatically on iikoTransport side. | [optional] 
**price** | **float** | Price per item unit. Can be sent different from the price in the base menu. | 
**product_id** | **UUID** | ID of menu item.                Can be obtained by &#x60;/api/1/nomenclature&#x60; operation. | 

## Example

```python
from iikocloud_client.models.delivery_order_create_product_item import DeliveryOrderCreateProductItem

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveryOrderCreateProductItem from a JSON string
delivery_order_create_product_item_instance = DeliveryOrderCreateProductItem.from_json(json)
# print the JSON string representation of the object
print(DeliveryOrderCreateProductItem.to_json())

# convert the object into a dict
delivery_order_create_product_item_dict = delivery_order_create_product_item_instance.to_dict()
# create an instance of DeliveryOrderCreateProductItem from a dict
delivery_order_create_product_item_from_dict = DeliveryOrderCreateProductItem.from_dict(delivery_order_create_product_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


