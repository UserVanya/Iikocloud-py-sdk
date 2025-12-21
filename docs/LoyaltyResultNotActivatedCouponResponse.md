# LoyaltyResultNotActivatedCouponResponse

Not activated coupon response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**not_activated_coupon** | [**List[LoyaltyResultNotActivatedCoupon]**](LoyaltyResultNotActivatedCoupon.md) | Not activated coupon. | [optional] 

## Example

```python
from iikocloud_client.models.loyalty_result_not_activated_coupon_response import LoyaltyResultNotActivatedCouponResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LoyaltyResultNotActivatedCouponResponse from a JSON string
loyalty_result_not_activated_coupon_response_instance = LoyaltyResultNotActivatedCouponResponse.from_json(json)
# print the JSON string representation of the object
print(LoyaltyResultNotActivatedCouponResponse.to_json())

# convert the object into a dict
loyalty_result_not_activated_coupon_response_dict = loyalty_result_not_activated_coupon_response_instance.to_dict()
# create an instance of LoyaltyResultNotActivatedCouponResponse from a dict
loyalty_result_not_activated_coupon_response_from_dict = LoyaltyResultNotActivatedCouponResponse.from_dict(loyalty_result_not_activated_coupon_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


