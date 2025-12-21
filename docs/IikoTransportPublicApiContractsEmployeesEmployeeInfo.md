# IikoTransportPublicApiContractsEmployeesEmployeeInfo

Employee info.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Employee ID. | 
**first_name** | **str** | Name of employee. | [optional] 
**middle_name** | **str** | Second name. | [optional] 
**last_name** | **str** | Last name. | [optional] 
**display_name** | **str** | Display name. | [optional] 
**email** | **str** | Email. | [optional] 
**phone** | **str** | Phone. | [optional] 
**cell_phone** | **str** | Cell phone. | [optional] 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_employees_employee_info import IikoTransportPublicApiContractsEmployeesEmployeeInfo

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsEmployeesEmployeeInfo from a JSON string
iiko_transport_public_api_contracts_employees_employee_info_instance = IikoTransportPublicApiContractsEmployeesEmployeeInfo.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsEmployeesEmployeeInfo.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_employees_employee_info_dict = iiko_transport_public_api_contracts_employees_employee_info_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsEmployeesEmployeeInfo from a dict
iiko_transport_public_api_contracts_employees_employee_info_from_dict = IikoTransportPublicApiContractsEmployeesEmployeeInfo.from_dict(iiko_transport_public_api_contracts_employees_employee_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


