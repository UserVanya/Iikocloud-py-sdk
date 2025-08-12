# TransportTerminalsGetTerminalGroupsByOrganizationsRequest

Request for list of terminal groups.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_ids** | **List[str]** | Organizations IDs for which information is requested.                 Can be obtained by &#x60;/organizations&#x60; operation. | 

## Example

```python
from iikocloud_client.models.transport_terminals_get_terminal_groups_by_organizations_request import TransportTerminalsGetTerminalGroupsByOrganizationsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TransportTerminalsGetTerminalGroupsByOrganizationsRequest from a JSON string
transport_terminals_get_terminal_groups_by_organizations_request_instance = TransportTerminalsGetTerminalGroupsByOrganizationsRequest.from_json(json)
# print the JSON string representation of the object
print(TransportTerminalsGetTerminalGroupsByOrganizationsRequest.to_json())

# convert the object into a dict
transport_terminals_get_terminal_groups_by_organizations_request_dict = transport_terminals_get_terminal_groups_by_organizations_request_instance.to_dict()
# create an instance of TransportTerminalsGetTerminalGroupsByOrganizationsRequest from a dict
transport_terminals_get_terminal_groups_by_organizations_request_from_dict = TransportTerminalsGetTerminalGroupsByOrganizationsRequest.from_dict(transport_terminals_get_terminal_groups_by_organizations_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


