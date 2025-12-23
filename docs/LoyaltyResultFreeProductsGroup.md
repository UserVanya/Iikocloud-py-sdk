# LoyaltyResultFreeProductsGroup

Free item to be added to order.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_action_id** | **str** | Id of action that caused the suggestion. | [optional] 
**description_for_user** | **str** | Description for user. Can be null. | [optional] 
**products** | [**List[LoyaltyResultFreeProduct]**](LoyaltyResultFreeProduct.md) | Products that should be added to order. | [optional] 

## Example

```python
from iikocloud_client.models.loyalty_result_free_products_group import LoyaltyResultFreeProductsGroup

# TODO update the JSON string below
json = "{}"
# create an instance of LoyaltyResultFreeProductsGroup from a JSON string
loyalty_result_free_products_group_instance = LoyaltyResultFreeProductsGroup.from_json(json)
# print the JSON string representation of the object
print(LoyaltyResultFreeProductsGroup.to_json())

# convert the object into a dict
loyalty_result_free_products_group_dict = loyalty_result_free_products_group_instance.to_dict()
# create an instance of LoyaltyResultFreeProductsGroup from a dict
loyalty_result_free_products_group_from_dict = LoyaltyResultFreeProductsGroup.from_dict(loyalty_result_free_products_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


