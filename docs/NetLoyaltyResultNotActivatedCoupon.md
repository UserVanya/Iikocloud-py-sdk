# NetLoyaltyResultNotActivatedCoupon

Not activated coupon.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Id. | [optional] 
**number** | **str** | Number. Can be null. | [optional] 
**series_name** | **str** | Series name. Can be null. | [optional] 
**series_id** | **str** | Series id. | [optional] 

## Example

```python
from iiko_cloud_client.models.net_loyalty_result_not_activated_coupon import NetLoyaltyResultNotActivatedCoupon

# TODO update the JSON string below
json = "{}"
# create an instance of NetLoyaltyResultNotActivatedCoupon from a JSON string
net_loyalty_result_not_activated_coupon_instance = NetLoyaltyResultNotActivatedCoupon.from_json(json)
# print the JSON string representation of the object
print(NetLoyaltyResultNotActivatedCoupon.to_json())

# convert the object into a dict
net_loyalty_result_not_activated_coupon_dict = net_loyalty_result_not_activated_coupon_instance.to_dict()
# create an instance of NetLoyaltyResultNotActivatedCoupon from a dict
net_loyalty_result_not_activated_coupon_from_dict = NetLoyaltyResultNotActivatedCoupon.from_dict(net_loyalty_result_not_activated_coupon_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


