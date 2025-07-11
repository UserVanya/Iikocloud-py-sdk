# NetLoyaltyResultNotActivatedCouponResponse

Not activated coupon response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**not_activated_coupon** | [**List[NetLoyaltyResultNotActivatedCoupon]**](NetLoyaltyResultNotActivatedCoupon.md) | Not activated coupon. | [optional] 

## Example

```python
from iikocloud_client.models.net_loyalty_result_not_activated_coupon_response import NetLoyaltyResultNotActivatedCouponResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NetLoyaltyResultNotActivatedCouponResponse from a JSON string
net_loyalty_result_not_activated_coupon_response_instance = NetLoyaltyResultNotActivatedCouponResponse.from_json(json)
# print the JSON string representation of the object
print(NetLoyaltyResultNotActivatedCouponResponse.to_json())

# convert the object into a dict
net_loyalty_result_not_activated_coupon_response_dict = net_loyalty_result_not_activated_coupon_response_instance.to_dict()
# create an instance of NetLoyaltyResultNotActivatedCouponResponse from a dict
net_loyalty_result_not_activated_coupon_response_from_dict = NetLoyaltyResultNotActivatedCouponResponse.from_dict(net_loyalty_result_not_activated_coupon_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


