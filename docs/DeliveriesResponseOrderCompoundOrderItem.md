# DeliveriesResponseOrderCompoundOrderItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**primary_component** | [**DeliveriesResponseOrderCompoundOrderItemComponent**](DeliveriesResponseOrderCompoundOrderItemComponent.md) | Main component. | 
**secondary_component** | [**DeliveriesResponseOrderCompoundOrderItemComponent**](DeliveriesResponseOrderCompoundOrderItemComponent.md) | Additional component. | [optional] 
**common_modifiers** | [**List[DeliveriesResponseOrderOrderItemModifier]**](DeliveriesResponseOrderOrderItemModifier.md) | Indivisible modifiers. | [optional] 
**template** | [**DeliveriesResponseOrderCompoundItemTemplate**](DeliveriesResponseOrderCompoundItemTemplate.md) | Modifier scheme. | [optional] 

## Example

```python
from iikocloud_client.models.deliveries_response_order_compound_order_item import DeliveriesResponseOrderCompoundOrderItem

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveriesResponseOrderCompoundOrderItem from a JSON string
deliveries_response_order_compound_order_item_instance = DeliveriesResponseOrderCompoundOrderItem.from_json(json)
# print the JSON string representation of the object
print(DeliveriesResponseOrderCompoundOrderItem.to_json())

# convert the object into a dict
deliveries_response_order_compound_order_item_dict = deliveries_response_order_compound_order_item_instance.to_dict()
# create an instance of DeliveriesResponseOrderCompoundOrderItem from a dict
deliveries_response_order_compound_order_item_from_dict = DeliveriesResponseOrderCompoundOrderItem.from_dict(deliveries_response_order_compound_order_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


