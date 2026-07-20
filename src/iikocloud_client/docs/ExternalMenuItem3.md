# ExternalMenuItem3


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allergen_group_ids** | **List[object]** | List of GUID groups of allergens | 
**barcodes** | [**List[BarcodeDto3]**](BarcodeDto3.md) |  | [optional] 
**can_set_open_price** | **bool** | Can set open price flag | [optional] [default to False]
**customer_tag_groups** | [**List[SelectedCustomerTag3]**](SelectedCustomerTag3.md) |  | [optional] 
**description** | **str** | Product description | [optional] [default to '']
**id** | **str** | Product ID | 
**is_hidden** | **bool** | Visibility flag | [optional] [default to False]
**is_marked** | **bool** | Marking flag | [optional] [default to False]
**item_sizes** | [**List[ExternalMenuItemSize3]**](ExternalMenuItemSize3.md) |  | 
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
**type** | **str** | Item type | [default to 'DISH']
**use_balance_for_sell** | **bool** |  | [optional] [default to False]

## Example

```python
from iikocloud_client.models.external_menu_item3 import ExternalMenuItem3

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalMenuItem3 from a JSON string
external_menu_item3_instance = ExternalMenuItem3.from_json(json)
# print the JSON string representation of the object
print(ExternalMenuItem3.to_json())

# convert the object into a dict
external_menu_item3_dict = external_menu_item3_instance.to_dict()
# create an instance of ExternalMenuItem3 from a dict
external_menu_item3_from_dict = ExternalMenuItem3.from_dict(external_menu_item3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


