# DeliveriesRequestCreateOrderDiscountCard

Discount card.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**track** | **str** | Track of discount card to be applied to order. | 

## Example

```python
from iikocloud_client.models.deliveries_request_create_order_discount_card import DeliveriesRequestCreateOrderDiscountCard

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveriesRequestCreateOrderDiscountCard from a JSON string
deliveries_request_create_order_discount_card_instance = DeliveriesRequestCreateOrderDiscountCard.from_json(json)
# print the JSON string representation of the object
print(DeliveriesRequestCreateOrderDiscountCard.to_json())

# convert the object into a dict
deliveries_request_create_order_discount_card_dict = deliveries_request_create_order_discount_card_instance.to_dict()
# create an instance of DeliveriesRequestCreateOrderDiscountCard from a dict
deliveries_request_create_order_discount_card_from_dict = DeliveriesRequestCreateOrderDiscountCard.from_dict(deliveries_request_create_order_discount_card_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


