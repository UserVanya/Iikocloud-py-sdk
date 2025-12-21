# IikoTransportPublicApiContractsTerminalsAwakeTerminalGroupsResponse

Response for request to awake terminal groups from sleep mode.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**successfully_processed** | **List[UUID]** | Identifiers of successfully processed terminal groups. | [optional] 
**failed_processed** | **List[UUID]** | Identifiers of terminal groups whose processing failed. | [optional] 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_terminals_awake_terminal_groups_response import IikoTransportPublicApiContractsTerminalsAwakeTerminalGroupsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsTerminalsAwakeTerminalGroupsResponse from a JSON string
iiko_transport_public_api_contracts_terminals_awake_terminal_groups_response_instance = IikoTransportPublicApiContractsTerminalsAwakeTerminalGroupsResponse.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsTerminalsAwakeTerminalGroupsResponse.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_terminals_awake_terminal_groups_response_dict = iiko_transport_public_api_contracts_terminals_awake_terminal_groups_response_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsTerminalsAwakeTerminalGroupsResponse from a dict
iiko_transport_public_api_contracts_terminals_awake_terminal_groups_response_from_dict = IikoTransportPublicApiContractsTerminalsAwakeTerminalGroupsResponse.from_dict(iiko_transport_public_api_contracts_terminals_awake_terminal_groups_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


