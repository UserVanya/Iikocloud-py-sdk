# TerminalsTerminalGroupsIsAliveRequest

Request for terminal group availability details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **str** | Organization ID. Deprecated, use \&quot;organizationIds\&quot;. | [optional] 
**organization_ids** | **List[str]** |  Organization IDs.     Can be obtained by &#x60;/api/1/organizations&#x60; operation. | [optional] 
**terminal_group_ids** | **List[str]** | List of terminal groups IDs.                 Can be obtained by &#x60;/api/1/terminal_groups&#x60; operation. | 

## Example

```python
from iikocloud_client.models.terminals_terminal_groups_is_alive_request import TerminalsTerminalGroupsIsAliveRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TerminalsTerminalGroupsIsAliveRequest from a JSON string
terminals_terminal_groups_is_alive_request_instance = TerminalsTerminalGroupsIsAliveRequest.from_json(json)
# print the JSON string representation of the object
print(TerminalsTerminalGroupsIsAliveRequest.to_json())

# convert the object into a dict
terminals_terminal_groups_is_alive_request_dict = terminals_terminal_groups_is_alive_request_instance.to_dict()
# create an instance of TerminalsTerminalGroupsIsAliveRequest from a dict
terminals_terminal_groups_is_alive_request_from_dict = TerminalsTerminalGroupsIsAliveRequest.from_dict(terminals_terminal_groups_is_alive_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


