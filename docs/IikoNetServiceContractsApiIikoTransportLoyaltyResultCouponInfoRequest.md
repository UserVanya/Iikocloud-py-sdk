# IikoNetServiceContractsApiIikoTransportLoyaltyResultCouponInfoRequest

Coupon info request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number** | **str** | Number. Can be null. | 
**series** | **str** | Series. Can be null. | [optional] 
**organization_id** | **UUID** | Organization id. | 

## Example

```python
from iikocloud_client.models.iiko_net_service_contracts_api_iiko_transport_loyalty_result_coupon_info_request import IikoNetServiceContractsApiIikoTransportLoyaltyResultCouponInfoRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IikoNetServiceContractsApiIikoTransportLoyaltyResultCouponInfoRequest from a JSON string
iiko_net_service_contracts_api_iiko_transport_loyalty_result_coupon_info_request_instance = IikoNetServiceContractsApiIikoTransportLoyaltyResultCouponInfoRequest.from_json(json)
# print the JSON string representation of the object
print(IikoNetServiceContractsApiIikoTransportLoyaltyResultCouponInfoRequest.to_json())

# convert the object into a dict
iiko_net_service_contracts_api_iiko_transport_loyalty_result_coupon_info_request_dict = iiko_net_service_contracts_api_iiko_transport_loyalty_result_coupon_info_request_instance.to_dict()
# create an instance of IikoNetServiceContractsApiIikoTransportLoyaltyResultCouponInfoRequest from a dict
iiko_net_service_contracts_api_iiko_transport_loyalty_result_coupon_info_request_from_dict = IikoNetServiceContractsApiIikoTransportLoyaltyResultCouponInfoRequest.from_dict(iiko_net_service_contracts_api_iiko_transport_loyalty_result_coupon_info_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


