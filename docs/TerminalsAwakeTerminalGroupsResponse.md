# TerminalsAwakeTerminalGroupsResponse

Response for request to awake terminal groups from sleep mode.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**successfully_processed** | **List[str]** | Identifiers of successfully processed terminal groups. | [optional] 
**failed_processed** | **List[str]** | Identifiers of terminal groups whose processing failed. | [optional] 

## Example

```python
from iikocloud_client.models.terminals_awake_terminal_groups_response import TerminalsAwakeTerminalGroupsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TerminalsAwakeTerminalGroupsResponse from a JSON string
terminals_awake_terminal_groups_response_instance = TerminalsAwakeTerminalGroupsResponse.from_json(json)
# print the JSON string representation of the object
print(TerminalsAwakeTerminalGroupsResponse.to_json())

# convert the object into a dict
terminals_awake_terminal_groups_response_dict = terminals_awake_terminal_groups_response_instance.to_dict()
# create an instance of TerminalsAwakeTerminalGroupsResponse from a dict
terminals_awake_terminal_groups_response_from_dict = TerminalsAwakeTerminalGroupsResponse.from_dict(terminals_awake_terminal_groups_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


