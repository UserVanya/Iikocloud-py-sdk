# DeliveriesRequestCreateOrderIikoCardDiscountItem

Card discount/surcharge item.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**position_id** | **UUID** | Position ID of order item. | 
**sum** | **float** | Discount/surcharge sum. | 
**amount** | **float** | Amount. | 

## Example

```python
from iikocloud_client.models.deliveries_request_create_order_iiko_card_discount_item import DeliveriesRequestCreateOrderIikoCardDiscountItem

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveriesRequestCreateOrderIikoCardDiscountItem from a JSON string
deliveries_request_create_order_iiko_card_discount_item_instance = DeliveriesRequestCreateOrderIikoCardDiscountItem.from_json(json)
# print the JSON string representation of the object
print(DeliveriesRequestCreateOrderIikoCardDiscountItem.to_json())

# convert the object into a dict
deliveries_request_create_order_iiko_card_discount_item_dict = deliveries_request_create_order_iiko_card_discount_item_instance.to_dict()
# create an instance of DeliveriesRequestCreateOrderIikoCardDiscountItem from a dict
deliveries_request_create_order_iiko_card_discount_item_from_dict = DeliveriesRequestCreateOrderIikoCardDiscountItem.from_dict(deliveries_request_create_order_iiko_card_discount_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


