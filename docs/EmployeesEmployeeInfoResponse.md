# EmployeesEmployeeInfoResponse

Response for employee info.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **UUID** | Operation ID. | 
**employee_info** | [**EmployeesEmployeeInfo**](EmployeesEmployeeInfo.md) | Employee info. | 

## Example

```python
from iikocloud_client.models.employees_employee_info_response import EmployeesEmployeeInfoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EmployeesEmployeeInfoResponse from a JSON string
employees_employee_info_response_instance = EmployeesEmployeeInfoResponse.from_json(json)
# print the JSON string representation of the object
print(EmployeesEmployeeInfoResponse.to_json())

# convert the object into a dict
employees_employee_info_response_dict = employees_employee_info_response_instance.to_dict()
# create an instance of EmployeesEmployeeInfoResponse from a dict
employees_employee_info_response_from_dict = EmployeesEmployeeInfoResponse.from_dict(employees_employee_info_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


