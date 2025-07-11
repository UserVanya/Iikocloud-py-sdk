# TransportDeliveriesRequestCreateOrderLoyaltyInfo

Information about Loyalty app.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**coupon** | **str** | Coupon No. that was considered when calculating loyalty program. | [optional] 
**applicable_manual_conditions** | **List[str]** | Information about applied manual conditions. | [optional] 

## Example

```python
from iikocloud_client.models.transport_deliveries_request_create_order_loyalty_info import TransportDeliveriesRequestCreateOrderLoyaltyInfo

# TODO update the JSON string below
json = "{}"
# create an instance of TransportDeliveriesRequestCreateOrderLoyaltyInfo from a JSON string
transport_deliveries_request_create_order_loyalty_info_instance = TransportDeliveriesRequestCreateOrderLoyaltyInfo.from_json(json)
# print the JSON string representation of the object
print(TransportDeliveriesRequestCreateOrderLoyaltyInfo.to_json())

# convert the object into a dict
transport_deliveries_request_create_order_loyalty_info_dict = transport_deliveries_request_create_order_loyalty_info_instance.to_dict()
# create an instance of TransportDeliveriesRequestCreateOrderLoyaltyInfo from a dict
transport_deliveries_request_create_order_loyalty_info_from_dict = TransportDeliveriesRequestCreateOrderLoyaltyInfo.from_dict(transport_deliveries_request_create_order_loyalty_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


