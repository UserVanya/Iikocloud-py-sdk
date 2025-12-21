# IikoTransportPublicApiContractsTerminalsTerminalGroupsIsAliveResponse

DTO containing terminal group availability details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **UUID** | Operation ID. | 
**is_alive_status** | [**List[IikoTransportPublicApiContractsTerminalsTerminalGroupAliveInfo]**](IikoTransportPublicApiContractsTerminalsTerminalGroupAliveInfo.md) | Availability attribute of each requested terminal. | 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_terminals_terminal_groups_is_alive_response import IikoTransportPublicApiContractsTerminalsTerminalGroupsIsAliveResponse

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsTerminalsTerminalGroupsIsAliveResponse from a JSON string
iiko_transport_public_api_contracts_terminals_terminal_groups_is_alive_response_instance = IikoTransportPublicApiContractsTerminalsTerminalGroupsIsAliveResponse.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsTerminalsTerminalGroupsIsAliveResponse.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_terminals_terminal_groups_is_alive_response_dict = iiko_transport_public_api_contracts_terminals_terminal_groups_is_alive_response_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsTerminalsTerminalGroupsIsAliveResponse from a dict
iiko_transport_public_api_contracts_terminals_terminal_groups_is_alive_response_from_dict = IikoTransportPublicApiContractsTerminalsTerminalGroupsIsAliveResponse.from_dict(iiko_transport_public_api_contracts_terminals_terminal_groups_is_alive_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


