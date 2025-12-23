# EmployeesEmployeeWithCheckedRole

Employee DTO.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**check_roles_result** | [**List[EmployeesRoleCheckResult]**](EmployeesRoleCheckResult.md) | Result of check employee&#39;s roles. | [optional] 
**id** | **str** | Employee ID. | 
**first_name** | **str** | Name of user. | [optional] 
**middle_name** | **str** | Second name. | [optional] 
**last_name** | **str** | Last name. | [optional] 
**display_name** | **str** | Displayed name (system name). | [optional] 
**code** | **str** | Code. | [optional] 
**is_deleted** | **bool** | User deletion flag. | [optional] 

## Example

```python
from iikocloud_client.models.employees_employee_with_checked_role import EmployeesEmployeeWithCheckedRole

# TODO update the JSON string below
json = "{}"
# create an instance of EmployeesEmployeeWithCheckedRole from a JSON string
employees_employee_with_checked_role_instance = EmployeesEmployeeWithCheckedRole.from_json(json)
# print the JSON string representation of the object
print(EmployeesEmployeeWithCheckedRole.to_json())

# convert the object into a dict
employees_employee_with_checked_role_dict = employees_employee_with_checked_role_instance.to_dict()
# create an instance of EmployeesEmployeeWithCheckedRole from a dict
employees_employee_with_checked_role_from_dict = EmployeesEmployeeWithCheckedRole.from_dict(employees_employee_with_checked_role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


