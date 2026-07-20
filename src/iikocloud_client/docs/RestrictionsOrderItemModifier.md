# RestrictionsOrderItemModifier

Order item modifier.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | Amount. | 
**id** | **UUID** | Product ID. | 
**product** | **str** | Product. | [optional] 

## Example

```python
from iikocloud_client.models.restrictions_order_item_modifier import RestrictionsOrderItemModifier

# TODO update the JSON string below
json = "{}"
# create an instance of RestrictionsOrderItemModifier from a JSON string
restrictions_order_item_modifier_instance = RestrictionsOrderItemModifier.from_json(json)
# print the JSON string representation of the object
print(RestrictionsOrderItemModifier.to_json())

# convert the object into a dict
restrictions_order_item_modifier_dict = restrictions_order_item_modifier_instance.to_dict()
# create an instance of RestrictionsOrderItemModifier from a dict
restrictions_order_item_modifier_from_dict = RestrictionsOrderItemModifier.from_dict(restrictions_order_item_modifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


