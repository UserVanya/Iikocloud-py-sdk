# LoyaltyDynamicDiscount

Manual discount.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sum** | **float** | Discount amount. | [optional] 
**manual_condition_id** | **UUID** | Manual discount condition identifier. | [optional] 

## Example

```python
from iikocloud_client.models.loyalty_dynamic_discount import LoyaltyDynamicDiscount

# TODO update the JSON string below
json = "{}"
# create an instance of LoyaltyDynamicDiscount from a JSON string
loyalty_dynamic_discount_instance = LoyaltyDynamicDiscount.from_json(json)
# print the JSON string representation of the object
print(LoyaltyDynamicDiscount.to_json())

# convert the object into a dict
loyalty_dynamic_discount_dict = loyalty_dynamic_discount_instance.to_dict()
# create an instance of LoyaltyDynamicDiscount from a dict
loyalty_dynamic_discount_from_dict = LoyaltyDynamicDiscount.from_dict(loyalty_dynamic_discount_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


