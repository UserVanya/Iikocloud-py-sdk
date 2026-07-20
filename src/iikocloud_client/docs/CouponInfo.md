# CouponInfo

Coupon info.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Id. | [optional] 
**is_deleted** | **bool** | Is deleted. | [optional] 
**number** | **str** | Number. Can be null. | [optional] 
**series_id** | **UUID** | Series id. | [optional] 
**series_name** | **str** | Series name. Can be null. | [optional] 
**when_activated** | **str** | When activated. | [optional] 

## Example

```python
from iikocloud_client.models.coupon_info import CouponInfo

# TODO update the JSON string below
json = "{}"
# create an instance of CouponInfo from a JSON string
coupon_info_instance = CouponInfo.from_json(json)
# print the JSON string representation of the object
print(CouponInfo.to_json())

# convert the object into a dict
coupon_info_dict = coupon_info_instance.to_dict()
# create an instance of CouponInfo from a dict
coupon_info_from_dict = CouponInfo.from_dict(coupon_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


