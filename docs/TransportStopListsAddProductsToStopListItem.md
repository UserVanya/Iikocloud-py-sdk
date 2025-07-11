# TransportStopListsAddProductsToStopListItem

Item for add to out-of-stock list.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_id** | **str** | Out-of-stock list product ID. | 
**size_id** | **str** | Out-of-stock list product size ID. | [optional] 
**balance** | **float** | Product balance. | 

## Example

```python
from iikocloud_client.models.transport_stop_lists_add_products_to_stop_list_item import TransportStopListsAddProductsToStopListItem

# TODO update the JSON string below
json = "{}"
# create an instance of TransportStopListsAddProductsToStopListItem from a JSON string
transport_stop_lists_add_products_to_stop_list_item_instance = TransportStopListsAddProductsToStopListItem.from_json(json)
# print the JSON string representation of the object
print(TransportStopListsAddProductsToStopListItem.to_json())

# convert the object into a dict
transport_stop_lists_add_products_to_stop_list_item_dict = transport_stop_lists_add_products_to_stop_list_item_instance.to_dict()
# create an instance of TransportStopListsAddProductsToStopListItem from a dict
transport_stop_lists_add_products_to_stop_list_item_from_dict = TransportStopListsAddProductsToStopListItem.from_dict(transport_stop_lists_add_products_to_stop_list_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


