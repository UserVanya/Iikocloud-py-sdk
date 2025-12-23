# DeliveryRestrictionsAllowedRestrictionsRestrictionsOrderItemModifier

Order item modifier.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Product ID. | 
**product** | **str** | Product. | [optional] 
**amount** | **float** | Amount. | 

## Example

```python
from iikocloud_client.models.delivery_restrictions_allowed_restrictions_restrictions_order_item_modifier import DeliveryRestrictionsAllowedRestrictionsRestrictionsOrderItemModifier

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveryRestrictionsAllowedRestrictionsRestrictionsOrderItemModifier from a JSON string
delivery_restrictions_allowed_restrictions_restrictions_order_item_modifier_instance = DeliveryRestrictionsAllowedRestrictionsRestrictionsOrderItemModifier.from_json(json)
# print the JSON string representation of the object
print(DeliveryRestrictionsAllowedRestrictionsRestrictionsOrderItemModifier.to_json())

# convert the object into a dict
delivery_restrictions_allowed_restrictions_restrictions_order_item_modifier_dict = delivery_restrictions_allowed_restrictions_restrictions_order_item_modifier_instance.to_dict()
# create an instance of DeliveryRestrictionsAllowedRestrictionsRestrictionsOrderItemModifier from a dict
delivery_restrictions_allowed_restrictions_restrictions_order_item_modifier_from_dict = DeliveryRestrictionsAllowedRestrictionsRestrictionsOrderItemModifier.from_dict(delivery_restrictions_allowed_restrictions_restrictions_order_item_modifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


