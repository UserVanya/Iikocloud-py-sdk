# ExternalMenuModifierItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sku** | **str** | Modifier&#39;s code | [optional] [default to '']
**name** | **str** | Modifier&#39;s name | [optional] [default to '']
**description** | **str** | Modifier&#39;s description | [optional] [default to '']
**restrictions** | [**ModifierRestrictionsDto5**](ModifierRestrictionsDto5.md) |  | [optional] 
**allergen_groups** | [**List[AllergenGroupDto4]**](AllergenGroupDto4.md) |  | [optional] 
**nutrition_per_hundred_grams** | [**NutritionInfoDto5**](NutritionInfoDto5.md) |  | [optional] 
**portion_weight_grams** | **float** | Modifier&#39;s weight in gramms | [optional] 
**tags** | [**List[TagDto3]**](TagDto3.md) | List of tag names | [optional] 
**labels** | [**List[LabelDto3]**](LabelDto3.md) | List of label names | [optional] 
**item_id** | **UUID** | Modifier&#39;s Id | [optional] 
**is_hidden** | **bool** |  | [optional] [default to False]
**prices** | [**List[ExternalMenuPriceByDepartmentsDto]**](ExternalMenuPriceByDepartmentsDto.md) |  | [optional] 
**position** | **int** |  | [optional] 
**independent_quantity** | **bool** |  | [optional] [default to False]
**product_category_id** | **str** |  | [optional] 
**customer_tag_groups** | [**List[SelectedCustomerTag5]**](SelectedCustomerTag5.md) |  | [optional] 
**payment_subject** | **str** |  | [optional] 
**outer_ean_code** | **str** |  | [optional] 
**is_marked** | **bool** |  | [optional] [default to False]
**measure_unit_type** | **str** |  | [optional] [default to 'GRAM']
**payment_subject_code** | **str** |  | [optional] 
**barcodes** | [**List[BarcodeDto5]**](BarcodeDto5.md) |  | [optional] 
**button_image_url** | **str** |  | [optional] 

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


