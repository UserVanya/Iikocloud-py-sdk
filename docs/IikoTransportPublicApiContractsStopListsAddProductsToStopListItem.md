# IikoTransportPublicApiContractsStopListsAddProductsToStopListItem

Item for add to out-of-stock list.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_id** | **UUID** | Out-of-stock list product ID. | 
**size_id** | **UUID** | Out-of-stock list product size ID. | [optional] 
**balance** | **float** | Product balance. | 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_stop_lists_add_products_to_stop_list_item import IikoTransportPublicApiContractsStopListsAddProductsToStopListItem

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsStopListsAddProductsToStopListItem from a JSON string
iiko_transport_public_api_contracts_stop_lists_add_products_to_stop_list_item_instance = IikoTransportPublicApiContractsStopListsAddProductsToStopListItem.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsStopListsAddProductsToStopListItem.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_stop_lists_add_products_to_stop_list_item_dict = iiko_transport_public_api_contracts_stop_lists_add_products_to_stop_list_item_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsStopListsAddProductsToStopListItem from a dict
iiko_transport_public_api_contracts_stop_lists_add_products_to_stop_list_item_from_dict = IikoTransportPublicApiContractsStopListsAddProductsToStopListItem.from_dict(iiko_transport_public_api_contracts_stop_lists_add_products_to_stop_list_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


