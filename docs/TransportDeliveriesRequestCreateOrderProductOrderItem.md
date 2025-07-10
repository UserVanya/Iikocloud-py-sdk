# TransportDeliveriesRequestCreateOrderProductOrderItem

Order item: item.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_id** | **str** | ID of menu item.                Can be obtained by &#x60;/api/1/nomenclature&#x60; operation. | 
**modifiers** | [**List[TransportDeliveriesRequestCreateOrderModifier]**](TransportDeliveriesRequestCreateOrderModifier.md) | Modifiers. | [optional] 
**price** | **float** | Price per item unit. Can be sent different from the price in the base menu. | 
**position_id** | **str** | Unique identifier of the item in the order.  MUST be unique for the whole system. Therefore it must be generated with Guid.NewGuid().  &gt; If sent null, it generates automatically on iikoTransport side. | [optional] 

## Example

```python
from iiko_cloud_client.models.transport_deliveries_request_create_order_product_order_item import TransportDeliveriesRequestCreateOrderProductOrderItem

# TODO update the JSON string below
json = "{}"
# create an instance of TransportDeliveriesRequestCreateOrderProductOrderItem from a JSON string
transport_deliveries_request_create_order_product_order_item_instance = TransportDeliveriesRequestCreateOrderProductOrderItem.from_json(json)
# print the JSON string representation of the object
print(TransportDeliveriesRequestCreateOrderProductOrderItem.to_json())

# convert the object into a dict
transport_deliveries_request_create_order_product_order_item_dict = transport_deliveries_request_create_order_product_order_item_instance.to_dict()
# create an instance of TransportDeliveriesRequestCreateOrderProductOrderItem from a dict
transport_deliveries_request_create_order_product_order_item_from_dict = TransportDeliveriesRequestCreateOrderProductOrderItem.from_dict(transport_deliveries_request_create_order_product_order_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


