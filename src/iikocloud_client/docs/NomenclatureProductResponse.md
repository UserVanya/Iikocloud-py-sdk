# NomenclatureProductResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accounting_category_id** | **UUID** | UUID of the accounting category (as configured in the accounting settings) | [optional] 
**alcohol_class** | **str** | Alcohol product class | [optional] 
**allergen_group_ids** | **List[UUID]** | UUIDs of allergen groups. The list of values can be retrieved via the \&quot;Get a list of allergen groups\&quot; method in the \&quot;Directories\&quot; category | [optional] 
**amount_independent_of_parent_amount** | **bool** | The amount does not depend on the parent dish&#39;s amount | [optional] 
**amount_unit_id** | **UUID** | UUID of the product&#39;s unit of measure (mainUnit). The list of values can be retrieved via the \&quot;Get a list of amount units\&quot; method in the \&quot;Directories\&quot; category | [optional] 
**assembly_chart_modified_at** | **str** | Date the assembly chart (dish build) was last modified. ISO 8601 | [optional] 
**barcodes** | [**List[NomenclatureProductBarcode]**](NomenclatureProductBarcode.md) | Product barcodes | [optional] 
**can_buy_from_cashdesk** | **bool** | Can be sold directly from the cash desk | [optional] 
**can_change_amount_cooked_dish** | **bool** | The amount of the cooked dish can be changed | [optional] 
**can_set_open_price** | **bool** | An open price can be set manually | [optional] 
**category_id** | **UUID** | UUID of the product (custom) category. The list of values can be retrieved via the \&quot;Get a list of product categories\&quot; method in the \&quot;Product categories\&quot; category | [optional] 
**cheque_printable** | **bool** | Print on the cheque | [optional] 
**code** | **str** | Product code: 0–8 digits | [optional] 
**cold_loss_percent** | **float** | Weight loss percentage during cold processing | [optional] 
**color** | [**NomenclatureProductRGBColor**](NomenclatureProductRGBColor.md) | Background button colour for POS | [optional] 
**containers** | [**List[NomenclatureProductContainer]**](NomenclatureProductContainer.md) | Product containers/packagings | [optional] 
**cook_with_main_dish** | **bool** | Cook together with the main dish | [optional] 
**cooking_time_normal** | **int** | Cooking time in normal mode, minutes | [optional] 
**cooking_time_peak** | **int** | Cooking time in peak mode, minutes | [optional] 
**cooking_type** | **str** | Cooking method | [optional] 
**created_at** | **str** | Object creation date. ISO 8601 | [optional] 
**created_by_user_id** | **UUID** | UUID of the user who created the object | [optional] 
**custom_categories** | [**List[NomenclatureProductCustomCategory]**](NomenclatureProductCustomCategory.md) | Custom nomenclature categories. Empty array or null - no categories set | [optional] 
**default_container_id** | **UUID** | UUID of the default container. The list of values can be retrieved via the \&quot;Get a list of containers\&quot; method in the \&quot;Directories\&quot; category | [optional] 
**default_course** | **int** | Default serving course. null - not set; 0 - VIP course; otherwise - course number | [optional] 
**default_included_in_menu** | **bool** | Include the product in the menu by default | [optional] 
**default_maximum_store_balance_level** | **float** | Default maximum stock level | [optional] 
**default_minimum_store_balance_level** | **float** | Default minimum stock level | [optional] 
**default_sale_price** | **float** | Default sale price | [optional] 
**deleted_at** | **str** | Deletion date. null - for non-deleted objects and for those deleted before v4.3.2. ISO 8601 | [optional] 
**description** | **str** | Product description | [optional] 
**description_english** | **str** | Product description in English | [optional] 
**disabled_fields** | **List[str]** | List of fields locked for editing (e.g. by the Franchise master nomenclature) | [optional] 
**disabled_product_size_ids** | **List[UUID]** | UUIDs of the dish sizes disabled for this product. The list of values can be retrieved via the \&quot;Get a list of product sizes\&quot; method in the \&quot;Directories\&quot; category | [optional] 
**egais_alc_code** | **str** | EGAIS product type code | [optional] 
**estimated_purchase_price** | **float** | Estimated purchase price | [optional] 
**excluded_section_ids** | **List[UUID]** | UUIDs of the menu sections the product is excluded from. The list of values can be retrieved via the \&quot;Get a list of menu sections\&quot; method in the \&quot;Directories\&quot; category | [optional] 
**expiration_date** | **int** | Shelf life, days | [optional] 
**font_color** | [**NomenclatureProductRGBColor**](NomenclatureProductRGBColor.md) | Font colour on the button for POS | [optional] 
**franchise_master_id** | **UUID** | UUID of the parent entity in the Franchise master nomenclature from which this one was last updated | [optional] 
**franchise_unique_id** | **UUID** | Globally unique UUID of the entity within Franchise | [optional] 
**front_image_id** | **UUID** | UUID of the image for POS | [optional] 
**full_name** | **str** | Full product name | [optional] 
**full_name_english** | **str** | Full product name in English | [optional] 
**gtin** | **str** | Global Trade Item Number (GTIN) | [optional] 
**hot_loss_percent** | **float** | Weight loss percentage during hot processing | [optional] 
**images** | [**List[NomenclatureProductImage]**](NomenclatureProductImage.md) | Product quality certificates | [optional] 
**invoice_supplier_id** | **UUID** | UUID of the default supplier (counterparty) for incoming invoices of this product. The list of values can be retrieved via the \&quot;Get counteragents list\&quot; method in the \&quot;Counteragents\&quot; category in \&quot;Inventory\&quot; section | [optional] 
**is_calculate_unit_weight** | **bool** | Calculate unit weight automatically | [optional] 
**is_deleted** | **bool** | Deletion flag | [optional] 
**is_dish_of_day** | **bool** | Dish of the day | [optional] 
**is_fixed_price** | **bool** | Price is set explicitly and does not depend on markup | [optional] 
**is_flyer_program** | **bool** | Participates in the flyer programme | [optional] 
**is_not_in_store_movement** | **bool** | Not included in warehouse stock movement | [optional] 
**is_nutrition_value_auto_calculated** | **bool** | Nutrition value is calculated automatically | [optional] 
**is_percentage_of_alcohol_applicable** | **bool** | Alcohol content is applicable to this product | [optional] 
**is_time_pay_product** | **bool** | Time-pay service product (time-based billing) | [optional] 
**item_category_id** | **UUID** | Item category (for fiscalisation/accounting) of the product. The list of values can be retrieved via the \&quot;Get a list of fiscal categories\&quot; method in the \&quot;Directories\&quot; category in \&quot;Finance\&quot; section | [optional] 
**last_modify_node_id** | **UUID** | UUID of the node (ServerNode) of the last change. null - last edit was on the current server | [optional] 
**markup_settings** | [**List[NomenclatureProductMarkupSetting]**](NomenclatureProductMarkupSetting.md) | Markup settings by organization (structural unit). If not set for an organization, priceMarkupPercent is used | [optional] 
**maximum_store_balance_levels** | [**List[NomenclatureProductStoreBalanceLevel]**](NomenclatureProductStoreBalanceLevel.md) | Maximum stock levels by warehouse. For warehouses without an explicit entry, defaultMaximumStoreBalanceLevel is used | [optional] 
**minimum_store_balance_levels** | [**List[NomenclatureProductStoreBalanceLevel]**](NomenclatureProductStoreBalanceLevel.md) | Minimum stock levels by warehouse. For warehouses without an explicit entry, defaultMinimumStoreBalanceLevel is used | [optional] 
**minimum_time_pay_product_duration_minutes** | **int** | Minimum duration of the time-pay service, minutes | [optional] 
**modified_at** | **str** | Date of the last modification. ISO 8601 | [optional] 
**modified_by_user_id** | **UUID** | UUID of the last user who modified the object | [optional] 
**modifier_schema_id** | **UUID** | UUID of the modifier schema. The list of values can be retrieved via the \&quot;Get a list of modifier schemas\&quot; method in the \&quot;Directories\&quot; category | [optional] 
**modifier_schema_redefinitions** | [**List[NomenclatureProductModifierSchemaRedefinition]**](NomenclatureProductModifierSchemaRedefinition.md) | Modifier schema value redefinitions for this product | [optional] 
**modifiers** | [**List[NomenclatureProductModifier]**](NomenclatureProductModifier.md) | Top-level dish modifiers | [optional] 
**name** | **str** | Product name | [optional] 
**name_english** | **str** | Product name in English | [optional] 
**name_kitchen** | **str** | Name for the kitchen screen/printer | [optional] 
**nutrition_values** | [**List[NomenclatureProductNutritionValue]**](NomenclatureProductNutritionValue.md) | Nutrition values by organization (structural unit) and dish size | [optional] 
**outer_economic_activity_nomenclature_code** | **str** | Foreign economic activity commodity nomenclature code (TN VED) | [optional] 
**parent_group_id** | **UUID** | UUID of the parent nomenclature group. The list of values can be retrieved via the \&quot;Get a list of nomenclature groups\&quot; method. null - the product belongs to the root level | [optional] 
**percentage_of_alcohol** | **float** | Alcohol content, % | [optional] 
**place_type_id** | **UUID** | Place of preparation/sale type. The list of values can be retrieved via the \&quot;Get a list of preparation place types\&quot; method in the \&quot;Directories\&quot; category | [optional] 
**position** | **int** | Menu position. 0 - sort by Code+Name; otherwise - sort by this value | [optional] 
**precheque_printable** | **bool** | Print on the pre-cheque | [optional] 
**price_markup_percent** | **float** | Fixed markup (%). Stored with up to 9 decimal places | [optional] 
**print_on_add** | **bool** | Print when added to the order | [optional] 
**producer_ids** | **List[UUID]** | UUIDs of the product&#39;s manufacturers. The list of values can be retrieved via the \&quot;Get a list of producers\&quot; method in the \&quot;Directories\&quot; category | [optional] 
**product_article** | **str** | Product article (num). If null or not provided, it will be assigned automatically by the API server | [optional] 
**product_id** | **UUID** | UUID of the nomenclature product | [optional] 
**product_scale_id** | **UUID** | UUID of the dish size scale. The list of values can be retrieved via the \&quot;Get a list of product size scales\&quot; method in the \&quot;Size scales\&quot; category | [optional] 
**product_size_factors** | [**NomenclatureProductSizeFactors**](NomenclatureProductSizeFactors.md) | Write-off factor table by dish size | [optional] 
**product_tag_ids** | **List[UUID]** | UUIDs of product tags. The list of values can be retrieved via the \&quot;Get a list of product tags\&quot; method in the \&quot;Directories\&quot; category | [optional] 
**product_type_for_cooking** | **str** | Product type for kitchen preparation | [optional] 
**rate_schedule** | [**NomenclatureProductRateSchedule**](NomenclatureProductRateSchedule.md) | Time-pay service rate schedule | [optional] 
**relative_rate_schedule** | **bool** | The rate schedule is relative (anchored to the start of the service rather than the time of day) | [optional] 
**revision** | **int** | Revision number of the last modification | [optional] 
**source_nature** | **str** | Raw material nature | [optional] 
**system** | **bool** | System object. System objects cannot be edited by users | [optional] 
**tax_category_id** | **UUID** | UUID of the tax category used for the product (VAT/tax calculation). The list of values can be retrieved via the \&quot;Get a list of tax categories\&quot; method in the \&quot;Directories\&quot; category in \&quot;Finance\&quot; section | [optional] 
**time_pay_product_duration_step_minutes** | **int** | Billing step of the time-pay service, minutes | [optional] 
**transfer_type** | **str** | Item transfer type | [optional] 
**type** | **str** | Product type: GOODS (goods/ingredients), DISH (dishes), PREPARED (semi-prepared items), SERVICE (services), MODIFIER (modifiers), OUTER, RATE, PETROL | [optional] 
**unit_capacity** | **float** | Volume of a product unit | [optional] 
**unit_weight** | **float** | Weight of a product unit | [optional] 
**use_balance_for_inventory** | **bool** | Use stock balance during inventory | [optional] 
**use_balance_for_sell** | **bool** | Use stock balance when selling | [optional] 
**use_default_cooking_time** | **bool** | Use the default cooking time | [optional] 
**use_range_for_invoices** | **bool** | Use a price range in invoices | [optional] 
**uz_fiscal_code** | **str** | Fiscal code of the product for Uzbekistan | [optional] 

## Example

```python
from iikocloud_client.models.nomenclature_product_response import NomenclatureProductResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NomenclatureProductResponse from a JSON string
nomenclature_product_response_instance = NomenclatureProductResponse.from_json(json)
# print the JSON string representation of the object
print(NomenclatureProductResponse.to_json())

# convert the object into a dict
nomenclature_product_response_dict = nomenclature_product_response_instance.to_dict()
# create an instance of NomenclatureProductResponse from a dict
nomenclature_product_response_from_dict = NomenclatureProductResponse.from_dict(nomenclature_product_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


