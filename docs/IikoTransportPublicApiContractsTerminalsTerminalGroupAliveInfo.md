# IikoTransportPublicApiContractsTerminalsTerminalGroupAliveInfo

DTO containing terminal group availability details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_alive** | **bool** | Attribute that shows whether a terminal is available to request processing. | 
**terminal_group_id** | **UUID** | ID of front group of terminals.                Can be obtained by &#x60;/terminal_groups&#x60; operation. | 
**organization_id** | **UUID** | Organizations ID.                Can be obtained by &#x60;/organizations&#x60; operation. | 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_terminals_terminal_group_alive_info import IikoTransportPublicApiContractsTerminalsTerminalGroupAliveInfo

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsTerminalsTerminalGroupAliveInfo from a JSON string
iiko_transport_public_api_contracts_terminals_terminal_group_alive_info_instance = IikoTransportPublicApiContractsTerminalsTerminalGroupAliveInfo.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsTerminalsTerminalGroupAliveInfo.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_terminals_terminal_group_alive_info_dict = iiko_transport_public_api_contracts_terminals_terminal_group_alive_info_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsTerminalsTerminalGroupAliveInfo from a dict
iiko_transport_public_api_contracts_terminals_terminal_group_alive_info_from_dict = IikoTransportPublicApiContractsTerminalsTerminalGroupAliveInfo.from_dict(iiko_transport_public_api_contracts_terminals_terminal_group_alive_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


