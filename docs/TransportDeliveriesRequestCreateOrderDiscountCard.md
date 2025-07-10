# TransportDeliveriesRequestCreateOrderDiscountCard

Discount card.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**track** | **str** | Track of discount card to be applied to order. | 

## Example

```python
from iiko_cloud_client.models.transport_deliveries_request_create_order_discount_card import TransportDeliveriesRequestCreateOrderDiscountCard

# TODO update the JSON string below
json = "{}"
# create an instance of TransportDeliveriesRequestCreateOrderDiscountCard from a JSON string
transport_deliveries_request_create_order_discount_card_instance = TransportDeliveriesRequestCreateOrderDiscountCard.from_json(json)
# print the JSON string representation of the object
print(TransportDeliveriesRequestCreateOrderDiscountCard.to_json())

# convert the object into a dict
transport_deliveries_request_create_order_discount_card_dict = transport_deliveries_request_create_order_discount_card_instance.to_dict()
# create an instance of TransportDeliveriesRequestCreateOrderDiscountCard from a dict
transport_deliveries_request_create_order_discount_card_from_dict = TransportDeliveriesRequestCreateOrderDiscountCard.from_dict(transport_deliveries_request_create_order_discount_card_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


