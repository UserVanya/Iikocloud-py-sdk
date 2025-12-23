# LoyaltyResultFreeProduct

Free item to be added to order.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Id of product. | [optional] 
**code** | **str** | Code of product. Can be null. | [optional] 
**size** | **List[str]** | Sizes available for that product. | [optional] 
**sizes** | [**List[LoyaltyResultFreeProductSize]**](LoyaltyResultFreeProductSize.md) | Sizes with IDs available for that product. | [optional] 

## Example

```python
from iikocloud_client.models.loyalty_result_free_product import LoyaltyResultFreeProduct

# TODO update the JSON string below
json = "{}"
# create an instance of LoyaltyResultFreeProduct from a JSON string
loyalty_result_free_product_instance = LoyaltyResultFreeProduct.from_json(json)
# print the JSON string representation of the object
print(LoyaltyResultFreeProduct.to_json())

# convert the object into a dict
loyalty_result_free_product_dict = loyalty_result_free_product_instance.to_dict()
# create an instance of LoyaltyResultFreeProduct from a dict
loyalty_result_free_product_from_dict = LoyaltyResultFreeProduct.from_dict(loyalty_result_free_product_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


