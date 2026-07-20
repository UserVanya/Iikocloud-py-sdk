# CalculateCheckinRequest

Request to calculate loyalty operations for order.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applicable_manual_conditions** | **List[UUID]** | Obsolete field. Use request.Order.LoyaltyInfo.ApplicableManualConditions instead. | [optional] 
**available_payment_marketing_campaign_ids** | **List[UUID]** | List of identifiers of applied campaigns. Should be empty if no payment method is used. | [optional] 
**coupon** | **str** | Obsolete field. Use Order.LoyaltyInfo.Coupon instead. Can be null. | [optional] 
**dynamic_discounts** | [**List[LoyaltyDynamicDiscount]**](LoyaltyDynamicDiscount.md) | Obsolete field. Use Order.LoyaltyInfo.DynamicDiscounts instead. Can be null.. | [optional] 
**is_loyalty_trace_enabled** | **bool** | Loyalty trace is enabled. | [optional] 
**order** | [**DeliveryOrderCreatePayload**](DeliveryOrderCreatePayload.md) | Order. | 
**organization_id** | **UUID** | Organization id. | 
**referrer_id** | **UUID** | Referrer id. | [optional] 
**terminal_group_id** | **UUID** | Identifier of a target terminal. Should be used only when auto distribution is off and no call center operator is available. | [optional] 

## Example

```python
from iikocloud_client.models.calculate_checkin_request import CalculateCheckinRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CalculateCheckinRequest from a JSON string
calculate_checkin_request_instance = CalculateCheckinRequest.from_json(json)
# print the JSON string representation of the object
print(CalculateCheckinRequest.to_json())

# convert the object into a dict
calculate_checkin_request_dict = calculate_checkin_request_instance.to_dict()
# create an instance of CalculateCheckinRequest from a dict
calculate_checkin_request_from_dict = CalculateCheckinRequest.from_dict(calculate_checkin_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


