# IikoTransportPublicApiContractsEmployeesEmployeeWithCheckedRole

Employee DTO.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**check_roles_result** | [**List[IikoTransportPublicApiContractsEmployeesRoleCheckResult]**](IikoTransportPublicApiContractsEmployeesRoleCheckResult.md) | Result of check employee&#39;s roles. | [optional] 
**id** | **UUID** | Employee ID. | 
**first_name** | **str** | Name of user. | [optional] 
**middle_name** | **str** | Second name. | [optional] 
**last_name** | **str** | Last name. | [optional] 
**display_name** | **str** | Displayed name (system name). | [optional] 
**code** | **str** | Code. | [optional] 
**is_deleted** | **bool** | User deletion flag. | [optional] 

## Example

```python
from iikocloud_client.models.iiko_transport_public_api_contracts_employees_employee_with_checked_role import IikoTransportPublicApiContractsEmployeesEmployeeWithCheckedRole

# TODO update the JSON string below
json = "{}"
# create an instance of IikoTransportPublicApiContractsEmployeesEmployeeWithCheckedRole from a JSON string
iiko_transport_public_api_contracts_employees_employee_with_checked_role_instance = IikoTransportPublicApiContractsEmployeesEmployeeWithCheckedRole.from_json(json)
# print the JSON string representation of the object
print(IikoTransportPublicApiContractsEmployeesEmployeeWithCheckedRole.to_json())

# convert the object into a dict
iiko_transport_public_api_contracts_employees_employee_with_checked_role_dict = iiko_transport_public_api_contracts_employees_employee_with_checked_role_instance.to_dict()
# create an instance of IikoTransportPublicApiContractsEmployeesEmployeeWithCheckedRole from a dict
iiko_transport_public_api_contracts_employees_employee_with_checked_role_from_dict = IikoTransportPublicApiContractsEmployeesEmployeeWithCheckedRole.from_dict(iiko_transport_public_api_contracts_employees_employee_with_checked_role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


