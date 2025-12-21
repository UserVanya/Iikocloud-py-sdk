# ExternalMenuItemSize3


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sku** | **str** | Unique size code, consists of the product code and the name of the size, if the product has one size, then the size code will be equal to the product code | [optional] [default to '']
**size_code** | **str** |  | [optional] 
**size_name** | **str** | Name of the product size, the name can be empty if there is only one size in the list | [optional] 
**is_default** | **bool** | Whether it is a default size of the product. If the product has one size, then the parameter will be true, if the product has several sizes, none of them can be default. | [optional] [default to False]
**item_modifier_groups** | [**List[ExternalMenuModifierGroup3]**](ExternalMenuModifierGroup3.md) |  | 
**prices** | [**List[ExternalMenuPriceByDepartmentsDto3]**](ExternalMenuPriceByDepartmentsDto3.md) |  | [optional] 
**nutritions** | [**List[NutritionInfoDto3]**](NutritionInfoDto3.md) | Nutrition per 100 g of product grouped by departments | [optional] 
**is_hidden** | **bool** |  | [optional] [default to False]
**measure_unit_type** | **str** |  | [optional] [default to 'GRAM']
**button_image_url** | **str** | links to images | [optional] 
**weight** | **float** |  | 
**id** | **str** |  | 

## Example

```python
from iikocloud_client.models.external_menu_item_size3 import ExternalMenuItemSize3

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalMenuItemSize3 from a JSON string
external_menu_item_size3_instance = ExternalMenuItemSize3.from_json(json)
# print the JSON string representation of the object
print(ExternalMenuItemSize3.to_json())

# convert the object into a dict
external_menu_item_size3_dict = external_menu_item_size3_instance.to_dict()
# create an instance of ExternalMenuItemSize3 from a dict
external_menu_item_size3_from_dict = ExternalMenuItemSize3.from_dict(external_menu_item_size3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


