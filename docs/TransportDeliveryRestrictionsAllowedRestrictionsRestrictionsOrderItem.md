# TransportDeliveryRestrictionsAllowedRestrictionsRestrictionsOrderItem

Order item.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Product ID. | 
**product** | **str** | Product. | 
**amount** | **float** | Amount. | 
**modifiers** | [**List[TransportDeliveryRestrictionsAllowedRestrictionsRestrictionsOrderItemModifier]**](TransportDeliveryRestrictionsAllowedRestrictionsRestrictionsOrderItemModifier.md) | Modifiers (absolute amount). | [optional] 

## Example

```python
from iikocloud_client.models.transport_delivery_restrictions_allowed_restrictions_restrictions_order_item import TransportDeliveryRestrictionsAllowedRestrictionsRestrictionsOrderItem

# TODO update the JSON string below
json = "{}"
# create an instance of TransportDeliveryRestrictionsAllowedRestrictionsRestrictionsOrderItem from a JSON string
transport_delivery_restrictions_allowed_restrictions_restrictions_order_item_instance = TransportDeliveryRestrictionsAllowedRestrictionsRestrictionsOrderItem.from_json(json)
# print the JSON string representation of the object
print(TransportDeliveryRestrictionsAllowedRestrictionsRestrictionsOrderItem.to_json())

# convert the object into a dict
transport_delivery_restrictions_allowed_restrictions_restrictions_order_item_dict = transport_delivery_restrictions_allowed_restrictions_restrictions_order_item_instance.to_dict()
# create an instance of TransportDeliveryRestrictionsAllowedRestrictionsRestrictionsOrderItem from a dict
transport_delivery_restrictions_allowed_restrictions_restrictions_order_item_from_dict = TransportDeliveryRestrictionsAllowedRestrictionsRestrictionsOrderItem.from_dict(transport_delivery_restrictions_allowed_restrictions_restrictions_order_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


