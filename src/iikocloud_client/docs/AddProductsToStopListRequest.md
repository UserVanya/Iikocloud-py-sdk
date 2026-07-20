# AddProductsToStopListRequest

Request for add items to out-of-stock list.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[AddProductsToStopListItem]**](AddProductsToStopListItem.md) | Items for adding to out-of-stock list. | 
**organization_id** | **UUID** | Organization ID.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 
**terminal_group_id** | **UUID** | Terminal group ID.                Can be obtained by &#x60;/api/1/terminal_groups&#x60; operation. | 

## Example

```python
from iikocloud_client.models.add_products_to_stop_list_request import AddProductsToStopListRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddProductsToStopListRequest from a JSON string
add_products_to_stop_list_request_instance = AddProductsToStopListRequest.from_json(json)
# print the JSON string representation of the object
print(AddProductsToStopListRequest.to_json())

# convert the object into a dict
add_products_to_stop_list_request_dict = add_products_to_stop_list_request_instance.to_dict()
# create an instance of AddProductsToStopListRequest from a dict
add_products_to_stop_list_request_from_dict = AddProductsToStopListRequest.from_dict(add_products_to_stop_list_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


