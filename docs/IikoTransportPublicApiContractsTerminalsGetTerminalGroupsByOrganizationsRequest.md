# IikoTransportPublicApiContractsTerminalsGetTerminalGroupsByOrganizationsRequest

Request for list of terminal groups.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_ids** | **List[UUID]** | Organizations IDs for which information is requested.                 Can be obtained by &#x60;/organizations&#x60; operation. | 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_terminals_get_terminal_groups_by_organizations_request import IikoTransportPublicApiContractsTerminalsGetTerminalGroupsByOrganizationsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsTerminalsGetTerminalGroupsByOrganizationsRequest from a JSON string
iiko_transport_public_api_contracts_terminals_get_terminal_groups_by_organizations_request_instance = IikoTransportPublicApiContractsTerminalsGetTerminalGroupsByOrganizationsRequest.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsTerminalsGetTerminalGroupsByOrganizationsRequest.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_terminals_get_terminal_groups_by_organizations_request_dict = iiko_transport_public_api_contracts_terminals_get_terminal_groups_by_organizations_request_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsTerminalsGetTerminalGroupsByOrganizationsRequest from a dict
iiko_transport_public_api_contracts_terminals_get_terminal_groups_by_organizations_request_from_dict = IikoTransportPublicApiContractsTerminalsGetTerminalGroupsByOrganizationsRequest.from_dict(iiko_transport_public_api_contracts_terminals_get_terminal_groups_by_organizations_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


