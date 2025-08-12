# TransportTerminalsTerminalGroupsIsAliveRequest

Request for terminal group availability details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **str** | Organization ID. Deprecated, use \&quot;organizationIds\&quot;. | [optional] 
**organization_ids** | **List[str]** |  Organization IDs.     Can be obtained by &#x60;/organizations&#x60; operation. | [optional] 
**terminal_group_ids** | **List[str]** | List of terminal groups IDs.                 Can be obtained by &#x60;/terminal_groups&#x60; operation. | 

## Example

```python
from iikocloud_client.models.transport_terminals_terminal_groups_is_alive_request import TransportTerminalsTerminalGroupsIsAliveRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TransportTerminalsTerminalGroupsIsAliveRequest from a JSON string
transport_terminals_terminal_groups_is_alive_request_instance = TransportTerminalsTerminalGroupsIsAliveRequest.from_json(json)
# print the JSON string representation of the object
print(TransportTerminalsTerminalGroupsIsAliveRequest.to_json())

# convert the object into a dict
transport_terminals_terminal_groups_is_alive_request_dict = transport_terminals_terminal_groups_is_alive_request_instance.to_dict()
# create an instance of TransportTerminalsTerminalGroupsIsAliveRequest from a dict
transport_terminals_terminal_groups_is_alive_request_from_dict = TransportTerminalsTerminalGroupsIsAliveRequest.from_dict(transport_terminals_terminal_groups_is_alive_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


