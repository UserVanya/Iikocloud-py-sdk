# AwakeTerminalGroupsRequest

Request to awake terminal groups from sleep mode.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_ids** | **List[UUID]** |  Organization IDs.     Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 
**terminal_group_ids** | **List[UUID]** | List of terminal groups IDs.                 Can be obtained by &#x60;/api/1/terminal_groups&#x60; operation. | 

## Example

```python
from iikocloud_client.models.awake_terminal_groups_request import AwakeTerminalGroupsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AwakeTerminalGroupsRequest from a JSON string
awake_terminal_groups_request_instance = AwakeTerminalGroupsRequest.from_json(json)
# print the JSON string representation of the object
print(AwakeTerminalGroupsRequest.to_json())

# convert the object into a dict
awake_terminal_groups_request_dict = awake_terminal_groups_request_instance.to_dict()
# create an instance of AwakeTerminalGroupsRequest from a dict
awake_terminal_groups_request_from_dict = AwakeTerminalGroupsRequest.from_dict(awake_terminal_groups_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


