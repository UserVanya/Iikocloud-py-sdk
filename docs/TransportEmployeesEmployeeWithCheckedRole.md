# TransportEmployeesEmployeeWithCheckedRole

Employee DTO.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**check_roles_result** | [**List[TransportEmployeesRoleCheckResult]**](TransportEmployeesRoleCheckResult.md) | Result of check employee&#39;s roles. | [optional] 
**id** | **str** | Employee ID. | 
**first_name** | **str** | Name of user. | [optional] 
**middle_name** | **str** | Second name. | [optional] 
**last_name** | **str** | Last name. | [optional] 
**display_name** | **str** | Displayed name (system name). | [optional] 
**code** | **str** | Code. | [optional] 
**is_deleted** | **bool** | User deletion flag. | [optional] 

## Example

```python
from iiko_cloud_client.models.transport_employees_employee_with_checked_role import TransportEmployeesEmployeeWithCheckedRole

# TODO update the JSON string below
json = "{}"
# create an instance of TransportEmployeesEmployeeWithCheckedRole from a JSON string
transport_employees_employee_with_checked_role_instance = TransportEmployeesEmployeeWithCheckedRole.from_json(json)
# print the JSON string representation of the object
print(TransportEmployeesEmployeeWithCheckedRole.to_json())

# convert the object into a dict
transport_employees_employee_with_checked_role_dict = transport_employees_employee_with_checked_role_instance.to_dict()
# create an instance of TransportEmployeesEmployeeWithCheckedRole from a dict
transport_employees_employee_with_checked_role_from_dict = TransportEmployeesEmployeeWithCheckedRole.from_dict(transport_employees_employee_with_checked_role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


