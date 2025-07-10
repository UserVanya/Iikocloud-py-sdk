# TransportDeliveriesRequestCreateOrderIikoCardDiscount

Card discount/surcharge.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**program_id** | **str** | Card program ID. | 
**program_name** | **str** | Card program name. | 
**discount_items** | [**List[TransportDeliveriesRequestCreateOrderIikoCardDiscountItem]**](TransportDeliveriesRequestCreateOrderIikoCardDiscountItem.md) | Discount information for order items. | 

## Example

```python
from iiko_cloud_client.models.transport_deliveries_request_create_order_iiko_card_discount import TransportDeliveriesRequestCreateOrderIikoCardDiscount

# TODO update the JSON string below
json = "{}"
# create an instance of TransportDeliveriesRequestCreateOrderIikoCardDiscount from a JSON string
transport_deliveries_request_create_order_iiko_card_discount_instance = TransportDeliveriesRequestCreateOrderIikoCardDiscount.from_json(json)
# print the JSON string representation of the object
print(TransportDeliveriesRequestCreateOrderIikoCardDiscount.to_json())

# convert the object into a dict
transport_deliveries_request_create_order_iiko_card_discount_dict = transport_deliveries_request_create_order_iiko_card_discount_instance.to_dict()
# create an instance of TransportDeliveriesRequestCreateOrderIikoCardDiscount from a dict
transport_deliveries_request_create_order_iiko_card_discount_from_dict = TransportDeliveriesRequestCreateOrderIikoCardDiscount.from_dict(transport_deliveries_request_create_order_iiko_card_discount_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


