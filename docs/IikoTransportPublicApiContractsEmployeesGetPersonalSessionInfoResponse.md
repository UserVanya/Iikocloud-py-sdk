# IikoTransportPublicApiContractsEmployeesGetPersonalSessionInfoResponse

Personal session info response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **UUID** | Operation ID. | 
**is_session_opened** | **bool** | Is personal session opened. | [optional] 
**error** | **str** | Error details. | [optional] 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_employees_get_personal_session_info_response import IikoTransportPublicApiContractsEmployeesGetPersonalSessionInfoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsEmployeesGetPersonalSessionInfoResponse from a JSON string
iiko_transport_public_api_contracts_employees_get_personal_session_info_response_instance = IikoTransportPublicApiContractsEmployeesGetPersonalSessionInfoResponse.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsEmployeesGetPersonalSessionInfoResponse.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_employees_get_personal_session_info_response_dict = iiko_transport_public_api_contracts_employees_get_personal_session_info_response_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsEmployeesGetPersonalSessionInfoResponse from a dict
iiko_transport_public_api_contracts_employees_get_personal_session_info_response_from_dict = IikoTransportPublicApiContractsEmployeesGetPersonalSessionInfoResponse.from_dict(iiko_transport_public_api_contracts_employees_get_personal_session_info_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


