# LoyaltyResultCalculateCheckinRequest

Request to calculate loyalty operations for order.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order** | [**DeliveriesRequestCreateOrderOrder**](DeliveriesRequestCreateOrderOrder.md) | Order details. | 
**coupon** | **str** | Number of applied coupon. Can be null. | [optional] 
**referrer_id** | **str** | Referrer id. | [optional] 
**terminal_group_id** | **str** | Identifier of a target terminal. Should be used only when auto distribution is off and no call center operator is available. | [optional] 
**available_payment_marketing_campaign_ids** | **List[str]** | List of identifiers of applied campaigns. Should be empty if no payment method is used. | [optional] 
**applicable_manual_conditions** | **List[str]** | List of manually applied to order conditions. | [optional] 
**dynamic_discounts** | [**List[LoyaltyResultDynamicDiscount]**](LoyaltyResultDynamicDiscount.md) | Applicable manual discounts. | [optional] 
**is_loyalty_trace_enabled** | **bool** | Loyalty trace is enabled. | [optional] 
**organization_id** | **str** | Organization id. | 

## Example

```python
from iikocloud_client.models.loyalty_result_calculate_checkin_request import LoyaltyResultCalculateCheckinRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LoyaltyResultCalculateCheckinRequest from a JSON string
loyalty_result_calculate_checkin_request_instance = LoyaltyResultCalculateCheckinRequest.from_json(json)
# print the JSON string representation of the object
print(LoyaltyResultCalculateCheckinRequest.to_json())

# convert the object into a dict
loyalty_result_calculate_checkin_request_dict = loyalty_result_calculate_checkin_request_instance.to_dict()
# create an instance of LoyaltyResultCalculateCheckinRequest from a dict
loyalty_result_calculate_checkin_request_from_dict = LoyaltyResultCalculateCheckinRequest.from_dict(loyalty_result_calculate_checkin_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


