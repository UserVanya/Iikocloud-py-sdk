# DeliveriesResponseOrderDiscountItem

Discount.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**discount_type** | [**DeliveriesResponseOrderDiscountType**](DeliveriesResponseOrderDiscountType.md) | Discount type.                 Can be obtained by &#x60;/api/1/discounts&#x60; operation. | 
**sum** | **float** | Total. | 
**selective_positions** | **List[UUID]** | Order item positions. | [optional] 
**selective_positions_with_sum** | [**List[DeliveriesResponseOrderPositionWithSum]**](DeliveriesResponseOrderPositionWithSum.md) | Order item positions with position discount sum.   &gt; Allowed from version &#x60;8.5.6&#x60;. | [optional] 

## Example

```python
from iikocloud_client.models.deliveries_response_order_discount_item import DeliveriesResponseOrderDiscountItem

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveriesResponseOrderDiscountItem from a JSON string
deliveries_response_order_discount_item_instance = DeliveriesResponseOrderDiscountItem.from_json(json)
# print the JSON string representation of the object
print(DeliveriesResponseOrderDiscountItem.to_json())

# convert the object into a dict
deliveries_response_order_discount_item_dict = deliveries_response_order_discount_item_instance.to_dict()
# create an instance of DeliveriesResponseOrderDiscountItem from a dict
deliveries_response_order_discount_item_from_dict = DeliveriesResponseOrderDiscountItem.from_dict(deliveries_response_order_discount_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


