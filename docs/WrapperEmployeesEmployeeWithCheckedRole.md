# WrapperEmployeesEmployeeWithCheckedRole

RMS pair wrapping - list of response items that belong to this RMS.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **str** | Organization ID.                Can be obtained by &#x60;/api/1/organizations&#x60; operation. | 
**items** | [**List[EmployeesEmployeeWithCheckedRole]**](EmployeesEmployeeWithCheckedRole.md) | Items for organization. | 

## Example

```python
from iikocloud_client.models.wrapper_employees_employee_with_checked_role import WrapperEmployeesEmployeeWithCheckedRole

# TODO update the JSON string below
json = "{}"
# create an instance of WrapperEmployeesEmployeeWithCheckedRole from a JSON string
wrapper_employees_employee_with_checked_role_instance = WrapperEmployeesEmployeeWithCheckedRole.from_json(json)
# print the JSON string representation of the object
print(WrapperEmployeesEmployeeWithCheckedRole.to_json())

# convert the object into a dict
wrapper_employees_employee_with_checked_role_dict = wrapper_employees_employee_with_checked_role_instance.to_dict()
# create an instance of WrapperEmployeesEmployeeWithCheckedRole from a dict
wrapper_employees_employee_with_checked_role_from_dict = WrapperEmployeesEmployeeWithCheckedRole.from_dict(wrapper_employees_employee_with_checked_role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


