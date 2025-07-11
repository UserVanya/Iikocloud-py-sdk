# TransportCommandsGetCommandStatusResponse

Class containing information about command status.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | **str** |  | 

## Example

```python
from iikocloud_client.models.transport_commands_get_command_status_response import TransportCommandsGetCommandStatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TransportCommandsGetCommandStatusResponse from a JSON string
transport_commands_get_command_status_response_instance = TransportCommandsGetCommandStatusResponse.from_json(json)
# print the JSON string representation of the object
print(TransportCommandsGetCommandStatusResponse.to_json())

# convert the object into a dict
transport_commands_get_command_status_response_dict = transport_commands_get_command_status_response_instance.to_dict()
# create an instance of TransportCommandsGetCommandStatusResponse from a dict
transport_commands_get_command_status_response_from_dict = TransportCommandsGetCommandStatusResponse.from_dict(transport_commands_get_command_status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


