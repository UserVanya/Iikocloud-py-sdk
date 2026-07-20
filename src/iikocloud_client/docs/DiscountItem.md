# DiscountItem

Discount.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**discount_type** | [**DiscountType**](DiscountType.md) | Discount type.                 Can be obtained by &#x60;/api/1/discounts&#x60; operation. | 
**selective_positions** | **List[UUID]** | Order item positions. | [optional] 
**selective_positions_with_sum** | [**List[PositionWithSum]**](PositionWithSum.md) | Order item positions with position discount sum.   &gt; Allowed from version &#x60;8.5.6&#x60;. | [optional] 
**sum** | **float** | Total. | 

## Example

```python
from iikocloud_client.models.discount_item import DiscountItem

# TODO update the JSON string below
json = "{}"
# create an instance of DiscountItem from a JSON string
discount_item_instance = DiscountItem.from_json(json)
# print the JSON string representation of the object
print(DiscountItem.to_json())

# convert the object into a dict
discount_item_dict = discount_item_instance.to_dict()
# create an instance of DiscountItem from a dict
discount_item_from_dict = DiscountItem.from_dict(discount_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


