# DeliveriesRequestCreateOrderCompoundOrderItemComponent

Item component

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_id** | **UUID** | Item ID. | 
**modifiers** | [**List[DeliveriesRequestCreateOrderModifier]**](DeliveriesRequestCreateOrderModifier.md) | Modifiers. | [optional] 
**price** | **float** | Price. | [optional] 
**position_id** | **UUID** | Unique identifier of the item in the order.  MUST be unique for the whole system. Therefore it must be generated with Guid.NewGuid().  &gt; If sent null, it generates automatically on iikoTransport side. | [optional] 

## Example

```python
from iikocloud_client.models.deliveries_request_create_order_compound_order_item_component import DeliveriesRequestCreateOrderCompoundOrderItemComponent

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveriesRequestCreateOrderCompoundOrderItemComponent from a JSON string
deliveries_request_create_order_compound_order_item_component_instance = DeliveriesRequestCreateOrderCompoundOrderItemComponent.from_json(json)
# print the JSON string representation of the object
print(DeliveriesRequestCreateOrderCompoundOrderItemComponent.to_json())

# convert the object into a dict
deliveries_request_create_order_compound_order_item_component_dict = deliveries_request_create_order_compound_order_item_component_instance.to_dict()
# create an instance of DeliveriesRequestCreateOrderCompoundOrderItemComponent from a dict
deliveries_request_create_order_compound_order_item_component_from_dict = DeliveriesRequestCreateOrderCompoundOrderItemComponent.from_dict(deliveries_request_create_order_compound_order_item_component_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


