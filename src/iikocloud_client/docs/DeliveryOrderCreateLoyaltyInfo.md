# DeliveryOrderCreateLoyaltyInfo

Information about Loyalty app.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applicable_manual_conditions** | **List[UUID]** | Information about applied manual conditions. | [optional] 
**coupon** | **str** | Coupon No. that was considered when calculating loyalty program. | [optional] 
**dynamic_discounts** | [**List[DeliveryOrderCreateDynamicDiscount]**](DeliveryOrderCreateDynamicDiscount.md) | Dynamic discounts.   &gt; Allowed from version &#x60;9.4.6&#x60;. | [optional] 

## Example

```python
from iikocloud_client.models.delivery_order_create_loyalty_info import DeliveryOrderCreateLoyaltyInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveryOrderCreateLoyaltyInfo from a JSON string
delivery_order_create_loyalty_info_instance = DeliveryOrderCreateLoyaltyInfo.from_json(json)
# print the JSON string representation of the object
print(DeliveryOrderCreateLoyaltyInfo.to_json())

# convert the object into a dict
delivery_order_create_loyalty_info_dict = delivery_order_create_loyalty_info_instance.to_dict()
# create an instance of DeliveryOrderCreateLoyaltyInfo from a dict
delivery_order_create_loyalty_info_from_dict = DeliveryOrderCreateLoyaltyInfo.from_dict(delivery_order_create_loyalty_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


