# NetLoyaltyResultDynamicDiscount

Manual discount.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**manual_condition_id** | **str** | Manual discount condition identifier. | [optional] 
**sum** | **float** | Discount amount. | [optional] 

## Example

```python
from iikocloud_client.models.net_loyalty_result_dynamic_discount import NetLoyaltyResultDynamicDiscount

# TODO update the JSON string below
json = "{}"
# create an instance of NetLoyaltyResultDynamicDiscount from a JSON string
net_loyalty_result_dynamic_discount_instance = NetLoyaltyResultDynamicDiscount.from_json(json)
# print the JSON string representation of the object
print(NetLoyaltyResultDynamicDiscount.to_json())

# convert the object into a dict
net_loyalty_result_dynamic_discount_dict = net_loyalty_result_dynamic_discount_instance.to_dict()
# create an instance of NetLoyaltyResultDynamicDiscount from a dict
net_loyalty_result_dynamic_discount_from_dict = NetLoyaltyResultDynamicDiscount.from_dict(net_loyalty_result_dynamic_discount_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


