# TransportStopListsAddProductsToStopListRequest

Request for add items to out-of-stock list.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **str** | Organization ID.                Can be obtained by &#x60;/organizations&#x60; operation. | 
**terminal_group_id** | **str** | Terminal group ID.                Can be obtained by &#x60;/terminal_groups&#x60; operation. | 
**items** | [**List[TransportStopListsAddProductsToStopListItem]**](TransportStopListsAddProductsToStopListItem.md) | Items for adding to out-of-stock list. | 

## Example

```python
from iikocloud_client.models.transport_stop_lists_add_products_to_stop_list_request import TransportStopListsAddProductsToStopListRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TransportStopListsAddProductsToStopListRequest from a JSON string
transport_stop_lists_add_products_to_stop_list_request_instance = TransportStopListsAddProductsToStopListRequest.from_json(json)
# print the JSON string representation of the object
print(TransportStopListsAddProductsToStopListRequest.to_json())

# convert the object into a dict
transport_stop_lists_add_products_to_stop_list_request_dict = transport_stop_lists_add_products_to_stop_list_request_instance.to_dict()
# create an instance of TransportStopListsAddProductsToStopListRequest from a dict
transport_stop_lists_add_products_to_stop_list_request_from_dict = TransportStopListsAddProductsToStopListRequest.from_dict(transport_stop_lists_add_products_to_stop_list_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


