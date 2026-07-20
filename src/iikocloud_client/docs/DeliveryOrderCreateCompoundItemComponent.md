# DeliveryOrderCreateCompoundItemComponent

Item component

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**modifiers** | [**List[Modifier]**](Modifier.md) | Modifiers. | [optional] 
**position_id** | **UUID** | Unique identifier of the item in the order.  MUST be unique for the whole system. Therefore it must be generated with Guid.NewGuid().  &gt; If sent null, it generates automatically on iikoTransport side. | [optional] 
**price** | **float** | Price. | [optional] 
**product_id** | **UUID** | Item ID. | 

## Example

```python
from iikocloud_client.models.delivery_order_create_compound_item_component import DeliveryOrderCreateCompoundItemComponent

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveryOrderCreateCompoundItemComponent from a JSON string
delivery_order_create_compound_item_component_instance = DeliveryOrderCreateCompoundItemComponent.from_json(json)
# print the JSON string representation of the object
print(DeliveryOrderCreateCompoundItemComponent.to_json())

# convert the object into a dict
delivery_order_create_compound_item_component_dict = delivery_order_create_compound_item_component_instance.to_dict()
# create an instance of DeliveryOrderCreateCompoundItemComponent from a dict
delivery_order_create_compound_item_component_from_dict = DeliveryOrderCreateCompoundItemComponent.from_dict(delivery_order_create_compound_item_component_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


