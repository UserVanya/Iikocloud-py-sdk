# ComboSizePrice

Product price within a combo meal for a specific size combination.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**combo_size_id** | **UUID** | Combo size ID (from ComboSize.sizeId). | 
**price** | **float** | Product price in combo for this size combination.  Can be null — the product/size is not available for sale.  Can be 0 — the component is included in the combo at no extra charge.  This is NOT a retail price (8-39% lower). | [optional] 
**product_size_id** | **UUID** | Product size ID (from Product.sizePrices[].sizeId).  Can be null for products without a size. | [optional] 

## Example

```python
from iikocloud_client.models.combo_size_price import ComboSizePrice

# TODO update the JSON string below
json = "{}"
# create an instance of ComboSizePrice from a JSON string
combo_size_price_instance = ComboSizePrice.from_json(json)
# print the JSON string representation of the object
print(ComboSizePrice.to_json())

# convert the object into a dict
combo_size_price_dict = combo_size_price_instance.to_dict()
# create an instance of ComboSizePrice from a dict
combo_size_price_from_dict = ComboSizePrice.from_dict(combo_size_price_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


