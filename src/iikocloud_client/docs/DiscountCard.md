# DiscountCard

Discount card.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**track** | **str** | Track of discount card to be applied to order. | 

## Example

```python
from iikocloud_client.models.discount_card import DiscountCard

# TODO update the JSON string below
json = "{}"
# create an instance of DiscountCard from a JSON string
discount_card_instance = DiscountCard.from_json(json)
# print the JSON string representation of the object
print(DiscountCard.to_json())

# convert the object into a dict
discount_card_dict = discount_card_instance.to_dict()
# create an instance of DiscountCard from a dict
discount_card_from_dict = DiscountCard.from_dict(discount_card_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


