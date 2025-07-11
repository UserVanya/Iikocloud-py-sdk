# NetLoyaltyResultCouponInfo

Coupon info.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Id. | [optional] 
**number** | **str** | Number. Can be null. | [optional] 
**series_name** | **str** | Series name. Can be null. | [optional] 
**series_id** | **str** | Series id. | [optional] 
**when_activated** | **str** | When activated. | [optional] 
**is_deleted** | **bool** | Is deleted. | [optional] 

## Example

```python
from iikocloud_client.models.net_loyalty_result_coupon_info import NetLoyaltyResultCouponInfo

# TODO update the JSON string below
json = "{}"
# create an instance of NetLoyaltyResultCouponInfo from a JSON string
net_loyalty_result_coupon_info_instance = NetLoyaltyResultCouponInfo.from_json(json)
# print the JSON string representation of the object
print(NetLoyaltyResultCouponInfo.to_json())

# convert the object into a dict
net_loyalty_result_coupon_info_dict = net_loyalty_result_coupon_info_instance.to_dict()
# create an instance of NetLoyaltyResultCouponInfo from a dict
net_loyalty_result_coupon_info_from_dict = NetLoyaltyResultCouponInfo.from_dict(net_loyalty_result_coupon_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


