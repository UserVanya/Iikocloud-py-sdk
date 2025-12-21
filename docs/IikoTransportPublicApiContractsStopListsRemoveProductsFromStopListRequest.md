# IikoTransportPublicApiContractsStopListsRemoveProductsFromStopListRequest

Request for remove items from out-of-stock list.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **UUID** | Organization ID.                Can be obtained by &#x60;/organizations&#x60; operation. | 
**terminal_group_id** | **UUID** | Terminal group ID.                Can be obtained by &#x60;/terminal_groups&#x60; operation. | 
**items** | [**List[IikoTransportPublicApiContractsStopListsRemoveProductsFromStopListItem]**](IikoTransportPublicApiContractsStopListsRemoveProductsFromStopListItem.md) | Items for removing from out-of-stock list. | 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_stop_lists_remove_products_from_stop_list_request import IikoTransportPublicApiContractsStopListsRemoveProductsFromStopListRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsStopListsRemoveProductsFromStopListRequest from a JSON string
iiko_transport_public_api_contracts_stop_lists_remove_products_from_stop_list_request_instance = IikoTransportPublicApiContractsStopListsRemoveProductsFromStopListRequest.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsStopListsRemoveProductsFromStopListRequest.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_stop_lists_remove_products_from_stop_list_request_dict = iiko_transport_public_api_contracts_stop_lists_remove_products_from_stop_list_request_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsStopListsRemoveProductsFromStopListRequest from a dict
iiko_transport_public_api_contracts_stop_lists_remove_products_from_stop_list_request_from_dict = IikoTransportPublicApiContractsStopListsRemoveProductsFromStopListRequest.from_dict(iiko_transport_public_api_contracts_stop_lists_remove_products_from_stop_list_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


