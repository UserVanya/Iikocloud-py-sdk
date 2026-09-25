# MenuV3SizePrice

Size price.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**button_image_url** | **str** | Button image URL. | [optional] 
**image** | [**Image**](Image.md) | Product size image. Replaces ButtonImageUrl. | [optional] 
**is_default** | **bool** | Flag indicating whether this is the default size. | [optional] 
**is_hidden** | **bool** | Flag indicating whether the size is hidden. | [optional] 
**measure_unit_type** | [**MeasureUnitType**](MeasureUnitType.md) | Unit of measurement. | [optional] 
**nutritions** | [**Nutritions**](Nutritions.md) | Nutritional value. | [optional] 
**price** | **float** | Price. | [optional] 
**size_code** | **str** | Size code. | [optional] 
**size_id** | **str** | Size ID. | [optional] 
**size_name** | **str** | Size name. | [optional] 
**sku** | **str** | Predefined size SKU. | [optional] 
**weight** | **float** | Weight. | [optional] 

## Example

```python
from iikocloud_client.models.menu_v3_size_price import MenuV3SizePrice

# TODO update the JSON string below
json = "{}"
# create an instance of MenuV3SizePrice from a JSON string
menu_v3_size_price_instance = MenuV3SizePrice.from_json(json)
# print the JSON string representation of the object
print(MenuV3SizePrice.to_json())

# convert the object into a dict
menu_v3_size_price_dict = menu_v3_size_price_instance.to_dict()
# create an instance of MenuV3SizePrice from a dict
menu_v3_size_price_from_dict = MenuV3SizePrice.from_dict(menu_v3_size_price_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


