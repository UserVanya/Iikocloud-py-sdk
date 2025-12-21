# IikoTransportPublicApiContractsCommandsGetCommandStatusRequest

Request for command status obtaining.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **UUID** | Organization id which \&quot;correlationId\&quot; belongs to.                Can be obtained by &#x60;/organizations&#x60; operation. | 
**correlation_id** | **UUID** | Operation ID obtained from any command supporting operations. | 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_commands_get_command_status_request import IikoTransportPublicApiContractsCommandsGetCommandStatusRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsCommandsGetCommandStatusRequest from a JSON string
iiko_transport_public_api_contracts_commands_get_command_status_request_instance = IikoTransportPublicApiContractsCommandsGetCommandStatusRequest.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsCommandsGetCommandStatusRequest.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_commands_get_command_status_request_dict = iiko_transport_public_api_contracts_commands_get_command_status_request_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsCommandsGetCommandStatusRequest from a dict
iiko_transport_public_api_contracts_commands_get_command_status_request_from_dict = IikoTransportPublicApiContractsCommandsGetCommandStatusRequest.from_dict(iiko_transport_public_api_contracts_commands_get_command_status_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


