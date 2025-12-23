# EmployeesEmployeeInfo

Employee info.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Employee ID. | 
**first_name** | **str** | Name of employee. | [optional] 
**middle_name** | **str** | Second name. | [optional] 
**last_name** | **str** | Last name. | [optional] 
**display_name** | **str** | Display name. | [optional] 
**email** | **str** | Email. | [optional] 
**phone** | **str** | Phone. | [optional] 
**cell_phone** | **str** | Cell phone. | [optional] 

## Example

```python
from iikocloud_client.models.employees_employee_info import EmployeesEmployeeInfo

# TODO update the JSON string below
json = "{}"
# create an instance of EmployeesEmployeeInfo from a JSON string
employees_employee_info_instance = EmployeesEmployeeInfo.from_json(json)
# print the JSON string representation of the object
print(EmployeesEmployeeInfo.to_json())

# convert the object into a dict
employees_employee_info_dict = employees_employee_info_instance.to_dict()
# create an instance of EmployeesEmployeeInfo from a dict
employees_employee_info_from_dict = EmployeesEmployeeInfo.from_dict(employees_employee_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


