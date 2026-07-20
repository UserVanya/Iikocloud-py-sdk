# IikoCardDiscountItem

Card discount/surcharge item.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | Amount. | 
**position_id** | **UUID** | Position ID of order item. | 
**sum** | **float** | Discount/surcharge sum. | 

## Example

```python
from iikocloud_client.models.iiko_card_discount_item import IikoCardDiscountItem

# TODO update the JSON string below
json = "{}"
# create an instance of IikoCardDiscountItem from a JSON string
iiko_card_discount_item_instance = IikoCardDiscountItem.from_json(json)
# print the JSON string representation of the object
print(IikoCardDiscountItem.to_json())

# convert the object into a dict
iiko_card_discount_item_dict = iiko_card_discount_item_instance.to_dict()
# create an instance of IikoCardDiscountItem from a dict
iiko_card_discount_item_from_dict = IikoCardDiscountItem.from_dict(iiko_card_discount_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


