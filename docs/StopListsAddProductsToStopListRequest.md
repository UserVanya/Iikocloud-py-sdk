# StopListsAddProductsToStopListRequest

Request for add items to out-of-stock list.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **UUID** | Organization ID.                Can be obtained by &#x60;/organizations&#x60; operation. | 
**terminal_group_id** | **UUID** | Terminal group ID.                Can be obtained by &#x60;/terminal_groups&#x60; operation. | 
**items** | [**List[StopListsAddProductsToStopListItem]**](StopListsAddProductsToStopListItem.md) | Items for adding to out-of-stock list. | 

## Example

```python
from iikocloud_client.models.stop_lists_add_products_to_stop_list_request import StopListsAddProductsToStopListRequest

# TODO update the JSON string below
json = "{}"
# create an instance of StopListsAddProductsToStopListRequest from a JSON string
stop_lists_add_products_to_stop_list_request_instance = StopListsAddProductsToStopListRequest.from_json(json)
# print the JSON string representation of the object
print(StopListsAddProductsToStopListRequest.to_json())

# convert the object into a dict
stop_lists_add_products_to_stop_list_request_dict = stop_lists_add_products_to_stop_list_request_instance.to_dict()
# create an instance of StopListsAddProductsToStopListRequest from a dict
stop_lists_add_products_to_stop_list_request_from_dict = StopListsAddProductsToStopListRequest.from_dict(stop_lists_add_products_to_stop_list_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


