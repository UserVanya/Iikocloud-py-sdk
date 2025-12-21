# TerminalsTerminalGroupsIsAliveResponse

DTO containing terminal group availability details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **UUID** | Operation ID. | 
**is_alive_status** | [**List[TerminalsTerminalGroupAliveInfo]**](TerminalsTerminalGroupAliveInfo.md) | Availability attribute of each requested terminal. | 

## Example

```python
from iikocloud_client.models.terminals_terminal_groups_is_alive_response import TerminalsTerminalGroupsIsAliveResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TerminalsTerminalGroupsIsAliveResponse from a JSON string
terminals_terminal_groups_is_alive_response_instance = TerminalsTerminalGroupsIsAliveResponse.from_json(json)
# print the JSON string representation of the object
print(TerminalsTerminalGroupsIsAliveResponse.to_json())

# convert the object into a dict
terminals_terminal_groups_is_alive_response_dict = terminals_terminal_groups_is_alive_response_instance.to_dict()
# create an instance of TerminalsTerminalGroupsIsAliveResponse from a dict
terminals_terminal_groups_is_alive_response_from_dict = TerminalsTerminalGroupsIsAliveResponse.from_dict(terminals_terminal_groups_is_alive_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


