# TerminalGroupsIsAliveResponse

DTO containing terminal group availability details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **UUID** | Operation ID. | 
**is_alive_status** | [**List[TerminalGroupAliveInfo]**](TerminalGroupAliveInfo.md) | Availability attribute of each requested terminal. | 

## Example

```python
from iikocloud_client.models.terminal_groups_is_alive_response import TerminalGroupsIsAliveResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TerminalGroupsIsAliveResponse from a JSON string
terminal_groups_is_alive_response_instance = TerminalGroupsIsAliveResponse.from_json(json)
# print the JSON string representation of the object
print(TerminalGroupsIsAliveResponse.to_json())

# convert the object into a dict
terminal_groups_is_alive_response_dict = terminal_groups_is_alive_response_instance.to_dict()
# create an instance of TerminalGroupsIsAliveResponse from a dict
terminal_groups_is_alive_response_from_dict = TerminalGroupsIsAliveResponse.from_dict(terminal_groups_is_alive_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


