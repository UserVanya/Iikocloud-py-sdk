# ExternalMenuModifierItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allergen_groups** | [**List[AllergenGroupDto]**](AllergenGroupDto.md) |  | [optional] 
**barcodes** | [**List[BarcodeDto2]**](BarcodeDto2.md) |  | [optional] 
**button_image_url** | **str** |  | [optional] 
**customer_tag_groups** | [**List[SelectedCustomerTag]**](SelectedCustomerTag.md) |  | [optional] 
**description** | **str** | Modifier&#39;s description | [optional] [default to '']
**independent_quantity** | **bool** |  | [optional] [default to False]
**is_hidden** | **bool** |  | [optional] [default to False]
**is_marked** | **bool** |  | [optional] [default to False]
**item_id** | **UUID** | Modifier&#39;s Id | [optional] 
**labels** | [**List[LabelDto]**](LabelDto.md) | List of label names | [optional] 
**measure_unit_type** | **str** |  | [optional] [default to 'GRAM']
**name** | **str** | Modifier&#39;s name | [optional] [default to '']
**nutrition_per_hundred_grams** | [**NutritionInfoDto**](NutritionInfoDto.md) | Nutrition per 100 g of modifier product | [optional] 
**outer_ean_code** | **str** |  | [optional] 
**payment_subject** | **str** |  | [optional] 
**payment_subject_code** | **str** |  | [optional] 
**portion_weight_grams** | **float** | Modifier&#39;s weight in gramms | [optional] 
**position** | **int** |  | [optional] 
**prices** | [**List[ExternalMenuPriceByDepartmentsDto]**](ExternalMenuPriceByDepartmentsDto.md) |  | [optional] 
**product_category_id** | **str** |  | [optional] 
**restrictions** | [**ModifierRestrictionsDto**](ModifierRestrictionsDto.md) |  | [optional] 
**sku** | **str** | Modifier&#39;s code | [optional] [default to '']
**tags** | [**List[TagDto]**](TagDto.md) | List of tag names | [optional] 

## Example

```python
from iikocloud_client.models.external_menu_modifier_item import ExternalMenuModifierItem

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalMenuModifierItem from a JSON string
external_menu_modifier_item_instance = ExternalMenuModifierItem.from_json(json)
# print the JSON string representation of the object
print(ExternalMenuModifierItem.to_json())

# convert the object into a dict
external_menu_modifier_item_dict = external_menu_modifier_item_instance.to_dict()
# create an instance of ExternalMenuModifierItem from a dict
external_menu_modifier_item_from_dict = ExternalMenuModifierItem.from_dict(external_menu_modifier_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


