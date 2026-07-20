# DeliveryOrderResponseProductItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**codes** | **List[List[OrderItemIdentifierCode]]** | List of product codes. Each outer list item represents a separate product unit;  each inner list contains codes associated with that unit.   &gt; Allowed from version &#x60;9.2.6&#x60;. | [optional] 
**cost** | **float** | Total cost per item without tax, discounts/surcharges. | 
**modifiers** | [**List[OrderItemModifier]**](OrderItemModifier.md) | Modifiers. | [optional] 
**position_id** | **UUID** | Unique identifier of the item in the order and for the whole system. | [optional] 
**price** | **float** | Price per item unit. Can be sent different from the price in the base menu. | 
**price_predefined** | **bool** | Whether price is predefined. | 
**product** | [**Product**](Product.md) | Item. | 
**result_sum** | **float** | Total amount per item including tax, discounts/surcharges. | [optional] 
**tax_percent** | **float** | Tax rate. | [optional] 

## Example

```python
from iikocloud_client.models.delivery_order_response_product_item import DeliveryOrderResponseProductItem

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveryOrderResponseProductItem from a JSON string
delivery_order_response_product_item_instance = DeliveryOrderResponseProductItem.from_json(json)
# print the JSON string representation of the object
print(DeliveryOrderResponseProductItem.to_json())

# convert the object into a dict
delivery_order_response_product_item_dict = delivery_order_response_product_item_instance.to_dict()
# create an instance of DeliveryOrderResponseProductItem from a dict
delivery_order_response_product_item_from_dict = DeliveryOrderResponseProductItem.from_dict(delivery_order_response_product_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


