# ProductCategoryDto3


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**is_deleted** | **bool** |  | [optional] [default to False]

## Example

```python
from iikocloud_client.models.product_category_dto3 import ProductCategoryDto3

# TODO update the JSON string below
json = "{}"
# create an instance of ProductCategoryDto3 from a JSON string
product_category_dto3_instance = ProductCategoryDto3.from_json(json)
# print the JSON string representation of the object
print(ProductCategoryDto3.to_json())

# convert the object into a dict
product_category_dto3_dict = product_category_dto3_instance.to_dict()
# create an instance of ProductCategoryDto3 from a dict
product_category_dto3_from_dict = ProductCategoryDto3.from_dict(product_category_dto3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


