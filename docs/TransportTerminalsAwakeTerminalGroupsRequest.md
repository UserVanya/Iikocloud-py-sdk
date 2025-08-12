# TransportTerminalsAwakeTerminalGroupsRequest

Request to awake terminal groups from sleep mode.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_ids** | **List[str]** |  Organization IDs.     Can be obtained by &#x60;/organizations&#x60; operation. | 
**terminal_group_ids** | **List[str]** | List of terminal groups IDs.                 Can be obtained by &#x60;/terminal_groups&#x60; operation. | 

## Example

```python
from iikocloud_client.models.transport_terminals_awake_terminal_groups_request import TransportTerminalsAwakeTerminalGroupsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TransportTerminalsAwakeTerminalGroupsRequest from a JSON string
transport_terminals_awake_terminal_groups_request_instance = TransportTerminalsAwakeTerminalGroupsRequest.from_json(json)
# print the JSON string representation of the object
print(TransportTerminalsAwakeTerminalGroupsRequest.to_json())

# convert the object into a dict
transport_terminals_awake_terminal_groups_request_dict = transport_terminals_awake_terminal_groups_request_instance.to_dict()
# create an instance of TransportTerminalsAwakeTerminalGroupsRequest from a dict
transport_terminals_awake_terminal_groups_request_from_dict = TransportTerminalsAwakeTerminalGroupsRequest.from_dict(transport_terminals_awake_terminal_groups_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


