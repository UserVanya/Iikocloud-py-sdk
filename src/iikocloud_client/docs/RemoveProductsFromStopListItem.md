# RemoveProductsFromStopListItem

Item for remove from out-of-stock list.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_id** | **UUID** | Out-of-stock list product ID. | 
**size_id** | **UUID** | Out-of-stock list product size ID. | [optional] 

## Example

```python
from iikocloud_client.models.remove_products_from_stop_list_item import RemoveProductsFromStopListItem

# TODO update the JSON string below
json = "{}"
# create an instance of RemoveProductsFromStopListItem from a JSON string
remove_products_from_stop_list_item_instance = RemoveProductsFromStopListItem.from_json(json)
# print the JSON string representation of the object
print(RemoveProductsFromStopListItem.to_json())

# convert the object into a dict
remove_products_from_stop_list_item_dict = remove_products_from_stop_list_item_instance.to_dict()
# create an instance of RemoveProductsFromStopListItem from a dict
remove_products_from_stop_list_item_from_dict = RemoveProductsFromStopListItem.from_dict(remove_products_from_stop_list_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


