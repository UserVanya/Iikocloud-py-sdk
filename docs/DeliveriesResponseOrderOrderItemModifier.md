# DeliveriesResponseOrderOrderItemModifier

Order item modifier.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product** | [**DeliveriesResponseOrderProduct**](DeliveriesResponseOrderProduct.md) | Item. | 
**amount** | **float** | Quantity. | 
**amount_independent_of_parent_amount** | **bool** | Whether quantity of modifier depends on quantity of item. | 
**codes** | **List[List[DeliveriesResponseOrderOrderItemIdentifierCode]]** | List of product codes. Each outer list item represents a separate product unit;  each inner list contains codes associated with that unit.   &gt; Allowed from version &#x60;9.3.6&#x60;. | [optional] 
**product_group** | [**DeliveriesResponseOrderProductGroup**](DeliveriesResponseOrderProductGroup.md) | Group of modifiers (in case of a group modifier). | [optional] 
**price** | **float** | Price per item unit. Can be sent different from the price in RMS. | 
**price_predefined** | **bool** | Whether price is predefined. | 
**result_sum** | **float** | Total amount per item including tax, discounts/surcharges. | 
**deleted** | [**DeliveriesResponseOrderItemDeletedInfo**](DeliveriesResponseOrderItemDeletedInfo.md) | Item deletion details. If specified, the item is deleted. | [optional] 
**position_id** | **UUID** | Unique identifier of the item in the order and for the whole system. | [optional] 
**default_amount** | **int** | Default amount. | [optional] 
**hide_if_default_amount** | **bool** | Hide modifier in UI if \&quot;amount\&quot; equals \&quot;defaultAmount\&quot;. | [optional] 
**tax_percent** | **float** | Tax rate. | [optional] 
**free_of_charge_amount** | **int** | Free of charge amount. | [optional] 

## Example

```python
from iikocloud_client.models.deliveries_response_order_order_item_modifier import DeliveriesResponseOrderOrderItemModifier

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveriesResponseOrderOrderItemModifier from a JSON string
deliveries_response_order_order_item_modifier_instance = DeliveriesResponseOrderOrderItemModifier.from_json(json)
# print the JSON string representation of the object
print(DeliveriesResponseOrderOrderItemModifier.to_json())

# convert the object into a dict
deliveries_response_order_order_item_modifier_dict = deliveries_response_order_order_item_modifier_instance.to_dict()
# create an instance of DeliveriesResponseOrderOrderItemModifier from a dict
deliveries_response_order_order_item_modifier_from_dict = DeliveriesResponseOrderOrderItemModifier.from_dict(deliveries_response_order_order_item_modifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


