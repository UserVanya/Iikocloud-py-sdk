# LoyaltyResultUpsaleProduct

Product that suggested to be added to order.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Id of product. | [optional] 
**code** | **str** | Code of product. | [optional] 

## Example

```python
from iikocloud_client.models.loyalty_result_upsale_product import LoyaltyResultUpsaleProduct

# TODO update the JSON string below
json = "{}"
# create an instance of LoyaltyResultUpsaleProduct from a JSON string
loyalty_result_upsale_product_instance = LoyaltyResultUpsaleProduct.from_json(json)
# print the JSON string representation of the object
print(LoyaltyResultUpsaleProduct.to_json())

# convert the object into a dict
loyalty_result_upsale_product_dict = loyalty_result_upsale_product_instance.to_dict()
# create an instance of LoyaltyResultUpsaleProduct from a dict
loyalty_result_upsale_product_from_dict = LoyaltyResultUpsaleProduct.from_dict(loyalty_result_upsale_product_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


