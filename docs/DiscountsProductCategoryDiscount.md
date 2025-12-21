# DiscountsProductCategoryDiscount

Product category discount details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category_id** | **UUID** | Category ID. | 
**category_name** | **str** | Category name. | 
**percent** | **float** | This category discount %. | 

## Example

```python
from iikocloud_client.models.discounts_product_category_discount import DiscountsProductCategoryDiscount

# TODO update the JSON string below
json = "{}"
# create an instance of DiscountsProductCategoryDiscount from a JSON string
discounts_product_category_discount_instance = DiscountsProductCategoryDiscount.from_json(json)
# print the JSON string representation of the object
print(DiscountsProductCategoryDiscount.to_json())

# convert the object into a dict
discounts_product_category_discount_dict = discounts_product_category_discount_instance.to_dict()
# create an instance of DiscountsProductCategoryDiscount from a dict
discounts_product_category_discount_from_dict = DiscountsProductCategoryDiscount.from_dict(discounts_product_category_discount_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


