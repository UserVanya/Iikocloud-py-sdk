# TerminalsTerminalGroupsResponse

DTO containing terminal groups details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **UUID** | Operation ID. | 
**terminal_groups** | [**List[WrapperTerminalsTerminalGroup]**](WrapperTerminalsTerminalGroup.md) | List of terminal groups broken down by organizations. | 
**terminal_groups_in_sleep** | [**List[WrapperTerminalsTerminalGroup]**](WrapperTerminalsTerminalGroup.md) | Terminal groups are in sleep mode because they are not active.    Can be awakened by &#x60;/api/1/terminal_groups/awake&#x60; operation. | 

## Example

```python
from iikocloud_client.models.terminals_terminal_groups_response import TerminalsTerminalGroupsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TerminalsTerminalGroupsResponse from a JSON string
terminals_terminal_groups_response_instance = TerminalsTerminalGroupsResponse.from_json(json)
# print the JSON string representation of the object
print(TerminalsTerminalGroupsResponse.to_json())

# convert the object into a dict
terminals_terminal_groups_response_dict = terminals_terminal_groups_response_instance.to_dict()
# create an instance of TerminalsTerminalGroupsResponse from a dict
terminals_terminal_groups_response_from_dict = TerminalsTerminalGroupsResponse.from_dict(terminals_terminal_groups_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


