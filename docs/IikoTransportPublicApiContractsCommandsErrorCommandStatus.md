# IikoTransportPublicApiContractsCommandsErrorCommandStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exception** | **object** | Occured exception details. | [optional] 
**error_reason** | **str** | Error reason. | [optional] 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_commands_error_command_status import IikoTransportPublicApiContractsCommandsErrorCommandStatus

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsCommandsErrorCommandStatus from a JSON string
iiko_transport_public_api_contracts_commands_error_command_status_instance = IikoTransportPublicApiContractsCommandsErrorCommandStatus.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsCommandsErrorCommandStatus.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_commands_error_command_status_dict = iiko_transport_public_api_contracts_commands_error_command_status_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsCommandsErrorCommandStatus from a dict
iiko_transport_public_api_contracts_commands_error_command_status_from_dict = IikoTransportPublicApiContractsCommandsErrorCommandStatus.from_dict(iiko_transport_public_api_contracts_commands_error_command_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


