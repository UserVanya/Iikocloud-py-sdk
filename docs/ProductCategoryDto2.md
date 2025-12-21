# ProductCategoryDto2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**is_deleted** | **bool** |  | [optional] [default to False]

## Example

```python
from iikocloud_client.models.product_category_dto2 import ProductCategoryDto2

# TODO update the JSON string below
json = "{}"
# create an instance of ProductCategoryDto2 from a JSON string
product_category_dto2_instance = ProductCategoryDto2.from_json(json)
# print the JSON string representation of the object
print(ProductCategoryDto2.to_json())

# convert the object into a dict
product_category_dto2_dict = product_category_dto2_instance.to_dict()
# create an instance of ProductCategoryDto2 from a dict
product_category_dto2_from_dict = ProductCategoryDto2.from_dict(product_category_dto2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


