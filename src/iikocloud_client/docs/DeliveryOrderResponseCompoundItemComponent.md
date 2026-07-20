# DeliveryOrderResponseCompoundItemComponent

Part of composite item.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cost** | **float** | Item total including tax, discounts/surcharges. | 
**modifiers** | [**List[OrderItemModifier]**](OrderItemModifier.md) | Modifiers. | [optional] 
**position_id** | **UUID** | Unique identifier of the item in the order and for the whole system. | [optional] 
**price** | **float** | Price per item unit. Can be sent different from the price in the base menu. | 
**price_predefined** | **bool** | Whether price is predefined. | 
**product** | [**Product**](Product.md) | Item. | 
**result_sum** | **float** | Total amount per item including tax, discounts/surcharges. | [optional] 
**tax_percent** | **float** | Tax rate. | [optional] 

## Example

```python
from iikocloud_client.models.delivery_order_response_compound_item_component import DeliveryOrderResponseCompoundItemComponent

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveryOrderResponseCompoundItemComponent from a JSON string
delivery_order_response_compound_item_component_instance = DeliveryOrderResponseCompoundItemComponent.from_json(json)
# print the JSON string representation of the object
print(DeliveryOrderResponseCompoundItemComponent.to_json())

# convert the object into a dict
delivery_order_response_compound_item_component_dict = delivery_order_response_compound_item_component_instance.to_dict()
# create an instance of DeliveryOrderResponseCompoundItemComponent from a dict
delivery_order_response_compound_item_component_from_dict = DeliveryOrderResponseCompoundItemComponent.from_dict(delivery_order_response_compound_item_component_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


