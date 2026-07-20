# ExternalMenuItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allergens** | [**List[AllergenGroupDto3]**](AllergenGroupDto3.md) | Allergens | [optional] 
**barcodes** | [**List[BarcodeDto]**](BarcodeDto.md) |  | [optional] 
**can_be_divided** | **bool** |  | [optional] [default to False]
**can_set_open_price** | **bool** | Can set open price flag | [optional] [default to False]
**customer_tag_groups** | [**List[SelectedCustomerTag]**](SelectedCustomerTag.md) |  | [optional] 
**description** | **str** | Product description | [optional] [default to '']
**is_hidden** | **bool** | Visibility flag | [optional] [default to False]
**is_marked** | **bool** | Marking flag | [optional] [default to False]
**item_id** | **str** | Product ID | [optional] [default to '']
**item_sizes** | [**List[ExternalMenuItemSize]**](ExternalMenuItemSize.md) |  | 
**labels** | [**List[LabelDto2]**](LabelDto2.md) |  | [optional] 
**measure_unit** | **str** | Measure unit | [optional] [default to '']
**modifier_schema_id** | **str** | Modifier schema ID | 
**modifier_schema_name** | **str** | Modifier schema name | [optional] 
**name** | **str** | Product name | [optional] [default to '']
**order_item_type** | **str** | Product or compound. Depends on modifiers scheme existence | 
**outer_ean_code** | **str** |  | [optional] 
**payment_subject** | **str** |  | [optional] 
**payment_subject_code** | **str** |  | [optional] 
**product_category_id** | **str** | Product category GUID | [optional] 
**sku** | **str** | Product code | [optional] [default to '']
**tags** | [**List[TagDto2]**](TagDto2.md) |  | [optional] 
**tax_category** | [**TaxCategoryDto3**](TaxCategoryDto3.md) | Tax category | 
**type** | **str** | Item type | [optional] [default to 'DISH']
**use_balance_for_sell** | **bool** |  | [optional] [default to False]

## Example

```python
from iikocloud_client.models.external_menu_item import ExternalMenuItem

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalMenuItem from a JSON string
external_menu_item_instance = ExternalMenuItem.from_json(json)
# print the JSON string representation of the object
print(ExternalMenuItem.to_json())

# convert the object into a dict
external_menu_item_dict = external_menu_item_instance.to_dict()
# create an instance of ExternalMenuItem from a dict
external_menu_item_from_dict = ExternalMenuItem.from_dict(external_menu_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


