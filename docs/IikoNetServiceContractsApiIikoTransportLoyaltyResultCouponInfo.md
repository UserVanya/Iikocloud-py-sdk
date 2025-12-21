# IikoNetServiceContractsApiIikoTransportLoyaltyResultCouponInfo

Coupon info.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Id. | [optional] 
**number** | **str** | Number. Can be null. | [optional] 
**series_name** | **str** | Series name. Can be null. | [optional] 
**series_id** | **UUID** | Series id. | [optional] 
**when_activated** | **str** | When activated. | [optional] 
**is_deleted** | **bool** | Is deleted. | [optional] 

## Example

```python
from iikocloud_client.models.iiko_net_service_contracts_api_iiko_transport_loyalty_result_coupon_info import IikoNetServiceContractsApiIikoTransportLoyaltyResultCouponInfo

# TODO update the JSON string below
json = "{}"
# create an instance of IikoNetServiceContractsApiIikoTransportLoyaltyResultCouponInfo from a JSON string
iiko_net_service_contracts_api_iiko_transport_loyalty_result_coupon_info_instance = IikoNetServiceContractsApiIikoTransportLoyaltyResultCouponInfo.from_json(json)
# print the JSON string representation of the object
print(IikoNetServiceContractsApiIikoTransportLoyaltyResultCouponInfo.to_json())

# convert the object into a dict
iiko_net_service_contracts_api_iiko_transport_loyalty_result_coupon_info_dict = iiko_net_service_contracts_api_iiko_transport_loyalty_result_coupon_info_instance.to_dict()
# create an instance of IikoNetServiceContractsApiIikoTransportLoyaltyResultCouponInfo from a dict
iiko_net_service_contracts_api_iiko_transport_loyalty_result_coupon_info_from_dict = IikoNetServiceContractsApiIikoTransportLoyaltyResultCouponInfo.from_dict(iiko_net_service_contracts_api_iiko_transport_loyalty_result_coupon_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


