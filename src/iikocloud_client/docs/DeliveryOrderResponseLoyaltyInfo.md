# DeliveryOrderResponseLoyaltyInfo

Information about Loyalty app.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applied_manual_conditions** | **List[UUID]** | Information about applied manual conditions. | [optional] 
**coupon** | **str** | Coupon No. that was considered when calculating loyalty program. | [optional] 
**dynamic_discounts** | [**List[DeliveryOrderResponseDynamicDiscount]**](DeliveryOrderResponseDynamicDiscount.md) | Dynamic discounts.   &gt; Allowed from version &#x60;9.4.6&#x60;. | [optional] 

## Example

```python
from iikocloud_client.models.delivery_order_response_loyalty_info import DeliveryOrderResponseLoyaltyInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveryOrderResponseLoyaltyInfo from a JSON string
delivery_order_response_loyalty_info_instance = DeliveryOrderResponseLoyaltyInfo.from_json(json)
# print the JSON string representation of the object
print(DeliveryOrderResponseLoyaltyInfo.to_json())

# convert the object into a dict
delivery_order_response_loyalty_info_dict = delivery_order_response_loyalty_info_instance.to_dict()
# create an instance of DeliveryOrderResponseLoyaltyInfo from a dict
delivery_order_response_loyalty_info_from_dict = DeliveryOrderResponseLoyaltyInfo.from_dict(delivery_order_response_loyalty_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


