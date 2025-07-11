# TransportDeliveriesResponseOrderDiscountItem

Discount.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**discount_type** | [**TransportDeliveriesResponseOrderDiscountType**](TransportDeliveriesResponseOrderDiscountType.md) | Discount type.                 Can be obtained by &#x60;/api/1/discounts&#x60; operation. | 
**sum** | **float** | Total. | 
**selective_positions** | **List[str]** | Order item positions. | [optional] 
**selective_positions_with_sum** | [**List[TransportDeliveriesResponseOrderPositionWithSum]**](TransportDeliveriesResponseOrderPositionWithSum.md) | Order item positions with position discount sum.   &gt; Allowed from version &#x60;8.5.6&#x60;. | [optional] 

## Example

```python
from iikocloud_client.models.transport_deliveries_response_order_discount_item import TransportDeliveriesResponseOrderDiscountItem

# TODO update the JSON string below
json = "{}"
# create an instance of TransportDeliveriesResponseOrderDiscountItem from a JSON string
transport_deliveries_response_order_discount_item_instance = TransportDeliveriesResponseOrderDiscountItem.from_json(json)
# print the JSON string representation of the object
print(TransportDeliveriesResponseOrderDiscountItem.to_json())

# convert the object into a dict
transport_deliveries_response_order_discount_item_dict = transport_deliveries_response_order_discount_item_instance.to_dict()
# create an instance of TransportDeliveriesResponseOrderDiscountItem from a dict
transport_deliveries_response_order_discount_item_from_dict = TransportDeliveriesResponseOrderDiscountItem.from_dict(transport_deliveries_response_order_discount_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


