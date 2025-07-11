# TransportCommandsGetCommandStatusRequest

Request for command status obtaining.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **str** | Organization id which \&quot;correlationId\&quot; belongs to.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 
**correlation_id** | **str** | Operation ID obtained from any command supporting operations. | 

## Example

```python
from iikocloud_client.models.transport_commands_get_command_status_request import TransportCommandsGetCommandStatusRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TransportCommandsGetCommandStatusRequest from a JSON string
transport_commands_get_command_status_request_instance = TransportCommandsGetCommandStatusRequest.from_json(json)
# print the JSON string representation of the object
print(TransportCommandsGetCommandStatusRequest.to_json())

# convert the object into a dict
transport_commands_get_command_status_request_dict = transport_commands_get_command_status_request_instance.to_dict()
# create an instance of TransportCommandsGetCommandStatusRequest from a dict
transport_commands_get_command_status_request_from_dict = TransportCommandsGetCommandStatusRequest.from_dict(transport_commands_get_command_status_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


