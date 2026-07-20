# NotActivatedCouponResponse

Not activated coupon response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**not_activated_coupon** | [**List[NotActivatedCoupon]**](NotActivatedCoupon.md) | Not activated coupon. | [optional] 

## Example

```python
from iikocloud_client.models.not_activated_coupon_response import NotActivatedCouponResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NotActivatedCouponResponse from a JSON string
not_activated_coupon_response_instance = NotActivatedCouponResponse.from_json(json)
# print the JSON string representation of the object
print(NotActivatedCouponResponse.to_json())

# convert the object into a dict
not_activated_coupon_response_dict = not_activated_coupon_response_instance.to_dict()
# create an instance of NotActivatedCouponResponse from a dict
not_activated_coupon_response_from_dict = NotActivatedCouponResponse.from_dict(not_activated_coupon_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


