# RestrictionsOrderItem

Order item.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | Amount. | 
**id** | **UUID** | Product ID. | 
**modifiers** | [**List[RestrictionsOrderItemModifier]**](RestrictionsOrderItemModifier.md) | Modifiers (absolute amount). | [optional] 
**product** | **str** | Product. | 

## Example

```python
from iikocloud_client.models.restrictions_order_item import RestrictionsOrderItem

# TODO update the JSON string below
json = "{}"
# create an instance of RestrictionsOrderItem from a JSON string
restrictions_order_item_instance = RestrictionsOrderItem.from_json(json)
# print the JSON string representation of the object
print(RestrictionsOrderItem.to_json())

# convert the object into a dict
restrictions_order_item_dict = restrictions_order_item_instance.to_dict()
# create an instance of RestrictionsOrderItem from a dict
restrictions_order_item_from_dict = RestrictionsOrderItem.from_dict(restrictions_order_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


