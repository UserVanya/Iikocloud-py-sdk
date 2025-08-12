# TransportStopListsRemoveProductsFromStopListRequest

Request for remove items from out-of-stock list.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **str** | Organization ID.                Can be obtained by &#x60;/organizations&#x60; operation. | 
**terminal_group_id** | **str** | Terminal group ID.                Can be obtained by &#x60;/terminal_groups&#x60; operation. | 
**items** | [**List[TransportStopListsRemoveProductsFromStopListItem]**](TransportStopListsRemoveProductsFromStopListItem.md) | Items for removing from out-of-stock list. | 

## Example

```python
from iikocloud_client.models.transport_stop_lists_remove_products_from_stop_list_request import TransportStopListsRemoveProductsFromStopListRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TransportStopListsRemoveProductsFromStopListRequest from a JSON string
transport_stop_lists_remove_products_from_stop_list_request_instance = TransportStopListsRemoveProductsFromStopListRequest.from_json(json)
# print the JSON string representation of the object
print(TransportStopListsRemoveProductsFromStopListRequest.to_json())

# convert the object into a dict
transport_stop_lists_remove_products_from_stop_list_request_dict = transport_stop_lists_remove_products_from_stop_list_request_instance.to_dict()
# create an instance of TransportStopListsRemoveProductsFromStopListRequest from a dict
transport_stop_lists_remove_products_from_stop_list_request_from_dict = TransportStopListsRemoveProductsFromStopListRequest.from_dict(transport_stop_lists_remove_products_from_stop_list_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


