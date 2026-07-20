# AwakeTerminalGroupsResponse

Response for request to awake terminal groups from sleep mode.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**failed_processed** | **List[UUID]** | Identifiers of terminal groups whose processing failed. | [optional] 
**successfully_processed** | **List[UUID]** | Identifiers of successfully processed terminal groups. | [optional] 

## Example

```python
from iikocloud_client.models.awake_terminal_groups_response import AwakeTerminalGroupsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AwakeTerminalGroupsResponse from a JSON string
awake_terminal_groups_response_instance = AwakeTerminalGroupsResponse.from_json(json)
# print the JSON string representation of the object
print(AwakeTerminalGroupsResponse.to_json())

# convert the object into a dict
awake_terminal_groups_response_dict = awake_terminal_groups_response_instance.to_dict()
# create an instance of AwakeTerminalGroupsResponse from a dict
awake_terminal_groups_response_from_dict = AwakeTerminalGroupsResponse.from_dict(awake_terminal_groups_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


