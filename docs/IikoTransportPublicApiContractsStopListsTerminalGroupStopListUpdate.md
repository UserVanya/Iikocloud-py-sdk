# IikoTransportPublicApiContractsStopListsTerminalGroupStopListUpdate

Out-of-stock list update for a group of front terminals.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Terminal ID. | 
**is_full** | **bool** | Whether out-of-stock list is fully updated. | 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_stop_lists_terminal_group_stop_list_update import IikoTransportPublicApiContractsStopListsTerminalGroupStopListUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsStopListsTerminalGroupStopListUpdate from a JSON string
iiko_transport_public_api_contracts_stop_lists_terminal_group_stop_list_update_instance = IikoTransportPublicApiContractsStopListsTerminalGroupStopListUpdate.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsStopListsTerminalGroupStopListUpdate.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_stop_lists_terminal_group_stop_list_update_dict = iiko_transport_public_api_contracts_stop_lists_terminal_group_stop_list_update_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsStopListsTerminalGroupStopListUpdate from a dict
iiko_transport_public_api_contracts_stop_lists_terminal_group_stop_list_update_from_dict = IikoTransportPublicApiContractsStopListsTerminalGroupStopListUpdate.from_dict(iiko_transport_public_api_contracts_stop_lists_terminal_group_stop_list_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


