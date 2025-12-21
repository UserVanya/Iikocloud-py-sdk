# IikoTransportPublicApiContractsTerminalsTerminalGroupsResponse

DTO containing terminal groups details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **UUID** | Operation ID. | 
**terminal_groups** | [**List[RmsItemsResponseWrapperTerminalsTerminalGroup]**](RmsItemsResponseWrapperTerminalsTerminalGroup.md) | List of terminal groups broken down by organizations. | 
**terminal_groups_in_sleep** | [**List[RmsItemsResponseWrapperTerminalsTerminalGroup]**](RmsItemsResponseWrapperTerminalsTerminalGroup.md) | Terminal groups are in sleep mode because they are not active.    Can be awakened by &#x60;/terminal_groups/awake&#x60; operation. | 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_terminals_terminal_groups_response import IikoTransportPublicApiContractsTerminalsTerminalGroupsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsTerminalsTerminalGroupsResponse from a JSON string
iiko_transport_public_api_contracts_terminals_terminal_groups_response_instance = IikoTransportPublicApiContractsTerminalsTerminalGroupsResponse.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsTerminalsTerminalGroupsResponse.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_terminals_terminal_groups_response_dict = iiko_transport_public_api_contracts_terminals_terminal_groups_response_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsTerminalsTerminalGroupsResponse from a dict
iiko_transport_public_api_contracts_terminals_terminal_groups_response_from_dict = IikoTransportPublicApiContractsTerminalsTerminalGroupsResponse.from_dict(iiko_transport_public_api_contracts_terminals_terminal_groups_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


