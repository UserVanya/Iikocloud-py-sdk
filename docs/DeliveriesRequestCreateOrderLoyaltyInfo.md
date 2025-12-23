# DeliveriesRequestCreateOrderLoyaltyInfo

Information about Loyalty app.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**coupon** | **str** | Coupon No. that was considered when calculating loyalty program. | [optional] 
**applicable_manual_conditions** | **List[str]** | Information about applied manual conditions. | [optional] 
**dynamic_discounts** | [**List[DeliveriesRequestCreateOrderDynamicDiscount]**](DeliveriesRequestCreateOrderDynamicDiscount.md) | Dynamic discounts.   &gt; Allowed from version &#x60;9.4.6&#x60;. | [optional] 

## Example

```python
from iikocloud_client.models.deliveries_request_create_order_loyalty_info import DeliveriesRequestCreateOrderLoyaltyInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveriesRequestCreateOrderLoyaltyInfo from a JSON string
deliveries_request_create_order_loyalty_info_instance = DeliveriesRequestCreateOrderLoyaltyInfo.from_json(json)
# print the JSON string representation of the object
print(DeliveriesRequestCreateOrderLoyaltyInfo.to_json())

# convert the object into a dict
deliveries_request_create_order_loyalty_info_dict = deliveries_request_create_order_loyalty_info_instance.to_dict()
# create an instance of DeliveriesRequestCreateOrderLoyaltyInfo from a dict
deliveries_request_create_order_loyalty_info_from_dict = DeliveriesRequestCreateOrderLoyaltyInfo.from_dict(deliveries_request_create_order_loyalty_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


