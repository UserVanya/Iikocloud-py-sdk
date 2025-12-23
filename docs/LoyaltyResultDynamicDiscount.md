# LoyaltyResultDynamicDiscount

Manual discount.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**manual_condition_id** | **str** | Manual discount condition identifier. | [optional] 
**sum** | **float** | Discount amount. | [optional] 

## Example

```python
from iikocloud_client.models.loyalty_result_dynamic_discount import LoyaltyResultDynamicDiscount

# TODO update the JSON string below
json = "{}"
# create an instance of LoyaltyResultDynamicDiscount from a JSON string
loyalty_result_dynamic_discount_instance = LoyaltyResultDynamicDiscount.from_json(json)
# print the JSON string representation of the object
print(LoyaltyResultDynamicDiscount.to_json())

# convert the object into a dict
loyalty_result_dynamic_discount_dict = loyalty_result_dynamic_discount_instance.to_dict()
# create an instance of LoyaltyResultDynamicDiscount from a dict
loyalty_result_dynamic_discount_from_dict = LoyaltyResultDynamicDiscount.from_dict(loyalty_result_dynamic_discount_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


