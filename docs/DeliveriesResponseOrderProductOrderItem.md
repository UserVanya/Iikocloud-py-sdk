# DeliveriesResponseOrderProductOrderItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product** | [**DeliveriesResponseOrderProduct**](DeliveriesResponseOrderProduct.md) | Item. | 
**modifiers** | [**List[DeliveriesResponseOrderOrderItemModifier]**](DeliveriesResponseOrderOrderItemModifier.md) | Modifiers. | [optional] 
**codes** | **List[List[DeliveriesResponseOrderOrderItemIdentifierCode]]** | List of product codes. Each outer list item represents a separate product unit;  each inner list contains codes associated with that unit.   &gt; Allowed from version &#x60;9.2.6&#x60;. | [optional] 
**price** | **float** | Price per item unit. Can be sent different from the price in the base menu. | 
**cost** | **float** | Total cost per item without tax, discounts/surcharges. | 
**price_predefined** | **bool** | Whether price is predefined. | 
**position_id** | **UUID** | Unique identifier of the item in the order and for the whole system. | [optional] 
**tax_percent** | **float** | Tax rate. | [optional] 
**result_sum** | **float** | Total amount per item including tax, discounts/surcharges. | [optional] 

## Example

```python
from iikocloud_client.models.deliveries_response_order_product_order_item import DeliveriesResponseOrderProductOrderItem

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveriesResponseOrderProductOrderItem from a JSON string
deliveries_response_order_product_order_item_instance = DeliveriesResponseOrderProductOrderItem.from_json(json)
# print the JSON string representation of the object
print(DeliveriesResponseOrderProductOrderItem.to_json())

# convert the object into a dict
deliveries_response_order_product_order_item_dict = deliveries_response_order_product_order_item_instance.to_dict()
# create an instance of DeliveriesResponseOrderProductOrderItem from a dict
deliveries_response_order_product_order_item_from_dict = DeliveriesResponseOrderProductOrderItem.from_dict(deliveries_response_order_product_order_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


