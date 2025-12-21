# IikoTransportPublicApiContractsDeliveriesRequestCreateOrderLoyaltyInfo

Information about Loyalty app.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**coupon** | **str** | Coupon No. that was considered when calculating loyalty program. | [optional] 
**applicable_manual_conditions** | **List[UUID]** | Information about applied manual conditions. | [optional] 
**dynamic_discounts** | [**List[IikoTransportPublicApiContractsDeliveriesRequestCreateOrderDynamicDiscount]**](IikoTransportPublicApiContractsDeliveriesRequestCreateOrderDynamicDiscount.md) | Dynamic discounts.   &gt; Allowed from version &#x60;9.4.6&#x60;. | [optional] 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_deliveries_request_create_order_loyalty_info import IikoTransportPublicApiContractsDeliveriesRequestCreateOrderLoyaltyInfo

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsDeliveriesRequestCreateOrderLoyaltyInfo from a JSON string
iiko_transport_public_api_contracts_deliveries_request_create_order_loyalty_info_instance = IikoTransportPublicApiContractsDeliveriesRequestCreateOrderLoyaltyInfo.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsDeliveriesRequestCreateOrderLoyaltyInfo.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_deliveries_request_create_order_loyalty_info_dict = iiko_transport_public_api_contracts_deliveries_request_create_order_loyalty_info_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsDeliveriesRequestCreateOrderLoyaltyInfo from a dict
iiko_transport_public_api_contracts_deliveries_request_create_order_loyalty_info_from_dict = IikoTransportPublicApiContractsDeliveriesRequestCreateOrderLoyaltyInfo.from_dict(iiko_transport_public_api_contracts_deliveries_request_create_order_loyalty_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


