# TransportTerminalsTerminalGroupsIsAliveResponse

DTO containing terminal group availability details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **str** | Operation ID. | 
**is_alive_status** | [**List[TransportTerminalsTerminalGroupAliveInfo]**](TransportTerminalsTerminalGroupAliveInfo.md) | Availability attribute of each requested terminal. | 

## Example

```python
from iikocloud_client.models.transport_terminals_terminal_groups_is_alive_response import TransportTerminalsTerminalGroupsIsAliveResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TransportTerminalsTerminalGroupsIsAliveResponse from a JSON string
transport_terminals_terminal_groups_is_alive_response_instance = TransportTerminalsTerminalGroupsIsAliveResponse.from_json(json)
# print the JSON string representation of the object
print(TransportTerminalsTerminalGroupsIsAliveResponse.to_json())

# convert the object into a dict
transport_terminals_terminal_groups_is_alive_response_dict = transport_terminals_terminal_groups_is_alive_response_instance.to_dict()
# create an instance of TransportTerminalsTerminalGroupsIsAliveResponse from a dict
transport_terminals_terminal_groups_is_alive_response_from_dict = TransportTerminalsTerminalGroupsIsAliveResponse.from_dict(transport_terminals_terminal_groups_is_alive_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


