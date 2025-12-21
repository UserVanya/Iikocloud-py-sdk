# IikoTransportPublicApiContractsNomenclatureProductInfo

DTO for outside transferring of external menu item details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fat_amount** | **float** | Fat per 100g. | [optional] 
**proteins_amount** | **float** | Protein per 100g. | [optional] 
**carbohydrates_amount** | **float** | Carbohydrate per 100g. | [optional] 
**energy_amount** | **float** | Calories per 100g. | [optional] 
**fat_full_amount** | **float** | Fat per item. | [optional] 
**proteins_full_amount** | **float** | Protein per item. | [optional] 
**carbohydrates_full_amount** | **float** | Carbohydrate per item. | [optional] 
**energy_full_amount** | **float** | Calories per item. | [optional] 
**weight** | **float** | Item weight. | [optional] 
**group_id** | **UUID** | Stock list group in RMS. | [optional] 
**product_category_id** | **UUID** | Product category in RMS. | [optional] 
**type** | **str** | dish | good | modifier. | [optional] 
**order_item_type** | [**IikoTransportPublicApiContractsNomenclatureOrderItemType**](IikoTransportPublicApiContractsNomenclatureOrderItemType.md) | Product or compound. Depends on modifiers scheme existence. | [optional] 
**modifier_schema_id** | **UUID** | Modifier schema&#39;s ID. | [optional] 
**modifier_schema_name** | **str** | Modifier schema&#39;s name. | [optional] 
**splittable** | **bool** | Is product splittable. | 
**measure_unit** | **str** | Item&#39;s unit of measurement. | [optional] 
**size_prices** | [**List[IikoTransportPublicApiContractsNomenclatureSizePrice]**](IikoTransportPublicApiContractsNomenclatureSizePrice.md) | Prices. | [optional] 
**modifiers** | [**List[IikoTransportPublicApiContractsNomenclatureSimpleModifierInfo]**](IikoTransportPublicApiContractsNomenclatureSimpleModifierInfo.md) | Modifiers. | [optional] 
**group_modifiers** | [**List[IikoTransportPublicApiContractsNomenclatureGroupModifierInfo]**](IikoTransportPublicApiContractsNomenclatureGroupModifierInfo.md) | Modifier groups. | [optional] 
**image_links** | **List[str]** | Links to images. | [optional] 
**do_not_print_in_cheque** | **bool** | Do not print on bill. | [optional] 
**parent_group** | **UUID** | External menu group. | [optional] 
**order** | **int** | Product&#39;s order (priority) in menu. | [optional] 
**full_name_english** | **str** | Full name in a foreign language. | [optional] 
**use_balance_for_sell** | **bool** | Weighed product. | 
**can_set_open_price** | **bool** | Open price. | 
**payment_subject** | **str** | Payment subject. | [optional] 
**id** | **UUID** | ID. | 
**code** | **str** | SKU. | [optional] 
**name** | **str** | Name. | 
**description** | **str** | Description. | [optional] 
**additional_info** | **str** | Additional information. | [optional] 
**tags** | **List[str]** | Tags. | [optional] 
**is_deleted** | **bool** | Is-Deleted attribute. | [optional] 
**seo_description** | **str** | SEO description for client. | [optional] 
**seo_text** | **str** | SEO text for robots. | [optional] 
**seo_keywords** | **str** | SEO key words. | [optional] 
**seo_title** | **str** | SEO header. | [optional] 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_nomenclature_product_info import IikoTransportPublicApiContractsNomenclatureProductInfo

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsNomenclatureProductInfo from a JSON string
iiko_transport_public_api_contracts_nomenclature_product_info_instance = IikoTransportPublicApiContractsNomenclatureProductInfo.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsNomenclatureProductInfo.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_nomenclature_product_info_dict = iiko_transport_public_api_contracts_nomenclature_product_info_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsNomenclatureProductInfo from a dict
iiko_transport_public_api_contracts_nomenclature_product_info_from_dict = IikoTransportPublicApiContractsNomenclatureProductInfo.from_dict(iiko_transport_public_api_contracts_nomenclature_product_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


