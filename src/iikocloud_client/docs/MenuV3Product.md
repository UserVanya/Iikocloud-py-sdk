# MenuV3Product

Product.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**barcodes** | [**List[BarcodeInfo]**](BarcodeInfo.md) | Barcodes. | [optional] 
**can_set_open_price** | **bool** | Flag indicating whether open price can be set. | [optional] 
**customer_tag_groups** | [**List[CustomerTagGroupItem]**](CustomerTagGroupItem.md) | Customer tag groups. | [optional] 
**id** | **str** | Product ID. | 
**is_marked** | **bool** | Flag indicating whether the product is marked. | [optional] 
**measure_unit** | **str** | Unit of measurement. | [optional] 
**modifier_schema_id** | **str** | Modifier schema ID. | [optional] 
**modifier_schema_name** | **str** | Modifier schema name. | [optional] 
**order_item_type** | [**MenuV3OrderItemType**](MenuV3OrderItemType.md) | Order item type. | [optional] 
**outer_ean_code** | **str** | External EAN code. | [optional] 
**payment_subject_code** | **str** | Payment subject code. | [optional] 
**product_category_id** | **str** | Product category ID. | [optional] 
**sku** | **str** | SKU. | 
**splittable** | **bool** | Flag indicating whether the product is splittable. | [optional] 
**tax_category_id** | **str** | Tax category ID. | [optional] 
**type** | [**ProductType**](ProductType.md) | Product type. | [optional] 
**use_balance_for_sell** | **bool** | Use balance for sale. | [optional] 

## Example

```python
from iikocloud_client.models.menu_v3_product import MenuV3Product

# TODO update the JSON string below
json = "{}"
# create an instance of MenuV3Product from a JSON string
menu_v3_product_instance = MenuV3Product.from_json(json)
# print the JSON string representation of the object
print(MenuV3Product.to_json())

# convert the object into a dict
menu_v3_product_dict = menu_v3_product_instance.to_dict()
# create an instance of MenuV3Product from a dict
menu_v3_product_from_dict = MenuV3Product.from_dict(menu_v3_product_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


