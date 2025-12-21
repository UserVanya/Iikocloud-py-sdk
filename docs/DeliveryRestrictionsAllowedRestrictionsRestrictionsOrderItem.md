# DeliveryRestrictionsAllowedRestrictionsRestrictionsOrderItem

Order item.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Product ID. | 
**product** | **str** | Product. | 
**amount** | **float** | Amount. | 
**modifiers** | [**List[DeliveryRestrictionsAllowedRestrictionsRestrictionsOrderItemModifier]**](DeliveryRestrictionsAllowedRestrictionsRestrictionsOrderItemModifier.md) | Modifiers (absolute amount). | [optional] 

## Example

```python
from iikocloud_client.models.delivery_restrictions_allowed_restrictions_restrictions_order_item import DeliveryRestrictionsAllowedRestrictionsRestrictionsOrderItem

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveryRestrictionsAllowedRestrictionsRestrictionsOrderItem from a JSON string
delivery_restrictions_allowed_restrictions_restrictions_order_item_instance = DeliveryRestrictionsAllowedRestrictionsRestrictionsOrderItem.from_json(json)
# print the JSON string representation of the object
print(DeliveryRestrictionsAllowedRestrictionsRestrictionsOrderItem.to_json())

# convert the object into a dict
delivery_restrictions_allowed_restrictions_restrictions_order_item_dict = delivery_restrictions_allowed_restrictions_restrictions_order_item_instance.to_dict()
# create an instance of DeliveryRestrictionsAllowedRestrictionsRestrictionsOrderItem from a dict
delivery_restrictions_allowed_restrictions_restrictions_order_item_from_dict = DeliveryRestrictionsAllowedRestrictionsRestrictionsOrderItem.from_dict(delivery_restrictions_allowed_restrictions_restrictions_order_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


