# IikoTransportPublicApiContractsStopListsAddProductsToStopListRequest

Request for add items to out-of-stock list.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **UUID** | Organization ID.                Can be obtained by &#x60;/organizations&#x60; operation. | 
**terminal_group_id** | **UUID** | Terminal group ID.                Can be obtained by &#x60;/terminal_groups&#x60; operation. | 
**items** | [**List[IikoTransportPublicApiContractsStopListsAddProductsToStopListItem]**](IikoTransportPublicApiContractsStopListsAddProductsToStopListItem.md) | Items for adding to out-of-stock list. | 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_stop_lists_add_products_to_stop_list_request import IikoTransportPublicApiContractsStopListsAddProductsToStopListRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsStopListsAddProductsToStopListRequest from a JSON string
iiko_transport_public_api_contracts_stop_lists_add_products_to_stop_list_request_instance = IikoTransportPublicApiContractsStopListsAddProductsToStopListRequest.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsStopListsAddProductsToStopListRequest.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_stop_lists_add_products_to_stop_list_request_dict = iiko_transport_public_api_contracts_stop_lists_add_products_to_stop_list_request_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsStopListsAddProductsToStopListRequest from a dict
iiko_transport_public_api_contracts_stop_lists_add_products_to_stop_list_request_from_dict = IikoTransportPublicApiContractsStopListsAddProductsToStopListRequest.from_dict(iiko_transport_public_api_contracts_stop_lists_add_products_to_stop_list_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


