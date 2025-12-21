# IikoTransportPublicApiContractsTerminalsAwakeTerminalGroupsRequest

Request to awake terminal groups from sleep mode.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_ids** | **List[UUID]** |  Organization IDs.     Can be obtained by &#x60;/organizations&#x60; operation. | 
**terminal_group_ids** | **List[UUID]** | List of terminal groups IDs.                 Can be obtained by &#x60;/terminal_groups&#x60; operation. | 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_terminals_awake_terminal_groups_request import IikoTransportPublicApiContractsTerminalsAwakeTerminalGroupsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsTerminalsAwakeTerminalGroupsRequest from a JSON string
iiko_transport_public_api_contracts_terminals_awake_terminal_groups_request_instance = IikoTransportPublicApiContractsTerminalsAwakeTerminalGroupsRequest.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsTerminalsAwakeTerminalGroupsRequest.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_terminals_awake_terminal_groups_request_dict = iiko_transport_public_api_contracts_terminals_awake_terminal_groups_request_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsTerminalsAwakeTerminalGroupsRequest from a dict
iiko_transport_public_api_contracts_terminals_awake_terminal_groups_request_from_dict = IikoTransportPublicApiContractsTerminalsAwakeTerminalGroupsRequest.from_dict(iiko_transport_public_api_contracts_terminals_awake_terminal_groups_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


