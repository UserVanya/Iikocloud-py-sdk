# RemoveProductsFromStopListRequest

Request for remove items from out-of-stock list.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[RemoveProductsFromStopListItem]**](RemoveProductsFromStopListItem.md) | Items for removing from out-of-stock list. | 
**organization_id** | **UUID** | Organization ID.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 
**terminal_group_id** | **UUID** | Terminal group ID.                Can be obtained by &#x60;/api/1/terminal_groups&#x60; operation. | 

## Example

```python
from iikocloud_client.models.remove_products_from_stop_list_request import RemoveProductsFromStopListRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RemoveProductsFromStopListRequest from a JSON string
remove_products_from_stop_list_request_instance = RemoveProductsFromStopListRequest.from_json(json)
# print the JSON string representation of the object
print(RemoveProductsFromStopListRequest.to_json())

# convert the object into a dict
remove_products_from_stop_list_request_dict = remove_products_from_stop_list_request_instance.to_dict()
# create an instance of RemoveProductsFromStopListRequest from a dict
remove_products_from_stop_list_request_from_dict = RemoveProductsFromStopListRequest.from_dict(remove_products_from_stop_list_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


