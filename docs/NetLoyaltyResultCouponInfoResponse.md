# NetLoyaltyResultCouponInfoResponse

Coupon info response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**coupon_info** | [**List[NetLoyaltyResultCouponInfo]**](NetLoyaltyResultCouponInfo.md) | Coupon info. | [optional] 

## Example

```python
from iiko_cloud_client.models.net_loyalty_result_coupon_info_response import NetLoyaltyResultCouponInfoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NetLoyaltyResultCouponInfoResponse from a JSON string
net_loyalty_result_coupon_info_response_instance = NetLoyaltyResultCouponInfoResponse.from_json(json)
# print the JSON string representation of the object
print(NetLoyaltyResultCouponInfoResponse.to_json())

# convert the object into a dict
net_loyalty_result_coupon_info_response_dict = net_loyalty_result_coupon_info_response_instance.to_dict()
# create an instance of NetLoyaltyResultCouponInfoResponse from a dict
net_loyalty_result_coupon_info_response_from_dict = NetLoyaltyResultCouponInfoResponse.from_dict(net_loyalty_result_coupon_info_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


