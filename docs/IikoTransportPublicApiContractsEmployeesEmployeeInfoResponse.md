# IikoTransportPublicApiContractsEmployeesEmployeeInfoResponse

Response for employee info.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **UUID** | Operation ID. | 
**employee_info** | [**IikoTransportPublicApiContractsEmployeesEmployeeInfo**](IikoTransportPublicApiContractsEmployeesEmployeeInfo.md) | Employee info. | 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_employees_employee_info_response import IikoTransportPublicApiContractsEmployeesEmployeeInfoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsEmployeesEmployeeInfoResponse from a JSON string
iiko_transport_public_api_contracts_employees_employee_info_response_instance = IikoTransportPublicApiContractsEmployeesEmployeeInfoResponse.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsEmployeesEmployeeInfoResponse.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_employees_employee_info_response_dict = iiko_transport_public_api_contracts_employees_employee_info_response_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsEmployeesEmployeeInfoResponse from a dict
iiko_transport_public_api_contracts_employees_employee_info_response_from_dict = IikoTransportPublicApiContractsEmployeesEmployeeInfoResponse.from_dict(iiko_transport_public_api_contracts_employees_employee_info_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


