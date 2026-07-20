# ComboProduct

Combo product.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**forbidden_modifiers** | **List[UUID]** | Forbidden modifiers. | [optional] 
**position** | **int** | Position. | [optional] 
**price_modification_amount** | **float** | Price modification amount. | [optional] 
**product_id** | **UUID** | Product id. | [optional] 
**size_id** | **UUID** | Size id. | [optional] 
**size_name** | **str** | Size name. Can be null. | [optional] 

## Example

```python
from iikocloud_client.models.combo_product import ComboProduct

# TODO update the JSON string below
json = "{}"
# create an instance of ComboProduct from a JSON string
combo_product_instance = ComboProduct.from_json(json)
# print the JSON string representation of the object
print(ComboProduct.to_json())

# convert the object into a dict
combo_product_dict = combo_product_instance.to_dict()
# create an instance of ComboProduct from a dict
combo_product_from_dict = ComboProduct.from_dict(combo_product_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


