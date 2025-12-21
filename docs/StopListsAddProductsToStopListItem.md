# StopListsAddProductsToStopListItem

Item for add to out-of-stock list.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_id** | **UUID** | Out-of-stock list product ID. | 
**size_id** | **UUID** | Out-of-stock list product size ID. | [optional] 
**balance** | **float** | Product balance. | 

## Example

```python
from iikocloud_client.models.stop_lists_add_products_to_stop_list_item import StopListsAddProductsToStopListItem

# TODO update the JSON string below
json = "{}"
# create an instance of StopListsAddProductsToStopListItem from a JSON string
stop_lists_add_products_to_stop_list_item_instance = StopListsAddProductsToStopListItem.from_json(json)
# print the JSON string representation of the object
print(StopListsAddProductsToStopListItem.to_json())

# convert the object into a dict
stop_lists_add_products_to_stop_list_item_dict = stop_lists_add_products_to_stop_list_item_instance.to_dict()
# create an instance of StopListsAddProductsToStopListItem from a dict
stop_lists_add_products_to_stop_list_item_from_dict = StopListsAddProductsToStopListItem.from_dict(stop_lists_add_products_to_stop_list_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


