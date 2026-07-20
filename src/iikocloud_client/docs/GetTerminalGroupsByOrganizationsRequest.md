# GetTerminalGroupsByOrganizationsRequest

Request for list of terminal groups.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_ids** | **List[UUID]** | Organizations IDs for which information is requested.                 Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 

## Example

```python
from iikocloud_client.models.get_terminal_groups_by_organizations_request import GetTerminalGroupsByOrganizationsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetTerminalGroupsByOrganizationsRequest from a JSON string
get_terminal_groups_by_organizations_request_instance = GetTerminalGroupsByOrganizationsRequest.from_json(json)
# print the JSON string representation of the object
print(GetTerminalGroupsByOrganizationsRequest.to_json())

# convert the object into a dict
get_terminal_groups_by_organizations_request_dict = get_terminal_groups_by_organizations_request_instance.to_dict()
# create an instance of GetTerminalGroupsByOrganizationsRequest from a dict
get_terminal_groups_by_organizations_request_from_dict = GetTerminalGroupsByOrganizationsRequest.from_dict(get_terminal_groups_by_organizations_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


