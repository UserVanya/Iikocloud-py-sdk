# LoyaltyResultCouponInfo

Coupon info.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Id. | [optional] 
**number** | **str** | Number. Can be null. | [optional] 
**series_name** | **str** | Series name. Can be null. | [optional] 
**series_id** | **UUID** | Series id. | [optional] 
**when_activated** | **str** | When activated. | [optional] 
**is_deleted** | **bool** | Is deleted. | [optional] 

## Example

```python
from iikocloud_client.models.loyalty_result_coupon_info import LoyaltyResultCouponInfo

# TODO update the JSON string below
json = "{}"
# create an instance of LoyaltyResultCouponInfo from a JSON string
loyalty_result_coupon_info_instance = LoyaltyResultCouponInfo.from_json(json)
# print the JSON string representation of the object
print(LoyaltyResultCouponInfo.to_json())

# convert the object into a dict
loyalty_result_coupon_info_dict = loyalty_result_coupon_info_instance.to_dict()
# create an instance of LoyaltyResultCouponInfo from a dict
loyalty_result_coupon_info_from_dict = LoyaltyResultCouponInfo.from_dict(loyalty_result_coupon_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


