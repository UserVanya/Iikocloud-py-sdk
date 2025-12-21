# ExternalMenuModifierItem3


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sku** | **str** | Modifier&#39;s code | [optional] [default to '']
**name** | **str** | Modifier&#39;s name | [optional] [default to '']
**description** | **str** | Modifier&#39;s description | [optional] [default to '']
**restrictions** | [**List[ModifierRestrictionsDto7]**](ModifierRestrictionsDto7.md) |  | [optional] 
**is_hidden** | **bool** |  | [optional] [default to False]
**prices** | [**List[ExternalMenuPriceByDepartmentsDto3]**](ExternalMenuPriceByDepartmentsDto3.md) |  | [optional] 
**nutritions** | [**List[NutritionInfoDto7]**](NutritionInfoDto7.md) | Nutrition per 100 g of product grouped by departments | [optional] 
**tax_category_id** | **str** |  | [optional] 
**independent_quantity** | **bool** |  | [optional] [default to False]
**product_category_id** | **str** |  | [optional] 
**customer_tag_groups** | [**List[SelectedCustomerTag7]**](SelectedCustomerTag7.md) |  | [optional] 
**payment_subject** | **str** |  | [optional] 
**outer_ean_code** | **str** |  | [optional] 
**is_marked** | **bool** |  | [optional] [default to False]
**measure_unit_type** | **str** |  | [optional] [default to 'GRAM']
**payment_subject_code** | **str** |  | [optional] 
**barcodes** | [**List[BarcodeDto7]**](BarcodeDto7.md) |  | [optional] 
**button_image_url** | **str** |  | [optional] 
**allergen_group_ids** | **List[object]** |  | 
**labels** | **List[object]** | List of label names | 
**tags** | **List[object]** | List of tag names | 
**id** | **UUID** |  | 
**weight** | **float** |  | 

## Example

```python
from iikocloud_client.models.external_menu_modifier_item3 import ExternalMenuModifierItem3

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalMenuModifierItem3 from a JSON string
external_menu_modifier_item3_instance = ExternalMenuModifierItem3.from_json(json)
# print the JSON string representation of the object
print(ExternalMenuModifierItem3.to_json())

# convert the object into a dict
external_menu_modifier_item3_dict = external_menu_modifier_item3_instance.to_dict()
# create an instance of ExternalMenuModifierItem3 from a dict
external_menu_modifier_item3_from_dict = ExternalMenuModifierItem3.from_dict(external_menu_modifier_item3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


