# ProductInfo

DTO for outside transferring of external menu item details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_info** | **str** | Additional information. | [optional] 
**can_set_open_price** | **bool** | Open price. | 
**carbohydrates_amount** | **float** | Carbohydrate per 100g. | [optional] 
**carbohydrates_full_amount** | **float** | Carbohydrate per item. | [optional] 
**code** | **str** | SKU. | [optional] 
**description** | **str** | Description. | [optional] 
**do_not_print_in_cheque** | **bool** | Do not print on bill. | [optional] 
**energy_amount** | **float** | Calories per 100g. | [optional] 
**energy_full_amount** | **float** | Calories per item. | [optional] 
**fat_amount** | **float** | Fat per 100g. | [optional] 
**fat_full_amount** | **float** | Fat per item. | [optional] 
**full_name_english** | **str** | Full name in a foreign language. | [optional] 
**group_id** | **UUID** | Stock list group in RMS. | [optional] 
**group_modifiers** | [**List[GroupModifierInfo]**](GroupModifierInfo.md) | Modifier groups. | [optional] 
**id** | **UUID** | ID. | 
**image_links** | **List[str]** | Links to images. | [optional] 
**is_deleted** | **bool** | Is-Deleted attribute. | [optional] 
**measure_unit** | **str** | Item&#39;s unit of measurement. | [optional] 
**modifier_schema_id** | **UUID** | Modifier schema&#39;s ID. | [optional] 
**modifier_schema_name** | **str** | Modifier schema&#39;s name. | [optional] 
**modifiers** | [**List[SimpleModifierInfo]**](SimpleModifierInfo.md) | Modifiers. | [optional] 
**name** | **str** | Name. | 
**order** | **int** | Product&#39;s order (priority) in menu. | [optional] 
**order_item_type** | [**OrderItemType**](OrderItemType.md) | Product or compound. Depends on modifiers scheme existence. | [optional] 
**parent_group** | **UUID** | External menu group. | [optional] 
**payment_subject** | **str** | Payment subject. | [optional] 
**product_category_id** | **UUID** | Product category in RMS. | [optional] 
**proteins_amount** | **float** | Protein per 100g. | [optional] 
**proteins_full_amount** | **float** | Protein per item. | [optional] 
**seo_description** | **str** | SEO description for client. | [optional] 
**seo_keywords** | **str** | SEO key words. | [optional] 
**seo_text** | **str** | SEO text for robots. | [optional] 
**seo_title** | **str** | SEO header. | [optional] 
**size_prices** | [**List[SizePrice]**](SizePrice.md) | Prices. | [optional] 
**splittable** | **bool** | Is product splittable. | 
**tags** | **List[str]** | Tags. | [optional] 
**type** | **str** | dish | good | modifier. | [optional] 
**use_balance_for_sell** | **bool** | Weighed product. | 
**weight** | **float** | Item weight. | [optional] 

## Example

```python
from iikocloud_client.models.product_info import ProductInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ProductInfo from a JSON string
product_info_instance = ProductInfo.from_json(json)
# print the JSON string representation of the object
print(ProductInfo.to_json())

# convert the object into a dict
product_info_dict = product_info_instance.to_dict()
# create an instance of ProductInfo from a dict
product_info_from_dict = ProductInfo.from_dict(product_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


