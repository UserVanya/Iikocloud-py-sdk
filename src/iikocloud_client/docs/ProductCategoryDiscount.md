# ProductCategoryDiscount

Product category discount details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category_id** | **UUID** | Category ID. | 
**category_name** | **str** | Category name. | 
**percent** | **float** | This category discount %. | 

## Example

```python
from iikocloud_client.models.product_category_discount import ProductCategoryDiscount

# TODO update the JSON string below
json = "{}"
# create an instance of ProductCategoryDiscount from a JSON string
product_category_discount_instance = ProductCategoryDiscount.from_json(json)
# print the JSON string representation of the object
print(ProductCategoryDiscount.to_json())

# convert the object into a dict
product_category_discount_dict = product_category_discount_instance.to_dict()
# create an instance of ProductCategoryDiscount from a dict
product_category_discount_from_dict = ProductCategoryDiscount.from_dict(product_category_discount_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


