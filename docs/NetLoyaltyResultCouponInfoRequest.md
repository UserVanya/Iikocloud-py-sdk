# NetLoyaltyResultCouponInfoRequest

Coupon info request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number** | **str** | Number. Can be null. | 
**series** | **str** | Series. Can be null. | [optional] 
**organization_id** | **str** | Organization id. | 

## Example

```python
from iikocloud_client.models.net_loyalty_result_coupon_info_request import NetLoyaltyResultCouponInfoRequest

# TODO update the JSON string below
json = "{}"
# create an instance of NetLoyaltyResultCouponInfoRequest from a JSON string
net_loyalty_result_coupon_info_request_instance = NetLoyaltyResultCouponInfoRequest.from_json(json)
# print the JSON string representation of the object
print(NetLoyaltyResultCouponInfoRequest.to_json())

# convert the object into a dict
net_loyalty_result_coupon_info_request_dict = net_loyalty_result_coupon_info_request_instance.to_dict()
# create an instance of NetLoyaltyResultCouponInfoRequest from a dict
net_loyalty_result_coupon_info_request_from_dict = NetLoyaltyResultCouponInfoRequest.from_dict(net_loyalty_result_coupon_info_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


