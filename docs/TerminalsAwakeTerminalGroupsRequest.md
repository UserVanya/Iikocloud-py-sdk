# TerminalsAwakeTerminalGroupsRequest

Request to awake terminal groups from sleep mode.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_ids** | **List[UUID]** |  Organization IDs.     Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 
**terminal_group_ids** | **List[UUID]** | List of terminal groups IDs.                 Can be obtained by &#x60;/api/1/terminal_groups&#x60; operation. | 

## Example

```python
from iikocloud_client.models.terminals_awake_terminal_groups_request import TerminalsAwakeTerminalGroupsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TerminalsAwakeTerminalGroupsRequest from a JSON string
terminals_awake_terminal_groups_request_instance = TerminalsAwakeTerminalGroupsRequest.from_json(json)
# print the JSON string representation of the object
print(TerminalsAwakeTerminalGroupsRequest.to_json())

# convert the object into a dict
terminals_awake_terminal_groups_request_dict = terminals_awake_terminal_groups_request_instance.to_dict()
# create an instance of TerminalsAwakeTerminalGroupsRequest from a dict
terminals_awake_terminal_groups_request_from_dict = TerminalsAwakeTerminalGroupsRequest.from_dict(terminals_awake_terminal_groups_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


