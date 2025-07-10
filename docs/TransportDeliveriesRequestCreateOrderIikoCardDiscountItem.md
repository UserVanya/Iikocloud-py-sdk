# TransportDeliveriesRequestCreateOrderIikoCardDiscountItem

Card discount/surcharge item.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**position_id** | **str** | Position ID of order item. | 
**sum** | **float** | Discount/surcharge sum. | 
**amount** | **float** | Amount. | 

## Example

```python
from iiko_cloud_client.models.transport_deliveries_request_create_order_iiko_card_discount_item import TransportDeliveriesRequestCreateOrderIikoCardDiscountItem

# TODO update the JSON string below
json = "{}"
# create an instance of TransportDeliveriesRequestCreateOrderIikoCardDiscountItem from a JSON string
transport_deliveries_request_create_order_iiko_card_discount_item_instance = TransportDeliveriesRequestCreateOrderIikoCardDiscountItem.from_json(json)
# print the JSON string representation of the object
print(TransportDeliveriesRequestCreateOrderIikoCardDiscountItem.to_json())

# convert the object into a dict
transport_deliveries_request_create_order_iiko_card_discount_item_dict = transport_deliveries_request_create_order_iiko_card_discount_item_instance.to_dict()
# create an instance of TransportDeliveriesRequestCreateOrderIikoCardDiscountItem from a dict
transport_deliveries_request_create_order_iiko_card_discount_item_from_dict = TransportDeliveriesRequestCreateOrderIikoCardDiscountItem.from_dict(transport_deliveries_request_create_order_iiko_card_discount_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


