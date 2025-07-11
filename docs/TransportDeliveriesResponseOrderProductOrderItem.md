# TransportDeliveriesResponseOrderProductOrderItem

Order item: item.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product** | [**TransportDeliveriesResponseOrderProduct**](TransportDeliveriesResponseOrderProduct.md) | Item. | 
**modifiers** | [**List[TransportDeliveriesResponseOrderOrderItemModifier]**](TransportDeliveriesResponseOrderOrderItemModifier.md) | Modifiers. | [optional] 
**price** | **float** | Price per item unit. Can be sent different from the price in the base menu. | 
**cost** | **float** | Total cost per item without tax, discounts/surcharges. | 
**price_predefined** | **bool** | Whether price is predefined. | 
**position_id** | **str** | Unique identifier of the item in the order and for the whole system. | [optional] 
**tax_percent** | **float** | Tax rate. | [optional] 
**result_sum** | **float** | Total amount per item including tax, discounts/surcharges. | [optional] 

## Example

```python
from iikocloud_client.models.transport_deliveries_response_order_product_order_item import TransportDeliveriesResponseOrderProductOrderItem

# TODO update the JSON string below
json = "{}"
# create an instance of TransportDeliveriesResponseOrderProductOrderItem from a JSON string
transport_deliveries_response_order_product_order_item_instance = TransportDeliveriesResponseOrderProductOrderItem.from_json(json)
# print the JSON string representation of the object
print(TransportDeliveriesResponseOrderProductOrderItem.to_json())

# convert the object into a dict
transport_deliveries_response_order_product_order_item_dict = transport_deliveries_response_order_product_order_item_instance.to_dict()
# create an instance of TransportDeliveriesResponseOrderProductOrderItem from a dict
transport_deliveries_response_order_product_order_item_from_dict = TransportDeliveriesResponseOrderProductOrderItem.from_dict(transport_deliveries_response_order_product_order_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


