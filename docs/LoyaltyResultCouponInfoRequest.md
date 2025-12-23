# LoyaltyResultCouponInfoRequest

Coupon info request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number** | **str** | Number. Can be null. | 
**series** | **str** | Series. Can be null. | [optional] 
**organization_id** | **str** | Organization id. | 

## Example

```python
from iikocloud_client.models.loyalty_result_coupon_info_request import LoyaltyResultCouponInfoRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LoyaltyResultCouponInfoRequest from a JSON string
loyalty_result_coupon_info_request_instance = LoyaltyResultCouponInfoRequest.from_json(json)
# print the JSON string representation of the object
print(LoyaltyResultCouponInfoRequest.to_json())

# convert the object into a dict
loyalty_result_coupon_info_request_dict = loyalty_result_coupon_info_request_instance.to_dict()
# create an instance of LoyaltyResultCouponInfoRequest from a dict
loyalty_result_coupon_info_request_from_dict = LoyaltyResultCouponInfoRequest.from_dict(loyalty_result_coupon_info_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


