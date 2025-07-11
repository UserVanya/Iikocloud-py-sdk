# TransportDeliveriesRequestCreateOrderCompoundOrderItemComponent

Item component

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_id** | **str** | Item ID. | 
**modifiers** | [**List[TransportDeliveriesRequestCreateOrderModifier]**](TransportDeliveriesRequestCreateOrderModifier.md) | Modifiers. | [optional] 
**price** | **float** | Price. | [optional] 
**position_id** | **str** | Unique identifier of the item in the order.  MUST be unique for the whole system. Therefore it must be generated with Guid.NewGuid().  &gt; If sent null, it generates automatically on iikoTransport side. | [optional] 

## Example

```python
from iikocloud_client.models.transport_deliveries_request_create_order_compound_order_item_component import TransportDeliveriesRequestCreateOrderCompoundOrderItemComponent

# TODO update the JSON string below
json = "{}"
# create an instance of TransportDeliveriesRequestCreateOrderCompoundOrderItemComponent from a JSON string
transport_deliveries_request_create_order_compound_order_item_component_instance = TransportDeliveriesRequestCreateOrderCompoundOrderItemComponent.from_json(json)
# print the JSON string representation of the object
print(TransportDeliveriesRequestCreateOrderCompoundOrderItemComponent.to_json())

# convert the object into a dict
transport_deliveries_request_create_order_compound_order_item_component_dict = transport_deliveries_request_create_order_compound_order_item_component_instance.to_dict()
# create an instance of TransportDeliveriesRequestCreateOrderCompoundOrderItemComponent from a dict
transport_deliveries_request_create_order_compound_order_item_component_from_dict = TransportDeliveriesRequestCreateOrderCompoundOrderItemComponent.from_dict(transport_deliveries_request_create_order_compound_order_item_component_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


