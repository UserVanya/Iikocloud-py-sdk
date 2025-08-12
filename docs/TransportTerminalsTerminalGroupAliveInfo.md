# TransportTerminalsTerminalGroupAliveInfo

DTO containing terminal group availability details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_alive** | **bool** | Attribute that shows whether a terminal is available to request processing. | 
**terminal_group_id** | **str** | ID of front group of terminals.                Can be obtained by &#x60;/terminal_groups&#x60; operation. | 
**organization_id** | **str** | Organizations ID.                Can be obtained by &#x60;/organizations&#x60; operation. | 

## Example

```python
from iikocloud_client.models.transport_terminals_terminal_group_alive_info import TransportTerminalsTerminalGroupAliveInfo

# TODO update the JSON string below
json = "{}"
# create an instance of TransportTerminalsTerminalGroupAliveInfo from a JSON string
transport_terminals_terminal_group_alive_info_instance = TransportTerminalsTerminalGroupAliveInfo.from_json(json)
# print the JSON string representation of the object
print(TransportTerminalsTerminalGroupAliveInfo.to_json())

# convert the object into a dict
transport_terminals_terminal_group_alive_info_dict = transport_terminals_terminal_group_alive_info_instance.to_dict()
# create an instance of TransportTerminalsTerminalGroupAliveInfo from a dict
transport_terminals_terminal_group_alive_info_from_dict = TransportTerminalsTerminalGroupAliveInfo.from_dict(transport_terminals_terminal_group_alive_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


