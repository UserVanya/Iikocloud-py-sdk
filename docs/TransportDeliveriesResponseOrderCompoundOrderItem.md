# TransportDeliveriesResponseOrderCompoundOrderItem

Order item: composite item.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**primary_component** | [**TransportDeliveriesResponseOrderCompoundOrderItemComponent**](TransportDeliveriesResponseOrderCompoundOrderItemComponent.md) | Main component. | 
**secondary_component** | [**TransportDeliveriesResponseOrderCompoundOrderItemComponent**](TransportDeliveriesResponseOrderCompoundOrderItemComponent.md) | Additional component. | [optional] 
**common_modifiers** | [**List[TransportDeliveriesResponseOrderOrderItemModifier]**](TransportDeliveriesResponseOrderOrderItemModifier.md) | Indivisible modifiers. | [optional] 
**template** | [**TransportDeliveriesResponseOrderCompoundItemTemplate**](TransportDeliveriesResponseOrderCompoundItemTemplate.md) | Modifier scheme. | [optional] 

## Example

```python
from iiko_cloud_client.models.transport_deliveries_response_order_compound_order_item import TransportDeliveriesResponseOrderCompoundOrderItem

# TODO update the JSON string below
json = "{}"
# create an instance of TransportDeliveriesResponseOrderCompoundOrderItem from a JSON string
transport_deliveries_response_order_compound_order_item_instance = TransportDeliveriesResponseOrderCompoundOrderItem.from_json(json)
# print the JSON string representation of the object
print(TransportDeliveriesResponseOrderCompoundOrderItem.to_json())

# convert the object into a dict
transport_deliveries_response_order_compound_order_item_dict = transport_deliveries_response_order_compound_order_item_instance.to_dict()
# create an instance of TransportDeliveriesResponseOrderCompoundOrderItem from a dict
transport_deliveries_response_order_compound_order_item_from_dict = TransportDeliveriesResponseOrderCompoundOrderItem.from_dict(transport_deliveries_response_order_compound_order_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


