# NomenclatureProductRGBColor


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**blue** | **int** | Blue channel: 0–255 | [optional] 
**green** | **int** | Green channel: 0–255 | [optional] 
**red** | **int** | Red channel: 0–255 | [optional] 

## Example

```python
from iikocloud_client.models.nomenclature_product_rgb_color import NomenclatureProductRGBColor

# TODO update the JSON string below
json = "{}"
# create an instance of NomenclatureProductRGBColor from a JSON string
nomenclature_product_rgb_color_instance = NomenclatureProductRGBColor.from_json(json)
# print the JSON string representation of the object
print(NomenclatureProductRGBColor.to_json())

# convert the object into a dict
nomenclature_product_rgb_color_dict = nomenclature_product_rgb_color_instance.to_dict()
# create an instance of NomenclatureProductRGBColor from a dict
nomenclature_product_rgb_color_from_dict = NomenclatureProductRGBColor.from_dict(nomenclature_product_rgb_color_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


