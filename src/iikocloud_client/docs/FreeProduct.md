# FreeProduct

Free item to be added to order.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Code of product. Can be null. | [optional] 
**id** | **UUID** | Id of product. | [optional] 
**size** | **List[str]** | Sizes available for that product. | [optional] 
**sizes** | [**List[FreeProductSize]**](FreeProductSize.md) | Sizes with IDs available for that product. | [optional] 

## Example

```python
from iikocloud_client.models.free_product import FreeProduct

# TODO update the JSON string below
json = "{}"
# create an instance of FreeProduct from a JSON string
free_product_instance = FreeProduct.from_json(json)
# print the JSON string representation of the object
print(FreeProduct.to_json())

# convert the object into a dict
free_product_dict = free_product_instance.to_dict()
# create an instance of FreeProduct from a dict
free_product_from_dict = FreeProduct.from_dict(free_product_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


