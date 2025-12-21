# EmployeesGetTerminalGroupsOfEmployeeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**employee_id** | **UUID** |  | 

## Example

```python
from iikocloud_client.models.employees_get_terminal_groups_of_employee_request import EmployeesGetTerminalGroupsOfEmployeeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EmployeesGetTerminalGroupsOfEmployeeRequest from a JSON string
employees_get_terminal_groups_of_employee_request_instance = EmployeesGetTerminalGroupsOfEmployeeRequest.from_json(json)
# print the JSON string representation of the object
print(EmployeesGetTerminalGroupsOfEmployeeRequest.to_json())

# convert the object into a dict
employees_get_terminal_groups_of_employee_request_dict = employees_get_terminal_groups_of_employee_request_instance.to_dict()
# create an instance of EmployeesGetTerminalGroupsOfEmployeeRequest from a dict
employees_get_terminal_groups_of_employee_request_from_dict = EmployeesGetTerminalGroupsOfEmployeeRequest.from_dict(employees_get_terminal_groups_of_employee_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


