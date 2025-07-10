# NetLoyaltyResultComboProduct

Combo product.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_id** | **str** | Product id. | [optional] 
**size_name** | **str** | Size name. Can be null. | [optional] 
**size_id** | **str** | Size id. | [optional] 
**forbidden_modifiers** | **List[str]** | Forbidden modifiers. | [optional] 
**price_modification_amount** | **float** | Price modification amount. | [optional] 

## Example

```python
from iiko_cloud_client.models.net_loyalty_result_combo_product import NetLoyaltyResultComboProduct

# TODO update the JSON string below
json = "{}"
# create an instance of NetLoyaltyResultComboProduct from a JSON string
net_loyalty_result_combo_product_instance = NetLoyaltyResultComboProduct.from_json(json)
# print the JSON string representation of the object
print(NetLoyaltyResultComboProduct.to_json())

# convert the object into a dict
net_loyalty_result_combo_product_dict = net_loyalty_result_combo_product_instance.to_dict()
# create an instance of NetLoyaltyResultComboProduct from a dict
net_loyalty_result_combo_product_from_dict = NetLoyaltyResultComboProduct.from_dict(net_loyalty_result_combo_product_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


