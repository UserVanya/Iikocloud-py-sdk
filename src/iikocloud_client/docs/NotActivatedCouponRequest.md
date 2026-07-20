# NotActivatedCouponRequest

Not activated coupon request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **UUID** | Organization id. | 
**page** | **int** | Page. | [optional] 
**page_size** | **int** | Page size. | [optional] 
**series** | **str** | Series. Can be null. | 

## Example

```python
from iikocloud_client.models.not_activated_coupon_request import NotActivatedCouponRequest

# TODO update the JSON string below
json = "{}"
# create an instance of NotActivatedCouponRequest from a JSON string
not_activated_coupon_request_instance = NotActivatedCouponRequest.from_json(json)
# print the JSON string representation of the object
print(NotActivatedCouponRequest.to_json())

# convert the object into a dict
not_activated_coupon_request_dict = not_activated_coupon_request_instance.to_dict()
# create an instance of NotActivatedCouponRequest from a dict
not_activated_coupon_request_from_dict = NotActivatedCouponRequest.from_dict(not_activated_coupon_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


