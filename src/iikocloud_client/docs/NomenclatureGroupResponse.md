# NomenclatureGroupResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accounting_category_id** | **UUID** | UUID of the accounting category (as configured in the accounting settings) | [optional] 
**category_id** | **UUID** | UUID of the product (custom) category. The list of values can be retrieved via the \&quot;Get a list of product categories\&quot; method in the \&quot;Product categories\&quot; category | [optional] 
**code** | **str** | Group code: 0–8 digits | [optional] 
**color** | [**NomenclatureGroupRGBColor**](NomenclatureGroupRGBColor.md) | Background button colour for POS | [optional] 
**created_at** | **str** | Object creation date. ISO 8601 | [optional] 
**created_by_user_id** | **UUID** | UUID of the user who created the object | [optional] 
**custom_categories** | [**List[NomenclatureGroupCustomCategory]**](NomenclatureGroupCustomCategory.md) | Custom nomenclature categories. Empty array or null - no categories set | [optional] 
**default_course** | **int** | Default serving course. null - not set; 0 - VIP course; otherwise - course number | [optional] 
**default_maximum_store_balance_level** | **float** | Default maximum stock level | [optional] 
**default_minimum_store_balance_level** | **float** | Default minimum stock level | [optional] 
**deleted_at** | **str** | Deletion date. null - for non-deleted objects and for those deleted before v4.3.2. ISO 8601 | [optional] 
**description** | **str** | Group description | [optional] 
**font_color** | [**NomenclatureGroupRGBColor**](NomenclatureGroupRGBColor.md) | Font colour on the button for POS | [optional] 
**franchise_master_id** | **UUID** | UUID of the parent entity in the Franchise master nomenclature from which this one was last updated | [optional] 
**franchise_unique_id** | **UUID** | Globally unique UUID of the entity within Franchise | [optional] 
**front_image_id** | **UUID** | UUID of the image for POS | [optional] 
**group_article** | **str** | Group article. If null or not provided, the field remains empty | [optional] 
**group_id** | **UUID** | UUID of the nomenclature group | [optional] 
**include_in_report** | **bool** | Include in the price list print form | [optional] 
**is_chain_root** | **bool** | Whether the group is the root of a chain. Read-only | [optional] 
**is_deleted** | **bool** | Deletion flag | [optional] 
**is_fixed_price** | **bool** | Price is set explicitly and does not depend on markup | [optional] 
**last_modify_node_id** | **UUID** | UUID of the node (ServerNode) of the last change. null - last edit was on the current server | [optional] 
**markup_settings** | [**List[NomenclatureGroupMarkupSetting]**](NomenclatureGroupMarkupSetting.md) | Markup settings by organization (structural unit). If not set for an organization, priceMarkupPercent is used | [optional] 
**maximum_store_balance_levels** | [**List[NomenclatureGroupStoreBalanceLevel]**](NomenclatureGroupStoreBalanceLevel.md) | Maximum stock levels by warehouse. For warehouses without an explicit entry, defaultMaximumStoreBalanceLevel is used | [optional] 
**minimum_store_balance_levels** | [**List[NomenclatureGroupStoreBalanceLevel]**](NomenclatureGroupStoreBalanceLevel.md) | Minimum stock levels by warehouse. For warehouses without an explicit entry, defaultMinimumStoreBalanceLevel is used | [optional] 
**modified_at** | **str** | Date of the last modification. ISO 8601 | [optional] 
**modified_by_user_id** | **UUID** | UUID of the last user who modified the object | [optional] 
**name** | **str** | Group name | [optional] 
**parent_id** | **UUID** | UUID of the parent group. The list of values can be retrieved via the \&quot;Get a list of nomenclature groups\&quot; method. null - the group belongs to the root level | [optional] 
**position** | **int** | Menu position. 0 - sort by Code+Name; otherwise - sort by this value | [optional] 
**price_markup_percent** | **float** | Fixed markup (%). Stored with up to 9 decimal places | [optional] 
**revision** | **int** | Revision number of the last modification | [optional] 
**system** | **bool** | System object. System objects cannot be edited by users | [optional] 
**tax_category_id** | **UUID** | UUID of the tax category used for the group (VAT/tax calculation). The list of values can be retrieved via the \&quot;Get a list of tax categories\&quot; method in the \&quot;Directories\&quot; category in \&quot;Finance\&quot; section | [optional] 
**visibility_filter** | [**NomenclatureGroupOrganizationFilter**](NomenclatureGroupOrganizationFilter.md) | Organization (structural unit) visibility filter. null - the group is visible in all organisations. Applies only to root groups | [optional] 

## Example

```python
from iikocloud_client.models.nomenclature_group_response import NomenclatureGroupResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NomenclatureGroupResponse from a JSON string
nomenclature_group_response_instance = NomenclatureGroupResponse.from_json(json)
# print the JSON string representation of the object
print(NomenclatureGroupResponse.to_json())

# convert the object into a dict
nomenclature_group_response_dict = nomenclature_group_response_instance.to_dict()
# create an instance of NomenclatureGroupResponse from a dict
nomenclature_group_response_from_dict = NomenclatureGroupResponse.from_dict(nomenclature_group_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


