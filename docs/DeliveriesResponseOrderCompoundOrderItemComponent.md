# DeliveriesResponseOrderCompoundOrderItemComponent

Part of composite item.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product** | [**DeliveriesResponseOrderProduct**](DeliveriesResponseOrderProduct.md) | Item. | 
**modifiers** | [**List[DeliveriesResponseOrderOrderItemModifier]**](DeliveriesResponseOrderOrderItemModifier.md) | Modifiers. | [optional] 
**price** | **float** | Price per item unit. Can be sent different from the price in the base menu. | 
**cost** | **float** | Item total including tax, discounts/surcharges. | 
**price_predefined** | **bool** | Whether price is predefined. | 
**position_id** | **UUID** | Unique identifier of the item in the order and for the whole system. | [optional] 
**tax_percent** | **float** | Tax rate. | [optional] 
**result_sum** | **float** | Total amount per item including tax, discounts/surcharges. | [optional] 

## Example

```python
from iikocloud_client.models.deliveries_response_order_compound_order_item_component import DeliveriesResponseOrderCompoundOrderItemComponent

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveriesResponseOrderCompoundOrderItemComponent from a JSON string
deliveries_response_order_compound_order_item_component_instance = DeliveriesResponseOrderCompoundOrderItemComponent.from_json(json)
# print the JSON string representation of the object
print(DeliveriesResponseOrderCompoundOrderItemComponent.to_json())

# convert the object into a dict
deliveries_response_order_compound_order_item_component_dict = deliveries_response_order_compound_order_item_component_instance.to_dict()
# create an instance of DeliveriesResponseOrderCompoundOrderItemComponent from a dict
deliveries_response_order_compound_order_item_component_from_dict = DeliveriesResponseOrderCompoundOrderItemComponent.from_dict(deliveries_response_order_compound_order_item_component_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


