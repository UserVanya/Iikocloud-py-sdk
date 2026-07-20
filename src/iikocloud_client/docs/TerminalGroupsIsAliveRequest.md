# TerminalGroupsIsAliveRequest

Request for terminal group availability details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **UUID** | Organization ID. Deprecated, use \&quot;organizationIds\&quot;. | [optional] 
**organization_ids** | **List[UUID]** |  Organization IDs.     Can be obtained by &#x60;/api/1/organizations&#x60; operation. | [optional] 
**terminal_group_ids** | **List[UUID]** | List of terminal groups IDs.                 Can be obtained by &#x60;/api/1/terminal_groups&#x60; operation. | 

## Example

```python
from iikocloud_client.models.terminal_groups_is_alive_request import TerminalGroupsIsAliveRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TerminalGroupsIsAliveRequest from a JSON string
terminal_groups_is_alive_request_instance = TerminalGroupsIsAliveRequest.from_json(json)
# print the JSON string representation of the object
print(TerminalGroupsIsAliveRequest.to_json())

# convert the object into a dict
terminal_groups_is_alive_request_dict = terminal_groups_is_alive_request_instance.to_dict()
# create an instance of TerminalGroupsIsAliveRequest from a dict
terminal_groups_is_alive_request_from_dict = TerminalGroupsIsAliveRequest.from_dict(terminal_groups_is_alive_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


