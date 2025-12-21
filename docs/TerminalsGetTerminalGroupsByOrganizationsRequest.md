# TerminalsGetTerminalGroupsByOrganizationsRequest

Request for list of terminal groups.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_ids** | **List[UUID]** | Organizations IDs for which information is requested.                 Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 

## Example

```python
from iikocloud_client.models.terminals_get_terminal_groups_by_organizations_request import TerminalsGetTerminalGroupsByOrganizationsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TerminalsGetTerminalGroupsByOrganizationsRequest from a JSON string
terminals_get_terminal_groups_by_organizations_request_instance = TerminalsGetTerminalGroupsByOrganizationsRequest.from_json(json)
# print the JSON string representation of the object
print(TerminalsGetTerminalGroupsByOrganizationsRequest.to_json())

# convert the object into a dict
terminals_get_terminal_groups_by_organizations_request_dict = terminals_get_terminal_groups_by_organizations_request_instance.to_dict()
# create an instance of TerminalsGetTerminalGroupsByOrganizationsRequest from a dict
terminals_get_terminal_groups_by_organizations_request_from_dict = TerminalsGetTerminalGroupsByOrganizationsRequest.from_dict(terminals_get_terminal_groups_by_organizations_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


