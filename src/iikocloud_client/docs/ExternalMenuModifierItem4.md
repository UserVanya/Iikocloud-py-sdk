# ExternalMenuModifierItem4


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allergen_group_ids** | **List[object]** |  | 
**barcodes** | [**List[BarcodeDto8]**](BarcodeDto8.md) |  | [optional] 
**button_image_url** | **str** |  | [optional] 
**customer_tag_groups** | [**List[SelectedCustomerTag8]**](SelectedCustomerTag8.md) |  | [optional] 
**description** | **str** | Modifier&#39;s description | [optional] [default to '']
**id** | **UUID** |  | 
**independent_quantity** | **bool** |  | [optional] [default to False]
**is_hidden** | **bool** |  | [optional] [default to False]
**is_marked** | **bool** |  | [optional] [default to False]
**labels** | **List[object]** | List of label names | 
**measure_unit_type** | **str** |  | [optional] [default to 'GRAM']
**name** | **str** | Modifier&#39;s name | [optional] [default to '']
**nutritions** | [**List[NutritionInfoDto8]**](NutritionInfoDto8.md) | Nutrition per 100 g of product grouped by departments | [optional] 
**outer_ean_code** | **str** |  | [optional] 
**payment_subject** | **str** |  | [optional] 
**payment_subject_code** | **str** |  | [optional] 
**prices** | [**List[ExternalMenuPriceByDepartmentsDto4]**](ExternalMenuPriceByDepartmentsDto4.md) |  | [optional] 
**product_category_id** | **str** |  | [optional] 
**restrictions** | [**List[ModifierRestrictionsDto8]**](ModifierRestrictionsDto8.md) |  | [optional] 
**sku** | **str** | Modifier&#39;s code | [optional] [default to '']
**tags** | **List[object]** | List of tag names | 
**tax_category_id** | **str** |  | [optional] 
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


