# ExternalMenuModifierItem3


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allergen_group_ids** | **List[object]** |  | 
**barcodes** | [**List[BarcodeDto7]**](BarcodeDto7.md) |  | [optional] 
**button_image_url** | **str** |  | [optional] 
**customer_tag_groups** | [**List[SelectedCustomerTag7]**](SelectedCustomerTag7.md) |  | [optional] 
**description** | **str** | Modifier&#39;s description | [optional] [default to '']
**id** | **UUID** |  | 
**independent_quantity** | **bool** |  | [optional] [default to False]
**is_hidden** | **bool** |  | [optional] [default to False]
**is_marked** | **bool** |  | [optional] [default to False]
**labels** | **List[object]** | List of label names | 
**measure_unit_type** | **str** |  | [optional] [default to 'GRAM']
**name** | **str** | Modifier&#39;s name | [optional] [default to '']
**nutritions** | [**List[NutritionInfoDto7]**](NutritionInfoDto7.md) | Nutrition per 100 g of product grouped by departments | [optional] 
**outer_ean_code** | **str** |  | [optional] 
**payment_subject** | **str** |  | [optional] 
**payment_subject_code** | **str** |  | [optional] 
**prices** | [**List[ExternalMenuPriceByDepartmentsDto3]**](ExternalMenuPriceByDepartmentsDto3.md) |  | [optional] 
**product_category_id** | **str** |  | [optional] 
**restrictions** | [**ModifierRestrictionsDto7**](ModifierRestrictionsDto7.md) |  | [optional] 
**sku** | **str** | Modifier&#39;s code | [optional] [default to '']
**tags** | **List[object]** | List of tag names | 
**tax_category_id** | **str** |  | [optional] 
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


