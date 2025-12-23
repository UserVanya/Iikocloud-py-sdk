# EmployeesEmployee

Employee DTO.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Employee ID. | 
**first_name** | **str** | Name of user. | [optional] 
**middle_name** | **str** | Second name. | [optional] 
**last_name** | **str** | Last name. | [optional] 
**display_name** | **str** | Displayed name (system name). | [optional] 
**code** | **str** | Code. | [optional] 
**is_deleted** | **bool** | User deletion flag. | [optional] 

## Example

```python
from iikocloud_client.models.employees_employee import EmployeesEmployee

# TODO update the JSON string below
json = "{}"
# create an instance of EmployeesEmployee from a JSON string
employees_employee_instance = EmployeesEmployee.from_json(json)
# print the JSON string representation of the object
print(EmployeesEmployee.to_json())

# convert the object into a dict
employees_employee_dict = employees_employee_instance.to_dict()
# create an instance of EmployeesEmployee from a dict
employees_employee_from_dict = EmployeesEmployee.from_dict(employees_employee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


