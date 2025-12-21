# CommandsErrorCommandStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exception** | **object** | Occured exception details. | [optional] 
**error_reason** | **str** | Error reason. | [optional] 

## Example

```python
from iikocloud_client.models.commands_error_command_status import CommandsErrorCommandStatus

# TODO update the JSON string below
json = "{}"
# create an instance of CommandsErrorCommandStatus from a JSON string
commands_error_command_status_instance = CommandsErrorCommandStatus.from_json(json)
# print the JSON string representation of the object
print(CommandsErrorCommandStatus.to_json())

# convert the object into a dict
commands_error_command_status_dict = commands_error_command_status_instance.to_dict()
# create an instance of CommandsErrorCommandStatus from a dict
commands_error_command_status_from_dict = CommandsErrorCommandStatus.from_dict(commands_error_command_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


