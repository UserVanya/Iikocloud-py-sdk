# LoyaltyResultNotActivatedCouponRequest

Not activated coupon request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**series** | **str** | Series. Can be null. | 
**page_size** | **int** | Page size. | [optional] 
**page** | **int** | Page. | [optional] 
**organization_id** | **str** | Organization id. | 

## Example

```python
from iikocloud_client.models.loyalty_result_not_activated_coupon_request import LoyaltyResultNotActivatedCouponRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LoyaltyResultNotActivatedCouponRequest from a JSON string
loyalty_result_not_activated_coupon_request_instance = LoyaltyResultNotActivatedCouponRequest.from_json(json)
# print the JSON string representation of the object
print(LoyaltyResultNotActivatedCouponRequest.to_json())

# convert the object into a dict
loyalty_result_not_activated_coupon_request_dict = loyalty_result_not_activated_coupon_request_instance.to_dict()
# create an instance of LoyaltyResultNotActivatedCouponRequest from a dict
loyalty_result_not_activated_coupon_request_from_dict = LoyaltyResultNotActivatedCouponRequest.from_dict(loyalty_result_not_activated_coupon_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


