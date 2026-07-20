# ExternalMenuItem2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allergen_group_ids** | **List[object]** | List of GUID groups of allergens | 
**barcodes** | [**List[BarcodeDto2]**](BarcodeDto2.md) |  | [optional] 
**can_set_open_price** | **bool** | Can set open price flag | [optional] [default to False]
**customer_tag_groups** | [**List[SelectedCustomerTag2]**](SelectedCustomerTag2.md) |  | [optional] 
**description** | **str** | Product description | [optional] [default to '']
**id** | **str** | Product ID | 
**is_hidden** | **bool** | Visibility flag | [optional] [default to False]
**is_marked** | **bool** | Marking flag | [optional] [default to False]
**item_sizes** | [**List[ExternalMenuItemSize2]**](ExternalMenuItemSize2.md) |  | 
**labels** | **List[str]** | List of labels | [optional] 
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
**splittable** | **bool** |  | 
**tags** | **List[str]** | List of tags | [optional] 
**tax_category_id** | **str** | Tax category GUID | [optional] 
**type** | **str** | Item type | [optional] [default to 'DISH']
**use_balance_for_sell** | **bool** |  | [optional] [default to False]

## Example

```python
from iikocloud_client.models.external_menu_item2 import ExternalMenuItem2

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalMenuItem2 from a JSON string
external_menu_item2_instance = ExternalMenuItem2.from_json(json)
# print the JSON string representation of the object
print(ExternalMenuItem2.to_json())

# convert the object into a dict
external_menu_item2_dict = external_menu_item2_instance.to_dict()
# create an instance of ExternalMenuItem2 from a dict
external_menu_item2_from_dict = ExternalMenuItem2.from_dict(external_menu_item2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


