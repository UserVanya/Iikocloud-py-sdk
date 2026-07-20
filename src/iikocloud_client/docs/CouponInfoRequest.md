# CouponInfoRequest

Coupon info request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number** | **str** | Number. Can be null. | 
**organization_id** | **UUID** | Organization id. | 
**series** | **str** | Series. Can be null. | [optional] 

## Example

```python
from iikocloud_client.models.coupon_info_request import CouponInfoRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CouponInfoRequest from a JSON string
coupon_info_request_instance = CouponInfoRequest.from_json(json)
# print the JSON string representation of the object
print(CouponInfoRequest.to_json())

# convert the object into a dict
coupon_info_request_dict = coupon_info_request_instance.to_dict()
# create an instance of CouponInfoRequest from a dict
coupon_info_request_from_dict = CouponInfoRequest.from_dict(coupon_info_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


