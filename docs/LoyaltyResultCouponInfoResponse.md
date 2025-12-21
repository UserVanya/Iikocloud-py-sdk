# LoyaltyResultCouponInfoResponse

Coupon info response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**coupon_info** | [**List[LoyaltyResultCouponInfo]**](LoyaltyResultCouponInfo.md) | Coupon info. | [optional] 

## Example

```python
from iikocloud_client.models.loyalty_result_coupon_info_response import LoyaltyResultCouponInfoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LoyaltyResultCouponInfoResponse from a JSON string
loyalty_result_coupon_info_response_instance = LoyaltyResultCouponInfoResponse.from_json(json)
# print the JSON string representation of the object
print(LoyaltyResultCouponInfoResponse.to_json())

# convert the object into a dict
loyalty_result_coupon_info_response_dict = loyalty_result_coupon_info_response_instance.to_dict()
# create an instance of LoyaltyResultCouponInfoResponse from a dict
loyalty_result_coupon_info_response_from_dict = LoyaltyResultCouponInfoResponse.from_dict(loyalty_result_coupon_info_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


