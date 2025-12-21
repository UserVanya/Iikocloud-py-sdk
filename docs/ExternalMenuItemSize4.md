# ExternalMenuItemSize4


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sku** | **str** | Unique size code, consists of the product code and the name of the size, if the product has one size, then the size code will be equal to the product code | [optional] [default to '']
**size_code** | **str** |  | [optional] 
**size_name** | **str** | Name of the product size, the name can be empty if there is only one size in the list | [optional] 
**is_default** | **bool** | Whether it is a default size of the product. If the product has one size, then the parameter will be true, if the product has several sizes, none of them can be default. | [optional] [default to False]
**item_modifier_groups** | [**List[ExternalMenuModifierGroup4]**](ExternalMenuModifierGroup4.md) |  | 
**prices** | [**List[ExternalMenuPriceByDepartmentsDto4]**](ExternalMenuPriceByDepartmentsDto4.md) |  | [optional] 
**nutritions** | [**List[NutritionInfoDto4]**](NutritionInfoDto4.md) | Nutrition per 100 g of product grouped by departments | [optional] 
**is_hidden** | **bool** |  | [optional] [default to False]
**measure_unit_type** | **str** |  | [optional] [default to 'GRAM']
**button_image_url** | **str** | links to images | [optional] 
**weight** | **float** |  | 
**id** | **str** |  | 

## Example

```python
from iikocloud_client.models.external_menu_item_size4 import ExternalMenuItemSize4

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalMenuItemSize4 from a JSON string
external_menu_item_size4_instance = ExternalMenuItemSize4.from_json(json)
# print the JSON string representation of the object
print(ExternalMenuItemSize4.to_json())

# convert the object into a dict
external_menu_item_size4_dict = external_menu_item_size4_instance.to_dict()
# create an instance of ExternalMenuItemSize4 from a dict
external_menu_item_size4_from_dict = ExternalMenuItemSize4.from_dict(external_menu_item_size4_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


