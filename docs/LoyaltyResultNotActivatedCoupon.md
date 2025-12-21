# LoyaltyResultNotActivatedCoupon

Not activated coupon.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Id. | [optional] 
**number** | **str** | Number. Can be null. | [optional] 
**series_name** | **str** | Series name. Can be null. | [optional] 
**series_id** | **UUID** | Series id. | [optional] 

## Example

```python
from iikocloud_client.models.loyalty_result_not_activated_coupon import LoyaltyResultNotActivatedCoupon

# TODO update the JSON string below
json = "{}"
# create an instance of LoyaltyResultNotActivatedCoupon from a JSON string
loyalty_result_not_activated_coupon_instance = LoyaltyResultNotActivatedCoupon.from_json(json)
# print the JSON string representation of the object
print(LoyaltyResultNotActivatedCoupon.to_json())

# convert the object into a dict
loyalty_result_not_activated_coupon_dict = loyalty_result_not_activated_coupon_instance.to_dict()
# create an instance of LoyaltyResultNotActivatedCoupon from a dict
loyalty_result_not_activated_coupon_from_dict = LoyaltyResultNotActivatedCoupon.from_dict(loyalty_result_not_activated_coupon_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


