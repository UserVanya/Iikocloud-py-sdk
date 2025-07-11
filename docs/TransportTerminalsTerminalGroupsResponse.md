# TransportTerminalsTerminalGroupsResponse

DTO containing terminal groups details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **str** | Operation ID. | 
**terminal_groups** | [**List[TransportCommonRmsItemsResponseWrapperTerminalGroup]**](TransportCommonRmsItemsResponseWrapperTerminalGroup.md) | List of terminal groups broken down by organizations. | 
**terminal_groups_in_sleep** | [**List[TransportCommonRmsItemsResponseWrapperTerminalGroup]**](TransportCommonRmsItemsResponseWrapperTerminalGroup.md) | Terminal groups are in sleep mode because they are not active.    Can be awakened by &#x60;/api/1/terminal_groups/awake&#x60; operation. | 

## Example

```python
from iikocloud_client.models.transport_terminals_terminal_groups_response import TransportTerminalsTerminalGroupsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TransportTerminalsTerminalGroupsResponse from a JSON string
transport_terminals_terminal_groups_response_instance = TransportTerminalsTerminalGroupsResponse.from_json(json)
# print the JSON string representation of the object
print(TransportTerminalsTerminalGroupsResponse.to_json())

# convert the object into a dict
transport_terminals_terminal_groups_response_dict = transport_terminals_terminal_groups_response_instance.to_dict()
# create an instance of TransportTerminalsTerminalGroupsResponse from a dict
transport_terminals_terminal_groups_response_from_dict = TransportTerminalsTerminalGroupsResponse.from_dict(transport_terminals_terminal_groups_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


