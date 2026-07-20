# CouponInfoResponse

Coupon info response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**coupon_info** | [**List[CouponInfo]**](CouponInfo.md) | Coupon info. | [optional] 

## Example

```python
from iikocloud_client.models.coupon_info_response import CouponInfoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CouponInfoResponse from a JSON string
coupon_info_response_instance = CouponInfoResponse.from_json(json)
# print the JSON string representation of the object
print(CouponInfoResponse.to_json())

# convert the object into a dict
coupon_info_response_dict = coupon_info_response_instance.to_dict()
# create an instance of CouponInfoResponse from a dict
coupon_info_response_from_dict = CouponInfoResponse.from_dict(coupon_info_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


