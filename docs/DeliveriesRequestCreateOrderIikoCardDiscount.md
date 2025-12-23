# DeliveriesRequestCreateOrderIikoCardDiscount

Card discount/surcharge.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**program_id** | **str** | Card program ID. | 
**program_name** | **str** | Card program name. | 
**discount_items** | [**List[DeliveriesRequestCreateOrderIikoCardDiscountItem]**](DeliveriesRequestCreateOrderIikoCardDiscountItem.md) | Discount information for order items. | 

## Example

```python
from iikocloud_client.models.deliveries_request_create_order_iiko_card_discount import DeliveriesRequestCreateOrderIikoCardDiscount

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveriesRequestCreateOrderIikoCardDiscount from a JSON string
deliveries_request_create_order_iiko_card_discount_instance = DeliveriesRequestCreateOrderIikoCardDiscount.from_json(json)
# print the JSON string representation of the object
print(DeliveriesRequestCreateOrderIikoCardDiscount.to_json())

# convert the object into a dict
deliveries_request_create_order_iiko_card_discount_dict = deliveries_request_create_order_iiko_card_discount_instance.to_dict()
# create an instance of DeliveriesRequestCreateOrderIikoCardDiscount from a dict
deliveries_request_create_order_iiko_card_discount_from_dict = DeliveriesRequestCreateOrderIikoCardDiscount.from_dict(deliveries_request_create_order_iiko_card_discount_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


