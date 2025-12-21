# CommandsGetCommandStatusResponse

Class containing information about command status.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | **str** |  | 

## Example

```python
from iikocloud_client.models.commands_get_command_status_response import CommandsGetCommandStatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CommandsGetCommandStatusResponse from a JSON string
commands_get_command_status_response_instance = CommandsGetCommandStatusResponse.from_json(json)
# print the JSON string representation of the object
print(CommandsGetCommandStatusResponse.to_json())

# convert the object into a dict
commands_get_command_status_response_dict = commands_get_command_status_response_instance.to_dict()
# create an instance of CommandsGetCommandStatusResponse from a dict
commands_get_command_status_response_from_dict = CommandsGetCommandStatusResponse.from_dict(commands_get_command_status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


