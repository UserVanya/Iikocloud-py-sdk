# EmployeesEmployeeInfoRequest

Request for employee info.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **UUID** | Organization ID.                Can be obtained by &#x60;/organizations&#x60; operation. | 
**id** | **UUID** | Employee ID. | 

## Example

```python
from iikocloud_client.models.employees_employee_info_request import EmployeesEmployeeInfoRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EmployeesEmployeeInfoRequest from a JSON string
employees_employee_info_request_instance = EmployeesEmployeeInfoRequest.from_json(json)
# print the JSON string representation of the object
print(EmployeesEmployeeInfoRequest.to_json())

# convert the object into a dict
employees_employee_info_request_dict = employees_employee_info_request_instance.to_dict()
# create an instance of EmployeesEmployeeInfoRequest from a dict
employees_employee_info_request_from_dict = EmployeesEmployeeInfoRequest.from_dict(employees_employee_info_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


