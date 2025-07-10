# TransportDiscountsProductCategoryDiscount

Product category discount details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category_id** | **str** | Category ID. | 
**category_name** | **str** | Category name. | 
**percent** | **float** | This category discount %. | 

## Example

```python
from iiko_cloud_client.models.transport_discounts_product_category_discount import TransportDiscountsProductCategoryDiscount

# TODO update the JSON string below
json = "{}"
# create an instance of TransportDiscountsProductCategoryDiscount from a JSON string
transport_discounts_product_category_discount_instance = TransportDiscountsProductCategoryDiscount.from_json(json)
# print the JSON string representation of the object
print(TransportDiscountsProductCategoryDiscount.to_json())

# convert the object into a dict
transport_discounts_product_category_discount_dict = transport_discounts_product_category_discount_instance.to_dict()
# create an instance of TransportDiscountsProductCategoryDiscount from a dict
transport_discounts_product_category_discount_from_dict = TransportDiscountsProductCategoryDiscount.from_dict(transport_discounts_product_category_discount_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


