# NotActivatedCoupon

Not activated coupon.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Id. | [optional] 
**number** | **str** | Number. Can be null. | [optional] 
**series_id** | **UUID** | Series id. | [optional] 
**series_name** | **str** | Series name. Can be null. | [optional] 

## Example

```python
from iikocloud_client.models.not_activated_coupon import NotActivatedCoupon

# TODO update the JSON string below
json = "{}"
# create an instance of NotActivatedCoupon from a JSON string
not_activated_coupon_instance = NotActivatedCoupon.from_json(json)
# print the JSON string representation of the object
print(NotActivatedCoupon.to_json())

# convert the object into a dict
not_activated_coupon_dict = not_activated_coupon_instance.to_dict()
# create an instance of NotActivatedCoupon from a dict
not_activated_coupon_from_dict = NotActivatedCoupon.from_dict(not_activated_coupon_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


