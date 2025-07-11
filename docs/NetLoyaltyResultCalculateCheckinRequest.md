# NetLoyaltyResultCalculateCheckinRequest

Request to calculate loyalty operations for order.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order** | [**TransportDeliveriesRequestCreateOrderOrder**](TransportDeliveriesRequestCreateOrderOrder.md) | Order. | 
**coupon** | **str** | Number of applied coupon. Can be null. | [optional] 
**referrer_id** | **str** | Referrer id. | [optional] 
**terminal_group_id** | **str** | Identifier of a target terminal. Should be used only when auto distribution is off and no call center operator is available. | [optional] 
**available_payment_marketing_campaign_ids** | **List[str]** | List of identifiers of applied campaigns. Should be empty if no payment method is used. | [optional] 
**applicable_manual_conditions** | **List[str]** | List of manually applied to order conditions. | [optional] 
**dynamic_discounts** | [**List[NetLoyaltyResultDynamicDiscount]**](NetLoyaltyResultDynamicDiscount.md) | Applicable manual discounts. | [optional] 
**is_loyalty_trace_enabled** | **bool** | Loyalty trace is enabled. | [optional] 
**organization_id** | **str** | Organization id. | 

## Example

```python
from iikocloud_client.models.net_loyalty_result_calculate_checkin_request import NetLoyaltyResultCalculateCheckinRequest

# TODO update the JSON string below
json = "{}"
# create an instance of NetLoyaltyResultCalculateCheckinRequest from a JSON string
net_loyalty_result_calculate_checkin_request_instance = NetLoyaltyResultCalculateCheckinRequest.from_json(json)
# print the JSON string representation of the object
print(NetLoyaltyResultCalculateCheckinRequest.to_json())

# convert the object into a dict
net_loyalty_result_calculate_checkin_request_dict = net_loyalty_result_calculate_checkin_request_instance.to_dict()
# create an instance of NetLoyaltyResultCalculateCheckinRequest from a dict
net_loyalty_result_calculate_checkin_request_from_dict = NetLoyaltyResultCalculateCheckinRequest.from_dict(net_loyalty_result_calculate_checkin_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


