# IikoTransportPublicApiContractsEmployeesChangePersonalSessionResponse

Personal session change response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **UUID** | Operation ID. | 
**error** | **str** | Error details. | [optional] 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_employees_change_personal_session_response import IikoTransportPublicApiContractsEmployeesChangePersonalSessionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsEmployeesChangePersonalSessionResponse from a JSON string
iiko_transport_public_api_contracts_employees_change_personal_session_response_instance = IikoTransportPublicApiContractsEmployeesChangePersonalSessionResponse.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsEmployeesChangePersonalSessionResponse.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_employees_change_personal_session_response_dict = iiko_transport_public_api_contracts_employees_change_personal_session_response_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsEmployeesChangePersonalSessionResponse from a dict
iiko_transport_public_api_contracts_employees_change_personal_session_response_from_dict = IikoTransportPublicApiContractsEmployeesChangePersonalSessionResponse.from_dict(iiko_transport_public_api_contracts_employees_change_personal_session_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


