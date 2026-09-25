# NomenclatureGroupCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accounting_category_id** | **UUID** | UUID of the accounting category (as configured in the accounting settings) | [optional] 
**category_id** | **UUID** | UUID of the product (custom) category. The list of values can be retrieved via the \&quot;Get a list of product categories\&quot; method in the \&quot;Product categories\&quot; category | [optional] 
**code** | **str** | Group code: 0–8 digits. Used for quick search on the order editing screen | [optional] 
**color** | [**NomenclatureGroupRGBColor**](NomenclatureGroupRGBColor.md) | Background button colour for POS | [optional] 
**custom_categories** | [**List[NomenclatureGroupCustomCategory]**](NomenclatureGroupCustomCategory.md) | Custom nomenclature categories. Empty array or null - no categories set | [optional] 
**default_course** | **int** | Default serving course. null - not set; 0 - VIP course; otherwise - course number | [optional] 
**default_maximum_store_balance_level** | **float** | Default maximum stock level | [optional] 
**default_minimum_store_balance_level** | **float** | Default minimum stock level | [optional] 
**description** | **str** | Group description | [optional] 
**font_color** | [**NomenclatureGroupRGBColor**](NomenclatureGroupRGBColor.md) | Font colour on the button for POS | [optional] 
**front_image_id** | **UUID** | UUID of the image for POS | [optional] 
**group_article** | **str** | Group article. If null or not provided, the field remains empty | [optional] 
**group_id** | **UUID** | UUID of the group to create. If not specified, the UUID will be generated automatically. | [optional] 
**include_in_report** | **bool** | Include in the price list print form | [optional] 
**is_fixed_price** | **bool** | Price is set explicitly and does not depend on markup | [optional] 
**markup_settings** | [**List[NomenclatureGroupMarkupSetting]**](NomenclatureGroupMarkupSetting.md) | Markup settings by organization (structural unit). If not set for an organization, priceMarkupPercent is used | [optional] 
**maximum_store_balance_levels** | [**List[NomenclatureGroupStoreBalanceLevel]**](NomenclatureGroupStoreBalanceLevel.md) | Maximum stock levels by warehouse. For warehouses without an explicit entry, defaultMaximumStoreBalanceLevel is used | [optional] 
**minimum_store_balance_levels** | [**List[NomenclatureGroupStoreBalanceLevel]**](NomenclatureGroupStoreBalanceLevel.md) | Minimum stock levels by warehouse. For warehouses without an explicit entry, defaultMinimumStoreBalanceLevel is used | [optional] 
**name** | **str** | Group name | 
**parent_id** | **UUID** | UUID of the parent group. The list of values can be retrieved via the \&quot;Get a list of nomenclature groups\&quot; method. null - the group belongs to the root level | [optional] 
**position** | **int** | Menu position. 0 - sort by Code+Name; otherwise - sort by this value | [optional] 
**price_markup_percent** | **float** | Fixed markup (%). Stored with up to 9 decimal places | [optional] 
**tax_category_id** | **UUID** | UUID of the tax category used for the group (VAT/tax calculation). The list of values can be retrieved via the \&quot;Get a list of tax categories\&quot; method in the \&quot;Directories\&quot; category in \&quot;Finance\&quot; section | [optional] 
**visibility_filter** | [**NomenclatureGroupOrganizationFilter**](NomenclatureGroupOrganizationFilter.md) | Organization (structural unit) visibility filter. null - the group is visible in all organisations. Applies only to root groups | [optional] 

## Example

```python
from iikocloud_client.models.nomenclature_group_create_request import NomenclatureGroupCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of NomenclatureGroupCreateRequest from a JSON string
nomenclature_group_create_request_instance = NomenclatureGroupCreateRequest.from_json(json)
# print the JSON string representation of the object
print(NomenclatureGroupCreateRequest.to_json())

# convert the object into a dict
nomenclature_group_create_request_dict = nomenclature_group_create_request_instance.to_dict()
# create an instance of NomenclatureGroupCreateRequest from a dict
nomenclature_group_create_request_from_dict = NomenclatureGroupCreateRequest.from_dict(nomenclature_group_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


