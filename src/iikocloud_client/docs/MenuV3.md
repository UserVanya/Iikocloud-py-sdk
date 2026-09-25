# MenuV3

Menu structure.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allergen_groups** | [**List[MenuV3AllergenGroup]**](MenuV3AllergenGroup.md) | Allergen groups. | [optional] 
**button_image_url** | **str** | Button image URL. | [optional] 
**combos** | [**List[MenuV3Combo]**](MenuV3Combo.md) | Combo meals. | [optional] 
**customer_tag_groups** | [**List[MenuV3CustomerTagGroup]**](MenuV3CustomerTagGroup.md) | Customer tag groups. | [optional] 
**description** | **str** | Menu description. | [optional] 
**id** | **str** | Menu ID. | 
**image** | [**Image**](Image.md) | Menu image. Replaces ButtonImageUrl. | [optional] 
**items_groups** | [**List[ItemsGroup]**](ItemsGroup.md) | Item groups. | [optional] 
**modifiers** | [**List[MenuV3Modifier]**](MenuV3Modifier.md) | Modifiers. | [optional] 
**name** | **str** | Menu name. | 
**product_categories** | [**List[ProductCategory]**](ProductCategory.md) | Product categories. | [optional] 
**products** | [**List[MenuV3Product]**](MenuV3Product.md) | Products. | [optional] 
**schedules** | [**List[Schedule]**](Schedule.md) | Schedules. | [optional] 
**tax_categories** | [**List[MenuV3TaxCategory]**](MenuV3TaxCategory.md) | Tax categories. | [optional] 

## Example

```python
from iikocloud_client.models.menu_v3 import MenuV3

# TODO update the JSON string below
json = "{}"
# create an instance of MenuV3 from a JSON string
menu_v3_instance = MenuV3.from_json(json)
# print the JSON string representation of the object
print(MenuV3.to_json())

# convert the object into a dict
menu_v3_dict = menu_v3_instance.to_dict()
# create an instance of MenuV3 from a dict
menu_v3_from_dict = MenuV3.from_dict(menu_v3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


