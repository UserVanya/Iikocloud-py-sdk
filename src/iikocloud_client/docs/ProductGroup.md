# ProductGroup

Item category.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | ID. | 
**name** | **str** | Name. | 

## Example

```python
from iikocloud_client.models.product_group import ProductGroup

# TODO update the JSON string below
json = "{}"
# create an instance of ProductGroup from a JSON string
product_group_instance = ProductGroup.from_json(json)
# print the JSON string representation of the object
print(ProductGroup.to_json())

# convert the object into a dict
product_group_dict = product_group_instance.to_dict()
# create an instance of ProductGroup from a dict
product_group_from_dict = ProductGroup.from_dict(product_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


