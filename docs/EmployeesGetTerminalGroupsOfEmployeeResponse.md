# EmployeesGetTerminalGroupsOfEmployeeResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**terminal_group_ids** | **List[UUID]** |  | 

## Example

```python
from iikocloud_client.models.employees_get_terminal_groups_of_employee_response import EmployeesGetTerminalGroupsOfEmployeeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EmployeesGetTerminalGroupsOfEmployeeResponse from a JSON string
employees_get_terminal_groups_of_employee_response_instance = EmployeesGetTerminalGroupsOfEmployeeResponse.from_json(json)
# print the JSON string representation of the object
print(EmployeesGetTerminalGroupsOfEmployeeResponse.to_json())

# convert the object into a dict
employees_get_terminal_groups_of_employee_response_dict = employees_get_terminal_groups_of_employee_response_instance.to_dict()
# create an instance of EmployeesGetTerminalGroupsOfEmployeeResponse from a dict
employees_get_terminal_groups_of_employee_response_from_dict = EmployeesGetTerminalGroupsOfEmployeeResponse.from_dict(employees_get_terminal_groups_of_employee_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


