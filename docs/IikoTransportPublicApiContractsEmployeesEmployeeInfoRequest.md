# IikoTransportPublicApiContractsEmployeesEmployeeInfoRequest

Request for employee info.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **UUID** | Organization ID.                Can be obtained by &#x60;/organizations&#x60; operation. | 
**id** | **UUID** | Employee ID. | 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_employees_employee_info_request import IikoTransportPublicApiContractsEmployeesEmployeeInfoRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsEmployeesEmployeeInfoRequest from a JSON string
iiko_transport_public_api_contracts_employees_employee_info_request_instance = IikoTransportPublicApiContractsEmployeesEmployeeInfoRequest.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsEmployeesEmployeeInfoRequest.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_employees_employee_info_request_dict = iiko_transport_public_api_contracts_employees_employee_info_request_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsEmployeesEmployeeInfoRequest from a dict
iiko_transport_public_api_contracts_employees_employee_info_request_from_dict = IikoTransportPublicApiContractsEmployeesEmployeeInfoRequest.from_dict(iiko_transport_public_api_contracts_employees_employee_info_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


