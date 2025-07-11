# TransportTerminalsAwakeTerminalGroupsResponse

Response for request to awake terminal groups from sleep mode.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**successfully_processed** | **List[str]** | Identifiers of successfully processed terminal groups. | [optional] 
**failed_processed** | **List[str]** | Identifiers of terminal groups whose processing failed. | [optional] 

## Example

```python
from iikocloud_client.models.transport_terminals_awake_terminal_groups_response import TransportTerminalsAwakeTerminalGroupsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TransportTerminalsAwakeTerminalGroupsResponse from a JSON string
transport_terminals_awake_terminal_groups_response_instance = TransportTerminalsAwakeTerminalGroupsResponse.from_json(json)
# print the JSON string representation of the object
print(TransportTerminalsAwakeTerminalGroupsResponse.to_json())

# convert the object into a dict
transport_terminals_awake_terminal_groups_response_dict = transport_terminals_awake_terminal_groups_response_instance.to_dict()
# create an instance of TransportTerminalsAwakeTerminalGroupsResponse from a dict
transport_terminals_awake_terminal_groups_response_from_dict = TransportTerminalsAwakeTerminalGroupsResponse.from_dict(transport_terminals_awake_terminal_groups_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


