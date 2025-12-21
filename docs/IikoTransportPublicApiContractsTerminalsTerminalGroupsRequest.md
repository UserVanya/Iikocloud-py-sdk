# IikoTransportPublicApiContractsTerminalsTerminalGroupsRequest

Request for list of terminal groups.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_ids** | **List[UUID]** | Organizations IDs for which information is requested.                 Can be obtained by &#x60;/organizations&#x60; operation. | 
**include_disabled** | **bool** | Attribute that shows that response contains disabled terminal groups. | [optional] 
**return_external_data** | **List[str]** | External data keys that have to be returned. | [optional] 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_terminals_terminal_groups_request import IikoTransportPublicApiContractsTerminalsTerminalGroupsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsTerminalsTerminalGroupsRequest from a JSON string
iiko_transport_public_api_contracts_terminals_terminal_groups_request_instance = IikoTransportPublicApiContractsTerminalsTerminalGroupsRequest.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsTerminalsTerminalGroupsRequest.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_terminals_terminal_groups_request_dict = iiko_transport_public_api_contracts_terminals_terminal_groups_request_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsTerminalsTerminalGroupsRequest from a dict
iiko_transport_public_api_contracts_terminals_terminal_groups_request_from_dict = IikoTransportPublicApiContractsTerminalsTerminalGroupsRequest.from_dict(iiko_transport_public_api_contracts_terminals_terminal_groups_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


