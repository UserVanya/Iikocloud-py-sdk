# MenuV3Modifier

Menu modifier.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allergen_group_ids** | **List[str]** | Allergen group IDs. | [optional] 
**barcodes** | [**List[BarcodeInfo]**](BarcodeInfo.md) | Barcodes. | [optional] 
**button_image_url** | **str** | Button image URL. | [optional] 
**customer_tag_groups** | [**List[CustomerTagGroupItem]**](CustomerTagGroupItem.md) | Customer tag groups. | [optional] 
**description** | **str** | Description. | [optional] 
**id** | **str** | Modifier ID. | 
**independent_quantity** | **bool** | Independent quantity. | [optional] 
**is_marked** | **bool** | Flag indicating whether the product is marked. | [optional] 
**labels** | **List[str]** | List of website tags associated with the element. May be empty or absent. | [optional] 
**nutritions** | [**Nutritions**](Nutritions.md) | Nutritional value. | [optional] 
**outer_ean_code** | **str** | External EAN code. | [optional] 
**payment_subject_code** | **str** | Payment subject code. | [optional] 
**product_category_id** | **str** | Product category ID. | [optional] 
**size_prices** | [**List[SizePriceShort]**](SizePriceShort.md) | Prices by size. | [optional] 
**sku** | **str** | SKU. | 
**tags** | **List[str]** | List of tags associated with the element. May be empty or absent. | [optional] 
**tax_category_id** | **str** | Tax category ID. | [optional] 

## Example

```python
from iikocloud_client.models.menu_v3_modifier import MenuV3Modifier

# TODO update the JSON string below
json = "{}"
# create an instance of MenuV3Modifier from a JSON string
menu_v3_modifier_instance = MenuV3Modifier.from_json(json)
# print the JSON string representation of the object
print(MenuV3Modifier.to_json())

# convert the object into a dict
menu_v3_modifier_dict = menu_v3_modifier_instance.to_dict()
# create an instance of MenuV3Modifier from a dict
menu_v3_modifier_from_dict = MenuV3Modifier.from_dict(menu_v3_modifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


