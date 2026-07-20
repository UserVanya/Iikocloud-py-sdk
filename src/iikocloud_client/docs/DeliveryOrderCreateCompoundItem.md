# DeliveryOrderCreateCompoundItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**common_modifiers** | [**List[Modifier]**](Modifier.md) | Indivisible modifiers. | [optional] 
**primary_component** | [**DeliveryOrderCreateCompoundItemComponent**](DeliveryOrderCreateCompoundItemComponent.md) | Main component. | 
**secondary_component** | [**DeliveryOrderCreateCompoundItemComponent**](DeliveryOrderCreateCompoundItemComponent.md) | Minor component. | [optional] 

## Example

```python
from iikocloud_client.models.delivery_order_create_compound_item import DeliveryOrderCreateCompoundItem

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveryOrderCreateCompoundItem from a JSON string
delivery_order_create_compound_item_instance = DeliveryOrderCreateCompoundItem.from_json(json)
# print the JSON string representation of the object
print(DeliveryOrderCreateCompoundItem.to_json())

# convert the object into a dict
delivery_order_create_compound_item_dict = delivery_order_create_compound_item_instance.to_dict()
# create an instance of DeliveryOrderCreateCompoundItem from a dict
delivery_order_create_compound_item_from_dict = DeliveryOrderCreateCompoundItem.from_dict(delivery_order_create_compound_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


