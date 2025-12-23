# StopListsRemoveProductsFromStopListItem

Item for remove from out-of-stock list.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_id** | **str** | Out-of-stock list product ID. | 
**size_id** | **str** | Out-of-stock list product size ID. | [optional] 

## Example

```python
from iikocloud_client.models.stop_lists_remove_products_from_stop_list_item import StopListsRemoveProductsFromStopListItem

# TODO update the JSON string below
json = "{}"
# create an instance of StopListsRemoveProductsFromStopListItem from a JSON string
stop_lists_remove_products_from_stop_list_item_instance = StopListsRemoveProductsFromStopListItem.from_json(json)
# print the JSON string representation of the object
print(StopListsRemoveProductsFromStopListItem.to_json())

# convert the object into a dict
stop_lists_remove_products_from_stop_list_item_dict = stop_lists_remove_products_from_stop_list_item_instance.to_dict()
# create an instance of StopListsRemoveProductsFromStopListItem from a dict
stop_lists_remove_products_from_stop_list_item_from_dict = StopListsRemoveProductsFromStopListItem.from_dict(stop_lists_remove_products_from_stop_list_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


