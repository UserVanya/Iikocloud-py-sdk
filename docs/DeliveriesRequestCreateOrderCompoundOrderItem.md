# DeliveriesRequestCreateOrderCompoundOrderItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**primary_component** | [**DeliveriesRequestCreateOrderCompoundOrderItemComponent**](DeliveriesRequestCreateOrderCompoundOrderItemComponent.md) | Main component. | 
**secondary_component** | [**DeliveriesRequestCreateOrderCompoundOrderItemComponent**](DeliveriesRequestCreateOrderCompoundOrderItemComponent.md) | Minor component. | [optional] 
**common_modifiers** | [**List[DeliveriesRequestCreateOrderModifier]**](DeliveriesRequestCreateOrderModifier.md) | Indivisible modifiers. | [optional] 

## Example

```python
from iikocloud_client.models.deliveries_request_create_order_compound_order_item import DeliveriesRequestCreateOrderCompoundOrderItem

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveriesRequestCreateOrderCompoundOrderItem from a JSON string
deliveries_request_create_order_compound_order_item_instance = DeliveriesRequestCreateOrderCompoundOrderItem.from_json(json)
# print the JSON string representation of the object
print(DeliveriesRequestCreateOrderCompoundOrderItem.to_json())

# convert the object into a dict
deliveries_request_create_order_compound_order_item_dict = deliveries_request_create_order_compound_order_item_instance.to_dict()
# create an instance of DeliveriesRequestCreateOrderCompoundOrderItem from a dict
deliveries_request_create_order_compound_order_item_from_dict = DeliveriesRequestCreateOrderCompoundOrderItem.from_dict(deliveries_request_create_order_compound_order_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


