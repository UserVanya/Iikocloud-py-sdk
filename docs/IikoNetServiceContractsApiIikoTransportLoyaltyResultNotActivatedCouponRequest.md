# IikoNetServiceContractsApiIikoTransportLoyaltyResultNotActivatedCouponRequest

Not activated coupon request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**series** | **str** | Series. Can be null. | 
**page_size** | **int** | Page size. | [optional] 
**page** | **int** | Page. | [optional] 
**organization_id** | **UUID** | Organization id. | 

## Example

```python
from iikocloud_client.models.iiko_net_service_contracts_api_iiko_transport_loyalty_result_not_activated_coupon_request import IikoNetServiceContractsApiIikoTransportLoyaltyResultNotActivatedCouponRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IikoNetServiceContractsApiIikoTransportLoyaltyResultNotActivatedCouponRequest from a JSON string
iiko_net_service_contracts_api_iiko_transport_loyalty_result_not_activated_coupon_request_instance = IikoNetServiceContractsApiIikoTransportLoyaltyResultNotActivatedCouponRequest.from_json(json)
# print the JSON string representation of the object
print(IikoNetServiceContractsApiIikoTransportLoyaltyResultNotActivatedCouponRequest.to_json())

# convert the object into a dict
iiko_net_service_contracts_api_iiko_transport_loyalty_result_not_activated_coupon_request_dict = iiko_net_service_contracts_api_iiko_transport_loyalty_result_not_activated_coupon_request_instance.to_dict()
# create an instance of IikoNetServiceContractsApiIikoTransportLoyaltyResultNotActivatedCouponRequest from a dict
iiko_net_service_contracts_api_iiko_transport_loyalty_result_not_activated_coupon_request_from_dict = IikoNetServiceContractsApiIikoTransportLoyaltyResultNotActivatedCouponRequest.from_dict(iiko_net_service_contracts_api_iiko_transport_loyalty_result_not_activated_coupon_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


