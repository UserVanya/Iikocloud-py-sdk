# NetLoyaltyResultNotActivatedCouponRequest

Not activated coupon request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**series** | **str** | Series. Can be null. | 
**page_size** | **int** | Page size. | [optional] 
**page** | **int** | Page. | [optional] 
**organization_id** | **str** | Organization id. | 

## Example

```python
from iiko_cloud_client.models.net_loyalty_result_not_activated_coupon_request import NetLoyaltyResultNotActivatedCouponRequest

# TODO update the JSON string below
json = "{}"
# create an instance of NetLoyaltyResultNotActivatedCouponRequest from a JSON string
net_loyalty_result_not_activated_coupon_request_instance = NetLoyaltyResultNotActivatedCouponRequest.from_json(json)
# print the JSON string representation of the object
print(NetLoyaltyResultNotActivatedCouponRequest.to_json())

# convert the object into a dict
net_loyalty_result_not_activated_coupon_request_dict = net_loyalty_result_not_activated_coupon_request_instance.to_dict()
# create an instance of NetLoyaltyResultNotActivatedCouponRequest from a dict
net_loyalty_result_not_activated_coupon_request_from_dict = NetLoyaltyResultNotActivatedCouponRequest.from_dict(net_loyalty_result_not_activated_coupon_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


