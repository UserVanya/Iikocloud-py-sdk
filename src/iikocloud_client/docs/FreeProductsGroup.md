# FreeProductsGroup

Free item to be added to order.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description_for_user** | **str** | Description for user. Can be null. | [optional] 
**products** | [**List[FreeProduct]**](FreeProduct.md) | Products that should be added to order. | [optional] 
**source_action_id** | **UUID** | Id of action that caused the suggestion. | [optional] 

## Example

```python
from iikocloud_client.models.free_products_group import FreeProductsGroup

# TODO update the JSON string below
json = "{}"
# create an instance of FreeProductsGroup from a JSON string
free_products_group_instance = FreeProductsGroup.from_json(json)
# print the JSON string representation of the object
print(FreeProductsGroup.to_json())

# convert the object into a dict
free_products_group_dict = free_products_group_instance.to_dict()
# create an instance of FreeProductsGroup from a dict
free_products_group_from_dict = FreeProductsGroup.from_dict(free_products_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


