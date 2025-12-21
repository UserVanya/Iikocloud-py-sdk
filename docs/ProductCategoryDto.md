# ProductCategoryDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**is_deleted** | **bool** |  | [optional] [default to False]

## Example

```python
from iikocloud_client.models.product_category_dto import ProductCategoryDto

# TODO update the JSON string below
json = "{}"
# create an instance of ProductCategoryDto from a JSON string
product_category_dto_instance = ProductCategoryDto.from_json(json)
# print the JSON string representation of the object
print(ProductCategoryDto.to_json())

# convert the object into a dict
product_category_dto_dict = product_category_dto_instance.to_dict()
# create an instance of ProductCategoryDto from a dict
product_category_dto_from_dict = ProductCategoryDto.from_dict(product_category_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


