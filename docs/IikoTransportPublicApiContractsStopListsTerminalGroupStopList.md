# IikoTransportPublicApiContractsStopListsTerminalGroupStopList

Out-of-stock list status for a group of front terminals.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**terminal_group_id** | **UUID** | Terminal ID. | [optional] 
**items** | [**List[IikoTransportPublicApiContractsStopListsStopListItem]**](IikoTransportPublicApiContractsStopListsStopListItem.md) | Out-of-stock list. | 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_stop_lists_terminal_group_stop_list import IikoTransportPublicApiContractsStopListsTerminalGroupStopList

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsStopListsTerminalGroupStopList from a JSON string
iiko_transport_public_api_contracts_stop_lists_terminal_group_stop_list_instance = IikoTransportPublicApiContractsStopListsTerminalGroupStopList.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsStopListsTerminalGroupStopList.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_stop_lists_terminal_group_stop_list_dict = iiko_transport_public_api_contracts_stop_lists_terminal_group_stop_list_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsStopListsTerminalGroupStopList from a dict
iiko_transport_public_api_contracts_stop_lists_terminal_group_stop_list_from_dict = IikoTransportPublicApiContractsStopListsTerminalGroupStopList.from_dict(iiko_transport_public_api_contracts_stop_lists_terminal_group_stop_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


