# IikoTransportPublicApiContractsStopListsStopListItem

Out-of-stock list.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**balance** | **float** | Product balance. | 
**product_id** | **UUID** | Out-of-stock list product ID. | 
**size_id** | **UUID** | Product size. | [optional] 
**sku** | **str** | Stock keeping unit. | [optional] 
**date_add** | **str** | Date the product was added to the out-of-stock list (UTC). | [optional] 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_stop_lists_stop_list_item import IikoTransportPublicApiContractsStopListsStopListItem

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsStopListsStopListItem from a JSON string
iiko_transport_public_api_contracts_stop_lists_stop_list_item_instance = IikoTransportPublicApiContractsStopListsStopListItem.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsStopListsStopListItem.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_stop_lists_stop_list_item_dict = iiko_transport_public_api_contracts_stop_lists_stop_list_item_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsStopListsStopListItem from a dict
iiko_transport_public_api_contracts_stop_lists_stop_list_item_from_dict = IikoTransportPublicApiContractsStopListsStopListItem.from_dict(iiko_transport_public_api_contracts_stop_lists_stop_list_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


