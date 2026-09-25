# ComboComponentProduct

Product available for selection in a combo meal component group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**forbidden_modifiers** | **List[str]** | List of modifier IDs that cannot be applied to this product in a combo. | [optional] 
**price_modification_amount** | **float** | Extra charge or discount for this product within the combo (in rubles).  Positive &#x3D; extra charge, negative &#x3D; discount.  Depends on PriceStrategy: always 0 for BY_COMPONENT. | [optional] 
**product_id** | **UUID** | Reference to a product from the Menu.products[] catalog. | 
**size_prices** | [**List[ComboSizePrice]**](ComboSizePrice.md) | Product prices in combo for different sizes.  If absent or empty — the product is not available for sale in the combo.  CRITICAL: prices differ from retail by 8-39%. | 

## Example

```python
from iikocloud_client.models.combo_component_product import ComboComponentProduct

# TODO update the JSON string below
json = "{}"
# create an instance of ComboComponentProduct from a JSON string
combo_component_product_instance = ComboComponentProduct.from_json(json)
# print the JSON string representation of the object
print(ComboComponentProduct.to_json())

# convert the object into a dict
combo_component_product_dict = combo_component_product_instance.to_dict()
# create an instance of ComboComponentProduct from a dict
combo_component_product_from_dict = ComboComponentProduct.from_dict(combo_component_product_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


