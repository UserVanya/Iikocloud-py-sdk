# CommandsGetCommandStatusRequest

Request for command status obtaining.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **UUID** | Organization id which \&quot;correlationId\&quot; belongs to.                Can be obtained by &#x60;/organizations&#x60; operation. | 
**correlation_id** | **UUID** | Operation ID obtained from any command supporting operations. | 

## Example

```python
from iikocloud_client.models.commands_get_command_status_request import CommandsGetCommandStatusRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CommandsGetCommandStatusRequest from a JSON string
commands_get_command_status_request_instance = CommandsGetCommandStatusRequest.from_json(json)
# print the JSON string representation of the object
print(CommandsGetCommandStatusRequest.to_json())

# convert the object into a dict
commands_get_command_status_request_dict = commands_get_command_status_request_instance.to_dict()
# create an instance of CommandsGetCommandStatusRequest from a dict
commands_get_command_status_request_from_dict = CommandsGetCommandStatusRequest.from_dict(commands_get_command_status_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


