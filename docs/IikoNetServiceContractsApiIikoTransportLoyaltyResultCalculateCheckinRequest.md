# IikoNetServiceContractsApiIikoTransportLoyaltyResultCalculateCheckinRequest

Request to calculate loyalty operations for order.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order** | [**IikoTransportPublicApiContractsDeliveriesRequestCreateOrderOrder**](IikoTransportPublicApiContractsDeliveriesRequestCreateOrderOrder.md) | Order details. | 
**coupon** | **str** | Number of applied coupon. Can be null. | [optional] 
**referrer_id** | **UUID** | Referrer id. | [optional] 
**terminal_group_id** | **UUID** | Identifier of a target terminal. Should be used only when auto distribution is off and no call center operator is available. | [optional] 
**available_payment_marketing_campaign_ids** | **List[UUID]** | List of identifiers of applied campaigns. Should be empty if no payment method is used. | [optional] 
**applicable_manual_conditions** | **List[UUID]** | List of manually applied to order conditions. | [optional] 
**dynamic_discounts** | [**List[IikoNetServiceContractsApiIikoTransportLoyaltyResultDynamicDiscount]**](IikoNetServiceContractsApiIikoTransportLoyaltyResultDynamicDiscount.md) | Applicable manual discounts. | [optional] 
**is_loyalty_trace_enabled** | **bool** | Loyalty trace is enabled. | [optional] 
**organization_id** | **UUID** | Organization id. | 

## Example

```python
from iikocloud_client.models.iiko_net_service_contracts_api_iiko_transport_loyalty_result_calculate_checkin_request import IikoNetServiceContractsApiIikoTransportLoyaltyResultCalculateCheckinRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IikoNetServiceContractsApiIikoTransportLoyaltyResultCalculateCheckinRequest from a JSON string
iiko_net_service_contracts_api_iiko_transport_loyalty_result_calculate_checkin_request_instance = IikoNetServiceContractsApiIikoTransportLoyaltyResultCalculateCheckinRequest.from_json(json)
# print the JSON string representation of the object
print(IikoNetServiceContractsApiIikoTransportLoyaltyResultCalculateCheckinRequest.to_json())

# convert the object into a dict
iiko_net_service_contracts_api_iiko_transport_loyalty_result_calculate_checkin_request_dict = iiko_net_service_contracts_api_iiko_transport_loyalty_result_calculate_checkin_request_instance.to_dict()
# create an instance of IikoNetServiceContractsApiIikoTransportLoyaltyResultCalculateCheckinRequest from a dict
iiko_net_service_contracts_api_iiko_transport_loyalty_result_calculate_checkin_request_from_dict = IikoNetServiceContractsApiIikoTransportLoyaltyResultCalculateCheckinRequest.from_dict(iiko_net_service_contracts_api_iiko_transport_loyalty_result_calculate_checkin_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


