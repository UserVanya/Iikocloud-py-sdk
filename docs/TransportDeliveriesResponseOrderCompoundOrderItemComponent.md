# TransportDeliveriesResponseOrderCompoundOrderItemComponent

Part of composite item.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product** | [**TransportDeliveriesResponseOrderProduct**](TransportDeliveriesResponseOrderProduct.md) | Item. | 
**modifiers** | [**List[TransportDeliveriesResponseOrderOrderItemModifier]**](TransportDeliveriesResponseOrderOrderItemModifier.md) | Modifiers. | [optional] 
**price** | **float** | Price per item unit. Can be sent different from the price in the base menu. | 
**cost** | **float** | Item total including tax, discounts/surcharges. | 
**price_predefined** | **bool** | Whether price is predefined. | 
**position_id** | **str** | Unique identifier of the item in the order and for the whole system. | [optional] 
**tax_percent** | **float** | Tax rate. | [optional] 
**result_sum** | **float** | Total amount per item including tax, discounts/surcharges. | [optional] 

## Example

```python
from iikocloud_client.models.transport_deliveries_response_order_compound_order_item_component import TransportDeliveriesResponseOrderCompoundOrderItemComponent

# TODO update the JSON string below
json = "{}"
# create an instance of TransportDeliveriesResponseOrderCompoundOrderItemComponent from a JSON string
transport_deliveries_response_order_compound_order_item_component_instance = TransportDeliveriesResponseOrderCompoundOrderItemComponent.from_json(json)
# print the JSON string representation of the object
print(TransportDeliveriesResponseOrderCompoundOrderItemComponent.to_json())

# convert the object into a dict
transport_deliveries_response_order_compound_order_item_component_dict = transport_deliveries_response_order_compound_order_item_component_instance.to_dict()
# create an instance of TransportDeliveriesResponseOrderCompoundOrderItemComponent from a dict
transport_deliveries_response_order_compound_order_item_component_from_dict = TransportDeliveriesResponseOrderCompoundOrderItemComponent.from_dict(transport_deliveries_response_order_compound_order_item_component_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


