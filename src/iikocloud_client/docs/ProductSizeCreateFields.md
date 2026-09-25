# ProductSizeCreateFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default** | **bool** | Whether this size is the default for the scale | [optional] 
**name** | **str** | Name of the size | [optional] 
**priority** | **int** | Display priority (order) | [optional] 
**short_name** | **str** | Short name of the size. null is treated as empty string | [optional] 

## Example

```python
from iikocloud_client.models.product_size_create_fields import ProductSizeCreateFields

# TODO update the JSON string below
json = "{}"
# create an instance of ProductSizeCreateFields from a JSON string
product_size_create_fields_instance = ProductSizeCreateFields.from_json(json)
# print the JSON string representation of the object
print(ProductSizeCreateFields.to_json())

# convert the object into a dict
product_size_create_fields_dict = product_size_create_fields_instance.to_dict()
# create an instance of ProductSizeCreateFields from a dict
product_size_create_fields_from_dict = ProductSizeCreateFields.from_dict(product_size_create_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


