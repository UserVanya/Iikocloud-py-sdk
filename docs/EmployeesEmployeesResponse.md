# EmployeesEmployeesResponse

Wrapping object to retrieve list of drivers from iikoRMS.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **str** | Operation ID. | 
**employees** | [**List[WrapperEmployeesEmployee]**](WrapperEmployeesEmployee.md) | List of drivers. | 

## Example

```python
from iikocloud_client.models.employees_employees_response import EmployeesEmployeesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EmployeesEmployeesResponse from a JSON string
employees_employees_response_instance = EmployeesEmployeesResponse.from_json(json)
# print the JSON string representation of the object
print(EmployeesEmployeesResponse.to_json())

# convert the object into a dict
employees_employees_response_dict = employees_employees_response_instance.to_dict()
# create an instance of EmployeesEmployeesResponse from a dict
employees_employees_response_from_dict = EmployeesEmployeesResponse.from_dict(employees_employees_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


