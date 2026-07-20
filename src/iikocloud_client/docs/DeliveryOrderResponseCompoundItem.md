# DeliveryOrderResponseCompoundItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**common_modifiers** | [**List[OrderItemModifier]**](OrderItemModifier.md) | Indivisible modifiers. | [optional] 
**primary_component** | [**DeliveryOrderResponseCompoundItemComponent**](DeliveryOrderResponseCompoundItemComponent.md) | Main component. | 
**secondary_component** | [**DeliveryOrderResponseCompoundItemComponent**](DeliveryOrderResponseCompoundItemComponent.md) | Additional component. | [optional] 
**template** | [**CompoundItemTemplate**](CompoundItemTemplate.md) | Modifier scheme. | [optional] 

## Example

```python
from iikocloud_client.models.delivery_order_response_compound_item import DeliveryOrderResponseCompoundItem

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveryOrderResponseCompoundItem from a JSON string
delivery_order_response_compound_item_instance = DeliveryOrderResponseCompoundItem.from_json(json)
# print the JSON string representation of the object
print(DeliveryOrderResponseCompoundItem.to_json())

# convert the object into a dict
delivery_order_response_compound_item_dict = delivery_order_response_compound_item_instance.to_dict()
# create an instance of DeliveryOrderResponseCompoundItem from a dict
delivery_order_response_compound_item_from_dict = DeliveryOrderResponseCompoundItem.from_dict(delivery_order_response_compound_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


