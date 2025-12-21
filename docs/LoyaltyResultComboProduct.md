# LoyaltyResultComboProduct

Combo product.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_id** | **UUID** | Product id. | [optional] 
**size_name** | **str** | Size name. Can be null. | [optional] 
**size_id** | **UUID** | Size id. | [optional] 
**forbidden_modifiers** | **List[UUID]** | Forbidden modifiers. | [optional] 
**price_modification_amount** | **float** | Price modification amount. | [optional] 

## Example

```python
from iikocloud_client.models.loyalty_result_combo_product import LoyaltyResultComboProduct

# TODO update the JSON string below
json = "{}"
# create an instance of LoyaltyResultComboProduct from a JSON string
loyalty_result_combo_product_instance = LoyaltyResultComboProduct.from_json(json)
# print the JSON string representation of the object
print(LoyaltyResultComboProduct.to_json())

# convert the object into a dict
loyalty_result_combo_product_dict = loyalty_result_combo_product_instance.to_dict()
# create an instance of LoyaltyResultComboProduct from a dict
loyalty_result_combo_product_from_dict = LoyaltyResultComboProduct.from_dict(loyalty_result_combo_product_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


