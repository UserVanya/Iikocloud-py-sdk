# TransportDeliveriesRequestCreateOrderCompoundOrderItem

Order item: composite item.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**primary_component** | [**TransportDeliveriesRequestCreateOrderCompoundOrderItemComponent**](TransportDeliveriesRequestCreateOrderCompoundOrderItemComponent.md) | Main component. | 
**secondary_component** | [**TransportDeliveriesRequestCreateOrderCompoundOrderItemComponent**](TransportDeliveriesRequestCreateOrderCompoundOrderItemComponent.md) | Minor component. | [optional] 
**common_modifiers** | [**List[TransportDeliveriesRequestCreateOrderModifier]**](TransportDeliveriesRequestCreateOrderModifier.md) | Indivisible modifiers. | [optional] 

## Example

```python
from iiko_cloud_client.models.transport_deliveries_request_create_order_compound_order_item import TransportDeliveriesRequestCreateOrderCompoundOrderItem

# TODO update the JSON string below
json = "{}"
# create an instance of TransportDeliveriesRequestCreateOrderCompoundOrderItem from a JSON string
transport_deliveries_request_create_order_compound_order_item_instance = TransportDeliveriesRequestCreateOrderCompoundOrderItem.from_json(json)
# print the JSON string representation of the object
print(TransportDeliveriesRequestCreateOrderCompoundOrderItem.to_json())

# convert the object into a dict
transport_deliveries_request_create_order_compound_order_item_dict = transport_deliveries_request_create_order_compound_order_item_instance.to_dict()
# create an instance of TransportDeliveriesRequestCreateOrderCompoundOrderItem from a dict
transport_deliveries_request_create_order_compound_order_item_from_dict = TransportDeliveriesRequestCreateOrderCompoundOrderItem.from_dict(transport_deliveries_request_create_order_compound_order_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


