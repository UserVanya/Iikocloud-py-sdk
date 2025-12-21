# ExternalMenuModifierItem4


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sku** | **str** | Modifier&#39;s code | [optional] [default to '']
**name** | **str** | Modifier&#39;s name | [optional] [default to '']
**description** | **str** | Modifier&#39;s description | [optional] [default to '']
**restrictions** | [**List[ModifierRestrictionsDto8]**](ModifierRestrictionsDto8.md) |  | [optional] 
**is_hidden** | **bool** |  | [optional] [default to False]
**prices** | [**List[ExternalMenuPriceByDepartmentsDto4]**](ExternalMenuPriceByDepartmentsDto4.md) |  | [optional] 
**nutritions** | [**List[NutritionInfoDto8]**](NutritionInfoDto8.md) | Nutrition per 100 g of product grouped by departments | [optional] 
**tax_category_id** | **str** |  | [optional] 
**independent_quantity** | **bool** |  | [optional] [default to False]
**product_category_id** | **str** |  | [optional] 
**customer_tag_groups** | [**List[SelectedCustomerTag8]**](SelectedCustomerTag8.md) |  | [optional] 
**payment_subject** | **str** |  | [optional] 
**outer_ean_code** | **str** |  | [optional] 
**is_marked** | **bool** |  | [optional] [default to False]
**measure_unit_type** | **str** |  | [optional] [default to 'GRAM']
**payment_subject_code** | **str** |  | [optional] 
**barcodes** | [**List[BarcodeDto8]**](BarcodeDto8.md) |  | [optional] 
**button_image_url** | **str** |  | [optional] 
**allergen_group_ids** | **List[object]** |  | 
**labels** | **List[object]** | List of label names | 
**tags** | **List[object]** | List of tag names | 
**id** | **UUID** |  | 
**weight** | **float** |  | 

## Example

```python
from iikocloud_client.models.external_menu_modifier_item4 import ExternalMenuModifierItem4

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalMenuModifierItem4 from a JSON string
external_menu_modifier_item4_instance = ExternalMenuModifierItem4.from_json(json)
# print the JSON string representation of the object
print(ExternalMenuModifierItem4.to_json())

# convert the object into a dict
external_menu_modifier_item4_dict = external_menu_modifier_item4_instance.to_dict()
# create an instance of ExternalMenuModifierItem4 from a dict
external_menu_modifier_item4_from_dict = ExternalMenuModifierItem4.from_dict(external_menu_modifier_item4_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


