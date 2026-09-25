# ProductSizeUpdateFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default** | **bool** | Whether this size is the default for the scale | [optional] 
**id** | **UUID** | UUID of the size (null when creating a new size inside update) | [optional] 
**name** | **str** | Name of the size | [optional] 
**priority** | **int** | Display priority (order) | [optional] 
**short_name** | **str** | Short name of the size. null is treated as empty string | [optional] 

## Example

```python
from iikocloud_client.models.product_size_update_fields import ProductSizeUpdateFields

# TODO update the JSON string below
json = "{}"
# create an instance of ProductSizeUpdateFields from a JSON string
product_size_update_fields_instance = ProductSizeUpdateFields.from_json(json)
# print the JSON string representation of the object
print(ProductSizeUpdateFields.to_json())

# convert the object into a dict
product_size_update_fields_dict = product_size_update_fields_instance.to_dict()
# create an instance of ProductSizeUpdateFields from a dict
product_size_update_fields_from_dict = ProductSizeUpdateFields.from_dict(product_size_update_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


