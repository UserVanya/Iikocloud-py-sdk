# AddProductsToStopListItem

Item for add to out-of-stock list.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**balance** | **float** | Product balance. | 
**product_id** | **UUID** | Out-of-stock list product ID. | 
**size_id** | **UUID** | Out-of-stock list product size ID. | [optional] 

## Example

```python
from iikocloud_client.models.add_products_to_stop_list_item import AddProductsToStopListItem

# TODO update the JSON string below
json = "{}"
# create an instance of AddProductsToStopListItem from a JSON string
add_products_to_stop_list_item_instance = AddProductsToStopListItem.from_json(json)
# print the JSON string representation of the object
print(AddProductsToStopListItem.to_json())

# convert the object into a dict
add_products_to_stop_list_item_dict = add_products_to_stop_list_item_instance.to_dict()
# create an instance of AddProductsToStopListItem from a dict
add_products_to_stop_list_item_from_dict = AddProductsToStopListItem.from_dict(add_products_to_stop_list_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


