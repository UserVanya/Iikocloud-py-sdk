# EmployeesEmployeesWithRoleSignResponse

Wrapping object to retrieve list of drivers from iikoRMS with checked role.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **str** | Operation ID. | 
**employees_with_check_roles** | [**List[WrapperEmployeesEmployeeWithCheckedRole]**](WrapperEmployeesEmployeeWithCheckedRole.md) | List of drivers. | 

## Example

```python
from iikocloud_client.models.employees_employees_with_role_sign_response import EmployeesEmployeesWithRoleSignResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EmployeesEmployeesWithRoleSignResponse from a JSON string
employees_employees_with_role_sign_response_instance = EmployeesEmployeesWithRoleSignResponse.from_json(json)
# print the JSON string representation of the object
print(EmployeesEmployeesWithRoleSignResponse.to_json())

# convert the object into a dict
employees_employees_with_role_sign_response_dict = employees_employees_with_role_sign_response_instance.to_dict()
# create an instance of EmployeesEmployeesWithRoleSignResponse from a dict
employees_employees_with_role_sign_response_from_dict = EmployeesEmployeesWithRoleSignResponse.from_dict(employees_employees_with_role_sign_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


