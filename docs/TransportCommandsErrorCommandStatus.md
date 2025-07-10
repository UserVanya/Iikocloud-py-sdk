# TransportCommandsErrorCommandStatus

Command completed with error.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exception** | **object** | Occured exception details. | [optional] 

## Example

```python
from iiko_cloud_client.models.transport_commands_error_command_status import TransportCommandsErrorCommandStatus

# TODO update the JSON string below
json = "{}"
# create an instance of TransportCommandsErrorCommandStatus from a JSON string
transport_commands_error_command_status_instance = TransportCommandsErrorCommandStatus.from_json(json)
# print the JSON string representation of the object
print(TransportCommandsErrorCommandStatus.to_json())

# convert the object into a dict
transport_commands_error_command_status_dict = transport_commands_error_command_status_instance.to_dict()
# create an instance of TransportCommandsErrorCommandStatus from a dict
transport_commands_error_command_status_from_dict = TransportCommandsErrorCommandStatus.from_dict(transport_commands_error_command_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


