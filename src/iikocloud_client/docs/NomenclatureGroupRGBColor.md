# NomenclatureGroupRGBColor


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**blue** | **int** | Blue channel: 0–255 | [optional] 
**green** | **int** | Green channel: 0–255 | [optional] 
**red** | **int** | Red channel: 0–255 | [optional] 

## Example

```python
from iikocloud_client.models.nomenclature_group_rgb_color import NomenclatureGroupRGBColor

# TODO update the JSON string below
json = "{}"
# create an instance of NomenclatureGroupRGBColor from a JSON string
nomenclature_group_rgb_color_instance = NomenclatureGroupRGBColor.from_json(json)
# print the JSON string representation of the object
print(NomenclatureGroupRGBColor.to_json())

# convert the object into a dict
nomenclature_group_rgb_color_dict = nomenclature_group_rgb_color_instance.to_dict()
# create an instance of NomenclatureGroupRGBColor from a dict
nomenclature_group_rgb_color_from_dict = NomenclatureGroupRGBColor.from_dict(nomenclature_group_rgb_color_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


